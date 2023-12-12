import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
import numpy as np
sns.set(style='dark')
import calendar

day_Data = pd.read_csv("Bike-sharing-dataset/day.csv")
hour_Data = pd.read_csv("Bike-sharing-dataset/hour.csv")
day_Data_2011 = day_Data[day_Data['yr'] == 0]
day_Data_2012 = day_Data[day_Data['yr'] == 1]
workingday_1 = hour_Data[hour_Data['workingday'] == 0]
workingday_2 = hour_Data[hour_Data['workingday'] == 1]

def convert_month(mnth_number):
    return calendar.month_abbr[mnth_number]

def create_sum_bike_(df):
    sum_bike_ = df.groupby('mnth')['cnt'].sum().reset_index()
    sum_bike_['mnth'] = sum_bike_['mnth'].apply(convert_month)
    return sum_bike_

def create_sum_bike_year(df):
    total_Y = df.groupby('yr')['cnt'].sum().reset_index()
    return total_Y

def create_mean_bike_season(df):
    season_Y = df.groupby('season')['cnt'].mean().reset_index()
    return season_Y

def create_mean_bike_weathersit(df):
    weathersit_Y = df.groupby('weathersit')['cnt'].mean().reset_index()
    return weathersit_Y

def create_mean_bike_hour(df):
    bike_hour = df.groupby('hr')['cnt'].mean().reset_index()
    return bike_hour

def create_mean_bike_workingday(df):
    data_workingday = df.groupby('workingday')['cnt'].mean().reset_index()
    return data_workingday

with st.sidebar:
    st.sidebar.header('Analisis Penyewaan Sepeda :blue[_Bike Sharing_] 2011-2012 🚴')
    st.image("logo3.png", width=250)
    selected_menu = st.sidebar.radio("-PILIH MENU ANALISIS DATA", ["jumlah sewaan sepeda sepanjang tahun", 
                                                               "Pengaruh Musim Terhadap Sewaan Sepeda", 
                                                               "Pengaruh Cuaca Terhadap Sewaan Sepeda",
                                                               "Pengaruh Hari libur Terhadap Sewaan Sepeda",
                                                               "Distribusi Sewaan Sepeda Berdasarkan Hari",
                                                               "Keterangan"])

sum_bike_ = create_sum_bike_(day_Data)
sum_bike_2011 = create_sum_bike_(day_Data_2011)
sum_bike_2012 = create_sum_bike_(day_Data_2012)
total_Y = create_sum_bike_year(day_Data)
season_Y = create_mean_bike_season(day_Data)
weathersit_Y = create_mean_bike_weathersit(day_Data)
bike_hour = create_mean_bike_hour(hour_Data)
bike_hour_0 = create_mean_bike_hour(workingday_1)
bike_hour_1 = create_mean_bike_hour(workingday_2)
data_workingday = create_mean_bike_workingday(day_Data)

if selected_menu == "jumlah sewaan sepeda sepanjang tahun":  
    st.header("Grafik Jumlah Penyewaan Sepeda di tahun 2011-2012")
    total_X = ['2011', '2012']
    colors = ["#5E808C", "#01B6E1"]
    fig, ax = plt.subplots(figsize=(4, 3))
    sns.barplot(
        y="cnt",  
        x= total_X,  
        data = total_Y,  
        palette= colors,  
        ax=ax
    )
    ax.set_xlabel('years', fontsize=9)
    ax.set_ylabel('total', fontsize=9)
    ax.tick_params(axis='x', labelsize=7)
    ax.tick_params(axis='y', labelsize=7)
    ax.set_title('total bicycle rental - 2011/2012', loc="center", fontsize=9.5)
    st.pyplot(fig)
    with st.expander(":orange[PENJELASAN]"):
        st.write(
            """Dari grafk diatas terlihat bahwa data jumlah penyewaan sepeda mengalami kenaikan ditahun 2012. 
            Pada tahun 2011 jumlah penyewaan sebesar 1.243.103 dan pada tahun 2012 sebesar 2.049.576, sehingga
            terjadi kenaikan jumlah sewa sebesar 806.473 atau sekitar 24.49%.
            """
        )

    fig, ax = plt.subplots()
    plt.plot(sum_bike_['mnth'], sum_bike_['cnt'], marker='o', color="#01B6E1")
    ax.set_xlabel('Month')
    ax.set_ylabel('Total bicycle rental')
    ax.set_title('Total bicycle rental/Month', loc="center")
    ax.grid(True)
    st.pyplot(fig)

    col1, col2 = st.columns(2)
    with col1:
        fig, ax = plt.subplots()
        plt.plot(sum_bike_2011['mnth'], sum_bike_2011['cnt'], marker='o', color="#01B6E1")
        ax.set_xlabel('Month')
        ax.set_ylabel('Total bicycle rental')
        ax.set_title('Total bicycle rental/Month - 2011')
        ax.grid(True)
        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots()
        plt.plot(sum_bike_2012['mnth'], sum_bike_2012['cnt'], marker='o', color="#01B6E1")
        ax.set_xlabel('Month')
        ax.set_ylabel('Total bicycle rental')
        ax.set_title('Total bicycle rental/Month - 2012')
        ax.grid(True)
        st.pyplot(fig)
    
    with st.expander(":orange[PENJELASAN]"):
        st.write(
            """Gambar diatas terdiri dari 3 grafik yaitu grafik jumlah penyewaan sepeda perbulan secara kesluruhan 
            dan dibawahnya terdapat 2 grafik jumlah penyewaan berdasarkan tahun yaitu 2011 dan 2012. 
            jika diperharikan dari ketiga garfik tersebut dapat terlihat bahwa jumlah penyewaan selalu naik cukup 
            signifikan dibulan mei, kemudian cukup mendapatkan kestabilan hingga bulan september kemudian turun 
            dimulai bulan oktober. Selain itu, dapat dilihat bahwa bulan januari selalu memiliki jumlah sewa
            terkecil bahkan secara keseluruhan bulan januari didapat jumlah sewa sebesar 134.933.
            """
        )
    
elif selected_menu == "Pengaruh Musim Terhadap Sewaan Sepeda":
    st.header('Grafik rata rata Penyewaan Sepeda berdasarkan Musim')
    season_X = ['Semi', 'Panas', 'Gugur', 'Dingin']
    colors = ["#5E808C", "#5E808C", "#01B6E1", "#5E808C"]
    fig, ax = plt.subplots()
    sns.barplot(
        y="cnt",  
        x= season_X,  
        data = season_Y,  
        palette= colors,
        ax=ax  
    )
    ax.set_title("Rata Rata Sewa Sepeda Berdasarkan Musim", loc="center")
    ax.set_ylabel("Rata Rata jumlah Sewa")
    ax.set_xlabel("Musim")
    st.pyplot(fig)
    with st.expander(":orange[PENJELASAN]"):
        st.write(
            """Dari grafik diatas terlihat bahwa rata rata jumlah sewa tertinggi ada
            dimusim gugur dengan rata rata sewaan 5644,303 sepeda, dan terendah ada 
            di musim semi dengan rata rata sewaan 2604.132 sepeda. 
            Dalam data, musim gugur berada dibulan juni-agustus dan musim semi dibulan 
            desember-februari. Jika kita hubungkan dengan data penyewaan berdarkan bulan 
            dalam grafik sebelumnya, terlihat bahwa pada bulan juni-agustus jumlah sewa
            memang cenderung stabil dalam kondisi tertinggi, dan dibulan des-februari jumlah
            sewa menunjukan jumlah yang sedikit.
            """
        )

elif selected_menu == "Pengaruh Cuaca Terhadap Sewaan Sepeda":
    st.header('Grafik rata rata Penyewaan Sepeda berdasarkan Cuaca')
    colors = ["#01B6E1", "#5E808C", "#5E808C"]
    fig, ax = plt.subplots()
    sns.barplot(
        y='cnt',  
        x= 'weathersit',  
        data = weathersit_Y,  
        palette= colors  
    )
    ax.set_title("Rata Rata Sewa Sepeda Berdasarkan Cuaca", loc="center")
    ax.set_ylabel("Rata Rata jumlah Sewa")
    ax.set_xlabel("Cuaca")
    st.pyplot(fig)
    st.markdown("**Keterangan Grafik 3:**")
    st.text("1 = Cuaca cerah, sedikit awan, berawan sebagian")
    st.text("2 = kabur berawan, kabut sedikit awan, kabut")
    st.text("3 = salju ringan, hujan ringan badai petir dan hujan ringan awan berserakan")
    st.text("4 = hujan lebat badai petir kabut salju")
    with st.expander(":orange[PENJELASAN]"):
        st.write(
            """Dari grafik diatas terlihat bahwa rata rata jumlah sewa tertinggi yaitu saat cuaca cenderung cerah (1)
            dengan rata rata sewa 4876.786 sepeda dan terendah adalah cuaca keempat atau cenderung hujan lebat, 
            bahkan dicuaca ini tidak ada satu sewa sepeda yang terjadi.
            """
        )
    
elif selected_menu == "Pengaruh Hari libur Terhadap Sewaan Sepeda":
    st.header('Grafik rata rata Penyewaan Sepeda saat hari libur dan hari kerja')
    fig, ax = plt.subplots()
    Working_Day = ['Akhir minggu/Libur', 'bukan akhir minggu dan bukan hari libur']
    sns.barplot(x='workingday', y='cnt', data=data_workingday, palette="deep")
    ax.set_xlabel(None)
    ax.set_ylabel('Rata Rata Sewa Sepeda')
    ax.set_title('Sewa Sepeda Akhir minggu/Libur vs. Hari Kerja')
    st.pyplot(fig)
    st.markdown("**Keterangan Grafik 4:**")
    st.text("0 = Akhir minggu/Libur")
    st.text("1 = bukan akhir minggu dan bukan hari libur")
    with st.expander(":orange[PENJELASAN]"):
        st.write(
            """Dari grafik diatas terlihat bahwa rata rata jumlah sewa tertinggi yaitu saat hari weekda atau bukan hari
            libur dan bukan akhir minggu.
            """
        )

    st.header('Grafik rata rata Penyewaan Sepeda saat hari libur atau hari kerja dalam satuan jam')
    col3, col4 = st.columns(2)
    with col3:
        fig, ax = plt.subplots()
        ax.plot(bike_hour['hr'], bike_hour['cnt'], marker='o', linewidth=2, color="#01B6E1")
        ax.set_xticks(np.arange(0, 24, 1))
        ax.set_xlabel('Jam')
        ax.set_ylabel('Rata Rata Sewa Sepeda')
        ax.set_title('Rata Rata Sewa Sepeda/Jam')
        ax.grid(True)
        st.pyplot(fig)
        st.markdown("**Keterangan Grafik:**")
        st.text("- Rata Rata Sewa Sepeda (Baik Hari Libur ")
        st.text(" atau Bukan)")

    with col4:
        fig, ax = plt.subplots()
        plt.plot(bike_hour_0['hr'], bike_hour_0['cnt'], marker='o', linewidth=2, color="#0092F6")
        plt.plot(bike_hour_1['hr'], bike_hour_1['cnt'], marker='o', linewidth=2, color="#F4029E")
        ax.set_xticks(np.arange(0, 24, 1))
        ax.set_xlabel('Jam')
        ax.set_ylabel('Rata Rata Sewa Sepeda')
        ax.set_title('Rata Rata Sewa Sepeda/Jam')
        ax.grid(True)
        st.pyplot(fig)
        st.markdown("**Keterangan Grafik:**")
        st.text("- Akhir Minggu/Hari Libur (Biru)")
        st.text("- Bukan Akhir Minggu dan Bukan Hari Libur (Merah)")
    
    with st.expander(":orange[PENJELASAN]"):
        st.write(
            """Dari grafik diatas secara keseluruhan terlihat bahwa rata rata jumlah sewa tertinggi terjadi di jam 
            8 pagi dan jam 5-6 sore.
            """
        )
        st.write(
            """Namun jika kita lihar dari garfik berdasarkan jenis hari, terlihat bahwa pada akhir minggu atau 
            hari libur rata rata jumlah sepeda mencapai puncak tertingginya di jam 12 siang hingga jam 5 sore."""
        )


elif selected_menu == "Distribusi Sewaan Sepeda Berdasarkan Hari":
    st.header("Distribusi Sewa Sepeda Berdasarkan Hari dalam Seminggu")
    fig, ax = plt.subplots()
    sns.boxplot(x='weekday', y='cnt', data=day_Data, palette = 'deep')
    ax.set_title("Rata Rata Sewa Sepeda Berdasarkan Hari dalam Seminggu", loc="center")
    ax.set_ylabel("Rata Rata jumlah Sewa")
    ax.set_xlabel("Hari")
    ax.grid(True)
    st.pyplot(fig)
    st.markdown("**Keterangan Grafik:**")
    st.text("0 = Senin| 1 = Selasa| 2 = Rabu|3 = Kamis| 4 = Jum'at| 5 = Sabtu| 6 = Minggu")
    with st.expander(":orange[PENJELASAN]"):
        st.write(
            """Jika kita lihat berdasarkan tabel jumlah sewa, hari sabtu memiliki jumlah 
            tertinggi sebesar 487.790 sewa, akan tetapi dalam boxplot terlihat bahwa hari 
            jumat memiliki nilai median tertinggi diantara lainnya hal ini menunjukkan bahwa 
            distribusi penyewaan sepeda pada hari Jumat lebih merata dan konsisten.
            """
        )

elif selected_menu == "Keterangan":
    st.header("WELCOME TO MY PROJECT! :sparkles:")
    st.write(
        """Hai, Saya adalah seorang yang sedang belajar banyak mengenai data science. 
        Adapun terkait Data analisis ini diambil dari sumber 
        [Bike-sharing-dataset](https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset) mengenai sewa sepeda 
        di tahun 2011-2012. analisis data yang tampil digunakan untuk project akhir dari 
        pelatihan data science dari dicoding. adapun logo yang tampil disebelah bukan logo 
        asli dari sumber data, dan tidak ada maksud untuk mengklaim data. logo yang tampil 
        penulis buat sendiri hanya untuk keperluan latihan project agar data yang tampil 
        lebih menarik. Saya terbuka terkait saran dari data analis yang saya buat terlebih 
        dari segala kekurangan dan keterbatasan yang saya miliki, silahkan tulis saran anda 
        jika berkenan. [My_Form](https://forms.gle/De9V6tCBX6CTokK87).

        """
    )
    st.text(" ")
    st.text("Hormat Saya,")
    st.text("Sri Nur Marshella")
    