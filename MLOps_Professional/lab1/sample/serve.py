import uvicorn
import logging
import warnings

from fastapi import FastAPI
from data_model import MaintenancePayload
from maintenance import test_maintenance


app = FastAPI()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
warnings.filterwarnings("ignore")


@app.get("/ping")
async def ping():
    """Ping server to determine status

    Returns
    -------
    API response
        response from server on health status
    """
    return {"message":"Server is Running"}

@app.post("/maintenance")
async def predict(payload:MaintenancePayload):
    # Lab-1: Answer
    maintenance_result = test_maintenance(payload.temperature, payload.pressure)
    return {"msg": "Completed Analysis", "Maintenance Status": maintenance_result}

# Lab-1: Answer
@app.get("/supportbot")
async def supportbot(input: str = None):
    if input=="help":
        return {"message":"Bring the harvester in for maintenance"}
    return {"message":"SupportBot is working"}



if __name__ == "__main__":
    uvicorn.run("serve:app", host="0.0.0.0", port=5000, log_level="info")