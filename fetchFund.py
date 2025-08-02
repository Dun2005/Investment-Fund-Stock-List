import time
from fastapi import FastAPI
from vnstock import Fund
from fastapi.middleware.cors import CORSMiddleware

fund = Fund()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/get-top-holding")
async def root():
    data = fund.details.top_holding('SSISCA')
    # time.sleep(60)
    return data.to_dict(orient="records")