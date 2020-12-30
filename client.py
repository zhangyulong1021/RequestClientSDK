from urllib import parse

import requests

from django.conf import settings

import apis
from models import request, response


class SupplierRequestLog(object):
    """model"""
    pass


class Order(object):
    """model"""
    pass


class Client:
    def __init__(self):
        self.host = settings.DIDI_DELIVERY_PACKAGE_HOST
        self.headers = {"Content-Type": "application/x-www-form-urlencoded"}

    def _send(self, req: apis.Request, order: Order):
        with requests.session() as session:
            prepared_req = requests.Request(
                url=f"{self.host}{req.url}",
                method=req.method,
                data=parse.urlencode(req.data),
                headers=self.headers,
            ).prepare()
            log = self._save_log(req, order)
            resp = session.send(prepared_req)
            response_data = resp.json()
            log.response = response_data
            log.save()
            return req.response.parse_obj(response_data)

    def _save_log(self, req: apis.Request, order) -> SupplierRequestLog:
        """记录请求日志"""
        log = SupplierRequestLog.objects.create(
            order=order,
            supplier=SupplierRequestLog.SupplierChoices.DIDI,
            api_type=req.api_type,
            uri=f"{self.host}{req.url}",
            method=req.method,
            body=req.data,
            headers=self.headers,
        )
        return log

    def delivery_package(
        self, req: request.DeliveryPackageRequest, order
    ) -> response.DeliveryPackageResponse:
        return self._send(apis.DeliveryPackage(req), order)
