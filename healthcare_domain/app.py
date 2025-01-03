import streamlit as st
import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

with open("random_forest_model_health.pkl", 'rb') as file:
    model = pickle.load(file)

st.title("Medical Test Results Classification")
st.write("This app classifies test results into Normal, Abnormal, Inconclusive.")

st.subheader("Enter Patient Information")

age = st.number_input("Age", min_value=0, max_value=120)
days = st.number_input("Days_numeric", min_value=0, max_value=120)
gender = st.selectbox("Gender",['Male','Female'])
blood_type = st.selectbox("Blood Type", ['B-','A+','A-','O+','AB+','AB-','B+','O-'])
medical_condition = st.selectbox("Medical Condition", ['Cancer','Obesity','Diabetes','Asthma','Hypertension','Arthritis'])
admission_type = st.selectbox("Admission Tyoe",['Urgent','Emergency','Elective'])
medication = st.selectbox("Medication",['Paracetmol','Ibuprofen','Aspirin','Penicillin','Lipitor'])

input_data = pd.DataFrame({
    'Age': [age],
    'Days_numeric':[days],
    'Gender_Male':[1 if gender == 'Male' else 0],
    'Blood Type_A-': [1 if blood_type == 'A-' else 0],
    'Blood Type_AB+': [1 if blood_type == 'AB+' else 0],
    'Blood Type_AB-': [1 if blood_type == 'AB-' else 0],
    'Blood Type_B+' : [1 if blood_type == 'B+' else 0],
    'Blood Type_B-' : [1 if blood_type == 'B-' else 0],
    'Blood Type_O+' : [1 if blood_type == 'O+' else 0],
    'Blood Type_O-' : [1 if blood_type == 'O-' else 0],
    'Medical Condition_Asthma' : [1 if medical_condition == 'Asthma' else 0],
    'Medical Condition_Cancer' : [1 if medical_condition == 'Cancer' else 0],
    'Medical Condition_Diabetes':[1 if medical_condition =='Diabetes' else 0],
    'Medical Condition_Hypertension' :[1 if medical_condition == 'Hypertension' else 0],
    'Medical Condition_Obesity':[1 if medical_condition == 'Obesity' else 0],
    'Admission Type_Emergency':[1 if admission_type == 'Emergency' else 0],
    'Admission Type_Urgent': [1 if admission_type == 'Urgent' else 0],
    'Medication_Ibuprofen':[1 if medication == 'Ibuprofen' else 0],
    'Medication_Lipitor' : [1 if medication == 'Lipitor' else 0],
    'Medication_Paracetamol': [1 if medication == 'Paracetamol' else 0],
    'Medication_Penicillin':[1 if medication == 'Penicillin' else 0],
})

expected_order = [
    'Age','Days_numeric','Gender_Male','Blood Type_A-','Blood Type_AB+','Blood Type_AB-',
    'Blood Type_B+','Blood Type_B-','Blood Type_O+','Blood Type_O-','Medical Condition_Asthma',
    'Medical Condition_Cancer','Medical Condition_Diabetes','Medical Condition_Hypertension',
    'Medical Condition_Obesity','Admission Type_Emergency','Admission Type_Urgent','Medication_Ibuprofen',
    'Medication_Lipitor','Medication_Paracetamol','Medication_Penicillin'
]

input_data = input_data.reindex(columns = expected_order)

if st.button("Predict"):
    prediction = model.predict(input_data)
    result_mapping = {0 : 'Normal', 1: 'Abnormal', 2:'Inconclusive'}
    result = result_mapping[prediction[0]]
    st.write(f'The Predictive test result is : **{result}**')

