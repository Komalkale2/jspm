import streamlit as st
import pickle
import numpy as np

#load the model
with open("lrmodel_sustainable.pkl", "rb") as file:
    model = pickle.load(file)

    #Title for your application
    carbon_emissions=st.number_input("Carbon emissions amout:",min_value=0.0,format="%f")
    energy_output=st.number_input("Enter the energy output amount:",min_value=0.0,format="%f")
    renewability_index=st.number_input("Enter the renewability index:",min_value=0.0,format="%f")
    cost_effiency=st.number_input("Enter the cost efficiency:",min_value=0.0,format="%f")

    #Predict button
    if st.button("Predict"):
        #Prepare the input data for prediction
        input_data = np.array([[carbon_emissions, energy_output, renewability_index, cost_effiency]])
        
        #Make prediction
        prediction = model.predict(input_data)
        
        #Display the prediction result
        if prediction[0] == 1:
            st.success("Congrats , it is Sustainable.")
        else:
            st.info("It is not Sustainable, Need to Improve.")