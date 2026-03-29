from pydantic import BaseModel

class SensorData(BaseModel):
    temperature: float
    humidity: float
    motion: int
    smoke: int
    power_usage: float