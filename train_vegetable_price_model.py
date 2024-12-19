import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error
import pickle

file_path = 'Vegetable_market.csv'  
data = pd.read_csv(file_path)

label_encoders = {}
categorical_columns = ['Vegetable', 'Season', 'Month', 'Deasaster Happen in last 3month', 'Vegetable condition']

for column in categorical_columns:
    if data[column].dtype == 'object':  
        data[column] = data[column].fillna('') 
        data[column] = data[column].str.lower() 

for column in categorical_columns:
    if data[column].dtype == 'object':  
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le

X = data.drop(columns='Price per kg')
y = data['Price per kg']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error: {mae}")

with open('vegetable_price_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('label_encoders.pkl', 'wb') as f:
    pickle.dump(label_encoders, f)

print("Model and encoders saved successfully!")
