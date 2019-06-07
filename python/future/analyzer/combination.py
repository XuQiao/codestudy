from __future__ import print_function

import logging
import pandas as pd
import numpy as np
from optparse import OptionParser
import sys
from time import time
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder, LabelBinarizer

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, HashingVectorizer
from sklearn.feature_selection import VarianceThreshold, SelectKBest,chi2, RFE
from sklearn.linear_model import RidgeClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC, SVC
from sklearn.linear_model import SGDClassifier, Perceptron, PassiveAggressiveClassifier
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.neighbors import KNeighborsClassifier, NearestCentroid
from sklearn.ensemble import RandomForestClassifier ,ExtraTreesClassifier
from sklearn.utils.extmath import density
from sklearn import metrics
from sklearn.model_selection import train_test_split
import itertools


# collect data for training and test
trainall_df = pd.read_csv("../input/train.csv")

# split a training set and a test set
data_train, data_test, y_train, y_test = train_test_split(trainall_df.text, trainall_df.author, test_size = 0.2, random_state = 1)


vectorizationModels = (
    (CountVectorizer(),'Count'),
    (CountVectorizer(ngram_range=(1,2), token_pattern = r'\b\w+\b', min_df = 1),'1/2-gram'),
    (HashingVectorizer(stop_words='english',  alternate_sign=False ,n_features=2**16),'Hashing'),
    (TfidfVectorizer(sublinear_tf=True, max_df=0.5, stop_words='english'),'Tfidf')
    )

rfesvc = SVC(kernel="linear", C=1)
featureSelectionModels = (
    (SelectKBest(chi2, k=5000),'5000-Univariance'),
 #   (LinearSVC(C=0.1, penalty="l1", dual=False),'L1'),
 #   (ExtraTreesClassifier(),'Tree'),
 #   (RFE(estimator=rfesvc, n_features_to_select=10000, step=1),'RFE')
 )

classificationModels = (
    (RidgeClassifier(tol=1e-2, solver="sag"), "Ridge Classifier"),
    (Perceptron(max_iter=50), "Perceptron"),
    (KNeighborsClassifier(n_neighbors=10), "kNN"),
    (RandomForestClassifier(n_estimators=20), "Random forest"),
    (LinearSVC(loss='squared_hinge', penalty='l1', dual=False, tol=1e-3),"SVC-L1"),
    (LinearSVC(loss='squared_hinge', penalty='l2', dual=False, tol=1e-3),"SVC-L2"),
    (SGDClassifier(alpha=.0001, max_iter=50,penalty='l1'),'SGD-L1'),
    (SGDClassifier(alpha=.0001, max_iter=50,penalty='l2'),'SGD-L2'),
    (SGDClassifier(alpha=.0001, max_iter=50,penalty='elasticnet'),'SGD-ElasticNet'),
    (NearestCentroid(),'Nearest neighbor'),
    (MultinomialNB(alpha=.01),'NB1'),
    (BernoulliNB(alpha=.01),'NB2'))

def benchmark(classifier):
    classifier.fit(X_train,y_train)
    pred = classifier.predict(X_test)
    score = metrics.accuracy_score(y_test, pred)
    try:
        pred_prob = classifier.predict_proba(X_test)
    except AttributeError:
        try:
            dec_f = classifier.decision_function(X_test)
            pred_prob = np.exp(dec_f) / np.sum(np.exp(dec_f)) #softmax
        except AttributeError:
            pred_prob = LabelBinarizer().fit_transform(pred.tolist())
    y_test_prob = LabelBinarizer().fit_transform(y_test)
    log_loss = metrics.log_loss(y_test_prob, pred_prob)
    return score, log_loss

results = []
for (vectorizer,vectorizerName),(selector,selectorName),(classifier,classifierName) in list(itertools.product(vectorizationModels,featureSelectionModels,classificationModels)):
    # vectorize input
    if vectorizerName=='Hashing':
        X_train = vectorizer.transform(data_train)
    else:
        X_train = vectorizer.fit_transform(data_train)
    X_test = vectorizer.transform(data_test)
    # print(X_train.shape)
    # feature selection
    X_train = selector.fit_transform(X_train,y_train)
    X_test = selector.transform(X_test)
    # classification model
    # print(vectorizerName, selectorName, classifierName)
    bench = benchmark(classifier)
    results.append((vectorizerName,selectorName,classifierName,bench[0], bench[1]))

for x in results:
    print(x)
