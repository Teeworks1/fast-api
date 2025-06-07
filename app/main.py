from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "API is running"}

@app.get("/hello")
def say_hello(name: str = "World"):
    return {"message": f"Hello, {name}!"}
