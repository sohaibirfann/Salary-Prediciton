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
  
  
  