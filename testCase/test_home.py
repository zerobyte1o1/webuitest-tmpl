import allure
import pytest
from handlers.home_handlers import HomeHandlers


@allure.epic("用户交互功能测试")
@allure.feature("场景：用户修改密码以及登出操作")
class TestHome:
    def setup_class(self):
        self.home = HomeHandlers()

    def teardown_class(self):
        pass

    def setup(self):
        self.home.page.goto('https://partner.shifang.co/#/homepage')

    @allure.story("用例-用户修改密码")
    @allure.title("修改密码_正常填写")
    @allure.description("进入修改密码页面，输入符合要求的密码确定保存")
    @allure.issue("", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("", name="点击，跳转到对应用例的链接地址")
    @pytest.mark.p0
    def test_change_password(self):
        with allure.step('进入修改密码页面'):
            self.home.change_password_handler()