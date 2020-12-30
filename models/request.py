import json
from typing import Optional

from pydantic import validator
from pydantic.main import BaseModel

from tools.aes import AESCBCEncrypt


class _Data(BaseModel):
    country_code: Optional[str]  # 手机号国家码, 如: +86
    phone: str  # 手机号码
    source: str  # 渠道（商家）
    city_id: Optional[str]  # 城市id
    geo: Optional[str]  # 经纬度信息
    ext: Optional[str]  # 扩展字段, json


class DeliveryPackageRequest(BaseModel):
    """发券接口"""

    source: str
    data: _Data

    @validator("data")
    def encrypt(cls, data):
        data_ = json.dumps({k: v for k, v in data.dict().items() if v is not None})
        aes = AESCBCEncrypt()
        return aes.encrypt(data_)
