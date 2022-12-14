# -*- coding: utf-8 -*-
"""Feynn labs.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UcB1H2Fbcel245IqaimALGnx8feD93Pp
"""

# Commented out IPython magic to ensure Python compatibility.
# data visualisation and manipulation
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline 
from datetime import datetime
import calendar


#label Encoding on Train and Test 
from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
from sklearn.preprocessing import LabelEncoder


#model selection
from sklearn.model_selection import train_test_split,cross_validate
from sklearn.model_selection import GridSearchCV

#import the necessary modelling algos
from sklearn.ensemble import RandomForestRegressor,BaggingRegressor,GradientBoostingRegressor,AdaBoostRegressor
#from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor


#evaluation metrics
from sklearn.metrics import mean_squared_log_error,mean_squared_error, r2_score,mean_absolute_error

data=pd.read_csv('/content/traindataset.txt')
data1=pd.read_csv('/content/testdataset.txt')

data.head()

data1.head()

# Shape of the dataset
print('Shape of the Train data:',data.shape)
print('Shape of the Test data:',data1.shape)

# Checking the data types of each column of this dataset.
print('Data type of Train data :\n', data.dtypes,'\n\n')
print('Data type of Test data :\n', data1.dtypes)

# Checking the columns of both the data.
print('Columns of Train data :\n' , data.columns,'\n\n\n')
print('Columns of Test data :\n', data1.columns)

# Information of both the data
print( data.info(),'\n\n')
print( data1.info())

# Describe both data
data.describe()

data1.describe()

data["date"] = data.datetime.apply(lambda x : x.split()[0])
data["day"] = data.datetime.apply(lambda x : x.split()[0].split("-")[2])
data["hour"] = data.datetime.apply(lambda x : x.split()[1].split(":")[0])
data["year"] = data.datetime.apply(lambda x : x.split()[0].split("-")[0])
data["weekday"] = data.date.apply(lambda x : calendar.day_name[datetime.strptime(x,"%Y-%m-%d").weekday()])
data["month"] = data.date.apply(lambda dateString : calendar.month_name[datetime.strptime(dateString,"%Y-%m-%d").month])

data.head()

data1["date"] = data1.datetime.apply(lambda x : x.split()[0])
data1["day"] = data1.datetime.apply(lambda x : x.split()[0].split("-")[2])
data1["hour"] = data1.datetime.apply(lambda x : x.split()[1].split(":")[0])
data1["year"] = data1.datetime.apply(lambda x : x.split()[0].split("-")[0])
data1["weekday"] = data1.date.apply(lambda x : calendar.day_name[datetime.strptime(x,"%Y-%m-%d").weekday()])
data1["month"] = data1.date.apply(lambda dateString : calendar.month_name[datetime.strptime(dateString,"%Y-%m-%d").month])

data1.head()

# Number of unique values in each columns and unique values in each columns.

for i in data.columns:
    print("Unique value of = {} [[{}]]\n{}\n".format(i, len(data[i].unique()), data[i].unique()))

plt.figure(figsize=(15,15))    
ax = sns.heatmap(data.corr(), cmap = "coolwarm", annot=True, linewidth=1)
bottom, top = ax.get_ylim()

print(data1.hour.value_counts())
values=data1['hour'].value_counts().values
label=['00', '01', '02', '03', '04', '05','06', '07', '08', '09', '10', '11','12','13','14', '15','16','17','18','19', '20', '21', '22', '23']
fig,ax1=plt.subplots()
ax1.pie(values,labels=label,shadow=True,startangle=200,autopct='%1.1f%%')
plt.show()

sns.barplot(x='hour',y='count',data=data1,estimator = np.sum)
label=['00', '01', '02', '03', '04', '05','06', '07', '08', '09', '10', '11','12','13','14', '15','16','17','18','19', '20', '21', '22', '23']
plt.show()

print(data1.season.value_counts())
values=data1['season'].value_counts().values
label=[ "Spring", "Summer", "Fall", "Winter"]
fig,ax1=plt.subplots()
ax1.pie(values,labels=label,shadow=True,startangle=90,autopct='%1.1f%%')
plt.show()

sns.barplot(x='season',y='count',data=data1,estimator = np.sum)
label=[ "Spring", "Summer", "Fall", "Winter"]
plt.show()

print(data1.holiday.value_counts())
values=data['holiday'].value_counts().values
label=[0,1]
fig,ax1=plt.subplots()
ax1.pie(values,labels=label,shadow=True,startangle=90,autopct='%1.1f%%')
plt.show()

sns.barplot(x='holiday',y='count',data=data1, estimator = np.sum)
label=[0,1]
plt.show()

print(data1.weather.value_counts())
values=data1['weather'].value_counts().values
label=[" Clear + Few clouds + Partly cloudy + Partly cloudy", " Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist ",  " Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds", " Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog "]
fig,ax1=plt.subplots()
ax1.pie(values,labels=label,shadow=True,startangle=120,autopct='%1.1f%%')
plt.show()

sns.barplot(x='weather',y='count',data=data1,estimator = np.sum)
label=[" Clear + Few clouds + Partly cloudy + Partly cloudy", " Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist ",  " Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds", " Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog "]

plt.show()

print(data1.weekday.value_counts())
values=data1['weekday'].value_counts().values
label=['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
fig,ax1=plt.subplots()
ax1.pie(values,labels=label,shadow=True,startangle=90,autopct='%1.1f%%')
plt.show()

print(data1.month.value_counts())
values=data1['month'].value_counts().values
label=['January', 'February', 'March', 'April', 'May', 'June','July', 'August', 'September', 'October', 'November', 'December']
fig,ax1=plt.subplots()
ax1.pie(values,labels=label,shadow=True,startangle=150,autopct='%1.1f%%')
plt.show()

sns.barplot(x='weekday',y='count',data=data1, estimator = np.sum)
label=['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
plt.show()

data1  = data1.drop(["datetime", 'casual', 'registered','date' ],axis=1)

data1.head()

data=data.drop(['date'],axis=1)

data.shape

# Train data set
print(data1.isnull().sum())

# Visualizing the same using heatmap.
sns.heatmap(data1.isnull(), cmap = 'YlGnBu')

# Train data set
print(data.isnull().sum())

# Visualizing the same using heatmap.
sns.heatmap(data.isnull(), cmap = 'YlGnBu')

sns.boxplot(data=data1[['temp','atemp', 'humidity', 'windspeed', 'count']])
fig=plt.gcf()
fig.set_size_inches(10,10)

cnames = ['temp','atemp', 'humidity', 'windspeed', 'count']
for i in cnames:
    print(i)
    q75, q25 = np.percentile( data1.loc[:,i],[75,25])
    iqr = q75-q25
    min = q25-(iqr*1.5)
    max = q75+(iqr*1.5)
    print(min)
    print(max)
   
    data1= data1.drop( data1[ data1.loc[:,i] < min].index)
    data1 = data1.drop( data1[ data1.loc[:,i] > max].index)

data1.shape

#Train data
data1['weekday']=label_encoder.fit_transform(data1['weekday'])
data1['month']=label_encoder.fit_transform(data1['month'])
data1['year']=label_encoder.fit_transform(data1['year'])

#Test data
data['weekday']=label_encoder.fit_transform(data['weekday'])
data['month']=label_encoder.fit_transform(data['month'])
data['year']=label_encoder.fit_transform(data['year'])

object_Variable_List = ["hour",'day']
for i in object_Variable_List:
    data1[i] = data1[i].astype("int64")
    data[i] = data[i].astype("int64")

data1.dtypes

data.dtypes

X = data1.drop('count', axis=1)
Y = data1['count']

# Let's check the Shape of Input and Output variables.

print(X.shape)
print(Y.shape)

X.head()

# Checking the Dependent variable.

Y.head()

# Importing library for split Train data
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,random_state=42,test_size=0.25)

models=[RandomForestRegressor(),AdaBoostRegressor(),BaggingRegressor(),KNeighborsRegressor()]
model_names=['RandomForestRegressor','AdaBoostRegressor','BaggingRegressor','KNeighborsRegressor']
r2score=[]
d={}
for model in range (len(models)):
    clf=models[model]
    clf.fit(X_train,Y_train)
    test_pred=clf.predict(X_test)
    r2score.append(np.sqrt(r2_score(test_pred,Y_test)))
d={'Modelling Algo':model_names,'R2_error':r2score}

d

rmsle_frame=pd.DataFrame(d)
rmsle_frame

#for random forest regresion.
no_of_test=[500]
params_dict={'n_estimators':no_of_test,'n_jobs':[-1],'max_features':["auto",'sqrt','log2']}
clf_rf=GridSearchCV(estimator=RandomForestRegressor(),param_grid=params_dict,scoring='neg_mean_squared_log_error')
clf_rf.fit(X_train,Y_train)
pred=clf_rf.predict(X_test)
print((np.sqrt(mean_squared_log_error(pred,Y_test))))

pred=clf_rf.predict(data.drop('datetime',axis=1))
d={'datetime':data['datetime'],'count':pred}
ans=pd.DataFrame(d)
ans.to_csv('answer.csv',index=False)

pd.read_csv('answer.csv')



