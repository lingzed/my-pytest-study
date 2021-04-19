#理解pytestd的结构setup和teardown
import pytest
# python中一个模块就是一个文件,setup_module可以实现整个模块中执行一次
def setup_module():
    print("\n￥￥￥￥￥setup module:整个模块中开始只执行一次￥￥￥￥￥")

def teardown_module():
    print("\n￥￥￥￥￥teardown module:整个模块中结束只执行一次￥￥￥￥￥")
#这是类外的测试用例
def setup_function():
    print("\nsetup function: 每个不在类中的用例开始前会执行！")
def teardown_function():
    print("\nteardown function: 每个不在类中的用例开始后会执行！")
def test_one():
    print("\n正在执行测试模块：test one")
def test_two():
    print("\n正在执行测试模块：test two")
# 测试类
class TestCase():
    def setup_class(self):
        print("\n**setup class:class类里面所有用例执行前执行")
    def teardown_class(self):
        print("\n**teardown class:class类里面所有用例执行后执行")
    def setup(self):
        print("\nsetup: 每个用例开始前都会执行")
    def teardown(self):
        print("\nteardown: 每个用例结束后执行")
    def test_three(self):
        print("\n正在执行测试模块：test three")
    def test_four(self):
        print("\n正在执行测试模块：test four")

