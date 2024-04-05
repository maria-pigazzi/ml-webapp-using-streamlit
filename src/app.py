#from utils import db_connect
#engine = db_connect()
#commented out because it was giving many errors during the 

# your code here
import pickle
import streamlit as st
from pickle import load
# installed streamlit locally through terminal using pip install streamlit 
# as indicated in "https://docs.streamlit.io/get-started/installation/command-line"
# then gave command python -m streamlit hello to open welcome page in web browser

#Local URL: http://localhost:8501 where to find the hello page/"webapp"
# Network URL: http://192.168.178.43:8501

# to exit welcome message in terminal: ctrl+C
# rememeber to install requirements!!!

st.title("Hello, World!!")

# Create skeleton/blocks for webapp
# E.g. create sliders
# Assign values to types of flowers
# petal_width, petal_length, sepal_width, sepal_length
# Connect feature decided by user to model:
model_file = load(open("C:/Users/Anna/Desktop/Bootcamp/Repositories/ml-webapp-using-streamlit-1/src/decision_tree_iris.sav", "rb"))
classes = {
    0: "Iris setosa",
    1: "Iris versicolor",
    2: "Iris virginica"
}
st.title("Iris - Decision tree prediction")
# we want to predict type of flower (after loading the model)
st.slider("Petal width", min_value=0.0, max_value=5.0, step=0.4)
st.slider("Petal length", min_value=0.0, max_value=5.0, step=0.4)
st.slider("Sepal width", min_value=0.0, max_value=5.0, step=0.4)
st.slider("Sepal length", min_value=0.0, max_value=5.0, step=0.4)
#button to predict what flower corresponds to the features data
# st.button("Predict!", )
if st.button("Predict flower"):
    prediction = model_file.predict([petal_width, petal_length, sepal_width, sepal_length])[0]
    flower_
    st.write("The flower is", flower_) #flower and features still undefined!
