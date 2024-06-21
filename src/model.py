import joblib

class Model:
    def __init__(self):
        self.model = joblib.load('model/catboost_model.pkl')

    def predict(self, input_features):
        return self.model.predict(input_features)

        # Add in this code chunk temporarily (delete it after this run)


cat_features = {
    "account_id": "AFEO-XOOCP",
    "has_internet_service": 1,
    "internet_type": "Fiber Optic",
    "has_unlimited_data": 1,
    "has_multiple_lines": 1,
    "contract_type": "Two Year",
    "paperless_billing": 1,
    "payment_method": "Credit Card",
    "stream_tv": 1,
    "stream_movie": 1,
    "gender": "Female",
    "senior_citizen": 1,
    "city": "Camarillo"
}
model_inputs = list(cat_features.values())

print(model_inputs)                  
print(Model().predict(model_inputs)) 