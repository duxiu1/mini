import logging

import requests
import app


class UserApi:
    """用户API接口方法"""

    def __init__(self):
        # 获取Token
        self.get_token_url = app.base_url + "/token/user"
        # Token验证
        self.token_verify_url = app.base_url + "/token/verify"
        # 地址信息
        self.user_address_url = app.base_url + "/address"

    def get_token_api(self):
        """获取Token"""
        # 请求体
        data = {"code": app.code}
        logging.info("获取token")
        # 返回请求对象
        return requests.post(self.get_token_url, json=data, headers=app.headers)

    def verify_token_api(self):
        """验证token"""
        # 请求参数
        data = {"token": app.headers.get("token")}
        logging.info("验证token")
        # 返回响应对象
        return requests.post(self.token_verify_url, json=data, headers=app.headers)

    def user_address_api(self):
        """地址信息"""
        logging.info("地址信息")
        return requests.get(self.user_address_url, headers=app.headers)
