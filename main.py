from fastapi import FastAPI

app = FastAPI(
    title="JBener API",
    description="API para JBener Dashboard",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Hello, JBener! FastAPI corriendo en Docker."}
