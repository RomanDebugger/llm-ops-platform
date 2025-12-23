from fastapi import FastAPI

app = FastAPI(title="LLM Ops Platform")

@app.get("/health")
def health():
    return {"status": "ok"}
