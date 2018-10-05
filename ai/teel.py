import numpy as np
import pandas as pd
from hangle import normalize



def loading_data(data_path, eng=True, num=True, punc=False):
    # data example : "title","content"
    # data format : csv, utf-8
    corpus = pd.read_table(data_path, sep=",", encoding="utf-8")


    corpus = np.array(corpus)


    category = []
    contents = []
    for doc in corpus:

        if len( doc[0] ) > 0 :
            category.append( doc[0] )

        if type(doc[2]) is not str:
            continue
        if len(doc[2]) > 0:
            tmpcontents = normalize(doc[2], english=eng, number=num, punctuation=punc)
            contents.append(tmpcontents)

    return category , contents

