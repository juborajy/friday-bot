import os
import time
import requests
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

# --- ১. রেন্ডার পোর্ট লক সিস্টেম ---
class FridayServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"FRIDAY VIRUS-99 IS FULLY OPERATIONAL")

def run_port_fixer():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), FridayServer)
    print(f"[*] Port {port} secured. Render connection stable.")
    server.serve_forever()

# --- ২. হাই-ইন্টেলিজেন্স ট্রেডিং ইঞ্জিন (Binance) ---
def get_crypto_data(symbol):
    try:
        # আরও সঠিক ডেটা পাওয়ার জন্য এপিআই কল
        url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}"
        res = requests.get(url, timeout=10)
        data = res.json()
        # গত স্ক্রিনশটের এরর ফিক্স করতে গেট মেথড ব্যবহার
        return {
            'price': data.get('lastPrice', 'N/A'),
            'change': data.get('priceChangePercent', '0')
        }
    except Exception:
        return None

def start_friday_brain():
    print("--- 🧠 FRIDAY NEURAL NETWORK: SYNCED WITH GEMINI ---")
    my_coins = ["BTCUSDT", "PEPEUSDT", "VINUUSDT"]
    
    while True:
        print(f"\n[!] TIME: {time.strftime('%H:%M:%S')}")
        for coin in my_coins:
            info = get_crypto_data(coin)
            if info:
                price = info['price']
                change = float(info['change'])
                vibe = "🔥 BULLISH" if change > 0 else "🩸 BEARISH"
                print(f"[{coin}] Price: {price} | 24h: {change}% | Signal: {vibe}")
        
        print("--- 🤖 GEMINI AI ANALYZING NEXT MOVE... ---")
        time.sleep(30) # ৩০ সেকেন্ড পর পর আপডেট

if __name__ == "__main__":
    # পোর্ট সার্ভার চালু (রেন্ডার যাতে অফ না হয়)
    threading.Thread(target=run_port_fixer, daemon=True).start()
    
    # মেইন ইন্টেলিজেন্স ইঞ্জিন চালু
    start_friday_brain()
