from fastapi import FastAPI, Request
from messages_controler import message

app = FastAPI()


@app.post("/getUpdates")
async def root(request: Request):
    data = await request.json()
    message(data)
    print("goida")
    return {"status": "ok"}

