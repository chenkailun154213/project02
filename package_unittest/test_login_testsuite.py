# 1、使用TestSuite(),可以将不同的测试用例添加到套件中（作用）

"""
b.TestSuite()功能
    1、addTset(testcase),tsetcase代表的是测试用例，可以添加不同的测试用例到套件中（单条）

"""

# 2、使用TextTestRunner（）类进行运行测试套件
"""
c.TextTestRunner()功能
1.run(suite),suite就是测试套件，可以将测试套件进行运行
"""
# 解决了可以按照不同的测试套件去运行

from  projiece01.iter03_add_user import login
import unittest
import sys
class TestLogin(unittest.TestCase):
#创建了TestLogin类继承了unittest.TestCase方法 方法是自带的
# 初始类方法
    @classmethod
    def setUpClass(cls) -> None:
        print("开始运行方法：",sys._getframe().f_code.co_name)

# 初始化方法
    def setUp(self)->None:
        print("开始运行方法：",sys._getframe().f_code.co_name)
# 清除方法
    def tearDowd(self) -> None:
        print("开始运行方法：",sys._getframe().f_code.co_name)



# 1、测试登录的测试用例
# case1:输入正确的用户名密码进行登录
    def test_login_success(self):
        print("开始运行方法：",sys._getframe().f_code.co_name)
        except_value = 0
        actual_value = login('admin','123456').get('code')
        self.assertEqual(except_value,actual_value)
# case2:输入错误的用户名或者密码登录
    def test_user_wrong(self):
        print("开始运行方法：",sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login('bca','123456').get('code')
        self.assertEqual(except_value,actual_value)
# case3:输入空的用户名或者密码登录
    def test_password_is_null(self):
        print("开始运行方法：",sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login('admin','').get('code')
        self.assertEqual(except_value,actual_value)

if __name__ == '__main__':
    #创建一个套件a
    suite_a = unittest.TestSuite()
    suite_a.addTest(TestLogin('test_login_success'))
    suite_a.addTest(TestLogin('test_user_wrong'))
    print(suite_a)

    runner = unittest.TextTestRunner()
    runner.run(suite_a)