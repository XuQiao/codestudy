import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score

train_df = pd.read_csv("../input/train.csv")
test_df = pd.read_csv("../input/test.csv")

unigrams_pipeline = Pipeline([('text', CountVectorizer()),('mnb', MultinomialNB())])
unigrams_pipeline.fit(train_df.text, train_df.author)

predictions = pd.DataFrame(
    unigrams_pipeline.predict_proba(test_df.text),
    columns=unigrams_pipeline.classes_
                           )
predictions['id'] = test_df['id']
predictions.to_csv("submission.csv", index=False, columns=['id','EAP','HPL','MWS'])
