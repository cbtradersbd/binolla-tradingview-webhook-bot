from fastapi import FastAPI
app = FastAPI()

@app.post("/webhook/tradingview")
async def handle_alert(payload: dict):
    print("Received TradingView alert for Binolla:", payload)
    return {"status": "success"}
