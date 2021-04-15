import pytest
class Test_Demo2():
    @pytest.mark.demo
    def test_demo(self):
        a=5
        b=-1
        assert a!=b
        print("这是打标签为demo的用例")
    @pytest.mark.smoke
    def test_two(self):
        a=2
        b=-1
        assert a!=b
        print("这是打标签为smoke的用例")
    @pytest.mark.smoke
    @pytest.mark.demo
    def test_three(self):
        b=2
        assert 0==b #注意这个用例会失败
        print("这是打标签为smoke和add的用例")