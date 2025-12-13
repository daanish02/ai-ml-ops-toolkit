from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {"hello": "world"}


@app.get("/health")
async def health_check():
    return {"status": "ok"}
