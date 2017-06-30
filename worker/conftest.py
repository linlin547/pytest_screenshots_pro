#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest,time,os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = None
browser = None
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    # 失败截图
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # file_name = report.nodeid.replace("::", "_") + ".png"
            file_name = "screenshots"+os.sep+time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))+".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                    'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    # 截图
    driver.get_screenshot_as_file(name)
def pytest_cmdline_main(config):
    # 从命令行参数中取参数值
    global browser
    browser=config.getoption("--browser")[0]

def pytest_addoption(parser):
    # 添加参数
    parser.addoption("--browser", action="append",default = [], help="run by browser driver")

def pytest_generate_tests(metafunc):
    # 将参数添加到parametrize
    if 'browser' in metafunc.fixturenames:
        metafunc.parametrize("browser", metafunc.config.option.browser)

@pytest.fixture(scope='session', autouse=True)
def app():
    global driver
    browserMap = {
        "chrome": {
            "url": "http://127.0.0.1:5559/wd/hub",
            "type": DesiredCapabilities.CHROME,
        },
        "firefox": {
            "url": "http://127.0.0.1:5555/wd/hub",
            "type": DesiredCapabilities.FIREFOX,
        },
    }
    try:
        driver = webdriver.Remote(
            command_executor=browserMap.get(browser).get("url"),
            desired_capabilities=browserMap.get(browser).get("type")
        )
    except Exception,e:
        print e.message
    return driver
