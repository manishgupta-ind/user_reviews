import pickle 
# import dill as pickle
import os
import pandas as pd
# import numpy as np
# from sklearn.preprocessing import LabelEncoder
# import multiprocessing as mp
# from multiprocessing.pool import ThreadPool as Pool
# import nltk
# from collections import Counter

current_path = os.getcwd()
model_path = os.path.join(current_path, 'static/')

happy_tc = pickle.load(open(model_path+"model.pkl", "rb"))

# label_encoder_r = LabelEncoder()
# label_encoder_r.classes_ = np.load(model_path+'\\classes.npy',allow_pickle=True)


# df_in = pd.read_csv(data_path+"chrome_reviews.csv")
# df_in = df_in[~df_in['Text'].isnull()]

# happy_tc = pickle.load(open('model.pkl', 'rb'))

def pred_label(text):    
    result = happy_tc.classify_text(text) 
    return result.label, result.score 

def predictor(df_in):
    df_in = df_in[~df_in['Text'].isnull()]
    df_in['sentiment'], df_in['score'] = zip(*df_in['Text'].apply(pred_label))

    df_out = df_in[(df_in['sentiment']=='POSITIVE') & (df_in['Star'] <=2)]
    df_out = df_out.drop(['sentiment','score'], axis=1)
    return df_out
