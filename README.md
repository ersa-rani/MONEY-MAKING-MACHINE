# 💰 MONEY MAKING MACHINE 💰  

This is a fun and interactive Streamlit web app that generates random money amounts, provides side hustle ideas, and shares motivational money quotes.  

## 🚀 Features  

1. **Instant Cash Generator** – Click a button to randomly generate an amount of money.  
2. **Side Hustle Ideas** – Get random side hustle suggestions from an API.  
3. **Money Making Motivation** – Receive money-related motivational quotes from an API.  

## 🛠️ Technologies Used  

- **Python**  
- **Streamlit** – For building the web app.  
- **Random module** – To generate random money amounts.  
- **Time module** – For simulating a delay when generating money.  
- **Requests module** – For fetching side hustles and quotes from an external API.  

## 📜 How It Works  

1. **Money Generator**  
   - When you click the "Generate Money" button, the app picks a random amount between $1 and $1000 and displays it after a short delay.  

2. **Side Hustle Generator**  
   - Fetches a random side hustle idea from an API (`http://127.0.0.1:8000/side_hustles`).  
   - If the API is unavailable, it defaults to "Freelancing."  

3. **Money Quotes Generator**  
   - Retrieves a random money-related quote from an API (`http://127.0.0.1:8000/money_quotes`).  
   - If the API is unavailable, it defaults to "Money is the root of all evil."  

## 🎨 Custom Styling  

The app includes custom styling for buttons using Streamlit's `st.markdown()` method with embedded CSS.  

## 📝 Notes  

- The API endpoints used in this project are placeholders. Make sure to update them if you're using a real API.  
- If the API is unavailable, the app provides default values to ensure smooth functionality.  
