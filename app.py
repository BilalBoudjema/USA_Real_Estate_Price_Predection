# Importation des bibliothèques nécessaires
import streamlit as st
import numpy as np
import joblib


# Configuration de la page, doit être la première commande
st.set_page_config(
    page_title="Real Estate Price Prediction",  # Titre de la page
    page_icon="🏠",  # Icône de la page
    layout="wide",  # Mise en page large
    initial_sidebar_state="expanded"  # Sidebar ouverte par défaut
)

# Fonction pour charger les modèles et le scaler
@st.cache_resource
def load_resources():
    try:
        scaler = joblib.load('scaler.pkl')
        model = joblib.load('model.pkl')
        return scaler, model
    except FileNotFoundError as e:
        st.error("⚠️ Required files are missing. Please ensure 'scaler.pkl' and 'model.pkl' are in the directory.")
        st.stop()

# Chargement des ressources
scaler, model = load_resources()


# Ajout d'une image de bannière
st.image(
    "https://images.unsplash.com/photo-1582407947304-fd86f028f716?q=80&w=1992&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    use_container_width=True
)

# Titre et description
st.title('USA Real Estate Price Prediction Tool 🏠')
st.markdown(
    """
    Welcome to the **Real Estate Price Prediction App**!  
    This app helps you predict the price of a property based on the number of bedrooms, bathrooms, size in square feet, and lot size.  
    Simply fill in the details below and click **Predict** to get an estimate.
    """,
    unsafe_allow_html=True
)

# Ligne de séparation
st.divider()

# Fonction pour collecter les entrées utilisateur
def get_user_input():
    col1, col2, col3 = st.columns(3)

    with col1:
        bed = st.number_input('🛏️ Number of bedrooms', min_value=1, step=1, value=3)
    with col2:
        bath = st.number_input('🛁 Number of bathrooms', min_value=1, step=1, value=2)
    with col3:
        size = st.number_input('📏 Size in square feet', step=50, value=1500)
    with col3:
        acre_lot = st.number_input('📏 Lot Size (in acres)', step=0.1, value=0.21)

    return [bed, bath, size, acre_lot]

# Collecte des données utilisateur
X = get_user_input()

# Ligne de séparation
st.divider()

# Bouton pour prédire
if st.button('🔮 Predict'):
    try:
        # Transformation des données
        X_array = scaler.transform([np.array(X)])
        prediction = model.predict(X_array)[0]

        # Affichage du résultat
        st.success(f'🎉 The predicted price is: **${prediction:,.2f}**')
        st.balloons()
        
    except Exception as e:
        st.error(f"⚠️ An error occurred: {e}")
else:
    st.info('💡 Fill in the details above and click **Predict** to estimate the price.')