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
def pump_dump_detector():
    """
    يكتشف العملات التي ارتفعت أو هبطت بسرعة أكثر من 10% خلال 24 ساعة
    """
    try:
        url = "https://api.binance.com/api/v3/ticker/24hr"
        data = requests.get(url).json()
        pumps = [d for d in data if float(d["priceChangePercent"]) >= 10]
        dumps = [d for d in data if float(d["priceChangePercent"]) <= -10]
        return {"pumps": pumps[:10], "dumps": dumps[:10]}  # أعلى 10 لكل
    except Exception as e:
        return {"error": str(e)}
