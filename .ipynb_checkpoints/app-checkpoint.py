import streamlit as st
import joblib
import numpy as np 

model = joblib.load('gb_booking_model.pkl')

st.title("Hotel Booking Cancellation Predictor")
st.divider()
st.write("Enter booking details to predict cancellation. ")

lead_time = st.slider("lead Time", 0, 500, 50)
avg_price = st.number_input("Average Price per Room", 0.0, 500.0, 100.0)
special_requests = st.slider("Number of Special Requestes", 0, 5, 1)
total_guests = st.slider("Total Guests", 1, 10, 2)
total_nights = st.slider("Total Nights", 1, 20, 3)
repeated_guest = st.selectbox("Repeated Guest", [0,1])

if st.button("Predict"):
    input_data = np.array([[
        'lead_time',
         'avg_price_per_room',
         'no_of_special_requests',
         'total_guests',
         'total_nights',
         'repeated_guest'  
    ]])
    prediction = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.success(f"Prediction: Not canceled (Probability: {prob:.2f})")
    else:
        st.error(f"Prediction: Canceled (Probability: {1 - prob:.2f})")