from flask import Flask, request, render_template
import numpy as np
import pickle


app = Flask(__name__)


model = None
label_encoders = None


try:
    with open('vegetable_price_model.pkl', 'rb') as f:
        model = pickle.load(f)

    with open('label_encoders.pkl', 'rb') as f:
        label_encoders = pickle.load(f)
    
    print("Model and encoders loaded successfully!")
except Exception as e:
    print(f"Error loading model or encoders: {e}")

@app.route('/', methods=['GET', 'POST'])
def home():
    predicted_price = None  
    
    if request.method == 'POST':
        if model is None or label_encoders is None:
            return "Model or encoders not loaded properly. Please check server logs for errors."

        
        vegetable = request.form['vegetable']
        season = request.form['season']
        month = request.form['month']
        temp = int(request.form['temp'])
        disaster = request.form['disaster']
        condition = request.form['condition']

        
        print("Available keys in label_encoders:", label_encoders.keys())

        try:
            
            vegetable_encoded = label_encoders['Vegetable'].transform([vegetable])[0]
            season_encoded = label_encoders['Season'].transform([season])[0]
            month_encoded = label_encoders['Month'].transform([month])[0]
            disaster_encoded = label_encoders['Deasaster Happen in last 3month'].transform([disaster])[0]
            condition_encoded = label_encoders['Vegetable condition'].transform([condition])[0]

            
            features = np.array([[vegetable_encoded, season_encoded, month_encoded, temp, disaster_encoded, condition_encoded]])

            
            predicted_price = model.predict(features)[0]
            predicted_price = round(predicted_price, 2)  

        except KeyError as e:
            
            print(f"KeyError: {e} - Check that the column names match exactly in both the dataset and the label encoders.")
            return f"Error: {e}. Please ensure that the vegetable, season, month, disaster, and condition are correctly entered."

        except Exception as e:
            
            print(f"Error during prediction: {e}")
            return f"An error occurred: {e}. Please try again."

    
    return render_template('index.html', prediction=predicted_price)

if __name__ == '__main__':
    app.run(debug=True)
