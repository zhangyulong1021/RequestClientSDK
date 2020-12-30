from typing import Optional, List

from pydantic.main import BaseModel


class _Card(BaseModel):
    id: str
    name: str
    startTime: str  # noqa: N815
    endTime: str  # noqa: N815
    days: str
    citys: str


class Package(BaseModel):
    amount: int  # 券金额，单位为分，couponType为3时使用
    name: Optional[str]  # 券名称/卡名称
    desc: Optional[str]  # 券第三行文案描述
    expireTime: str  # 券过期时间    # noqa: N815
    couponType: str  # 券类型 3：抵扣券，固定金额 100：折扣券   # noqa: N815
    discount: Optional[str]  # 折扣力度，couponType为100时使用，90表示9折
    batchid: str


class _Data(BaseModel):
    number: int  # 券总张数
    amount: int  # 券总金额
    coupon_list: List[Package]  # 券/月卡列表
    card_list: Optional[List[_Card]]


class DeliveryPackageResponse(BaseModel):
    """发券接口"""

    errno: int  # 错误码
    errmsg: str  # 券总张数
    data: Optional[_Data]
