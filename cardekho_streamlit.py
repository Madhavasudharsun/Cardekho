import streamlit as st
import pickle
import numpy as np
from PIL import Image
#from sklearn.ensemble import GradientBoostingRegressor
model_path = "C:/Users/Madhava/Downloads/gb_car.pkl"
with open(model_path, 'rb') as file:
    model = pickle.load(file)
# Input feature names
input_features = ['modelYear', 'RTO', 'Year of Manufacture', 'Driving Experience Control Eco',
                  'Max Power', 'Width', 'Wheel Base', 'Rear Tread', 'Kerb Weight', 'Acceleration']
# RTO mappings for selected states
rto_mappings = {"Karnataka": {"KA51": 100,"KA05": 81,"KA03": 79,},"Tamil Nadu": {"TN10": 112,"TN09": 172,"TN19": 269,},"Maharashtra": {"MH48": 45,"MH02": 123,"MH04": 120,},}

# Streamlit app
st.title("Used Car Price Prediction")

# Sidebar for input features
st.sidebar.header("Input Parameters")

# Create sidebar inputs for each parameter
params = {}
params['modelYear'] = st.sidebar.slider('Model Year', 1980, 2025, 2015)
selected_state = st.sidebar.selectbox('State', list(rto_mappings.keys()))
selected_rto_code = st.sidebar.selectbox('RTO', list(rto_mappings[selected_state].keys()))

# Map the selected RTO code to its corresponding numerical value
params['RTO'] = rto_mappings[selected_state][selected_rto_code]
params['Year of Manufacture'] = st.sidebar.slider('Year of Manufacture', 1980, 2025, 2014)
# Use dropdowns with Yes/No options for binary features
params['Driving Experience Control Eco'] = st.sidebar.selectbox('Driving Experience Control Eco', ['Yes', 'No'])
params['Driving Experience Control Eco'] = 1 if params['Driving Experience Control Eco'] == 'Yes' else 0
params['Max Power'] = st.sidebar.slider('Max Power (in hp)', 50, 600, 150)
params['Width'] = st.sidebar.slider('Width (in mm)', 1000, 2500, 1800)
params['Wheel Base'] = st.sidebar.slider('Wheel Base (in mm)', 2000, 4000, 2700)
params['Rear Tread'] = st.sidebar.slider('Rear Tread (in mm)', 1000, 2500, 1500)
params['Kerb Weight'] = st.sidebar.slider('Kerb Weight (in kg)', 500, 3000, 1500)
params['Acceleration'] = st.sidebar.slider('Acceleration (0-100 km/h in seconds)', 2, 15, 10)

# Display an image in the center (use a valid image URL or local path)
st.image("C:/Users/Madhava/Downloads/original.png", caption="Used Car Price Prediction", use_column_width=True)

# Convert the params to a format that the model can use for prediction
input_data = np.array([params[feature] for feature in input_features]).reshape(1, -1)

# Predict the car price
predicted_price = model.predict(input_data)[0]

# Display the result
st.write(f"The predicted car price is: ₹{predicted_price:,.2f}")
