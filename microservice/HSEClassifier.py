import pandas as pd
#import numpy as np
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

#text in column 1, classifier in column 2.
data = pd.read_csv('classifier.csv', encoding = 'ISO-8859-1') 

numpy_array = data.as_matrix()
X = numpy_array[:,0].astype('U')
Y = numpy_array[:,1].astype('U')

class text_clf:
	def __init__(self):
		self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(
		 X, Y, test_size=0.4, random_state=30)	

		self.clf = Pipeline([('vect', CountVectorizer(stop_words='english')),
		 ('tfidf', TfidfTransformer()),
		 ('clf', MultinomialNB()),
		])

		self.text_clf1 = self.clf.fit(self.X_train,self.Y_train)

#	uncomment to see accuracy of classifier on train/test splits
#	predicted_text = text_clf.predict(X_test)
#	predicted_accuracy = np.mean(predicted == Y_test)

		self.parameters = {'vect__ngram_range': [(1, 1), (1, 2)],
					   'tfidf__use_idf': (True, False),
					   'clf__alpha': (1e-2, 1e-3),
		}

		self.gs_clf = GridSearchCV(self.text_clf1, self.parameters, n_jobs=-1)
		self.gs_clf = self.gs_clf.fit(self.X_train,self.Y_train)