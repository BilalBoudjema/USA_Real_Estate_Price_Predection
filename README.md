Real Estate Price Predictor (USA)
This project predicts property prices across the USA using a machine learning model trained on real estate data. Built with Python, Pandas, Matplotlib, Scikit-learn, and deployed via Streamlit, it offers an intuitive interface to estimate property values based on features like bedrooms, bathrooms, and size.
🎯 Objective
Enable users—analysts, real estate agents, or enthusiasts—to estimate U.S. property prices by inputting:

Number of bedrooms and bathrooms
Lot size (acres)
Living area (square feet)
State and property status

📦 Dataset
🌐 Source
Sourced from the USA Real Estate Dataset on Kaggle, by Ahmed Shahriar Sakib.
📋 Characteristics

Initial Rows: 2,226,382
Key Columns: price, bed, bath, acre_lot, house_size, state, status
Challenges: Missing values, duplicates, irrelevant columns

🧹 Data Cleaning
Steps to prepare the dataset:

Removed columns: brokered_by, zip_code, prev_sold_date
Dropped rows with missing data
Removed duplicates
Encoded state and status to numerical formats
Final Dataset: 1.35M clean rows

df.drop(columns=["brokered_by", "zip_code", "prev_sold_date"], inplace=True)
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)

📊 Exploratory Analysis
Key insights:

Top 3 Most Expensive States:
Virgin Islands: $1,947,522
Hawaii: $1,491,548
District of Columbia: $1,209,649


Property distribution by state
Statistics on price, size, and other features

🤖 Modeling
A RandomForestRegressor from Scikit-learn predicts prices using:

bed: Number of bedrooms
bath: Number of bathrooms
acre_lot: Lot size (acres)
house_size: Living area (square feet)
state: Encoded state
status: Property status (sold or for_sale)

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(X_train, y_train)

🚀 Deployment
Hosted on Streamlit Cloud, the app provides a user-friendly interface for price estimates. Access it at: Real Estate Price Predictor.
📁 Project Structure
real_estate_price_predictor/
├── .devcontainer/              # Development container configuration
├── .gitattributes              # Git attributes
├── .gitignore                  # Git ignore file
├── README.md                   # Project documentation
├── Real_Estate_Prediction.ipynb # Jupyter Notebook with workflow
├── app.py                      # Streamlit application script
├── model.pkl                   # Trained RandomForestRegressor model
├── requirements.txt            # Python dependencies
├── scaler.pkl                  # Feature scaler

⚙️ Setup Instructions

Clone the Repository:
git clone https://github.com/BilalBoudjema/Real_Estate_USA_Price_Predection.git
cd real-estate-price-prediction


Install Dependencies:
pip install -r requirements.txt


Run the Application:
streamlit run app.py



✅ Results
The app delivers reliable price estimates based on 1.35M cleaned data points, ideal for real estate analysis and decision-making.
📬 Contact

Creator: Bilal Boudjema
Email: pro.bilal.boudjema@gmail.com
LinkedIn: Bilal Boudjema

