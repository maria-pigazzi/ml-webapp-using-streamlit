#from utils import db_connect
#engine = db_connect()
#commented out because it was giving many errors during the 

# your code here
import streamlit as st
from pickle import load
# installed streamlit locally through terminal using pip install streamlit 
# as indicated in "https://docs.streamlit.io/get-started/installation/command-line"
# then gave command python -m streamlit hello to open welcome page in web browser
# streamlit run app.py - to run streamlit code in app.py

#Local URL: http://localhost:8501 where to find the hello page/"webapp"
# Network URL: http://192.168.178.43:8501

# to exit welcome message in terminal: ctrl+C
# rememeber to install requirements!!!

# Create skeleton/blocks for webapp
# E.g. create sliders
# Assign values to types of flowers
# petal_width, petal_length, sepal_width, sepal_length
# Connect feature decided by user to model:
model_file = load(open("C:/Users/Anna/Desktop/Bootcamp/Repositories/ml-webapp-using-streamlit-1/src/decision_tree_iris.sav", "rb"))
# Remember to update path when uploading to github
classes = {
    "0": "Iris setosa",
    "1": "Iris versicolor",
    "2": "Iris virginica"
}
st.title("Iris - Decision tree prediction")
# we want to predict type of flower (after loading the model)
petal_width = st.slider("Petal width", min_value=0.0, max_value=5.0, step=0.2)
petal_length = st.slider("Petal length", min_value=0.0, max_value=5.0, step=0.2)
sepal_width = st.slider("Sepal width", min_value=0.0, max_value=5.0, step=0.2)
sepal_length = st.slider("Sepal length", min_value=0.0, max_value=5.0, step=0.2)
#button to predict what flower corresponds to the features data
# st.button("Predict!", )

if st.button("Predict flower"): #if user clicks the button the function will be executed
    prediction = str(model_file.predict([[petal_width, petal_length, sepal_width, sepal_length]])[0])
    flower = classes[prediction]
    st.write("The flower is", flower) #flower and features still undefined!
