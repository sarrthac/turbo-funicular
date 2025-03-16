import alpaca_trade_api as tradeapi
from dotenv import load_dotenv
import os
import time

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
BASE_URL = 'https://paper-api.alpaca.markets'

# Initialize Alpaca API
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

# Function to check account details
def get_account():
    account = api.get_account()
    print(f"Account status: {account.status}")
    print(f"Cash available: ${account.cash}")

# Function to confirm order fill before proceeding
def confirm_order_filled(order_id):
    while True:
        order_status = api.get_order(order_id).status
        if order_status == 'filled':
            print("Order filled successfully.")
            break
        print("Waiting for order to fill...")
        time.sleep(5)

# Function to place a buy order with limit
def buy_stock(symbol, qty, limit_price):
    order = api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='limit',
        limit_price=limit_price,
        time_in_force='gtc'
    )
    print(f"Buy order placed for {qty} shares of {symbol} at ${limit_price}")
    confirm_order_filled(order.id)

# Function to place a sell order with limit
def sell_stock(symbol, qty, limit_price):
    time.sleep(10)  # Increased delay to ensure price movement
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='sell',
        type='limit',
        limit_price=limit_price,
        time_in_force='gtc',
        extended_hours=True
    )
    print(f"Sell order placed for {qty} shares of {symbol} at ${limit_price}")


def check_market_status():
    clock = api.get_clock()
    if clock.is_open:
        print("Market is OPEN.")
    else:
        print("Market is CLOSED.")
        print(f"Next open time: {clock.next_open}")
        print(f"Next close time: {clock.next_close}")

# Example Usage
if __name__ == "__main__":
    get_account()
    # buy_stock('AAPL', 1, 180)    # Buy at $180
    # sell_stock('AAPL', 1, 185)   # Sell at $185
    check_market_status()