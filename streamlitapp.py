import numpy as np
import joblib
import streamlit as st

# Load the pre-trained model
model = joblib.load(open("diabetes_model.pkl","rb"))

# creating a function for prediction

def diabetes_prediction(input_data):
    #converting input data into np array

    array = np.asarray(input_data)

    #reshaping np array
    reshaped_array = array.reshape(1,-1)  

    #prediction
    prediction = model.predict(reshaped_array) 
    print(prediction)

    if (prediction[0] == 0):
        return "High risk of Diabetes."
    else:
        return "Low risk of Diabetes."
    
def main():
       
    #Title of webb app
    st.title("Diabetes Prediction Web App")
    st.write("Enter patient details to predict diabetes risk.")
    
    #Input fields for user data
    Pregnancies = st.text_input("Number of Pregnancies")
    Glucose = st.text_input("Glucose levels")
    BloodPressure = st.text_input("Blood Pressure value")
    SkinThickness = st.text_input("Skin Thickness value")
    Insulin = st.text_input("Insulin level")
    BMI = st.text_input("BMI value")
    DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function value")
    Age = st.text_input("Age of the person")

   #code for prediction
    diagnosis = ''

   #creating button for prediction
    if st.button("Diabetes Test Result"):
        diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])

    st.success(diagnosis)


if __name__ == '__main__':
    main()


