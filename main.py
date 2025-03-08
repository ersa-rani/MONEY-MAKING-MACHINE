import streamlit as st
import random 
import time
import requests

# Custom styling
st.markdown(
    """
    <style>
        .stButton button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            border-radius: 10px;
            padding: 10px 20px;
        }
        .stButton button:hover {
            background-color: #45a049;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("💰 MONEY MAKING MACHINE 💰")

# Money Generator
def generate_money():
    return random.randint(1, 1000)

st.subheader("💵 Instant Cash Generator")
if st.button("Generate Money"):
    st.write("Counting your money... 💸")
    time.sleep(2)
    amount = generate_money()
    st.success(f"You made ${amount}!")

# Side Hustle Generator
def fetch_side_hustle():
    try: 
        response = requests.get("http://127.0.0.1:8000/side_hustles?api_key=1234567890")
        if response.status_code == 200:
            hustles = response.json()
            return hustles.get("side_hustle", "Freelancing")
        else:
            return "Freelancing"
    except:
        return "Something went wrong..."

st.subheader("💼 Side Hustle Ideas")
if st.button("Generate Hustle"):
    idea = fetch_side_hustle()
    st.success(idea)

# Money Quotes Generator
def fetch_money_quotes():
    try: 
        response = requests.get("http://127.0.0.1:8000/money_quotes?api_key=1234567890")
        if response.status_code == 200:
            quotes = response.json()
            return quotes.get("money_quote", "Money is the root of all evil")
        else:
            return "Money is the root of all evil"
    except:
        return "Something went wrong..."

st.subheader("📢 Money Making Motivation")
if st.button("Get Inspired"):
    quote = fetch_money_quotes()
    st.info(quote)
