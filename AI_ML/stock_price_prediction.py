import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def prepare_data(df,forecast_col,forecast_out,test_size):
    label = df[forecast_col].shift(-forecast_out) #creating new column called label with the last 5 rows are nan
    X = np.array(df[[forecast_col]]) #creating the feature array
    X = preprocessing.scale(X) #processing the feature array
    X_lately = X[-forecast_out:] #creating the column i want to use later in the predicting method
    X = X[:-forecast_out] # X that will contain the training and testing
    label.dropna(inplace=True) #dropping na values
    y = np.array(label)  # assigning Y
    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size=test_size, random_state=0) #cross validation

    response = [X_train,X_test , Y_train, Y_test , X_lately]
    return response


df = pd.read_csv("prices.csv")
# df_close = df[:30][['Date']] #selecting only the date and close columns
df_close = df["Close"]

forecast_col = "Close"
forecast_out = 5
test_size = 0.2

X_train, X_test, Y_train, Y_test , X_lately = prepare_data(df,forecast_col,forecast_out,test_size); #calling the method were the cross validation and data preparation is in
learner = LinearRegression() #initializing linear regression model

learner.fit(X_train,Y_train) #training the linear regression model

score=learner.score(X_test,Y_test) #testing the linear regression model
forecast= learner.predict(X_lately) #set that will contain the forecasted data
response={} #creating json object
response['test_score']=score
response['forecast_set']=forecast


print(df)
# print(df.index)
# print(response) #loc method to access a group of rows and columns by label(s) or a boolean array.
# print(df.head()) # By default, head() & tail() returns the first & last 5 rows
# print(df.tail(10))
# print(df.describe()) #descriptive statistics