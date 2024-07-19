import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from streamlit_option_menu import option_menu

df = pd.read_csv("23.csv")
last_df = pd.read_csv("23.csv")
def missing_val_check(data):
    total = data.isnull().sum().sort_values(ascending=False)
    percent = (data.isnull().sum() / data.isnull().count()).sort_values(ascending=False)
    missing_data = pd.concat(
        [total, percent * 100], axis=1, keys=["Soni", "Foizi (%)"]
    )
    return missing_data

# Sidebarni to'girlash:
st.set_page_config(layout="wide", page_title="GamersData", page_icon="🌟")
with st.sidebar:
    selected = option_menu(
        menu_title=None, 
        options=["DataFrame haqida", "Statistik tahlil", "Grafik tahlil", "Xulosa"],
        default_index=0,
        styles={
            "container": {"padding": "0!important", "background-color": "#262731"},
            "icon": {"display": "none"}, 
            "nav-link": {
                "font-size": "20px", 
                "text-align": "left", 
                "margin": "0px", 
                "--hover-color": "#3e4a5e"
            },
            "nav-link-selected": {"background-color": "#3e4a5e"},
        }
    )



# Birinchisi
if selected == "DataFrame haqida":
    st.write("## DataFrame haqida:")
    
    # DataFrame'ni ko'rish tugmasi:
    with st.expander("DataFrameni ko'rish:"):
        st.write("## DataFrame")
        st.dataframe(df)
        
    #Ikkita ustun
    col1, col2 = st.columns(2)
    gameDifficulty = df['GameDifficulty'].unique()
    location = df['Location'].unique()
    
    # GameDifficulty unikal qiymatlari:
    with col1:
        st.subheader("GameDifficulty ustunining unikal qiymatlari:")
        st.table({"GameDifficulty unique": gameDifficulty})
        
    # Location unikal qiymatlari:
    with col2:
        st.subheader("Location ustunining unikal qiymatlari:")
        st.table({"Location unique": location})
        
    # GameGenre unikal qiymatlar:
    col = st.columns(1)
    game_genres = df['GameGenre'].unique()
    with col1:
        st.subheader("GameGenre ustunining unikal qiymatlari:")
        st.table({"GameDifficulty unique": game_genres})
        
    # DataFrame haqida 
    st.write("### Strategiya: rejalashtirish, taktika va qaror qabul qilish qobiliyatlarini ta'kidlaydigan o'yinlar.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/58/Starcraft_Gamescom_2017_%2836851382835%29.jpg/440px-Starcraft_Gamescom_2017_%2836851382835%29.jpg", caption="Strategy games", use_column_width=True)
    st.write("### Sport: Sport amaliyotini taqlid qiluvchi o'yinlar. Bunga 'FIFA' (futbol) kabi jamoaviy sport turlari.")
    st.image("""https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1RhEyurtgdbeQ9eel4GwGw0uztE_aT3dhsQ&s""", use_column_width=True, caption="Sport games")
    st.write("### Action: Ular ko'pincha jangovar, platforma va boshqa dinamik faoliyatni o'z ichiga oladi. Masalan: 'Call of Duty' (otishma).")
    st.image("https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/42700/capsule_616x353.jpg?t=1654809667", use_column_width=True, caption="Action")
    st.write("### Simulation: Masalan:'The Sims' kabi hayotni simulyatsiya qilish o'yinlari, 'SimCity' kabi biznes simulyatsiya o'yinlari.")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSarIu01D_yHhSYKXUSyOXIU0C07kKIAgqoWA&s", use_column_width=True, caption="Simulation")
    
    # DataFrame shape
    rows, cols = df.shape
    st.write('## DataFrame shape:')
    st.write(df.shape)
    st.markdown(f"'DataFrame'da **{rows}** ta qator va **{cols}** ta ustun mavjud.")
    
    # Ikkita ustun:
    col1, col2 = st.columns(2)
    # Data Type lar
    with col1:
        st.subheader("Data Types:")
        st.table({"DataTypes": df.dtypes})
        st.write("Umumiy:")
        game_genres = ["int - 1 ta","float - 8 ta","object - 5 ta"]
        for genre in game_genres:
            st.write(f"- {genre}")
            
    # Column nomlari
    with col2:
        st.subheader("Columns:")
        st.table({"Columns": df.columns})
        
    # Numeric ustunlar:
    st.write("Numeric bo'lgan ustunlar:")
    st.write(df.select_dtypes("number"))
    
    # Object ustunlar:
    st.write("Object bo'lgan ustunlar:")
    st.write(df.select_dtypes("object"))

    
# Ikkinchisi
elif selected=="Statistik tahlil":
    st.title("Statistik tahlil")

    st.write("### Missing values")
    
    # DataFrame'ni ko'rish tugmasi:
    with st.expander("'DataFrame'ni ko'rish:"):
        st.write("## DataFrame")
        st.dataframe(df)
        
    # DataFramedagi NaN qiymatlar necha foizni tashkil qilishi:
    df.replace(r"^\s*$", np.nan, regex=True, inplace=True)
    st.dataframe(missing_val_check(df))
    
    # PlayerID nan delete
    with st.expander("PlayerID ustunni NaN qiymatlarini delete:"):
            code="""
            son = 9000
            lst = []
            for i in range(40034):
                lst.append(son)
                son+=1
            df['PlayerID']=pd.DataFrame(lst).values
            """
            st.code(code, language='python')
    son = 9000
    lst = []
    for i in range(40034):
        lst.append(son)
        son+=1
    df['PlayerID']=pd.DataFrame(lst).values
    
    # Unnamed ustunini drop
    with st.expander("'Unnamed: 0' ustunini drop qilindi:"):
        st.code("df = df.drop(columns=['Unnamed: 0'])", language='python')
        df = df.drop(columns=['Unnamed: 0'])
    
    # Age ustuni fillna
    with st.expander("'Age' ustunidagi NaN qiymatlarni o'rniga median qo'yildi:"):
        df['Age']=df['Age'].fillna(df['Age'].median())
        st.code("df['Age']=df['Age'].fillna(df['Age'].median())", language='python')
    
    # GameGenre ustuni fillna
    with st.expander("'GameGenre' ustunidagi NaN qiymatlar o'rniga har bir mintaqaga alohida modasi qo'yildi:"):
        GameGenre_mode_for_USA = df[df['Location'] == 'USA']['GameGenre'].mode()[0]
        df.loc[df['Location'] == 'USA', 'GameGenre'] = df.loc[df['Location'] == 'USA', 'GameGenre'].fillna(GameGenre_mode_for_USA)
        GameGenre_mode_for_Europe = df[df['Location'] == 'Europe']['GameGenre'].mode()[0]
        df.loc[df['Location'] == 'Europe', 'GameGenre'] = df.loc[df['Location'] == 'Europe', 'GameGenre'].fillna(GameGenre_mode_for_Europe)
        GameGenre_mode_for_Other = df[df['Location'] == 'Other']['GameGenre'].mode()[0]
        df.loc[df['Location'] == 'Other', 'GameGenre'] = df.loc[df['Location'] == 'Other', 'GameGenre'].fillna(GameGenre_mode_for_Other)
        GameGenre_mode_for_Asia = df[df['Location'] == 'Asia']['GameGenre'].mode()[0]
        df.loc[df['Location'] == 'Asia', 'GameGenre'] = df.loc[df['Location'] == 'Asia', 'GameGenre'].fillna(GameGenre_mode_for_Asia)
        df['GameGenre']=df['GameGenre'].fillna(df['GameGenre'].mode()[0])
        code = """
        GameGenre_mode_for_USA = df[df['Location'] == 'USA']['GameGenre'].mode()[0]
        df.loc[df['Location'] == 'USA', 'GameGenre'] = df.loc[df['Location'] == 'USA', 'GameGenre'].fillna(GameGenre_mode_for_USA)
        GameGenre_mode_for_Europe = df[df['Location'] == 'Europe']['GameGenre'].mode()[0]
        df.loc[df['Location'] == 'Europe', 'GameGenre'] = df.loc[df['Location'] == 'Europe', 'GameGenre'].fillna(GameGenre_mode_for_Europe)
        GameGenre_mode_for_Other = df[df['Location'] == 'Other']['GameGenre'].mode()[0]
        df.loc[df['Location'] == 'Other', 'GameGenre'] = df.loc[df['Location'] == 'Other', 'GameGenre'].fillna(GameGenre_mode_for_Other)
        GameGenre_mode_for_Asia = df[df['Location'] == 'Asia']['GameGenre'].mode()[0]
        df.loc[df['Location'] == 'Asia', 'GameGenre'] = df.loc[df['Location'] == 'Asia', 'GameGenre'].fillna(GameGenre_mode_for_Asia)"""
        st.code(code, language='python')
    
    # Gender ustuni fillna
    with st.expander("'Gender' ustunidagi NaN qiymatlarga ustunning modasi qo'yildi:"):
        df['Gender']=df['Gender'].fillna(df['Gender'].mode()[0])
        st.code("df['Gender']=df['Gender'].fillna(df['Gender'].mode()[0])", language='python')
    
    # Qolganlari
    with st.expander("Qolgan ustunlar ham fillna qilindi:"):
        df['Location']=df['Location'].fillna(df['Location'].mode()[0])
        df['PlayTimeHours']=df['PlayTimeHours'].fillna(df['PlayTimeHours'].median())
        df['InGamePurchases']=df['InGamePurchases'].fillna(df['InGamePurchases'].median())
        df['GameDifficulty']=df['GameDifficulty'].fillna(df['GameDifficulty'].mode()[0])
        df['SessionsPerWeek']=df['SessionsPerWeek'].fillna(df['SessionsPerWeek'].median())
        df['AvgSessionDurationMinutes']=df['AvgSessionDurationMinutes'].fillna(df['AvgSessionDurationMinutes'].median())
        df['PlayerLevel']=df['PlayerLevel'].fillna(df['PlayerLevel'].median())
        df['AchievementsUnlocked']=df['AchievementsUnlocked'].fillna(df['AchievementsUnlocked'].median())
        df['EngagementLevel']=df['EngagementLevel'].fillna(df['EngagementLevel'].mode()[0])
        code = """
        df['Location']=df['Location'].fillna(df['Location'].mode()[0])
        df['PlayTimeHours']=df['PlayTimeHours'].fillna(df['PlayTimeHours'].median())
        df['InGamePurchases']=df['InGamePurchases'].fillna(df['InGamePurchases'].median())
        df['GameDifficulty']=df['GameDifficulty'].fillna(df['GameDifficulty'].mode()[0])
        df['SessionsPerWeek']=df['SessionsPerWeek'].fillna(df['SessionsPerWeek'].median())
        df['AvgSessionDurationMinutes']=df['AvgSessionDurationMinutes'].fillna(df['AvgSessionDurationMinutes'].median())
        df['PlayerLevel']=df['PlayerLevel'].fillna(df['PlayerLevel'].median())
        df['AchievementsUnlocked']=df['AchievementsUnlocked'].fillna(df['AchievementsUnlocked'].median())
        df['EngagementLevel']=df['EngagementLevel'].fillna(df['EngagementLevel'].mode()[0])
        """
        st.code(code, language='python')

    # NaN qiymatlar soni (tozalangandan so'ng)
    st.write("Tozalangandan so'ng NaN qiymatlar soni:")
    df.replace(r"^\s*$", np.nan, regex=True, inplace=True)
    st.dataframe(missing_val_check(df))

    # Missing qilingan DataFrame
    with st.expander("Tozalangan 'DataFrame'ni ko'rish:"):
        st.write("## DataFrame")
        st.dataframe(df)





# Uchinchisi
elif selected=="Grafik tahlil":
    df['Location']=df['Location'].fillna(df['Location'].mode()[0])
    df['PlayTimeHours']=df['PlayTimeHours'].fillna(df['PlayTimeHours'].median())
    df['InGamePurchases']=df['InGamePurchases'].fillna(df['InGamePurchases'].median())
    df['GameDifficulty']=df['GameDifficulty'].fillna(df['GameDifficulty'].mode()[0])
    df['SessionsPerWeek']=df['SessionsPerWeek'].fillna(df['SessionsPerWeek'].median())
    df['AvgSessionDurationMinutes']=df['AvgSessionDurationMinutes'].fillna(df['AvgSessionDurationMinutes'].median())
    df['PlayerLevel']=df['PlayerLevel'].fillna(df['PlayerLevel'].median())
    df['AchievementsUnlocked']=df['AchievementsUnlocked'].fillna(df['AchievementsUnlocked'].median())
    df['EngagementLevel']=df['EngagementLevel'].fillna(df['EngagementLevel'].mode()[0])
    df['Gender']=df['Gender'].fillna(df['Gender'].mode()[0])
    df = df.drop(columns=['Unnamed: 0'])
    df['Age']=df['Age'].fillna(df['Age'].median())
    GameGenre_mode_for_USA = df[df['Location'] == 'USA']['GameGenre'].mode()[0]
    df.loc[df['Location'] == 'USA', 'GameGenre'] = df.loc[df['Location'] == 'USA', 'GameGenre'].fillna(GameGenre_mode_for_USA)
    GameGenre_mode_for_Europe = df[df['Location'] == 'Europe']['GameGenre'].mode()[0]
    df.loc[df['Location'] == 'Europe', 'GameGenre'] = df.loc[df['Location'] == 'Europe', 'GameGenre'].fillna(GameGenre_mode_for_Europe)
    GameGenre_mode_for_Other = df[df['Location'] == 'Other']['GameGenre'].mode()[0]
    df.loc[df['Location'] == 'Other', 'GameGenre'] = df.loc[df['Location'] == 'Other', 'GameGenre'].fillna(GameGenre_mode_for_Other)
    GameGenre_mode_for_Asia = df[df['Location'] == 'Asia']['GameGenre'].mode()[0]
    df.loc[df['Location'] == 'Asia', 'GameGenre'] = df.loc[df['Location'] == 'Asia', 'GameGenre'].fillna(GameGenre_mode_for_Asia)
    df['GameGenre']=df['GameGenre'].fillna(df['GameGenre'].mode()[0])
    
    # title
    st.title("Grafik tahlil")
    
    # DataFrame
    with st.expander("'DataFrame'ni ko'rish:"):
        st.write("## DataFrame")
        st.dataframe(df)
        
    # Cuntplot Gender bo'yicha
    with st.expander("Gender bo'yicha o'yinchilar soni (countplot):"):
        fig, ax = plt.subplots()
        sns.countplot(x="Gender", data=df, palette=sns.color_palette("husl"))
        ax.set_title("Gender bo'yicha o'yinchilar soni")
        for p in ax.patches:
            ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='center', fontsize=12, color='black', xytext=(0, 10), 
                    textcoords='offset points')
        ax.set_xlabel("Gender", fontsize=14)
        ax.set_ylabel("Count", fontsize=14)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        sns.despine()
        st.pyplot(fig)
        
        st.write("Foizlarda (pie char):")
        fig, ax = plt.subplots()
        gender_counts = df['Gender'].value_counts()
        ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  
        st.pyplot(fig)
    
    # O'yin vaqti 
    with st.expander("Gender bo'yicha o'yinchilarni o'rtacha o'yin vaqti:"):
        PlayTime_by_Gender = df.groupby('Gender')['PlayTimeHours'].mean()
        total_play_time = PlayTime_by_Gender.sum()
        percent = (PlayTime_by_Gender / total_play_time) * 100
        fig, ax = plt.subplots()
        colors = ['blue' if gender == 'Male' else 'red' for gender in PlayTime_by_Gender.index]
        bars = ax.bar(PlayTime_by_Gender.index, PlayTime_by_Gender.values, color=colors)
        for bar, percentage in zip(bars, percent):
            height = bar.get_height()
            ax.annotate(f'{percentage:.1f}%', xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='center')
        ax.set_xlabel('Gender')
        ax.set_ylabel("O'yin vaqti (soat)")
        ax.set_title("Gender bo'yicha o'rtacha o'yin vaqti")
        sns.despine()
        st.pyplot(fig)



    # O'yinga qiziqish darajasi
    with st.expander("O'yinga qiziqish darajasi bo'yicha countplot:"):
        fig, ax = plt.subplots()
        sns.countplot(x="EngagementLevel", data=df, palette=sns.color_palette("husl"))
        ax.set_xlabel('Qiziqish darajasi')
        st.pyplot(fig)
        
        fig, ax = plt.subplots()
        sns.countplot(x="EngagementLevel", data=last_df, palette=sns.color_palette("husl"))
        ax.set_xlabel('Qiziqish darajasi')
        st.pyplot(fig)
        
        st.write("O'yinga qiziquvchilarning darajasi va gender bo'yicha umumiy soni:")
        fig, ax = plt.subplots()
        sns.countplot(x="EngagementLevel", data=df, palette=sns.color_palette("husl"), hue='Gender')
        ax.set_xlabel('Qiziqish darajasi')
        st.pyplot(fig)
        
        st.write("O'yinga qiziqish darajasi bo'yicha (pie char):")
        fig, ax = plt.subplots()
        engagement_counts = df['EngagementLevel'].value_counts()
        ax.pie(engagement_counts, labels=engagement_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal') 
        st.pyplot(fig)
        
    # Countplot by Location
    with st.expander("Location bo'yicha countplot:"):
        fig, ax = plt.subplots()
        sns.countplot(x="Location", data=df, palette=sns.color_palette("husl"))
        st.pyplot(fig)
        
        st.write("Location va Gender bo'yicha:")
        fig, ax = plt.subplots()
        sns.countplot(x="Location", data=df, palette=sns.color_palette("husl"), hue='Gender')
        st.pyplot(fig)
        
        st.write("Location bo'yicha (pie char):")
        fig, ax = plt.subplots()
        Location_counts = df['Location'].value_counts()
        ax.pie(Location_counts, labels=Location_counts.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal') 
        st.pyplot(fig)

    # Countplot by GameGenre
    with st.expander("O'yin janrlari bo'yicha o'yinchilar soni:"):
        fig, ax = plt.subplots(figsize=(10, 6))
        category_order = ["RPG", "Simulation", "Strategy", "Sports", "Action"]
        sns.countplot(x="GameGenre", data=df, order=category_order, palette=sns.color_palette("husl"), ax=ax)
        ax.set_title("O'yin janrlari bo'yicha o'yinchilar soni", fontsize=16, fontweight='bold')
        ax.set_xlabel("O'yin janrlari", fontsize=14)
        ax.set_ylabel("Count", fontsize=14)
        for p in ax.patches:
            ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='center', fontsize=12, color='black', xytext=(0, 10), 
                    textcoords='offset points')
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        sns.despine()
        st.pyplot(fig)
        
        st.write("O'yin janrlari va Gender bo'yicha o'yinchilar soni:")
        fig, ax = plt.subplots(figsize=(10, 6))
        category_order = ["RPG", "Simulation", "Strategy", "Sports", "Action"]
        sns.countplot(x="GameGenre", data=df, hue='Gender',order=category_order, palette=sns.color_palette("husl"), ax=ax)
        ax.set_title("O'yin janrlari va Gender bo'yicha o'yinchilar soni", fontsize=16, fontweight='bold')
        ax.set_xlabel("O'yin janrlari", fontsize=14)
        ax.set_ylabel("Count", fontsize=14)
        for p in ax.patches:
            ax.annotate(f'{p.get_height()}', (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='center', fontsize=12, color='black', xytext=(0, 10), 
                    textcoords='offset points')
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        sns.despine()
        st.pyplot(fig)

        st.write("O'yin janrlari va Location bo'yicha o'yinchilar soni:")
        fig, ax = plt.subplots(figsize=(10, 6))
        category_order = ["RPG", "Simulation", "Strategy", "Sports", "Action"]
        sns.countplot(x="GameGenre", data=df, hue='Location',order=category_order, palette=sns.color_palette("husl"), ax=ax)
        ax.set_title("O'yin janrlari va Location bo'yicha o'yinchilar soni", fontsize=16, fontweight='bold')
        ax.set_xlabel("O'yin janrlari", fontsize=14)
        ax.set_ylabel("Count", fontsize=14)
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        sns.despine()
        st.pyplot(fig)

    # Bar plot chizish
    with st.expander("O'yin janri bo'yicha o'rtacha o'yin vaqti"):
        plt.figure(figsize=(12, 8))
        sns.barplot(x='GameGenre', y='PlayTimeHours', data=df, estimator=lambda x: sum(x) / len(x))
        plt.title("O'yin janri bo'yicha o'rtacha o'yin vaqti")
        plt.xlabel("O'yin janri")
        plt.ylabel("O'rtacha o'yin vaqti (soatda)")
        plt.xticks()
        st.pyplot(plt)
        
        st.write("O'yin janri va gender bo'yicha o'rtacha o'yin vaqti:")
        plt.figure(figsize=(12, 8))
        sns.barplot(x='GameGenre', y='PlayTimeHours',hue='Gender',  data=df, estimator=lambda x: sum(x) / len(x))
        plt.title("O'yin janri va gender bo'yicha o'rtacha o'yin vaqti")
        plt.xlabel("O'yin janri")
        plt.ylabel("O'rtacha o'yin vaqti (soatda)")
        plt.xticks()
        st.pyplot(plt)

    # Histplot binlar tanlash orqali\
    with st.expander("O'yinchilarning yosh taqsimoti (histplot):"):
        bin_number = st.select_slider(
            "Bin sonini tanlang:",
            options=list(range(1, 26)),
            value=20
        )
        fig, ax = plt.subplots()
        sns.histplot(df['Age'], bins=bin_number, kde=True, ax=ax)
        st.pyplot(fig)
        
        fig, ax = plt.subplots()
        sns.boxplot(x=df['Age'], ax=ax)
        ax.set_title("O'yinchilarning yosh taqsimoti (boxplot)")
        ax.set_xlabel("Yosh")
        st.pyplot(fig)

    # O'yin qiyinligi bo'yicha o'rtacha sessiya davomiyligi
    with st.expander("O'yin qiyinligi bo'yicha o'rtacha sessiya davomiyligi:"):
        fig, ax = plt.subplots()
        sns.boxplot(x='GameDifficulty', y='AvgSessionDurationMinutes', data=df, ax=ax)
        ax.set_xlabel("Oyin qiyinliligi")
        ax.set_ylabel("Ortacha seans davomiyligi (minutda)")
        st.pyplot(fig)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x='GameDifficulty', y='AvgSessionDurationMinutes', data=df, estimator='mean', ax=ax)
        ax.set_xlabel("O'yin qiyinligi")
        ax.set_ylabel("O'rtacha sessiya davomiyligi (minutda)")
        ax.set_title("O'yin qiyinligi bo'yicha o'rtacha sessiya davomiyligi")
        st.pyplot(fig)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.pointplot(x='GameDifficulty', y='AvgSessionDurationMinutes', data=df, ax=ax)
        ax.set_xlabel("O'yin qiyinligi")
        ax.set_ylabel("O'rtacha sessiya davomiyligi (munutda)")
        ax.set_title("O'yin qiyinligi bo'yicha o'rtacha sessiya davomiyligi")
        st.pyplot(fig)
    
    # Streamlit app title
    with st.expander("Mashg'ulotlar darajasi bo'yicha haftada sessiyalarni taqsimlash:"):
        fig, ax = plt.subplots(figsize=(12, 6))
        df.boxplot(column='SessionsPerWeek', by='EngagementLevel', grid=False, patch_artist=True, showmeans=True, ax=ax)
        ax.set_title("Ishtirok etish darajasi bo'yicha haftaslik sessiyalar")
        plt.suptitle('') 
        ax.set_xlabel('Ishtirok etish darajasi')
        ax.set_ylabel('Haftalik sessiyalar')
        st.pyplot(fig)
        
        fig, ax = plt.subplots(figsize=(12, 6))
        sns.barplot(x='EngagementLevel', y='SessionsPerWeek', data=df, estimator='mean', ax=ax)
        ax.set_title("Ishtirok etish darajasi bo'yicha haftalik sessiyalar")
        ax.set_xlabel('Ishtirok etish darajasi')
        ax.set_ylabel('O\'rtacha haftalik sessiyalar')
        st.pyplot(fig)
    
    # Streamlit app title
    with st.expander("Yosh taqsimoti:"):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.hist(df['Age'].dropna(), bins=20, edgecolor='k')
        ax.set_title('Yosh taqsimoti')
        ax.set_xlabel('Yosh')
        ax.grid(True)
        st.pyplot(fig)
    
    # Calculate the average play time by game genre
    with st.expander("O'yin janri bo'yicha o'rtacha o'yin vaqti:"):
        avg_play_time = df.groupby('GameGenre')['PlayTimeHours'].mean()
        fig, ax = plt.subplots(figsize=(12, 6))
        avg_play_time.plot(kind='bar', color='skyblue', edgecolor='k', ax=ax)
        ax.set_title("O'yin janri bo'yicha o'rtacha o'yin vaqti")
        ax.set_xlabel("O'yin janri")
        ax.set_ylabel("O'rtacha o'yin vaqti (soatda)")
        ax.grid(True)
        st.pyplot(fig)
        
    # Plotting
    with st.expander("Jins va o'yin janri bo'yicha sessiya davomiyligi taqsimoti:"):
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.violinplot(x='GameGenre', y='AvgSessionDurationMinutes', hue='Gender', data=df, split=True, ax=ax)
        ax.set_xlabel("O'yin janri")
        ax.set_ylabel("Sessiya davomiyligi (minutda)")
        st.pyplot(fig)
    
    # Plotting
    with st.expander("O'yin darajasi va o'yin qiyinligi o'rtasidagi bog'liqlik:"):
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.stripplot(x='GameDifficulty', y='PlayerLevel', data=df, jitter=True, ax=ax)
        ax.set_xlabel("O'yin qiyinligi")
        ax.set_ylabel("O'yin darajasi")
    
    # Plotting
    with st.expander("O'yin janriga qarab yutgan yutuqlar taqsimoti:"):
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.boxplot(x='GameGenre', y='AchievementsUnlocked', data=df, ax=ax)
        ax.set_xlabel("O'yin janri")
        ax.set_ylabel("Yutgan yutuqlar soni")
        plt.xticks()
        st.pyplot(fig)
        
    # Pivot table yaratish
    with st.expander("O'yin janri va qiyinligi bo'yicha o'rtacha o'yin darajasi:"):
        pivot_table = df.pivot_table(values='PlayerLevel', index='GameGenre', columns='GameDifficulty', aggfunc='mean')
        plt.figure(figsize=(10, 8))
        sns.heatmap(pivot_table, annot=True, cmap='coolwarm', fmt='.1f')
        plt.title("O'yin janri va qiyinligi bo'yicha o'rtacha o'yin darajasi")
        plt.xlabel("O'yin qiyinligi")
        plt.ylabel("O'yin janri")
        st.pyplot(plt)

    # heatmap
    with st.expander("Correlation Heatmap:"):
        corr = df.drop(["PlayerID", "Gender", 'Location', 'GameGenre', 'GameDifficulty', 'EngagementLevel'], axis=1).corr()
        plt.figure(figsize=(14, 12))
        sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
        plt.title('Correlation Heatmap')
        plt.xticks(rotation=45)
        plt.yticks(rotation=0)
        st.pyplot(plt)
        
    with st.expander("Scatter plot:"):
        st.write("Age vs PlayTimeHours")
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        sns.scatterplot(x='Age', y='PlayTimeHours', data=df, ax=ax1, hue='Gender')
        ax1.set_title('Age vs PlayTimeHours')
        ax1.set_xlabel('Age')
        ax1.set_ylabel('PlayTimeHours')
        st.pyplot(fig1)
        
        st.write("PlayerLevel vs AchievementsUnlocked")
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        sns.scatterplot(x='PlayerLevel', y='AchievementsUnlocked', data=df, ax=ax2, hue='EngagementLevel')
        ax2.set_title('PlayerLevel vs AchievementsUnlocked')
        ax2.set_xlabel('PlayerLevel')
        ax2.set_ylabel('AchievementsUnlocked')
        st.pyplot(fig2)

        st.write("PlayTimeHours vs O'yin ichidagi xaridlar")
        fig3, ax3 = plt.subplots(figsize=(10, 6))
        sns.scatterplot(x='PlayTimeHours', y='InGamePurchases', data=df, ax=ax3, hue='GameGenre')
        ax3.set_title("PlayTimeHours vs O'yin ichidagi xaridlar")
        ax3.set_xlabel('PlayTimeHours')
        ax3.set_ylabel("O'yin ichidagi xaridlar")
        st.pyplot(fig3)


# To'rtinchisi xulosa
elif selected=="Xulosa":
    st.subheader("O'yinchilar statistikasi haqida umumiy xulosa.")
    st.write("""
    1. Erkaklar soni ayollardan ancha ko'p. Bu o'yinda erkaklar ko'proq ishtirok etishini xulosa qilishimiz mumkin. 
    2. Ayollar ham erkaklar ham ortacha 12 soatdan o'yin o'ynashadi.
    3. O'yinga qiziqishi o'rta bo'lgan o'yinchilarning soni , qiziqishi past va qiziqishi yuqori bo'lgan o'yinchilardan ikki barobar ko'p. Gender bo'yicha esa o'yin erkaklarga ko'proq yoqarkan.
    4. Eng ko'p gamerlar Amerikadan 16000 yaqin , keyin Yevropadan 12000 gamerlar bundan bu o'yinlar bu davlatlarda mashxur deb tahmin qilishimiz mumkin.
    5. O'yin janrlari bo'yicha qaraydigan bo'lsak , ular bir biridan katta farq qilmaydigan darajada o'yinchilar soni mavjud. Gender bo'yicha qaraydigan bo'lsak erkaklar yana janrlar kesimida ham tahminan ikki barobar koproq.
    6. O'yin janrlari o'rtacha o'yin vaqti bo'yicha bir biridan katta farq qilmaydi. Bundan barcha o'yin janrlari bir biridan katta farq qilmagan holda o'ziga jalb qiladi.
    7. 30 yosh atrofidagi o'yinchilar soni ko'p , bundan kelib chiqadiki bu yosh toifasidagilar o'yinlarga koproq qiziqishini va faol ekanligini korsatadi va bu o'yinlar ularga yoqishini ham bilishimiz mumkin. Boshqa yosh guruhlari taxminan teng taqsimlangan. Biroq 30 yoshdan kichik yoki katta bolgan guruhlar orasida sezilarli farqlar yoq.
    8. Oyin qiyinligi qanchalik yuqori bo'lsa, o'rtacha sessiya davomiyligi ham oshyabdi, bu o'yinchilarning qiyin oyinlarga yaxshi munosabatda ekanligini korishimiz mumkin.
    """)