
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import openai

openai.api_key = "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"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatRequest):
    completion = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": req.message}]
    )
    reply = completion["choices"][0]["message"]["content"]
    return {"reply": reply}
