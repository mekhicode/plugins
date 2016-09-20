#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import jieba
from jieba.analyse import extract_tags
dir_temp = 'xxx.json'
file = open(dir_temp)
file_data = file.read()

def cosine(rate1, rate2):
    sum_xy = 0
    sum_x = 0
    sum_y = 0
    n = 0
    for key in rate1:
        if key in rate2:
            n += 1
            x = rate1[key]
            y = rate2[key]
            sum_xy += x*y
            sum_x += x*x
            sum_y += y*y

    if n == 0:
        return 0
    else:
        sx = pow(sum_x, 1/2)
        sy = pow(sum_y, 1/2)
        if sum_xy != 0:
            denominator = sx*sy/sum_xy
        else:
            denominator = 0
    return denominator

#返回最近距离用户
def computeNearestNeighbor(username,users):
    distances = []
    for key in users:
        if key != username:
            distance = cosine(users[username], users[key])
            distances.append((distance, key))
    distances.sort(reverse=True)
    return distances


def recommend(username, users):
    print computeNearestNeighbor(username, users)
    nearest = computeNearestNeighbor(username, users)[0][1]
    recommendations =[]
    # neighborRatings = users[nearest]
    # for key in neighborRatings:
    #     if not key in users[username]:
    #         recommendations.append((key, neighborRatings[key]))
    # recommendations.sort(key=lambda rat: rat[1], reverse=True)
    return recommendations

def get_result():
    users = dict()
    for i in json.loads(file_data)['results']:
        try:
            category = ''.join(i.get('category'))
            tags = ''.join(i.get('tags'))
            # color = i['color']['name']
            # spider_desc_product = i['spider_desc_product']
            # name = i['name']
            # desc_product = i['desc_product']
            # scene = ''.join(i['scene'])
            # brand = i['brand']
            str_data = category + tags  #  + color + spider_desc_product + name + desc_product + scene + brand
            str_data = str_data.replace('\n', '').replace('\r', '').replace('\t', '')
            temp_dict = dict()
            for key in extract_tags(str_data, topK=200):
                temp_dict[key] = 1

            users[i['objectId']] = temp_dict

        except:
            continue

    return users

print recommend("56c69ff2d342d30053d4a215", get_result())
