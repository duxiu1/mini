from Api.apiFactory import ApiFactory
from Api.product import ProductApi
from Api.user import UserApi

# 调用轮播图
# print("轮播图:{}".format(ApiFactory.get_home_api().banner_api().json()))

# 调用主题
# print("专题栏:{}".format(ApiFactory.get_home_api().theme_api().json()))

# 调用最近新品
# print("最近新品:{}".format(ApiFactory.get_home_api().recent_product_api().json()))

# 调用商品分类
# print("分类:{}".format(ApiFactory.get_product_api().product_classify_api().json()))

# 调用分类下商品
# print("分类下商品:{}".format(ApiFactory.get_product_api().classify_product_api(5).json()))

# 调用商品信息
# print("商品信息:{}".format(ApiFactory.get_product_api().product_detail_api(26).json()))

# print(f"返回值:{ApiFactory.get_user_api().get_token_api().json()}")

print(f"查看订单：{ApiFactory.get_order_api().order_list_api().json()}")
print(f"创建订单：{ApiFactory.get_order_api().create_order_api(12, 7).json()}")
print(f"订单详情：{ApiFactory.get_order_api().query_order_api(110).json()}")
