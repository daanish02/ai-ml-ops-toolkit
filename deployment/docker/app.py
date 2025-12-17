from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/")
async def home():
    return {"hello": "world"}


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.get("/predict")
async def predict(x: float = Query(..., description="Number to cube")):
    return {"input": x, "cube": x**3}
