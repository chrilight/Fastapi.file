from fastapi import FastAPI

app = FastAPI


@app.get("/ola")
def say_hello():
    return "Hello"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
