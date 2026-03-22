import time
from binance.client import Client

# Boss Juboraj's Master Keys
API_KEY = 'qYU8FJNEXj6KQctco3qzjoAOYgcYDtXwjCQUg7vhyo6Vn5DhXbwnZQtOxR7Pz4lu'
API_SECRET = 'jcqhCTJR2xKuRNwQc2ucLmYE7FogBCHTfRAIZ77ttwSXgMf1crS8N6uRq9k9xxbl'

def start_bot():
    print("--- 🚀 FRIDAY VIRUS-99 IS LIVE ON RENDER 🚀 ---")
    try:
        # Render সার্ভারে কোনো প্রক্সি লাগে না
        client = Client(API_KEY, API_SECRET)
        print("Connected to Binance Successfully! ✅")
        
        while True:
            ticker = client.get_symbol_ticker(symbol="BTCUSDT")
            print(f"🕒 {time.strftime('%H:%M:%S')} | BTC Price: ${float(ticker['price']):,.2f}")
            time.sleep(60)
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    start_bot()

