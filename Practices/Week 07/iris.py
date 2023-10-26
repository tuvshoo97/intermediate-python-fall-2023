import streamlit as st
from joblib import load
from PIL import Image

model = load('data/iris_model.joblib')

col1, col2 = st.columns(2)

with col1:
    sepal_len = st.number_input('Sepal Len')
    sepal_width = st.number_input('Sepal width')

with col2:
    petal_len = st.number_input('Petal len')
    petal_width = st.number_input('Petal width')

c1, c2, c3 = st.columns(3)

with c2:
    if st.button("Predict"):
        prediction = model.predict([[sepal_len, 
                                     sepal_width, 
                                     petal_len, 
                                     petal_width]])[0]
        if prediction == 0:
            image = Image.open('images/iris_setosa.png')
        elif prediction == 1:
            image = Image.open('images/iris_versicolor.png')
        else:
            image = Image.open('images/iris_virginica.png') 
            
        st.image(image)

    
