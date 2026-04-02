import streamlit as st
import pandas as pd
import pickle
import os

st.title('IPL Win Predictor')

# Teams and cities
teams = ['Sunrisers Hyderabad', 'Mumbai Indians', 'Royal Challengers Bangalore', 
         'Kolkata Knight Riders', 'Kings XI Punjab', 'Chennai Super Kings', 
         'Rajasthan Royals', 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
          'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
          'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
          'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
          'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
          'Sharjah', 'Mohali', 'Bengaluru']

# Load model 
pipe = None
if os.path.exists('pipe.pkl'):
    try:
        pipe = pickle.load(open('pipe.pkl','rb'))
    except Exception as e:
        st.error(f"Failed to load model: {e}")
else:
    st.warning("pipe.pkl not found.")

# User inputs
col1, col2 = st.columns(2)
with col1:
    batting_team = st.selectbox('Select the batting team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the bowling team', sorted(teams))

selected_city = st.selectbox('Select host city', sorted(cities))
target = st.number_input('Target', min_value=0, step=1)

col3, col4, col5 = st.columns(3)
with col3:
    score = st.number_input('Score', min_value=0, step=1)
with col4:
    overs = st.number_input('Overs completed', min_value=0.0, step=0.1, format="%.1f")
with col5:
    wickets = st.number_input('Wickets out', min_value=0, max_value=10, step=1)

# Prediction button
if st.button('Predict Probability'):
    if pipe is None:
        st.error("Prediction model not loaded. Please check pipe.pkl file.")
    else:
        # Avoiding division by zero
        runs_left = max(target - score, 0)
        balls_left = max(120 - (overs*6), 1)
        wickets_left = max(10 - wickets, 0)
        crr = score / overs if overs > 0 else 0
        rrr = (runs_left*6) / balls_left if balls_left > 0 else 0

        input_df = pd.DataFrame({
            'batting_team':[batting_team],
            'bowling_team':[bowling_team],
            'city':[selected_city],
            'runs_left':[runs_left],
            'balls_left':[balls_left],
            'wickets':[wickets_left],
            'total_runs_x':[target],
            'currentrr':[crr],
            'requiredrr':[rrr]
        })

        try:
            result = pipe.predict_proba(input_df)
            loss = result[0][0]
            win = result[0][1]
            st.header(f"{batting_team} - {round(win*100)}% chance of winning")
            st.header(f"{bowling_team} - {round(loss*100)}% chance of winning")
        except Exception as e:
            st.error(f"Prediction failed: {e}")