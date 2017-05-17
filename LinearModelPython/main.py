# -*- coding: utf-8 -*-
"""
Created on Tue May 16 17:45:44 2017

@author: Garbojax
"""

import DataHandling as dh
import LogisticRegression as lh
import datetime as dt

test_data = "TestDataSet.txt"
test_logit = "TestLogit.txt"
training = "scaleTrain.txt"
testing = "scaleTest.txt"

ds = dh.DataSet.DataSetFromFile(test_data)
training = dh.DataSet.DataSetFromFile(training)
testing = dh.DataSet.DataSetFromFile(testing)
    
logit = lh.LogisticRegression(test_logit)

total_wrong = 0
for point in training.examples:
    logit.compute_output(point.inputs)
    temp = 1
    if logit.output < .5:
        temp = -1
    if(temp != point.output):
        total_wrong += 1
        
print("{}".format(total_wrong / training.number_examples))

total_wrong = 0
for point in testing.examples:
    logit.compute_output(point.inputs)
    temp = 1
    if logit.output < .5:
        temp = -1
    if(temp != point.output):
        total_wrong += 1
        
print("{}".format(total_wrong / testing.number_examples))

logit.max_itterations = 10000
logit.learn(training)

total_wrong = 0
for point in training.examples:
    logit.compute_output(point.inputs)
    temp = 1
    if logit.output < .5:
        temp = -1
    if(temp != point.output):
        total_wrong += 1
        
print("{}".format(total_wrong / training.number_examples))

total_wrong = 0
for point in testing.examples:
    logit.compute_output(point.inputs)
    temp = 1
    if logit.output < .5:
        temp = -1
    if(temp != point.output):
        total_wrong += 1
        
print("{}".format(total_wrong / testing.number_examples))
