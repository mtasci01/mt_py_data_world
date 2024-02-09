
import json
import numpy as np

from sklearn.calibration import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf


class WeatherPredictor:

  #this program is meant to be a weather forecast application. We try to guess the amount of rain in a place, given previous
  #forecasts in the same place and in nearby coordinates (ideally in a circle). The data is based on https://open-meteo.com/
  #WARNING this is not meant to be a usable program with real data, just a demo. Given the small amount of data we are happy with 
  #overfitting.
  #the target is a categorical value for the amount of rain (high,low,none). the input is a sequence of hourly forecasts, concatenated

  scaler = MinMaxScaler() #normalize X to 0 - 1
  PRECIPITATION_IX = 5
  DATETIME_IX = 2
  LAT_IX = 0
  LON_IX = 1
  DAYS_AHEAD = 2
  HOUR_INTERVAL=3
  TARGET_COORDS_KEY=2

  def getTrainTest(self):
    
          #columns=["lat", "lon", "date_time","temperature","humidity","precipitation","pressure","clouds","wind_speed","wind_direction","wind_gust"]
          f = open("resources/open_weather_dump.json")
          dataMap = json.load(f)
          f.close()

          keysList = [*dataMap]
          lenDataPoints=len(dataMap[keysList[0]])
          
          trexs  = []
          ys = []    

          for i in range(lenDataPoints):
              if (i % self.HOUR_INTERVAL == 0):
                  seqRangeIx=i + 24*self.DAYS_AHEAD
                  maxRangeIx = i + 24*self.DAYS_AHEAD + 18
                  if (maxRangeIx >= lenDataPoints):
                      break 
                  
                  targetIx12 = i + 24*self.DAYS_AHEAD + 12
                  sequence = []
                  for z in range(i,seqRangeIx):
                      
                      if (z % self.HOUR_INTERVAL == 0):
                          for k in dataMap:
                              dataRow = dataMap[k]
                              sequence = sequence + dataRow[z]
                      
                  targetDataset = dataMap[str(self.TARGET_COORDS_KEY)]

                  target = targetDataset[targetIx12][self.PRECIPITATION_IX]
                  if (target >= 1):
                      target = 'high'
                  elif(target > 0 and target < 1):
                      target = 'low'
                  else:
                      target = 'none'                  
                  ys.append(target)   
                  trexs.append(sequence)

          trexs = np.array(trexs).astype('float64')                  
          ys = LabelEncoder().fit_transform(ys)
      
          trexsScaled = self.scaler.fit_transform(trexs)
    
          X_train, X_test, y_train, y_test = train_test_split(trexsScaled, ys, test_size=0.1)
          
          return trexsScaled, ys, X_train, X_test, y_train, y_test
  
  def runPredictions(self, model, X_test, y_test):
      predictions = model.predict(X_test)
      tot = 0
      right = 0
      ret={}
      retList = []
      for i in range(len(predictions)):
        pred = np.argmax(predictions[i], axis=-1)
        tot = tot + 1
        if (y_test[i] == pred):
            right = right + 1
        obj = {}
        obj["test_ix"] = i
        obj["y_test"] = str(y_test[i])
        obj["prediction"] = str(pred)
        retList.append(obj)
      ret["tot"]=tot
      ret["right"]=right
      ret["tot_right_ratio"]=right/tot
      ret["retList"]= retList
      return ret   

  def runANNCatModel(self):
      
          trexsScaled, ys,X_train, X_test, y_train, y_test = self.getTrainTest()
          n_features = trexsScaled.shape[1]
          nOutputs = 3

          model = tf.keras.Sequential()
          model.add(tf.keras.layers.Dense(1000, activation='relu',input_shape=(n_features,), kernel_initializer='he_normal'))
          model.add(tf.keras.layers.Dense(nOutputs, activation='softmax'))

          model.compile(loss='sparse_categorical_crossentropy', optimizer=tf.keras.optimizers.Adam(), metrics=['accuracy'])
          model.fit(trexsScaled, ys, epochs=500, batch_size=10000)

          return self.runPredictions(model,trexsScaled, ys)


          