from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"FirstInitiate":"Hello World"}