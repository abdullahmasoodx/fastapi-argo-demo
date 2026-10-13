from fastapi import FastAPI

app = FastAPI(
    title="FastAPI GitOps Demo",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Hello from FastAPI",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }