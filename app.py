import joblib

model = joblib.load("gb_booking_model.pkl")

print(type(model))
print(model)