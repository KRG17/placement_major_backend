from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from cn_subject import cn
from dbms_subject import dbms
from os_subject import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)

app.include_router(cn.router,
                   prefix="/cn",
                   tags=["Computer Networks"])

app.include_router(dbms.router,
                   prefix="/dbms",
                   tags=["DBMS"])

app.include_router(os.router,
                   prefix="/os",
                   tags=["OS"])

@app.get("/")
async def root():
    return {
        "message": "WOO-HOO!! Server UP!"
    }

