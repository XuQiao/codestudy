
# coding: utf-8

# ## More Feature extraction and some other classifiers

# Import useful sklearn kits and other functions

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from time import time

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import LabelBinarizer

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_selection import VarianceThreshold
from sklearn.model_selection import RandomizedSearchCV, GridSearchCV, train_test_split

from sklearn.linear_model import Perceptron
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_selection import SelectFromModel
from sklearn.feature_selection import SelectKBest, chi2, f_regression
from sklearn.linear_model import RidgeClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestCentroid
from sklearn.ensemble import RandomForestClassifier
from sklearn.utils.extmath import density
from sklearn.decomposition import PCA, NMF
from sklearn import metrics

###########################################
use_hashing = False
select_chi2 = 1000
n_features = 2 ** 16
print_top10 = False
print_report = True
print_cm = True
n_gram = 1

###########################################
# read in data
trainall_df = pd.read_csv("../input/train.csv")

# split a training set and a test set
X_train, X_test, y_train, y_test = train_test_split(trainall_df.text, trainall_df.author, test_size = 0.2, random_state = 1)
# y_train = LabelBinarizer().fit_transform(y_train)
# y_test = LabelBinarizer().fit_transform(y_test)


# Data pre-processing and extract features(use Vectorizer)

# In[ ]:

target_names = ['EAP','HPL','MWS']

t0 = time()
y_train = LabelBinarizer().fit_transform(y_train)
print(y_train)

clf = Pipeline([
      #('text', CountVectorizer()),
      ('text',TfidfVectorizer(sublinear_tf=True, max_df=0.5)),
      #('feature_selection', SelectFromModel(LinearSVC(penalty="l1"))),
      ('feature_selection', SelectKBest(f_regression, k=1000)),
      #('reduce_dims',PCA()),
      ('mnb', MultinomialNB())
        ])
clf.fit(X_train, y_train)

train_time = time() - t0
print("train time: %0.3fs" % train_time)

t0 = time()
pred = clf.predict(X_test)
try:
    pred_prob = clf.predict_proba(X_test)
except AttributeError:
    try:
        dec_f = clf.decision_function(X_test)
        pred_prob = np.exp(dec_f) / np.sum(np.exp(dec_f))
    except AttributeError:
        pred_prob = LabelBinarizer().fit_transform(pred.tolist())

test_time = time() - t0
print("test time:  %0.3fs" % test_time)

score = metrics.accuracy_score(y_test, pred)
print("accuracy:   %0.3f" % score)

y_test_prob = LabelBinarizer().fit_transform(y_test)
log_loss = metrics.log_loss(y_test_prob, pred_prob)
print("log_loss:   %0.3f" % log_loss)

if hasattr(clf, 'coef_'):
    print("dimensionality: %d" % clf.coef_.shape[1])
    print("density: %f" % density(clf.coef_))

if print_report:
    print("classification report:")
    print(metrics.classification_report(y_test, pred,
                                        target_names=target_names))

if print_cm:
    print("confusion matrix:")
    print(metrics.confusion_matrix(y_test, pred))

print()
clf_descr = str(clf).split('(')[0]
