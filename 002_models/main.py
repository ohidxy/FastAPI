from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Device(BaseModel):
    device_id: str
    name: str
    status: int
    is_alive: Optional[bool] = None


@app.put('/device/{device_id}')
def update_item(device_id: str, device: Device):
    return {"device_id": device_id, "device_name": device.status}
