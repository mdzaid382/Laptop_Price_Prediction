# Laptop Price Prediction

What if we have a system that can predict the prices of products that we use in our routine life.That's exactly
  what my poject aim to do.
 Using Machine Learning Algorithm i built a smart system that learns from the data and predicts the prices of Laptops 
  available in market.
 In this project i went through the all steps of Machine Learning Life-Cycle.
## 1.Data Gathering
- The first main step is to gather the data. i used the laptop price dataset from the kaggle.it contains the various feature columns like Brand,Processor,Gpu,Operating system,Ram,SSD etc and one target column that is Price.

## 2.Data Cleaning and Preprocessing
- Raw data, is often messy and unstructured. Data cleaning involves addressing issues such as missing values, outliers that could compromise the accuracy of the machine learning model.

## 3.EDA
- Now, focus turns to understanding the underlying patterns and characteristics of the collected data. Exploratory Data Analysis (EDA) phase, where various statistical and visual tools are use to gain insights into the dataset's structure.
- To visualise the data i got the help of Seaborn and matplotlib liberaries.

## 4.Feature Engineering and Selection
- Feature engineering elevates raw data into meaningful predictors. Simultaneously, feature selection identifies the most relevant features to enhance model efficiency and effectiveness.

## 5.Model Selection
-  Model selection is a pivotal decision that determines the predictive capabilities of the machine learning solution. The choice depends on the nature of the data, the complexity of the problem, and the desired outcomes.
- After testing various machine learning Algorithm i select the XGBoost Algorithm due to its highest accuracy among all the other Algorithm.

## 6.Model Training
- This process involves exposing the model to historical data, allowing it to learn patterns, relationships, and dependencies within the dataset.
- After training our model is ready to predict the prices of laptop. 

## 7.Deploying 
- Last step is to deploy our model to website. i used the streamlit library to built web-application and streamlit cloud services to host my Laptop Price Pridiction Website.
  


# Dependencies
- Python
- Numpy
- Pandas
- Seaborn
- Matplotlib
- Scikit-learn
- XGBoost
