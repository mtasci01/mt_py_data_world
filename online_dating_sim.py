
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
import logging
 
#We simulate a dating app where users give positive/negative ratings to other users.
#This program is meant to be a JOKE and not serious. 
#Even though this is not meant to represent reality, I know some of you will still get triggered. I don't care.
#We make the following assumptions: there are 2 sexes. Males only rate females and viceversa.
#We generate some traits, like hobbies, age, salary, a profile picture.
#For males, the attractiveness of the image is the most prominent factor. For females, the salary, but much less, so in the end 
#we end up with most males rating females high, but few females giving good ratings.
#we generate images as follows: random colors overall, and a uniform diagonal. 
#we define an attractive image as follows: for males rating females, 1st pixel > 50 RGB. for females, 1st pixel > 200 RGB
#We run KNN and a Neural Network and we compare them. Of course playing more with hyper parameters could yield better results

class OnlineDatingSim:

    ISMAN = 1

    IMGWIDTH = 5
    IMGHEIGHT = 5
    IXFIRSTPIXEL = 0
    LENIMGARR = IMGWIDTH*IMGHEIGHT*3
    IXSPORT = LENIMGARR
    IXMUSIC = LENIMGARR + 1
    IXTRAVELLING = LENIMGARR + 2
    IXCOOKING = LENIMGARR + 3
    IXTECH = LENIMGARR + 4
    IXSEX = LENIMGARR + 5
    IXAGE = LENIMGARR + 6
    IXSALARY = LENIMGARR + 7
    logging.basicConfig(level = logging.INFO)

    def random_img(self, width, height):

        array = np.random.random_integers(0,255, (height,width,3))
        
        randColor = np.random.randint(0,255)
        for i in range(width):
            array[i][i] = [randColor,randColor,randColor]

        array = np.array(array, dtype=np.uint8)
        return array.reshape(-1)


    def generateUsers(self, n):
        users = []
        for i in range(n):
            user = []
            imgArr = self.random_img(self.IMGWIDTH, self.IMGHEIGHT)
            user = user + imgArr.tolist()
            sports = np.random.randint(0,1)
            user.append(sports)

            music = np.random.randint(0,2)
            user.append(music)

            travelling = np.random.randint(0,2)
            user.append(travelling)

            cooking = np.random.randint(0,2)
            user.append(cooking)

            technology = np.random.randint(0,2)
            user.append(technology)

            sex = np.random.randint(0,2)
            user.append(sex)

            minAge = 20
            maxAge = 40

            age = np.random.randint(minAge,maxAge + 1)
            user.append(age)

            minSalaryF = 20000
            maxSalaryF = 60000
            minSalaryM = 20000
            maxSalaryM = 80000

            salary = np.random.randint(minSalaryM,maxSalaryM + 1)

            if (sex != self.ISMAN):
                salary = np.random.randint(minSalaryF,maxSalaryF + 1)

            ageSalarybonus = (age - minAge)*500
            salary = salary + ageSalarybonus
            user.append(salary)
            users.append(user)
        return users    

    def runModel(self, nPers):
        logging.info("Running runModel with " + str(nPers) + " nPers")

        ratings = []
        trexs = []

        users = self.generateUsers(nPers)

        totMaleRatings = 0
        totFemaleRatings = 0

        posMaleRatings = 0
        posFemaleRatings = 0

        for i in range(len(users)):
            userI = users[i]
            for j in range(len(users)):
                userJ = users[j]
                if (userI[self.IXSEX] != userJ[self.IXSEX]):
                    trexs.append(userI + userJ) 
                    probGoodRating = 0
                    probBadRating = 1
                    if (userI[self.IXSEX]== self.ISMAN):
                        if (userJ[self.IXFIRSTPIXEL] > 50):
                            probGoodRating += 0.8
                        if (userJ[self.IXSPORT] == 1):
                            probGoodRating += 0.1
                        if (userJ[self.IXCOOKING] == 1):
                            probGoodRating += 0.1
                        if (userJ[self.IXAGE] < 35):
                            probGoodRating += 0.1
                        

                        probBadRating = 1 - probGoodRating
                        if (probGoodRating > 1):
                            probGoodRating = 1
                            probBadRating = 0
                        rating = np.random.choice(np.array([1, 0]), p=[probGoodRating, probBadRating])    
                        ratings.append(rating)
                        if (rating == 1):
                            posMaleRatings = posMaleRatings + 1
                        totMaleRatings = totMaleRatings + 1    
                    else:
                        if (userJ[self.IXFIRSTPIXEL] > 200):
                            probGoodRating += 0.2
                        if (userJ[self.IXSPORT] == 1):
                            probGoodRating += 0.05
                        if (userJ[self.IXCOOKING] == 1):
                            probGoodRating += 0.05
                        if (userJ[self.IXAGE] >= userI[self.IXAGE]):
                            probGoodRating += 0.1
                        if (userJ[self.IXSALARY] >= userI[self.IXSALARY]):
                            probGoodRating += 0.1
                        if (userJ[self.IXSALARY] - userI[self.IXSALARY] > 20000):
                            probGoodRating += 0.2             

                        probBadRating = 1 - probGoodRating
                        rating = np.random.choice(np.array([1, 0]), p=[probGoodRating, probBadRating]) 
                        if (rating == 1):
                            posFemaleRatings = posFemaleRatings + 1
                        totFemaleRatings = totFemaleRatings + 1     

                        ratings.append(rating)  
                                     
                

        scaler = MinMaxScaler() #normalize X to 0 - 1
        trexScaled = scaler.fit_transform(trexs)
        trexScaled = trexScaled.astype('float64')
        ratings = np.array(ratings).astype('float64')

        ret = {}

        X_train, X_test, y_train, y_test = train_test_split(trexScaled, ratings, test_size=0.1)
        maxKnnAccuracy = 0
        bestK = 0
        for k in range(2, 20):
            logging.info("Running knn with " + str(k) + " k")
            knn = KNeighborsClassifier(n_neighbors=k) 
            
            knn.fit(X_train, y_train) 

            ratingsAI = knn.predict(X_test)

                
            tot = 0
            right = 0
            for i in range(len(ratingsAI)):

                tot = tot + 1
                if (y_test[i] == ratingsAI[i]):
                    right = right + 1   
            per = right/tot
            if (per > maxKnnAccuracy):
                bestK = k
                maxKnnAccuracy = per        

        ret['maxKnnAccuracy'] = maxKnnAccuracy
        ret['bestK'] = bestK
        ret['numGeneratedUsers'] = nPers
        ret['numTrainingExamples'] = len(trexs)
        ret['perFemaleRating'] = posFemaleRatings/totFemaleRatings
        ret['perMaleRating'] = posMaleRatings/totMaleRatings

        return ret      



