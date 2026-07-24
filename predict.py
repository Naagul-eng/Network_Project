import joblib
import pandas as pd

model = joblib.load('traffic_model.pkl')

sample = pd.DataFrame({
    'pps': [120],
    'avg_size': [850]
})

prediction = model.predict(sample)
print("Traffic type:", prediction[0])