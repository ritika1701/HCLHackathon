import pickle
import csv
from nltk.corpus import stopwords
class NaiveBayes():
    total_words = 0
    total_sentimental_occurences = {'0':0,'2': 0, '4': 0}
    feature_list = {}


    #function to clean the tweet
    def process_tweet(tweet):
        # Convert to lower case
        tweet = tweet.lower()
        tweets = list(set(tweet.split))
        feature_vector = []
        for word in tweets:
            #remove punctuations symbols
            word = word.strip()
            word = word.replace("\'", "")
            word = word.replace("\\", "")
            word = word.replace("?", "")
            word = word.replace(".", "")
            word = word.replace("!", "")
            word = word.replace("\"", "")
            word = word.replace(",", "")
            word = word.replace("\'", "")
            word = word.replace(")", "")
            word = word.replace("(", "")
            word = word.replace("[", "")
            word = word.replace("]", "")
            #ignore some text
            if ((word in stopwords.words('English'))or(word.startswith(":"))or(word.startswith(" ")) or (word.startswith("@")) or (
                    word.startswith("&")) or (word.startswith("www")) or (
                    word.startswith("#")) or (word.startswith("http")) or (
            word.isdigit())) :
                continue
            else:
                #add to feature_vector if word is formatted
                feature_vector.append(word.lower())
        return feature_vector



    

    def training():    #Feature Extractor which makes feature list
        inp_tweets = csv.reader(open('newFile.csv', 'r',encoding='utf8'), delimiter=',', quotechar='\"', )
        tweets = []
        i=0
        for row in inp_tweets:
            i=i+1
            if i==1: # Leaving The header of Csv File
                continue
            if i==20000:
                break
        
        #first element in given dataset gives sentiment and 6th gives the actual tweet
         
            sentiment = row[3]
            tweet = row[4]
            #extract feature vector from a tweet by cleaning it
            feature_vector = NaiveBayes.process_tweet(tweet)
            for feature in feature_vector:
                if not feature in NaiveBayes.feature_list:
                    #if a word is not in currently maintained list , then add it
                    NaiveBayes.feature_list[feature] = {'0': 0, '2': 0,'4':0, 'count': 0}
                #increment the sentiment count  of the word
                NaiveBayes.feature_list[feature][sentiment] += 1
                NaiveBayes.feature_list[feature]['count'] += 1
                NaiveBayes.total_sentimental_occurences[sentiment] += 1
                NaiveBayes.total_words += 1
        
        NaiveBayes.feature_list['total_words']=NaiveBayes.total_words
        NaiveBayes.feature_list['total_sentimental_occurences']=NaiveBayes.total_sentimental_occurences
    

        ob=NaiveBayes.feature_list                        #Storing the trained set Uding Pickle library
        file=open("classifier.pickle","wb")
        pickle.dump(ob,file)


        #function to find max element key in a dictionary
    def find_max(mydict):
        return max(mydict, key=mydict.get)


    #get probability of occurence of a feature if it belongs to a certain class - P(feature|class)
    def get_prob_features_under_class(feature_vector, sentiment):
        result = 1
        counter = 0
        for word in feature_vector:
            if word in NaiveBayes.feature_list:
                counter = 1
                if NaiveBayes.feature_list['total_sentimental_occurences'][sentiment] != 0:
                    result *= NaiveBayes.feature_list[word][sentiment] / NaiveBayes.feature_list['total_sentimental_occurences'][sentiment]
                else:
                    return 0
        if counter == 0:
            return 0
        return result

    #get probability of occurence of a certain class - P(class)
    def get_prob_class(sentiment):
        result = NaiveBayes.feature_list['total_sentimental_occurences'][sentiment] / NaiveBayes.feature_list['total_words']
        return result

    #get probability of occurence of a certain feature - P(feature)
    def get_prob_features(feature_vector):
        result = 1.0000
        counter = 0
        for feature in feature_vector:
            if feature in NaiveBayes.feature_list:
                counter = 1
                result *= NaiveBayes.feature_list[feature]['count'] / NaiveBayes.feature_list['total_words']

        if counter == 0:
            return 0
        return result

    #predict nature of a sentence according to its feature vector
    def predict(tweet):
        feature_vector=NaiveBayes.process_tweet(tweet)
        prob_acc_to_sentiments = {}
        prob_of_features = NaiveBayes.get_prob_features(feature_vector)
        if prob_of_features == 0:
            return '2'
    
        #calculating probability of occuring of sentence in each class
        else:
            for sentiment in NaiveBayes.total_sentimental_occurences:
                # P(class|features) = P(features|class)*P(class)/P(features)
                prob_acc_to_sentiments[sentiment] = NaiveBayes.get_prob_features_under_class(feature_vector, sentiment) * \
                                                 NaiveBayes.get_prob_class(sentiment) / prob_of_features
            #find class with maximum probability
            result = NaiveBayes.find_max(prob_acc_to_sentiments)    
            return result
        

    


    
