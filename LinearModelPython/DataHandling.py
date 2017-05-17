# -*- coding: utf-8 -*-
"""
Created on Tue May 16 17:29:42 2017

@author: Garbojax
"""

class DataPoint:
    #properties
    inputs = "None"
    output = 0
    
    #main constructor
    def __init__(self, inputs, output):
        self.output = float(output)
        self.inputs = [1.]
        for val in inputs:
            self.inputs.append(float(val))
        

class DataSet:
    #properties
    number_examples = 0
    input_size = 0
    examples = "None"
    
    #main constructor
    def __init__(self, points):
        self.examples = []
        for point in points:
            self.examples.append(point)
        self.number_examples = len(self.examples)
        
    #other constructorz
    def DataSetFromFile(fileName):
        ds = DataSet([])
        file = open(fileName, "r+")
        examples = file.read().split("\n")
        file.close()
        for example in examples:
            inpt = []
            output = 0
            vals = example.split(",")
            for x in range(0, len(vals)):
                if x == (len(vals) - 1):
                    output = float(vals[x])
                else:
                    inpt.append(float(vals[x]))
            ds.examples.append(DataPoint(inpt, output))
        ds.number_examples = len(ds.examples)
        return ds
