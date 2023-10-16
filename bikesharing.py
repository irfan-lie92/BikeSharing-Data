import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the datasets
all_data = pd.read_csv('analisadata.csv')
weather_rentals = all_data.groupby('season_x')['cnt_y'].mean().reset_index()

# Create the Streamlit app
import streamlit as st
name="Irfan Ali"
email="ir.vanaly@gmail.com"
IDDicoding="irfanlie92"
def main():
    st.title("Bike Sharing Data Analysis - submission dicoding")

    # Sidebar
    with st.sidebar:
        st.markdown("![bikesharing](https://media.giphy.com/media/vML5C45h1vHBC/giphy.gif)")
        st.subheader("Profil Saya")
        st.write("Nama : "+ name)
        st.write("Email : "+ email)
        st.write("IDDicoding : "+ IDDicoding)

    # First row
    st.subheader('Pada Season/Musim apa pengguna Bike Sharing lebih banyak beraktivitas?')

    # Create a bar plot
    fig_season = plt.figure(figsize=(8, 6))
    sns.barplot(data=weather_rentals, x='season_x', y='cnt_y')
    plt.xlabel('Season/musim')
    plt.ylabel('Rata-rata Pengguna')
    plt.xticks(range(4),['spring', 'summer', 'fall', 'winter'])
    plt.title('Rata-rata Bike Rentals berdasarkan season/musim')
    st.pyplot(fig_season)

    # Second row with three columns
    st.subheader('Pada jam berapa rata-rata Aktivitas Bike Rentals per-jam dan per-hari dalam seminggu?')
    col1, col2 = st.columns(2)
    with col1:
        st.write("Jam")
        fig_hr = plt.figure(figsize=(12, 6))
        sns.barplot(data=all_data, x='hr', y='cnt_y')
        plt.xlabel('jam dalam sehari')
        plt.ylabel('Pengguna')
        plt.title('Rata-rata Bike Rentals setiap jam')
        st.pyplot(fig_hr)
    with col2:
        st.write("Hari")
        fig_day = plt.figure(figsize=(12, 6))
        sns.barplot(data=all_data, x='weekday_x', y='cnt_y')
        plt.xlabel('Hari dalam seminggu')
        plt.ylabel('pengguna')
        plt.title('Rata-rata Bike Rentals setiap hari')
        plt.xticks(range(7), ['Sen', 'Sel', 'Rab', 'Kam', 'Jum', 'Sab', 'Min'])
        st.pyplot(fig_day)

    # Third row
    st.subheader('Conclusion')
    st.subheader('1. Pada Season/Musim apa pengguna Bike Sharing lebih banyak beraktivitas?')
    st.write('dapat di lihat bahwa aktivitas Bike Rentals terbanyak pada season/musim `summer`.')
    st.subheader('2. Pada jam berapa rata-rata Aktivitas Bike Rentals per-jam dan per-hari dalam seminggu?')
    st.write('dari data tersebut aktivitas Bike Rentals terbanyak pada jam `17.00` dan dan aktivitas Bike Rentals terbanyak pada hari `Tuesday`.')

if __name__ == '__main__':
    main()
