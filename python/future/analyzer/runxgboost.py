import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.corpus import stopwords
import string
import itertools
import xgboost as xgb
from nltk import FreqDist
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.linear_model import RidgeClassifier
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC, SVC
from sklearn.linear_model import SGDClassifier, Perceptron, PassiveAggressiveClassifier
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.neighbors import KNeighborsClassifier, NearestCentroid
from sklearn.ensemble import RandomForestClassifier ,ExtraTreesClassifier
from sklearn import ensemble, metrics, model_selection, naive_bayes
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import pickle, sys
from datetime import datetime
import time

color = sns.color_palette()
#nltk.download('stopwords')
def run(name = 'NB1', n_comp = 50, ngram_cv = 3, ngram_tfidf= 5, eta = 0.1, gamma = 0, startday = 360, endday = 0, test_size = 0.2):
    now = datetime.now()
    now = time.mktime(now.timetuple())
    trainall_df = pd.read_csv("data/btc_usd_matrix_full_next_quarter_future.csv",sep='\t',index_col=0)
    if startday < 0:
        startindex = 0
    else:
        startindex = trainall_df['date'].searchsorted(now - startday * 24 * 3600)[0]
    endindex = trainall_df['date'].searchsorted(now - endday * 24 * 3600)[0]
    trainall_df = trainall_df.iloc[startindex:endindex]
    trainall_df = trainall_df.dropna(axis=0)
    mapping_dict = {-1:0, 1:1}
    train_y = trainall_df['flag'].map(mapping_dict)
#    train_y = trainall_df['flag']
    train_x = trainall_df.drop(['date', 'flag','open','high','low','close'],axis=1)
    saved_stdout = sys.stdout
    sys.stdout = open('data/class_report_xgb.txt', 'w')
    train_X, test_X, train_y, test_y = train_test_split(train_x, train_y, test_size = test_size, random_state = 1)
    print(train_X.shape, train_y.shape)
    print(test_X.shape, test_y.shape)

    def runXGB(train_X, train_y, test_X, test_y=None, test_X2=None, seed_val=0, child=1, colsample=0.2, eta = 0.2, gamma = 0):
        param = {}
        param['objective'] = 'multi:softprob'
        param['max_depth'] = 5
        param['silent'] = True
        param['num_class'] = 2
        param['eval_metric'] = "mlogloss"
        param['min_child_weight'] = child
        param['subsample'] = 0.8
        param['colsample_bytree'] = colsample
        param['seed'] = seed_val
        param['learning_rate'] = eta
        param['n_estimators'] = 100
        param['gamma'] = gamma
        param['nthread'] = 4
        param['scale_pos_weight'] = 1
        num_rounds = 50000

        plst = list(param.items())
        xgtrain = xgb.DMatrix(train_X, label=train_y)

        if test_y is not None:
            xgtest = xgb.DMatrix(test_X, label=test_y)
            watchlist = [ (xgtrain,'train'), (xgtest, 'test') ]
            model = xgb.train(plst, xgtrain, num_rounds, watchlist, early_stopping_rounds=50, verbose_eval=False)
        else:
            xgtest = xgb.DMatrix(test_X)
            model = xgb.train(plst, xgtrain, num_rounds)

        prob_test_y = model.predict(xgtest, ntree_limit = model.best_ntree_limit)
        pred_test_y = pd.DataFrame(prob_test_y).idxmax(axis=1).values
        cv_score = metrics.log_loss(test_y, prob_test_y,labels=[0,1])
        f1_score = metrics.f1_score(test_y, pred_test_y,labels=[0,1])
        precision_score = metrics.precision_score(test_y, pred_test_y,labels=[0,1])
        score = metrics.accuracy_score(test_y, pred_test_y)
        print("accuracy:   %0.3f" % score)
        print("f1-score:   %0.3f" % f1_score)
        print("log-loss:   %0.3f" % cv_score)
        if test_X2 is not None:
            xgtest2 = xgb.DMatrix(test_X2)
            prob_test_y2 = model.predict(xgtest2, ntree_limit = model.best_ntree_limit)
        print("classification report:")
        target_names = ['-1', '1']
        print(metrics.classification_report(test_y, pred_test_y, target_names=target_names))

        print("confusion matrix:")
        print(metrics.confusion_matrix(test_y, pred_test_y))
        feature_importances = pd.DataFrame(model.get_score(importance_type='weight'), index = train_X.columns,columns=['importance']).sort_values('importance',ascending=False)
        feature_importances.to_csv('data/feature_importance_xgb.csv',sep='\t')
        return model, cv_score, f1_score, precision_score

    ###XGBoost model:
    #cols_to_drop = ['id', 'text']
    #train_X = train_df.drop(cols_to_drop+['author'], axis=1)
    #test_X = test_df.drop(cols_to_drop, axis=1)


    #def predictXGB(model, test_X):
    #    kf = model_selection.KFold(n_splits=5, shuffle=True, random_state=2018)
    #    cv_scores = []
    #    pred_full_test = 0
    #    pred_train = np.zeros([train_df.shape[0], 3])
    #    for dev_index, val_index in kf.split(train_X):
    #        dev_X, val_X = train_X.loc[dev_index], train_X.loc[val_index]
    #        dev_y, val_y = train_y[dev_index], train_y[val_index]
    #        pred_val_y, pred_test_y, model = runXGB(dev_X, dev_y, val_X, val_y, test_X, seed_val=0, colsample=0.7,eta=eta, gamma=gamma)
    #        pred_full_test = pred_full_test + pred_test_y
    #        pred_train[val_index,:] = pred_val_y
    #    cv_scores.append(metrics.log_loss(val_y, pred_val_y))
    #    pred_full_test = pred_full_test / 5.
    #    print("XGB on new variables, cv scores : ", np.mean(cv_scores))
    #    return pred_full_test

    model, cv_score, f1_score, precision_score = runXGB(train_X, train_y, test_X, test_y, test_X2=None)
    filename = 'data/btc_full_next_quarter_XGB.sav'
    pickle.dump(model, open(filename, 'wb'))

    #out_df = pd.DataFrame(pred_full_test)
    #out_df.columns = ['Long', 'Hold', 'Short']
    #out_df.insert(0, 'id', test_id)
    #out_df.to_csv(name+"_"+str(n_comp)+"_"+str(ngram_cv)+"_"+str(ngram_tfidf)+"_"+str(eta)+"_"+str(gamma)+"_submission.csv", index=False)

    ### Plot the important variables ###
    #fig, ax = plt.subplots(figsize=(12,12))
    #xgb.plot_importance(model, height=0.8, ax=ax)
    #plt.show()

    #cnf_matrix = confusion_matrix(val_y, np.argmax(pred_val_y,axis=1))
    #np.set_printoptions(precision=2)
    #print(cnf_matrix)

    #return np.mean(cv_scores)

    # Plot non-normalized confusion matrix
    #plt.figure(figsize=(8,8))
    #plt_confusion_matrix(cnf_matrix, classes=['EAP', 'HPL', 'MWS'],title='Confusion matrix of XGB, without normalization')
    #plt.show()

    sys.stdout.close()
    sys.stdout = saved_stdout
    
    return cv_score, f1_score, precision_score
