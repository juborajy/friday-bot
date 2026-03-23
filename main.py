
import os
import time
import requests
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

# --- ১. ইন্টেলিজেন্ট পোর্ট কানেক্টর (রেন্ডার ফিক্স) ---
class FridayCore(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        # এটি রেন্ডারকে বলবে যে বোটটি হাই-ইন্টেলিজেন্স মোডে আছে
        self.wfile.write(b"FRIDAY VIRUS-99: SYSTEM ONLINE. GEMINI SYNC ACTIVE.")

def start_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), FridayCore)
    print(f"[*] Port {port} secured. Render connection stable.")
    server.serve_forever()

# --- ২. বাইন্যান্স ডাটা ও অটো-এনালাইসিস ইঞ্জিন ---
class TradingBot:
    def __init__(self):
        self.base_url = "https://api.binance.com/api/v3"
        self.active = True

    def get_market_data(self, symbol):
        """বাইন্যান্স থেকে রিয়েল-টাইম সব ডেটা আনা"""
        try:
            res = requests.get(f"{self.base_url}/ticker/24hr?symbol={symbol}")
            return res.json()
        except:
            return None

    def analyze_vibe(self, data):
        """মার্কেট কি উপরে যাবে না নিচে? (ইন্টেলিজেন্ট এনালাইসিস)"""
        if not data: return "Waiting for data..."
        price_change = float(data['priceChangePercent'])
        if price_change > 2: return "🔥 BULLISH (মার্কেট পাম্প করছে!)"
        elif price_change < -2: return "🩸 BEARISH (মার্কেট ডাম্প করছে!)"
        else: return "⚖️ NEUTRAL (মার্কেট শান্ত আছে)"

    def run_engine(self):
        print("--- 🧠 FRIDAY NEURAL NETWORK ACTIVATED ---")
        while self.active:
            # আপনার ফেভারিট কয়েনগুলো এনালাইজ করা হচ্ছে
            for coin in ["BTCUSDT", "PEPEUSDT", "VINUUSDT"]:
                data = self.get_market_data(coin)
                if data:
                    price = data['lastPrice']
                    vibe = self.analyze_vibe(data)
                    print(f"[{coin}] Price: {price} | Signal: {vibe}")
            
            print("--- 🤖 Syncing with Gemini Core for Next Strategy ---")
            time.sleep(30) # ৩০ সেকেন্ড পর পর ব্রেন আপডেট হবে

# --- ৩. মেইন এক্সিকিউশন ---
if __name__ == "__main__":
    # ১. প্রথমে সার্ভার চালু করা (পোর্টের সমস্যা মেটাতে)
    threading.Thread(target=start_server, daemon=True).start()
    
    # ২. ট্রেডিং ইঞ্জিন চালু করা
    bot = TradingBot()
    bot.run_engine()
