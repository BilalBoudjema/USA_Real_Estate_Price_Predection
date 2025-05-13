# Real Estate Price Predictor (USA)

This project leverages a machine learning model to forecast property prices across the United States, utilizing real estate data. Developed using **Python**, **Pandas**, **Matplotlib**, **Scikit-learn**, and deployed with **Streamlit**, it provides an easy-to-use interface for estimating property values based on features such as bedrooms, bathrooms, and size.

## 🎯 Objective

The goal is to empower users—whether analysts, real estate professionals, or enthusiasts—to predict U.S. property prices by entering:

- Number of bedrooms and bathrooms  
- Lot size (in acres)  
- Living area (in square feet)  
- State and property status  

## 📊 Dataset

### 📁 Source  
Data is obtained from the [USA Real Estate Dataset](https://www.kaggle.com/datasets/ahmedshahriarsakib/us-real-estate-dataset) on Kaggle, authored by **Ahmed Shahriar Sakib**.

### 📌 Characteristics

- **Initial Rows**: 2,226,382  
- **Key Columns**: `price`, `bed`, `bath`, `acre_lot`, `house_size`, `state`, `status`  
- **Challenges**: Missing values, duplicate entries, and irrelevant columns  

## 🧹 Data Cleaning

The dataset was refined through the following steps:

### 🧹 Data Cleaning (Continued)

- **Removed columns**: `brokered_by`, `zip_code`, `prev_sold_date`
- **Eliminated rows with missing values**
- **Removed duplicate records**
- **Converted state and status into numerical formats**

### 📊 Final Dataset
- **Rows**: 1.35 million clean rows

```python
df.drop(columns=["brokered_by", "zip_code", "prev_sold_date"], inplace=True)
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
```


## 🔍 Exploratory Analysis

Key findings include:

### 🏆 Top 3 Most Expensive States:

1. **Virgin Islands**: $1,947,522
2. **Hawaii**: $1,491,548
3. **District of Columbia**: $1,209,649


## 📊 Distribution of Properties by State

Statistical insights on price, size, and additional features.

## 🧠 Modeling

A **RandomForestRegressor** from **Scikit-learn** is employed to predict prices, utilizing:

- `bed`: Number of bedrooms
- `bath`: Number of bathrooms
- `acre_lot`: Lot size (in acres)
- `house_size`: Living area (in square feet)
- `state`: Numerically encoded state
- `status`: Property status (sold or for_sale)

```python
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(X_train, y_train)
```

## Deployment
The application is hosted on Streamlit Cloud, offering a user-friendly interface for price predictions. Access it here: Real Estate Price Predictor.

## Project Structure

Real_Estate_USA_Price_Predection/
- `.devcontainer/`               # Development container configuration
- `.gitattributes`               # Git attributes
- `.gitignore`                   # Git ignore file
- `README.md`                    # Project documentation
- `Real_Estate_Prediction.ipynb` # Jupyter Notebook with workflow
- `app.py`                       # Streamlit application script
- `model.pkl`                    # Trained RandomForestRegressor model
- `requirements.txt`             # Python dependencies
- `scaler.pkl`                   # Feature scaler


## Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/BilalBoudjema/Real_Estate_USA_Price_Predection.git
cd Real_Estate_USA_Price_Predection
```


### Install Dependencies :
```bash
pip install -r requirements.txt
```

### Run the Application :
```bash
streamlit run app.py
```

## Results

The app provides accurate price estimates derived from 1.35 million cleaned data points, making it a valuable tool for real estate analysis and decision-making.

## Contact

**Creator:** Bilal Boudjema  
**Email:** [pro.bilal.boudjema@gmail.com](mailto:pro.bilal.boudjema@gmail.com)  
**LinkedIn:** [Bilal Boudjema](https://www.linkedin.com/in/bilalboudjema)

## App Link

[Real Estate Price Prediction App](https://bilalboudjema-usa-real-estate-price-predection-app-rwyfgv.streamlit.app/)

