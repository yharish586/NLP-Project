##0-Suffix,1-Previous case,2-Next case ,3-Previous wordform,4-next wordform, 5-post position,6-present word form,7-POS####
from preprocess_train import features,category;
from preprocess_test import features_test,category_test;
from nltk.classify import SklearnClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import SVC
train_data=[[x for x in range(2)] for y in range(357)]
test_data=[[x for x in range(1)] for y in range(11)]
for i in range(0,357):
    train_data[i][0]={'Suffix':features[i][0], 'Previous morph':features[i][1],'Next morph':features[i][2],'Previous wordform':features[i][3],
                      'Next wordform':features[i][4],'postposition':features[i][5],'wordform':features[i][6],'pos':features[i][7]}
    train_data[i][1]=category[i]
for i in range(0,11):
    test_data[i]={'Suffix':features_test[i][0], 'Previous morph':features_test[i][1],'Next morph':features_test[i][2],'Previous wordform':features_test[i][3],
                  'Next wordform':features_test[i][4],'postposition':features_test[i][5],'wordform':features[i][6],'pos':features[i][7]} 
classif = SklearnClassifier(SVC(), sparse=False).train(train_data)
result=classif.classify_many(test_data)
classif1 = SklearnClassifier(BernoulliNB()).train(train_data)
result1=classif1.classify_many(test_data)
print result1
