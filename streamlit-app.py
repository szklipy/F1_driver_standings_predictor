import streamlit as st
import pickle
import numpy as np
import pandas as pd
import datetime
import plotly.graph_objects as go

st.write("""

""")

link = '[Kaggle - Formula 1 World Championship (1950 - 2023)](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020)'
st.markdown(link, unsafe_allow_html=True)

st.sidebar.header('User Input Parameters')


# Get user inputs
def user_input_features():
    driverId = st.sidebar.slider('driverId', 1, 900, 180)
    number_x = st.sidebar.slider('number_x', 1, 250, 12)
    totalRaces = st.sidebar.slider('totalRaces', 1, 100, 50)
    winRate = st.sidebar.slider('winRate', 0, 5, 0)
    age = st.sidebar.slider('age', 17, 50, 20)
    fastestLapRate = st.sidebar.slider('fastestLapRate', 0, 5, 0)
    qualifyingWinRate= st.sidebar.slider('qualifyingWinRate', 0, 5, 0)
    
    data = {'driverId': driverId,
            'number_x': number_x,
            'totalRaces': totalRaces,
            'winRate': winRate,
            'age': age,
            'fastestLapRate': fastestLapRate,
            'qualifyingWinRate': qualifyingWinRate
            }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

# Show user inputs
st.subheader('User Input parameters')
st.write(df)

# Create Plotly plot
columns = ['driverId', 'number_x', 'totalRaces', 'winRate', 'age','fastestLapRate','qualifyingWinRate']

# create a new DataFrame with the selected columns
df_result = df[columns]

# Convert the first row of the DataFrame to a list
y = df_result.values.tolist()[0]

fig = go.Figure(data=go.Bar(x=columns, y=y), layout_title_text='Movie Features')
st.plotly_chart(fig, use_container_width=True)

model_final_pipe = pickle.load(open('model_final.pkl', 'rb'))

prediction = model_final_pipe.predict(df)

st.subheader('Predicted Movie Popularity')
prediction = int(np.round(prediction, 0))
st.title(prediction)