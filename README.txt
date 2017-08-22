Hey guys! Here are the basics behind this project:
It's a simple linear learning model project which has the perceptron, linear regression, and logistic regression.
You can create any of these models with a file like so:

<Models Name>
<Number of Inputs> (including bias)
Weight0,Weight1,Weight2,...,WeightN (Weight0 is the bias)

You will see the constructors for the models can take an integer or nothing at all if you want a new
model to use to learn something. Once your model has learned based on your data call the Save() method, if you have
the FileName property set, or Save("FileName") if you do not. Note the constructor taking a file path will set the 
property so you should not have to worry about it after that. Files are saved in the above format.

DataSets:
files with lines like the following:

input1,input2,...inputN,output

The bias input of 1 is handled by DataSet("DataFileName") constructor.



It's a fairly simple project, so if you just open it up I'm sure you can have it working in no time. Though as I 
did not have forever and a day to work on this it isn't filled with ALL the error checking and what not so you 
have to be gentle with it and give it the formats it wants.

I'm thinking about adding some methods to the DataSet class that would allow basic non-linear transforms to be 
implemented without ones having to do it manually, but that's for another day. 

I will also be adding a project for basic Neural Networks and Support Vector Machines, but that won't happen for 
a little while yet.

I know there are plenty of other things like this out there but I had fun making it. If I end up making something 
super awesome I will move it to my main github.

Hope you all enjoy.

=> Just added the python version. Was added fairly quickly just for practice in python and only has the logistic model
but seems to run okay. Did not test this one excessively as it was just for gaining familiarity with python
