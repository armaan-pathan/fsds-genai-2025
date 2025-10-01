import streamlit as st
import pandas as pd
import pickle
import yfinance as yf

# ===========================
# Load the trained model
# ===========================
model_path = 'random_forest_model.pkl'
with open(model_path, 'rb') as file:
    model_rf = pickle.load(file)

# ===========================
# Prediction Function
# ===========================
def predict_btc_price(input_data):
    prediction = model_rf.predict(input_data)
    return prediction[0]

# ===========================
# Streamlit App
# ===========================
def main():
    # Title & Description
    st.title("Bitcoin Price Prediction App")
    st.write("""
    This interactive app predicts the **Bitcoin Closing Price** using a trained 
    **Random Forest Machine Learning Model**.  
    Enter USDT and BNB market values in the sidebar, and get the predicted BTC price instantly!
    """)

    # Sidebar Inputs
    st.sidebar.header("Input Market Data")

    usdt_close = st.sidebar.number_input("USDT Close Price", min_value=0.0, format="%.2f")
    usdt_volume = st.sidebar.number_input("USDT Volume", min_value=0.0, format="%.2f")
    bnb_close = st.sidebar.number_input("BNB Close Price", min_value=0.0, format="%.2f")
    bnb_volume = st.sidebar.number_input("BNB Volume", min_value=0.0, format="%.2f")

    # Example data button
    if st.sidebar.button("Use Example Data"):
        usdt_close, usdt_volume, bnb_close, bnb_volume = 1.00, 1000000.0, 300.0, 500000.0
        st.sidebar.write("Example values loaded!")

    # Prepare Input Data
    input_data = pd.DataFrame({
        'USDT_Close': [usdt_close],
        'USDT_Volume': [usdt_volume],
        'BNB_Close': [bnb_close],
        'BNB_Volume': [bnb_volume]
    })

    # Prediction Button
    if st.button("Predict BTC Close Price"):
        predicted_price = predict_btc_price(input_data)
        st.success(f"Predicted BTC Closing Price: **${predicted_price:,.2f}**")

        # Optional: Show recent BTC trend
        st.subheader("Recent BTC Market Trend")
        btc = yf.Ticker("BTC-USD")
        hist = btc.history(period="1mo")
        st.line_chart(hist["Close"])

if __name__ == '__main__':
    main()
