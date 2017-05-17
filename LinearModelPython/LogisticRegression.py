# -*- coding: utf-8 -*-
"""
Created on Tue May 16 17:49:50 2017

@author: Garbojax
"""
import math
import DataHandling as dh

class LogisticRegression:
    #properties
    name = ""
    filepath = ""
    input_size = 0
    inputs = "none"
    output = 0
    weights = "none"
    in_sample_error = 0
    error_gradient = "none"
    learning_rate = .1
    max_error = .01
    max_itterations = 1000000
    
    #main constructor
    def __init__(self, filepath):
        file = open(filepath, "r+")
        lines = file.read().split("\n")
        file.close()
        
        self.name = lines[0]
        self.input_size = int(lines[1])
        self.weights = []
        self.inputs = []
        self.error_gradient = []
        self.filepath = filepath
        
        weights = lines[2].split(",")
        for w in weights:
            self.weights.append(float(w))
            
        for index in range(self.input_size):
            self.error_gradient.append(0)
            
    
    #methods
    def compute_non_sigmoid_output(self, inpt):
        total = 0.0
        if(len(inpt) != self.input_size):
            return
        else:
            for x in range(0, self.input_size):
                total += self.weights[x] * inpt[x]
        return total
    
    def compute_output(self, inpt):
        total = 0
        if(len(inpt) != self.input_size):
            return
        else:
            for x in range(0, self.input_size):
                total += self.weights[x] * inpt[x]
        self.output = 1 / (1 + math.exp(-1 * total))
        
    def compute_single_point_error(self, point):
        self.compute_output(point.inputs)
        error = math.log(1 + math.exp(-1 * self.output * point.output))
        return error
    
    def compute_in_sample_error(self, dataset):
        self.in_sample_error = 0
        for point in dataset.examples:
            self.in_sample_error += self.compute_single_point_error(point)
        self.in_sample_error /= dataset.number_examples
        
    def compute_error_gradient(self, dataset):
        for index in range(self.input_size):
            self.error_gradient[index] = 0.0
        
        for point in dataset.examples:
            total = self.compute_non_sigmoid_output(point.inputs)
            
            for index in range(self.input_size):
                self.error_gradient[index]  += (point.output * point.inputs[index]) / (1 + math.exp( point.output * total ) )
                               
        for index in range(self.input_size):
            self.error_gradient[index] /= (-1 * dataset.number_examples)
            
    def learn(self, dataset):
        self.compute_in_sample_error(dataset)
        itteration = 0
        while(self.in_sample_error > self.max_error):
            self.compute_error_gradient(dataset)
            for idx in range(self.input_size):
                self.weights[idx] = (self.weights[idx] - self.learning_rate
                            * self.error_gradient[idx])
            
            self.compute_in_sample_error(dataset)
            itteration += 1
            if(itteration > self.max_itterations):
                break
            
    def save(self):
        save_string = "{}\n{}\n".format(self.name, self.input_size)
        for x in range(0, self.input_size - 1):
            save_string += ("{},".format(self.weights[x]))
        save_string += "{}".format(self.weights[self.input_size - 1])
        file = open(self.filepath, "wb")
        file.write(bytes(save_string, "UTF-8"))
        file.close()