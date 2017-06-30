#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest,time
driver = None
@pytest.mark.test
class TestDemo():
    def setup_class(self):
        pass
    @pytest.mark.parametrize('url,name',[("http://www.baidu.com","baidu"),("http://www.taobao.com","taobao")])
    def test_app(self,app,url,browser):
        # browser：命令行参数
        # app：conftest声明的driver
        print "----------->>>>>>>", browser
        global driver
        driver = app
        app.get(url)
        time.sleep(5)
        assert 0
    def teardown_class(self):
        driver.quit()



