import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("ckd_model.pkl")

st.set_page_config(page_title="CKD Prediction",layout="wide")

st.title("🩺 Chronic Kidney Disease Prediction System")

st.markdown("Enter patient medical details to predict CKD.")

col1,col2,col3 = st.columns(3)

with col1:
    age = st.number_input("Age",0,100)
    bp = st.number_input("Blood Pressure")
    sg = st.number_input("Specific Gravity",format="%.3f")
    al = st.number_input("Albumin")
    su = st.number_input("Sugar")
    rbc = st.selectbox("RBC",[0,1])
    pc = st.selectbox("Pus Cell",[0,1])
    pcc = st.selectbox("Pus Cell Clumps",[0,1])

with col2:
    ba = st.selectbox("Bacteria",[0,1])
    bgr = st.number_input("Blood Glucose Random")
    bu = st.number_input("Blood Urea")
    sc = st.number_input("Serum Creatinine")
    sod = st.number_input("Sodium")
    pot = st.number_input("Potassium")
    hemo = st.number_input("Hemoglobin")
    pcv = st.number_input("Packed Cell Volume")

with col3:
    wc = st.number_input("White Blood Cell Count")
    rc = st.number_input("Red Blood Cell Count")
    htn = st.selectbox("Hypertension",[0,1])
    dm = st.selectbox("Diabetes Mellitus",[0,1])
    cad = st.selectbox("Coronary Artery Disease",[0,1])
    appet = st.selectbox("Appetite",[0,1])
    pe = st.selectbox("Pedal Edema",[0,1])
    ane = st.selectbox("Anemia",[0,1])

if st.button("🔍 Predict CKD"):

    data = np.array([[age,bp,sg,al,su,rbc,pc,pcc,ba,bgr,bu,sc,sod,pot,
                      hemo,pcv,wc,rc,htn,dm,cad,appet,pe,ane]])

    prediction = model.predict(data)

    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.error("⚠ Patient is likely to have Chronic Kidney Disease")
    else:
        st.success("✅ Patient is NOT likely to have CKD")