from PIL import Image
import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import math
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from ucimlrepo import fetch_ucirepo
import re


df=pd.read_csv('diabete_maj')
df2=df.iloc[:10, :15]

def main():
    title_placeholder = st.empty()  # Placeholder pour le titre

        



    st.sidebar.title('Menu')
    option = st.sidebar.selectbox(
        'Sélectionnez une page',
        ('Accueil', 'dataset ', 'distribution des données', 'informations sur les prescriptions', 'informations sur les réadmissions','informations sur les maladies','Modèles de Machine Learning utilisés')
    )

    if option == 'Accueil':
        title_placeholder.title("Diabetes in 130-US hospitals during 1999-2008")
        
        
        
    elif option == 'dataset':
        title_placeholder.empty()
        st.dataframe(df2.head())
        
    elif option == 'informations sur les réadmissions':
         title_placeholder.empty()
         title_placeholder.title('influence des variables sur les réadmissions')
         st.write("") 
         st.write("") 
         st.write("réadmission selon l'âge")
         st.image("read_age.png")
         st.write("") 
         st.write("") 
         st.write("réadmission selon l'ethnie")
         st.image("read_ethnie.png")
         
        
        
        
    elif option == 'distribution des données':
        title_placeholder.empty()
        title_placeholder.title('répartition des données du dataset')
        st.image("distribution.png")
        
        
    elif option == 'informations sur les prescriptions':
        title_placeholder.empty()
        title_placeholder.title('Nombre de prescriptions par médicament')
        st.image("prescription.png")
        
    
    elif option == 'informations sur les maladies':
        title_placeholder.empty()
        title_placeholder.title("maladies les plus fréquentes selon le diagnostic")
        
        st.image("top10_diag1.png")
        st.write("")  
        st.image("top10_diag2.png")
        st.write("") 
        st.image("top10_diag3.png")
        
    elif option == 'Modèles de Machine Learning utilisés':
        title_placeholder.empty()
        st.image("ML.png")


if __name__ == '__main__':
    main()
