import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\WorkIGuess\Stuff\HousingData.csv")

df.replace('NA', pd.NA, inplace=True)

df.dropna(inplace=True)

df = df.apply(pd.to_numeric)

st.title('Boston Housing Data Analysis')

st.subheader('Data')
st.write(df)

st.write("""
### Explanation of Data Columns:
- CRIM: Per capita crime rate by town
- ZN: Proportion of residential land zoned for lots over 25,000 sq. ft.
- INDUS: Proportion of non-retail business acres per town
- CHAS: Charles River dummy variable (1 if tract bounds river; 0 otherwise)
- NOX: Nitric oxides concentration (parts per 10 million)
- RM: Average number of rooms per dwelling
- AGE: Proportion of owner-occupied units built prior to 1940
- DIS: Weighted distances to five Boston employment centers
- RAD: Index of accessibility to radial highways
- TAX: Full-value property tax rate per $10,000
- PTRATIO: Pupil-teacher ratio by town
- B: 1000(Bk - 0.63)^2 where Bk is the proportion of Black individuals by town
- LSTAT: Percentage lower status of the population
- MEDV: Median value of owner-occupied homes in $1000s
""")

st.subheader('Summary Statistics')
st.write(df.describe())

st.subheader('Correlation Matrix')
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
st.pyplot()

st.subheader('Distribution of Target Variable (MEDV)')
plt.figure(figsize=(10, 6))
sns.histplot(df['MEDV'], kde=True, bins=30, color='blue')
plt.xlabel('MEDV')
plt.ylabel('Frequency')
st.pyplot()

st.subheader('Scatter Plot: RM vs MEDV')
plt.figure(figsize=(10, 6))
sns.scatterplot(x='RM', y='MEDV', data=df, color='green')
plt.xlabel('Average Number of Rooms (RM)')
plt.ylabel('Median Value of Homes (MEDV)')
st.pyplot()

st.subheader('Scatter Plot: LSTAT vs MEDV')
plt.figure(figsize=(10, 6))
sns.scatterplot(x='LSTAT', y='MEDV', data=df, color='red')
plt.xlabel('% Lower Status of the Population (LSTAT)')
plt.ylabel('Median Value of Homes (MEDV)')
st.pyplot()

st.subheader('Scatter Plot: CRIM vs MEDV')
plt.figure(figsize=(10, 6))
sns.scatterplot(x='CRIM', y='MEDV', data=df, color='purple')
plt.xlabel('Per Capita Crime Rate (CRIM)')
plt.ylabel('Median Value of Homes (MEDV)')
st.pyplot()
