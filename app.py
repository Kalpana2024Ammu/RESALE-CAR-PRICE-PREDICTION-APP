import pandas as pd 
import numpy as np 
import streamlit as st 
import pickle 
st.title("WELCOME TO RESALE CAR WORLD")
st.set_page_config(layout="wide")
st.header(':blue [USED CAR PRICE PREDICTION]')

df=pd.read_csv("filterd_dataframe.csv")
print(df.columns)

col1,col2=st.columns(2)
with col1:
    ft=st.selectbox("Fuel Type",['Petrol', 'Diesel', 'Lpg', 'Cng', 'Electric'])
    bt=st.selectbox("Body Type",['Hatchback', 'SUV', 'Sedan', 'MUV', 'Coupe', 'Minivans','Convertibles', 'Hybrids', 'Wagon', 'Pickup Trucks'])
    tr=st.selectbox("Transmission",['Manual', 'Automatic'])
    owner=st.selectbox("Owner No",[0,1,2,3,4,5])
    brand=st.selectbox("Brand",options=df["Brand"].unique())
    filtered_model=df[(df["Brand"]==brand)&(df["Body Type"]==bt)&(df["Fuel Type"]==ft)]['Model'].unique()
    model=st.selectbox("Model",options=filtered_model)
    model_year=st.selectbox("Model Year",options=sorted(df['Model Year'].unique()))
    iv=st.selectbox("Insurance Validity",['Third Party insurance', 'Comprehensive', 'Third Party','Zero Dep', 'Second Party', 'First Party', 'Not Available'])
    km=st.slider("Kilometer",min_value=100,max_value=100000,step=1000)
    ml=st.number_input("Mileage",min_value=5,max_value=50,step=1)
    seats=st.selectbox("Seats",options=sorted(df['Seats'].unique()))
    color=st.selectbox("Color",df['Color'].unique())
    city=st.selectbox("City",options=df["City"].unique())
    engine=st.number_input("Engine",min_value=72.0,max_value=5000.0,step=100.0)
    car_age=st.selectbox("Car Age",options=sorted(df["Car Age"].unique()))
    car_size=st.number_input("Car Size",min_value=6747372000.0,max_value=101447608559025.0,step=100000.0)
with col2:
    submit=st.button("Predict")
    
    if submit:
        with open('car_price_prediction.pkl','rb') as file:
            pipeline=pickle.load(file)
            
            new_df=pd.DataFrame({
                "Fuel Type":ft,
                "Body Type":bt,
                'Transmission':tr,
                'Owner No':owner,
                'Brand':brand,
                'Model':model,
                'Model Year':model_year,
                'Insurance Validity':iv,
                'Kilometer':km,
                'Mileage':ml,
                'Seats':seats,
                'Color':color,
                'City':city,
                "Engine":engine,
                "Car Age":car_age,
                'Car Size':car_size
            },index=[0])
            data=[ft,bt,tr,owner,brand,model,model_year,iv,km,ml,seats,color,city]
            st.write(data)
            
            prediction=pipeline.predict(new_df)
            st.write(f"the price of the{new_df['Brand'].iloc[0]} car is:{round(prediction[0],2)} lakhs")