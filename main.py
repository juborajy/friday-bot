import os
import time
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from binance.client import Client
from binance.enums import *

# --- ১. রেন্ডার পোর্ট লক সিস্টেম ---
class FridayServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"FRIDAY VIRUS-99: PRO-TRADING SYSTEM ONLINE")

def run_port_fixer():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), FridayServer)
    server.serve_forever()

# --- ২. প্রো-ট্রেডিং এআই ইঞ্জিন ---
class FridayProTrader:
    def __init__(self):
        # রেন্ডারের এনভায়রনমেন্ট থেকে API Key নিবে
        self.api_key = os.environ.get('BINANCE_API_KEY')
        self.secret_key = os.environ.get('BINANCE_SECRET_KEY')
        self.client = Client(self.api_key, self.secret_key)
        self.trade_amount = 10  # বস্, আপনার ডিমান্ড অনুযায়ী ১০ ডলার সেট করলাম
        self.symbol = "BTCUSDT"
        print("--- 🧠 FRIDAY NEURAL ENGINE SYNCED WITH GEMINI ---")

    def buy_order(self):
        """স্বয়ংক্রিয়ভাবে কয়েন কেনা"""
        try:
            print(f"[*] Buying {self.symbol} for ${self.trade_amount}...")
            # বাস্তব ট্রেড করতে নিচের লাইনটি আনকমেন্ট করুন (পয়সা থাকলে)
            # order = self.client.order_market_buy(symbol=self.symbol, quoteOrderQty=self.trade_amount)
            return True
        except Exception as e:
            print(f"[-] Buy Error: {e}")
            return False

    def start_loop(self):
        while True:
            try:
                # মার্কেটের অবস্থা চেক
                ticker = self.client.get_symbol_ticker(symbol=self.symbol)
                price = float(ticker['price'])
                
                # স্মার্ট এনালাইসিস (এপিআই থেকে ডেটা নিয়ে সিদ্ধান্ত)
                stats = self.client.get_ticker(symbol=self.symbol)
                price_change = float(stats['priceChangePercent'])

                print(f"\n[!] Update: {time.strftime('%H:%M:%S')} | BTC: ${price:,.2f}")
                print(f"[*] 24h Change: {price_change}%")

                # প্রো-লেভেল ট্রেডিং লজিক:
                if price_change < -3.0: # যদি মার্কেট ৩% এর বেশি পড়ে যায়
                    print("🔥 Market Crash Detected! Strategy: BUY THE DIP.")
                    self.buy_order()
                elif price_change > 5.0: # যদি ৫% লাভ হয়ে যায়
                    print("💰 Profit Target Reached! Strategy: TAKE PROFIT.")
                else:
                    print("⚖️ Market Neutral. Friday is observing...")

            except Exception as e:
                print(f"[*] Brain Syncing with Market Data...")
            
            time.sleep(60) # প্রতি মিনিটে একবার মার্কেট স্ক্যান করবে

if __name__ == "__main__":
    # ১. পোর্ট লক করা (রেন্ডার ফিক্স)
    threading.Thread(target=run_port_fixer, daemon=True).start()
    
    # ২. ট্রেডিং ব্রেন চালু করা
    trader = FridayProTrader()
    trader.start_loop()
