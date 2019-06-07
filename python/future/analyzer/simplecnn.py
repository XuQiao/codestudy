import numpy as np
import pandas as pd
from keras.datasets import imdb
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM, Dropout, Flatten, RNN, SimpleRNN
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D, AveragePooling1D
from keras.layers.embeddings import Embedding
from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer
from keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder, LabelBinarizer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, HashingVectorizer
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import pickle, h5py
import time, sys
from datetime import datetime


# fix random seed for reproducibility
np.random.seed(7)
def runcnn(startday = -1, endday = 0):
    now = datetime.now()
    now = time.mktime(now.timetuple())
    trainall_df = pd.read_csv("data/btc_usd_matrix_full_next_quarter_future.csv",sep='\t',index_col=0)
    if startday < 0:
        startindex = 0
    else:
        startindex = trainall_df['date'].searchsorted(now - startday * 24 * 3600)[0]
    endindex = trainall_df['date'].searchsorted(now - endday * 24 * 3600)[0]
    trainall_df = trainall_df.dropna(axis=0)
    trainall_df = trainall_df.iloc[startindex:endindex]
    trainall_df1 = trainall_df.drop(['date', 'flag','open','high','low','close'],axis=1)
    trainall_df1 = trainall_df1.as_matrix()
    trainall_df1 = np.expand_dims(trainall_df1, axis=2)
    flag_df = trainall_df['flag']
    flag_df = LabelEncoder().fit_transform(flag_df)
    flag_df = to_categorical(flag_df)

    saved_stdout = sys.stdout
    sys.stdout = open('data/class_report_cnn.txt', 'w')

    X_train, X_test, y_train, y_test = train_test_split(trainall_df1, flag_df, test_size = 0.2, random_state = 1)
    # create the model
    embedding_vecor_length = 32
    model = Sequential()
    #model.add(Embedding(top_words, output_dim=embedding_vecor_length))
    #model.add(Conv1D(filters=64, kernel_size=4, padding='same', activation='relu',input_shape=X_train.shape[1:]))
    #model.add(AveragePooling1D(pool_size=2))
    #model.add(Conv1D(filters=4, kernel_size=12, padding='same', activation='sigmoid'))
    #model.add(Conv1D(filters=5, kernel_size=20, padding='same', activation='relu'))
    #model.add(AveragePooling1D(pool_size=2))
    model.add(Dropout(0.1))
    model.add(LSTM(50))
    #model.add(SimpleRNN(20))
    #model.add(LSTM(200))
    #model.add(LSTM(100, input_shape = X_train.shape[1:]))
#    model.add(LSTM(100))
    #model.add(Dense(20))
    #model.add(Flatten())
    #model.add(LSTM(50))
    #model.add(Dense(10, activation='sigmoid'))
    model.add(Dense(3, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    print(model.summary())
    model.fit(X_train, y_train, epochs=3, batch_size=32)
    #Once fit, we estimate the performance of the model on unseen reviews.


    # Final evaluation of the model
    scores = model.evaluate(X_test, y_test, verbose=1)
    print("Loss: %.3f, Accuracy: %.3f%%" % (scores[0], scores[1]*100))
    #For completeness, here is the full code listing for this LSTM network on the IMDB dataset.

    y_pred = model.predict(X_test, verbose=1)
    y_true = y_test
    #print(y_pred[:4], y_true[:4])
    log_loss = metrics.log_loss(y_true, y_pred)
    cnf_matrix = confusion_matrix(np.argmax(y_true, axis=1), np.argmax(y_pred, axis=1))
    np.set_printoptions(precision=2)
    print("Loss: %.3f" % (log_loss))
    print(cnf_matrix)

    ##k=flod
    #seed = 1
    #kfold = KFold(n_splits = 10, shuffle = True, random_state = seed)
    #results = cross_val_score(model, X_test, y_test, cv = kfold)
    #print("%2.f%(%.2f%%) " % (results.mean()*100, results.std()*100))

    #sub = model.predict(X_sub, verbose = 1)
    #predictions = pd.DataFrame(sub, columns=[''])
    #predictions['id'] = test_df['id']
    #predictions.to_csv("cnn_submission.csv", index=False, columns=['id','EAP','HPL','MWS'])
    filename = 'data/btc_full_next_quarter_CNN.sav'
    #pickle.dump(model, open(filename, 'wb'))
    model.save(filename)

runcnn()
