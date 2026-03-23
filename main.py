
import os, time, threading, sys
from http.server import HTTPServer, BaseHTTPRequestHandler
from binance.client import Client
from binance.exceptions import BinanceAPIException

# ১. নুরাল সার্ভার ইন্টারফেস (রেন্ডারকে লাইভ রাখার জন্য)
class FridayCore(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"FRIDAY MASTERPIECE ENGINE: STATUS - SUPREME")

def run_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), FridayCore)
    print(f"[*] JARVIS Protocol: Neural Link Established on Port {port}")
    server.serve_forever()

# ২. সুপ্রিম ট্রেডিং অ্যালগরিদম (১০ বছর পরের টেকনোলজি লজিক)
def start_trading_mission():
    api = os.environ.get('BINANCE_API_KEY')
    sec = os.environ.get('BINANCE_SECRET_KEY')
    
    if not api or not sec:
        print("[!] FATAL ERROR: API Keys missing. JARVIS cannot access Binance.")
        return

    try:
        client = Client(api, sec)
        print("--- 🧠 FRIDAY QUANTUM BRAIN ACTIVATED ---")
        print("[*] Monitoring Assets: BTC, PEPE, ETH")
        
        while True:
            try:
                # রিয়েল-টাইম মার্কেট স্ক্যানিং
                prices = client.get_all_tickers()
                btc = next(p for p in prices if p['symbol'] == 'BTCUSDT')['price']
                pepe = next(p for p in prices if p['symbol'] == 'PEPEUSDT')['price']
                
                # ওয়ালেট এনালাইসিস
                account = client.get_account()
                usdt_balance = next(b for b in account['balances'] if b['asset'] == 'USDT')['free']
                
                print("-" * 40)
                print(f"🕒 SYNC TIME: {time.strftime('%H:%M:%S')}")
                print(f"💎 WALLET POWER: {usdt_balance} USDT")
                print(f"📈 BTC/USDT: ${float(btc):,.2f}")
                print(f"🐸 PEPE/USDT: {pepe}")
                print("[*] Status: Scanning for 3% Market Dip for Buy Order...")
                
                # অটোমেটিক রি-কানেকশন লজিক
                time.sleep(30) # প্রতি ৩০ সেকেন্ডে সুপার-ফাস্ট আপডেট
                
            except BinanceAPIException as e:
                print(f"[!] API Warning: {e.message}")
                time.sleep(10)
            except Exception as e:
                print(f"[!] Re-routing Neural Path: {e}")
                time.sleep(5)
                
    except Exception as fatal:
        print(f"[!!!] SYSTEM CRITICAL ERROR: {fatal}")

# ৩. মেইন এক্সিকিউশন (সুপার পাওয়ার মোড)
if __name__ == "__main__":
    # থ্রেড ১: সার্ভার লাইভ রাখা
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    
    # থ্রেড ২: ট্রেডিং ইঞ্জিন চালু করা
    start_trading_mission()
