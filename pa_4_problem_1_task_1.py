# -*- coding: utf-8 -*-
"""PA-4-Problem-1-Task-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mXitR2UOX25-B5eP5P86Ap8V2hydcgbn
"""

#This is a helper code for problem-1 (Task-1) of PA-4
#Complete this code by writing the function definations
#Compute following terms and print them:\\
#1. Difference of class wise means = ${m_1-m_2}$\\
#2. Total Within-class Scatter Matrix $S_W$\\
#3. Between-class Scatter Matrix $S_B$\\
#4. The EigenVectors of matrix $S_W^{-1}S_B$ corresponding to highest EigenValue\\
#5. For any input 2-D point, print its projection according to LDA.

import csv
import numpy as np

def ComputeMeanDiff(X):
  return(0)

def ComputeSW(X):
  return(0)

def ComputeSB(X):
  return(0)

def GetLDAProjectionVector(X):
  return(0)

def project(x,y,w):
  return(0)

#########################################################
###################Helper Code###########################
#########################################################

X = np.empty((0, 3))
with open('data.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for sample in csvFile:
        X = np.vstack((X, sample))

print(X)
print(X.shape)
# X Contains (x,y) and class label 0.0 or 1.0

opt=int(input("Input your option (1-5): "))

match opt:
  case 1:
    meanDiff=ComputeMeanDiff(X)
    print(meanDiff)
  case 2:
    SW=ComputeSW(X)
    print(SW)
  case 3:
    SB=ComputeSB(X)
    print(SB)
  case 4:
    w=GetLDAProjectionVector(X)
    print(w)
  case 5:
    x=int(input("Input x dimension of a 2-dimensional point :"))
    y=int(input("Input y dimension of a 2-dimensional point:"))
    w=GetLDAProjectionVector(X)
    print(project(x,y,w))