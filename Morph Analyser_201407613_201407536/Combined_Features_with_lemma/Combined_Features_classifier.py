###0-suffix ,1-prev gender, 2-next gender, 3-prev person, 4 next person,5-prev number ,6-next number,7-prev category ,8-next category,9-prev root,10-next root,
###11-current root ,12-POS##
from Combined_Features_train import features,gender,person,number,category,lemma_labels;
from Combined_Features_test import features_test,gender_test,person_test,number_test,category_test;
from nltk.classify import SklearnClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.svm import SVC
train_data=[[x for x in range(2)] for y in range(357)]
test_data=[[x for x in range(1)] for y in range(11)]
for i in range(0,357):
    train_data[i][0]={'Suffix':features[i][0], 'Previous  gender':features[i][1],'Next gender':features[i][2],'Previous person':features[i][3],
                      'Next person':features[i][4],'Previous number':features[i][5],'Next number':features[i][6],
                      'Previous Category':features[i][7],'Next Category':features[i][8],'Previous root':features[i][9],'Next root':features[i][10],
                      'wordform':features[i][11],'POS':features[i][12]}
    train_data[i][1]=lemma_labels[i]
for i in range(0,11):
    test_data[i]={'Suffix':features_test[i][0], 'Previous  gender':features_test[i][1],'Next gender':features_test[i][2],'Previous person':features_test[i][3],
                      'Next person':features[i][4],'Previous number':features[i][5],'Next number':features[i][6],
                      'Previous Category':features_test[i][7],'Next Category':features_test[i][8],'Previous root':features_test[i][9],'Next root':features_test[i][10],
                      'wordform':features_test[i][11],'POS':features_test[i][12]}
classif = SklearnClassifier(SVC(), sparse=True).train(train_data)
result=classif.classify_many(test_data)
classif1 = SklearnClassifier(BernoulliNB()).train(train_data)
result1=classif1.classify_many(test_data)
print result
print result1
