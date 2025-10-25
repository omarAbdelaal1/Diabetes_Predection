# Diabetes Prediction Web Application

A machine learning-powered web application that predicts diabetes risk based on patient health data. Built with Python Flask backend and modern responsive frontend.

## 🎯 Project Overview

This application uses a trained machine learning model to predict diabetes risk by analyzing key health indicators including age, BMI, blood glucose levels, and medical history. The prediction helps users assess their diabetes risk and encourages early medical consultation.

## ✨ Features

- **Real-time Prediction**: Instant diabetes risk assessment
- **User-friendly Interface**: Modern, responsive web design with Bootstrap
- **Comprehensive Input**: Collects 8 key health indicators
- **Visual Feedback**: Clear results with color-coded alerts
- **Mobile Responsive**: Works seamlessly on all devices

## 🏗️ Project Structure

```
diabetes/
├── app.py                 # Flask web application
├── diabetes.ipynb        # Jupyter notebook with model training
├── diabetes.pkl          # Trained machine learning model
├── templates/
│   └── index.html        # Web interface
├── input/
│   └── diabetes_prediction_dataset.csv  # Training dataset
└── README.md             # This file
```

## 🔧 Technical Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Machine Learning**: scikit-learn, pandas, numpy
- **Model**: Random Forest Classifier, Decision Tree Classifier, Logistic Regression, XGBoost Classifier
- **Data Processing**: StandardScaler, LabelEncoder, train_test_split

## 📊 Dataset Features

The model analyzes the following health indicators:

| Feature | Description | Range/Values |
|---------|-------------|--------------|
| Gender | Biological sex | Male, Female |
| Age | Patient age in years | 0-80 |
| Hypertension | High blood pressure | 0 (No), 1 (Yes) |
| Heart Disease | Cardiovascular condition | 0 (No), 1 (Yes) |
| Smoking History | Tobacco use status | never, former, current, not current, others |
| BMI | Body Mass Index | 10.16-71.55 |
| HbA1c Level | Average blood sugar (2-3 months) | % |
| Blood Glucose | Current blood glucose level | mg/dL |

## 🚀 Installation & Setup

### Installation Steps

1. **Clone or download the project**
   ```bash
   cd path/to/folder
   ```

2. **Install required packages**
   ```bash
   pip install flask flask-cors joblib numpy scikit-learn pandas
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the application**
   - Open your browser and navigate to `http://localhost:5000`
   - The application will be running on port 5000

## 📱 Usage

1. **Fill the Form**: Enter your health information in the web form
2. **Submit**: Click the "Predict" button
3. **View Results**: 
   - ✅ **Green Alert**: Low diabetes risk
   - ⚠️ **Red Alert**: High diabetes risk (consult a doctor)

## 🔬 Model Details

- **Algorithm**: Random Forest Classifier
- **Training Data**: 100,000+ patient records
- **Features**: 8 health indicators
- **Target**: Binary classification (0: No Diabetes, 1: Diabetes)
- **Performance**: Optimized for accuracy and reliability

## ⚠️ Important Disclaimer

**This application is for educational and informational purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical concerns.**

## 🛠️ Development

### Model Training
The machine learning model was trained using the Jupyter notebook (`diabetes.ipynb`) which includes:
- Data preprocessing and cleaning
- Feature engineering
- Model training and evaluation
- Performance metrics analysis

### API Endpoints
- `GET /`: Serves the main web interface
- `POST /predict`: Returns diabetes prediction based on input data

## 📈 Future Enhancements

- [ ] User authentication and data persistence
- [ ] Detailed risk analysis and recommendations
- [ ] Integration with health tracking devices
- [ ] Multi-language support
- [ ] Advanced visualization of health trends

## 👨‍💻 Author

**Omar Abdelaal** - Machine Learning Engineer

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*Built with ❤️ for better health awareness*
