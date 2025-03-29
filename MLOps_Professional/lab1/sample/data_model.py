from pydantic import BaseModel
# Lab-1: Add pressure parameter
class MaintenancePayload(BaseModel):
    temperature: int
    pressure: int
