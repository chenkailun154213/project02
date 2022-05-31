
from  projiece01.iter03_add_user import login

# 1、测试登录的测试用例
# case1:输入正确的用户名密码进行登录
# case2:输入错误的用户名或者密码登录
# case3:输入空的用户名或者密码登录

# 2、进行测试- 使用断言：assert 值1 操作符 值2
# 测试方式：预期结果 和 实际结果进行比较
# 以上用例 登陆成功的预期结果是code =0 ，
login_result = login('admin','123456')
logger.debug("登录返回数据：{}".format(login_result))
assert 0 == login_result.get('code')

# 存在的问题：
"""
1.无法查看运行的用例数，比如成功了几条失败了几条
2、如果失败了是因为什么导致？最好给出失败的错误日志
3、无法去组织用例 不能控制那些用例执行那些不执行

"""
# 解决方案 ：使用unittest去解决以上问题
