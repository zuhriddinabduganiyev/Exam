import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("23.csv")
st.write("Hello")

df['Age']=df['Age'].fillna(df['Age'].median())
df['Gender']=df['Gender'].fillna(df['Gender'].mode()[0])
df['Location']=df['Location'].fillna(df['Location'].mode()[0])
df['PlayTimeHours']=df['PlayTimeHours'].fillna(df['PlayTimeHours'].median())
df['InGamePurchases']=df['InGamePurchases'].fillna(df['InGamePurchases'].median())
df['GameDifficulty']=df['GameDifficulty'].fillna(df['GameDifficulty'].mode()[0])
df['SessionsPerWeek']=df['SessionsPerWeek'].fillna(df['SessionsPerWeek'].median())
df['AvgSessionDurationMinutes']=df['AvgSessionDurationMinutes'].fillna(df['AvgSessionDurationMinutes'].median())
df['PlayerLevel']=df['PlayerLevel'].fillna(df['PlayerLevel'].median())
df['AchievementsUnlocked']=df['AchievementsUnlocked'].fillna(df['AchievementsUnlocked'].median())
df['EngagementLevel']=df['EngagementLevel'].fillna(df['EngagementLevel'].mode()[0])



GameGenre_mode_for_USA = df[df['Location'] == 'USA']['GameGenre'].mode()[0]
df.loc[df['Location'] == 'USA', 'GameGenre'] = df.loc[df['Location'] == 'USA', 'GameGenre'].fillna(GameGenre_mode_for_USA)
GameGenre_mode_for_Europe = df[df['Location'] == 'Europe']['GameGenre'].mode()[0]
df.loc[df['Location'] == 'Europe', 'GameGenre'] = df.loc[df['Location'] == 'Europe', 'GameGenre'].fillna(GameGenre_mode_for_Europe)
GameGenre_mode_for_Other = df[df['Location'] == 'Other']['GameGenre'].mode()[0]
df.loc[df['Location'] == 'Other', 'GameGenre'] = df.loc[df['Location'] == 'Other', 'GameGenre'].fillna(GameGenre_mode_for_Other)
GameGenre_mode_for_Asia = df[df['Location'] == 'Asia']['GameGenre'].mode()[0]
df.loc[df['Location'] == 'Asia', 'GameGenre'] = df.loc[df['Location'] == 'Asia', 'GameGenre'].fillna(GameGenre_mode_for_Asia)

df = df.drop(columns=['Unnamed: 0'])
# add_radio = st.sidebar.radio(
#     "Tanlang:",
#     ("DataFrame haqida", "Missing data", "Graphlar", "Xulosa")
# )
st.sidebar.title("Loyiha:")
# Sidebar options
options = [
    "Birinchisi",
    "Ikkinchisi",
    "Uchinchisi",
    "To'rtinchisi",
    "Xulosa",
]
# Display options in the sidebar
for option in options:
    st.sidebar.button(option)


# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )


gender_counts = df['Gender'].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Gender Distribution')
plt.axis('equal')
plt.show()
st.pyplot(plt)
# if add_radio == "DataFrame kirish":
#     st.title("DataFrame Sahifasi")
#     if st.button("'DataFrame'ni ko'rish"):
#         st.write("## DataFrame")
#         st.dataframe(df)
#         st.button("Yopish", type="primary")
