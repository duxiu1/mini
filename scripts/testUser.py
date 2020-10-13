import logging

from Api.apiFactory import ApiFactory
import app
import utils, pytest


@pytest.mark.run(order=0)
class TestUserApi:

    def test_get_token(self):
        res = ApiFactory.get_user_api().get_token_api()
        # 打印请求地址 请求参数 请求响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言token存在
        assert len(res.json().get("token")) > 0
        # 保存token到app配置文件
        app.headers["token"] = res.json().get("token")
        print("app.headers:{}".format(app.headers))

    def test_verify_token(self):
        """验证token"""
        res = ApiFactory.get_user_api().verify_token_api()
        # 打印请求地址 请求参数 请求响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言有效
        assert res.json().get("isValid") is True

    def test_user_address(self):
        """用户地址信息"""
        res = ApiFactory.get_user_api().user_address_api()
        # 打印请求地址 请求参数 请求响应数据
        logging.info("请求地址:{}".format(res.url))
        logging.info("响应数据:{}".format(res.json()))
        # 断言状态码
        utils.common_assert_code(res)
        # 断言信息
        assert False not in [i in res.text for i in ["小鬼", "1301111111", "上海市"]]
