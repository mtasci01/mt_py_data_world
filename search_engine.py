
import string
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import re

class SearchEngine:

  def search(self, q):

    if q is None:
      raise Exception("q is null")

    df_loc = pd.read_csv("resources/rss_ansa.csv", header=0,sep=';')

    docs = []
    docsOriginal = []
    TITLE_IX = 1
    CONTENT_IX = 2
    for row in df_loc.values:
      doc = row[TITLE_IX] + " " + row[CONTENT_IX]
      docOriginal = {}
      docOriginal["id"] = row[0]
      docOriginal["title"] = row[TITLE_IX]
      docOriginal["content"] = row[CONTENT_IX]
      docsOriginal.append(docOriginal)
      docs.append(doc)
        

    docsClean = []
    for d in docs:
        docClean = d.replace('%20', ' ')
        docClean = re.sub(r'@\w+', '', docClean)
        docClean = docClean.lower()
        docClean = re.sub(r'[%s]' % re.escape(string.punctuation), ' ', docClean)
        docClean = re.sub(r'\s{2,}', ' ', docClean)
        
        docsClean.append(docClean)   
    
    vectoriser = TfidfVectorizer()
    X = vectoriser.fit_transform(docsClean)
    X = X.T.toarray()
    df = pd.DataFrame(X, index=vectoriser.get_feature_names_out())

  
    q = [q]
    vec = vectoriser.transform(q).toarray().reshape(df.shape[0],)
    cosSim = {}
    for i in range(df.values.shape[1]):
      cosSim[i] = np.dot(df.loc[:,i].values, vec)/np.linalg.norm(df.loc[:, i])*np.linalg.norm(vec)
    
    cosSimSorted = sorted(cosSim.items(), key=lambda x: x[1], reverse=True)

    ret = []
    for i, v in cosSimSorted:
      if v != 0.0:
        ret.append(docsOriginal[i])
        
    return ret    
