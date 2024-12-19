import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import LabelEncoder
import pickle


df = pd.read_csv('vegetable_market.csv')


le = LabelEncoder()
df['Vegetable'] = le.fit_transform(df['Vegetable'])
df['Season'] = le.fit_transform(df['Season'])
df['Month'] = le.fit_transform(df['Month'])
df['Deasaster Happen in last 3month'] = le.fit_transform(df['Deasaster Happen in last 3month'])
df['Vegetable condition'] = le.fit_transform(df['Vegetable condition'])

X = df.drop('Price per kg', axis=1)
y = df['Price per kg']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestRegressor(n_estimators=100, random_state=42)


model.fit(X_train, y_train)

print("Model training complete!")


with open('vegetable_model.pkl', 'wb') as f:
    pickle.dump(model, f)  
    print("Model saved to file!")


y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')
