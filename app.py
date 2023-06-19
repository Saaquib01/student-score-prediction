import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Load the data
data = pd.read_csv('data.csv')


# Train the linear regression model
X = data['Hours'].values.reshape(-1, 1)
y = data['Scores'].values.reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Compute metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# Create the web app
st.title('Student Score Prediction')
st.write('Enter the number of study hours:')
hours = st.number_input('', min_value=0, max_value=24, step=1)
score = int(model.predict([[hours]]))
if score > 100:
    score = 100

st.write(f'Predicted Score: {score} Marks if he studies {hours} hours')


# Perform EDA
# st.title('Exploratory Data Analysis')
# st.write('Data Summary:')
# st.write(data.describe())

st.write('Scatter Plot:')
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=data, x='Hours', y='Scores')
plt.xlabel('Hours')
plt.ylabel('Scores')
st.pyplot(fig)
