﻿﻿﻿﻿
##  Phishing Detection using Machine Learning

This Google chrome extension purpose is to identify and evaluate if they are deemed phishing or legitimate based on the URLS.  It is built with the understanding to **aid privacy, so that the user data browsing pattern is not collected.** 

Dataset:  [UCI repository](https://archive.ics.uci.edu/ml/datasets/phishing+websites) 

Machine Learning Technique used : Random Forest Classifier

## Step 1: Dataset

Dataset is taken from [UCI repository](https://archive.ics.uci.edu/ml/datasets/phishing+websites).

First, download the dataset and save it as `dataset.arff`.  The arff file is then loaded by `preprocess.py` in order to convert it to an array. Additionally the dataset is split for training and testing where **30%** is for testing set. 

Once this is completed - 

Change to `/backend/dataset` directory and run the file `preprocess.py` which will result into creating training and test data in a `*.npy` file into main working directory.

## Step 2:  Training and Exporting RandomForest

RandomForest an *(ensemble learner)* is then fit  with the training set and then,  Accuracy and Cross validation scores are printed to evaluate the performance of the model. 

Change working directory to `/backend/classifier` and Run    
> `training.py`

`classifier.py` is created into directory named `/static`.  


## Step 3:  Load/Install  the plugin extension

This requires you to turn on developer mode in chrome extensions. Navigate to `chrome://extensions/` on your google browser and turn on developer mode.

1.  Select **load unpacked** and choose the `frontend` directory of this repository.



## Requirements:
````
Libraries:
Python3.x
sklearn
numpy
liac-arff














