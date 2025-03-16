Trading Simulator

This Trading Simulator uses the Alpaca API to execute simulated stock trades for learning and testing purposes. Follow the steps below to set up and run the project.

🚀 Setup Instructions

1. Clone the Repository

git clone <repository-url>
cd TradingSimulator

2. Create a Virtual Environment

python -m venv venv

3. Activate the Virtual Environment

Windows:

.env\Scripts\activate

Mac/Linux:

source venv/bin/activate

4. Install Dependencies

pip install -r requirements.txt

5. Add Environment Variables

Create a .env file in the project root and add the following:

API_KEY=<Your_Alpaca_API_Key>
API_SECRET=<Your_Alpaca_API_Secret>

6. Run the Application

python main.py

🧩 Features

✅ Fetches account details✅ Places BUY and SELL orders using the Alpaca API✅ Uses limit orders to minimize wash trade detection✅ Ensures buy order is confirmed before proceeding with the sell order

🐞 Troubleshooting

If you face issues:

Verify the .env file has correct API credentials.

Ensure your Alpaca account is set to Paper Trading mode.

Confirm the virtual environment is activated before running the script.

📚 Dependencies

Python 3.11+

alpaca-trade-api

python-dotenv

requests

Run the following command to update pip if needed:

python.exe -m pip install --upgrade pip
