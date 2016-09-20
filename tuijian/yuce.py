# -*- coding: utf-8 -*-

temp = {'date_dict': [
      ("07-18", 32389), ("07-19", 59587), ("07-20", 42656), ("07-21", 52363),
      ("07-22", 45061), ("07-23", 47763), ("07-24", 47587), ("07-25", 42955),
      ("07-26", 53555), ("07-27", 39124), ]
}


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import random
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn import datasets, linear_model

def get_data():
    X_parameter = []
    Y_parameter = []
    for single_date, single_price in temp['date_dict']:
        X_parameter.append([int(single_date.replace('-', ''))])
        Y_parameter.append(float(single_price))
    return X_parameter, Y_parameter

def linear_model_main(X_parameters, Y_parameters, predict_value):
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    predict_outcome = regr.predict(predict_value)
    predictions = {}
    predictions['intercept'] = regr.intercept_
    predictions['coefficient'] = regr.coef_
    predictions['predicted_value'] = predict_outcome
    return predictions


def linear_model_main_temp(X_parameters, Y_parameters, predict_value):
    from sklearn.linear_model import LogisticRegression
    # print predict_value
    classifier = LogisticRegression()
    classifier.fit(X_parameters, Y_parameters)
    predict_outcome = classifier.predict(predict_value)
    # print predict_outcome
    predictions = {}
    predictions['intercept'] = classifier.intercept_
    predictions['coefficient'] = classifier.coef_
    predictions['predicted_value'] = predict_outcome
    return predictions


def show_linear_line(X_parameters,Y_parameters):
    # Create linear regression object
    regr = linear_model.LinearRegression()
    regr.fit(X_parameters, Y_parameters)
    plt.scatter(X_parameters,Y_parameters,color='blue')
    plt.plot(X_parameters,regr.predict(X_parameters),color='red',linewidth=4)
    plt.xticks(())
    plt.yticks(())
    plt.show()

X, Y = get_data()
print X
print Y
count = 664431
for predictvalue in ["7-28", "7-29", "7-30", "7-31"]:
    result = linear_model_main(X, Y, float(predictvalue.replace('-', '')))
    # print "Intercept value ", result['intercept']
    # print "coefficient", result['coefficient']
    print "Predicted value: ", result['predicted_value']
    count += result['predicted_value'][0]

print count
# print count + float(460000)

print "="*30

for predictvalue in ["7-28", "7-29", "7-30", "7-31"]:
# linear_model_main_temp(X, Y, map(lambda x: float(x.replace('-', '')), ["07-28", "07-29", "07-30", "07-31"]))
    result1 = linear_model_main_temp(X, Y, float(predictvalue.replace('-', '')))

    print "Predicted value: ", result1['predicted_value']
    # count += float(result['predicted_value'][0])

# print count + float(460000)

show_linear_line(X, Y)

