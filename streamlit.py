import streamlit as st
import joblib
import pandas as pd


def prediction(gender, city, employer1, employer2, monthly_income, banktype, contacted, source, existing_emi, month):
    model = joblib.load("train.pkl")

    if gender == "Male":
        gender = 0
    else:
        gender = 1

    if (month == "Jul"):
        month = 0
    elif (month == "Aug"):
        month = 1
    elif (month == "Sept"):
        month = 2

    if city == "A":
        city = 0
    elif city == "B":
        city = 1
    elif city == "C":
        city = 2

    if employer1 == "A":
        employer1 = 0
    elif employer1 == "B":
        employer1 = 1
    elif employer1 == "C":
        employer1 = 2

    if banktype == "G":
        banktype = 0
    elif banktype == "P":
        banktype = 1

    if contacted == "Yes":
        contacted = 0
    elif contacted == "No":
        contacted = 1
    if source == "A":
        source = 0
    elif source == "B":
        source = 1
    elif source == "C":
        source = 2
    elif source == "D":
        source = 3
    elif source == "E":
        source = 4
    elif source == "F":
        source = 5
    elif source == "G":
        source = 6

    if employer2 == "1":
        employer2 = 1
    elif employer2 == "2":
        employer2 = 2
    elif employer2 == ("3"):
        employer2 = 3


    re=model.predict([[gender, city, employer1, employer2, monthly_income, banktype, contacted, source, existing_emi, month]])

    if re[0]==0:
        st.error("The Customer will not get converted to marketing lead!")
    elif re[0]==1:
        st.success("The customer will get converted to marketing lead.")


def main():
    st.title("Welcome to the Prediction of Lead Conversion Page.")

    st.header("The page is meant for lead conversion prediction, whether your customer will get converted to marketing lead or not. A marketing lead is a person who shows interest in a brand's products or services, which makes the person a potential customer. The primary goal of any company is to generate as many leads as possible. A company must guide prospects down the sales funnel with relevant content and offers towards their purchase. The prediction is done with the help of XGBoost ML model.")

    st.text("Please input your data below.")

    monthly_income = st.number_input("Enter customer's monthly income")

    existing_emi=st.number_input("Enter customer's existing EMI")
    # monthly_income=int(monthly_income)
    # existing_emi=int(existing_emi)
    gender = st.radio("Select Gender: ", ('Male', 'Female'))

    month = st.radio("Select Lead Creation Month: ", ('Jul',"Aug", "Sept"))


    city=st.radio("Select City:", ("A", "B", "C"))


    employer1=st.radio("Select Employer Category 1:", ("A", "B", "C"))

    banktype=st.radio("Select Primary Bank Type:", ("G", "P"))


    contacted=st.radio("Select Contacted Customer or not:", ("Yes", "No"))

    source=st.radio("Select customer's source category:", ("A", "B", "C", "D", "E", "F", "G"))

    employer2=st.radio("Select Employer Category 2:", ("1", "2", "3"))

    if (st.button('Predict Lead Converison')):
        prediction(gender, city, employer1, employer2, monthly_income, banktype, contacted, source, existing_emi, month)

if __name__=='__main__':
    main()
