import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def welcome():
  print("Welcome to the Salary Prediction System")
  print("Press ENTER Key to proceed")
  input()
  
  
def checkcsv():
  csv_files = []
  cur_dir = os.getcwd()
  
  content_list = os.listdir(cur_dir)
  
  for x in content_list:
    if x.split('.')[-1] == 'csv':
      csv_files.append(x)
      
  if len(csv_files) == 0:
    return 'No csv files in the directory'
  else:
    return csv_files
  
def display_and_select_csv(csv_files):
  i = 0
  for file_name in csv_files:
    print(i, '...', file_name)
    i += 1
    
  return csv_files[int(input("Select file to create ML model"))]

def graph(X_train, Y_train, regressionObject, X_test, Y_test, Y_pred):
  plt.scatter(X_train, Y_train, color='red', label='training data')
  plt.plot(X_train, regressionObject.predict(X_train), color='blue', label='Best Fit')
  plt.scatter(X_test, Y_test, color='green', label='test data')
  plt.scatter(X_test, Y_pred, color='black', label='Pred test data')
  
  plt.title("Salary vs Experience")
  plt.xlabel('Years of Experience')
  plt.ylabel("Salary")
  
  plt.legend()
  plt.show()
  
  
  