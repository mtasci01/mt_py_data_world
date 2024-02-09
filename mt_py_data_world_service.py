from online_dating_sim import OnlineDatingSim
from search_engine import SearchEngine
from weather_predictor import WeatherPredictor

class MtPyDataWorldService:
    
    def runOnlineDatingSim(self):
        ow = OnlineDatingSim()
        return ow.runModel(300)
    
    def runSearchEngine(self, q):
        se = SearchEngine()
        return se.search(q)
    
    def runWeatherPredictor(self, m):
        we = WeatherPredictor()
        return we.runANNCatModel()
       