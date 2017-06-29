import pytest,time
driver = None
@pytest.mark.test
class TestDemo():
    def setup_class(self):
        pass
    @pytest.mark.parametrize('url,name',[("http://www.baidu.com","baidu"),("http://www.taobao.com","taobao")])
    def test_app(self,app,url,name):
        print "----------->>>>>>>", name
        global driver
        driver = app
        app.get(url)
        time.sleep(5)
        assert 0
    def teardown_class(self):
        driver.quit()



