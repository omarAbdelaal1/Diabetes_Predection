from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

model = joblib.load('diabetes.pkl')

gender_map = {'Male': 1, 'Female': 0}
smoke_map = {'never': 0, 'former': 1, 'current': 2, 'not current': 3, 'others': 4}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        gender = gender_map.get(data['gender'], 0)
        age = float(data['age'])
        hypertension = int(data['hypertension'])
        heart_disease = int(data['heart_disease'])
        smoking_history = smoke_map.get(data['smoking_history'], 0)
        bmi = float(data['bmi'])
        HbA1c_level = float(data['HbA1c_level'])
        blood_glucose_level = float(data['blood_glucose_level'])
        features = np.array([[gender, age, hypertension, heart_disease, smoking_history, bmi, HbA1c_level, blood_glucose_level]])
        pred = model.predict(features)[0]
        return jsonify({'result': int(pred)})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
