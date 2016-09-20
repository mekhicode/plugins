# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from sklearn import cross_validation as cv
from sklearn.metrics.pairwise import pairwise_distances


header = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('ml-100k/u.data', sep='\t', names=header)

n_users = df.user_id.unique().shape[0]
n_items = df.item_id.unique().shape[0]
#
# train_data, test_data = cv.train_test_split(df, test_size=0.25)
# print 'Number of users = ' + str(n_users) + ' | Number of movies = ' + str(n_items)

