import requests

BINANCE_API = "https://api.binance.com/api/v3/trades?symbol={symbol}&limit=500"

def whale_tracker(symbol="BTCUSDT", threshold=50000):
    """
    يراقب الصفقات الكبيرة على Binance
    symbol: الزوج الذي تريد مراقبته
    threshold: الحد الأدنى لقيمة الصفقة لتعتبر حوت
    """
    try:
        response = requests.get(BINANCE_API.format(symbol=symbol))
        trades = response.json()
        big_trades = [t for t in trades if float(t['qty'])*float(t['price']) >= threshold]
        return big_trades[-20:]  # آخر 20 صفقة كبيرة
    except Exception as e:
        return {"error": str(e)}
