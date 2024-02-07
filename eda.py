import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Konfigurasi layout webpage
st.set_page_config(
    page_title='Crop Recommendation for Sustainable Agriculture',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Set up the webpage
def run():
    # Title
    st.title('Crop Recommendation for Sustainable Agriculture')

    # Sub-header
    st.subheader('Rekomendasi Pemilihan Tanaman Berdasarkan Kondisi Lingkungan')

    # Deskripsi
    st.write('Webpage ini dibuat untuk menganalisa dan memberikan rekomendasi tanaman budidaya yang optimal \
              berdasarkan kondisi lingkungan yang ada. Dataset yang digunakan berisi parameter-parameter lingkungan \
              seperti suhu, kelembapan, pH tanah, dan curah hujan, yang semuanya mempengaruhi jenis tanaman \
              yang dapat dibudidayakan secara berkelanjutan.')

    st.write('Berikut adalah dataset yang bersangkutan:')
    
    # Load Dataframe
    df = pd.read_csv('Crop_recommendation_Rework.csv')
    st.dataframe(df)

    ## VISUALISASI ##
    # Set the aesthetic style of the plots
    sns.set_style("whitegrid")

    # Plotting distribution of numeric variables
    selected_crops = ['rice', 'wheat', 'mungbean', 'coffee']
    df_selected_crops = df[df['label'].isin(selected_crops)]
    # Initialize the figure
    plt.figure(figsize=(20, 10))
    for i, column in enumerate(['N', 'P', 'K', 'rainfall'], start=1):
        plt.subplot(2, 2, i)
        sns.boxplot(x='label', y=column, data=df_selected_crops)
        plt.title(f'{column} Requirement by Crop')
    st.pyplot(plt.gcf())  # Display the current figure using Streamlit
    plt.clf()  # Clear the current figure to prevent overlap with the next plot

    st.write('Input data untuk prediksi dapat dilakukan di page Prediction.')

    # Menambahkan gambar
    image_path = 'Ayo Mulai Hargai Jasa Petani Indonesia, Karena Mereka Perut Kita Terpenuhi.png'
    st.image(image_path, caption='Ayo Mulai Hargai Jasa Petani Indonesia, Karena Mereka Perut Kita Terpenuhi')

if __name__ == '__main__':
    run()
