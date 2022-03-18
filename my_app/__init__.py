from fastapi import FastAPI, Request

app = FastAPI()

custom_header = dict(key="value", foo="value_foo", bar="value_bar")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.middleware("http")
async def add_custom_header(request: Request, call_next):
    response = await call_next(request)
    response.headers.update(custom_header)
    return response
