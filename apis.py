from typing import Dict, Any

from pydantic.main import BaseModel

from models import request
from models.response import DeliveryPackageResponse


class Request:
    url: str
    method: str
    params: Dict[str, Any] = {}
    data: Dict[str, Any] = {}
    body: Dict[str, Any] = {}
    response: BaseModel
    api_type: str = ""


class DeliveryPackage(Request):
    """
    发券接口
    """

    url = "/veyron/market_entry/service/coupon/doBind"
    method = "post"
    response = DeliveryPackageResponse
    api_type = "didi_recharge"

    def __init__(self, req: request.DeliveryPackageRequest):
        self.data = req.dict()
