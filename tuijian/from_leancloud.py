#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from gensim import corpora,models,similarities,utils
import jieba
from jieba.analyse import extract_tags
import json

def etl(temp):
    return temp.replace(u'】', '').replace(u'【', '').replace(u"'", "'").replace(u'/', '')

file = open('leancloud_data.log')
train_set = []
line = file.readline()
while line:
    # line = line.encode('utf8')
    # print line.replace("u'", "'")
    # word_list = extract_tags(line)
    word_list = filter(lambda x: len(x) > 0, map(etl, jieba.cut(line, cut_all=False)))
    train_set.append(word_list)
    line = file.readline()
file.close()

# print train_set
# 生成字典
dictionary = corpora.Dictionary(train_set)
# 去除极低频的杂质词
dictionary.filter_extremes(no_below=1,no_above=1,keep_n=None)
# 将词典保存下来，方便后续使用
dictionary.save("all.dic")

corpus = [dictionary.doc2bow(text) for text in train_set]
tfidfModel = models.TfidfModel(corpus)
#存储tfidfModel
tfidfModel.save("allTFIDF.mdl")
#把全部语料向量化成TFIDF模式，这个tfidfModel可以传入二维数组
tfidfVectors = tfidfModel[corpus]
#建立索引并保存
indexTfidf = similarities.MatrixSimilarity(tfidfVectors)
indexTfidf.save("allTFIDF.idx")
#通过TFIDF向量生成LDA模型，id2word表示编号的对应词典，num_topics表示主题数，我们这里设定的50，主题太多时间受不了。
lda = models.LdaModel(tfidfVectors, id2word=dictionary, num_topics=50)
#把模型保存下来
lda.save("allLDA50Topic.mdl")
#把所有TFIDF向量变成LDA的向量
corpus_lda = lda[tfidfVectors]
#建立索引，把LDA数据保存下来
indexLDA = similarities.MatrixSimilarity(corpus_lda)
indexLDA.save("allLDA50Topic.idx")


