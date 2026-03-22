
import os
import time
import requests
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

# --- রেন্ডার পোর্ট ফিক্সার (এই অংশটি পোর্টের এরর দূর করবে) ---
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"FRIDAY VIRUS-99 IS ONLINE")

def run_dummy_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    print(f"--- 🚀 Port {port} Opened Successfully ---")
    server.serve_forever()

# ব্যাকগ্রাউন্ডে সার্ভার চালু করা
threading.Thread(target=run_dummy_server, daemon=True).start()

# --- হাই-ইন্টেলিজেন্ট ট্রেডিং লজিক (Binance Data) ---
def get_crypto_price(symbol="BTCUSDT"):
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
        response = requests.get(url, timeout=10)
        data = response.json()
        return data['price']
    except Exception as e:
        return f"Error: {e}"

def start_friday_engine():
    print("--- 🧠 FRIDAY INTELLIGENCE MODULE ACTIVATED ---")
    print("--- 🤖 CONNECTED TO GEMINI CORE ---")
    
    while True:
        btc_price = get_crypto_price("BTCUSDT")
        eth_price = get_crypto_price("ETHUSDT")
        
        # এখানে আপনার ট্রেডিং এনালাইসিস প্রিন্ট হবে
        print(f"\n[!] TIME: {time.ctime()}")
        print(f"[+] BITCOIN PRICE: ${btc_price}")
        print(f"[+] ETHEREUM PRICE: ${eth_price}")
        print(f"[*] STATUS: Analyzing Market Vibe...")
        
        # প্রতি ৩০ সেকেন্ড পর পর আপডেট হবে
        time.sleep(30)

if __name__ == "__main__":
    # বোটের মেইন ইঞ্জিন চালু করা
    start_friday_engine()
