# 搜集selenium的一些常用知识
  * 使用Grid</br>
    * 必须先启动hub：Java -jar selenium-server-standalone-3.3.0.jar -role hub</br>
    * 启动节点，改变端口即可：Java -jar selenium-server-standalone-3.3.0.jar -role node -port 5555 -hub http://27.0.0.1:4444/grid/register </br>
      * -hub url 为节点指定hub地址，这个地址启动hub时会展示</br>
    * selenium控制台浏览器打开：http://127.0.0.1:4444/grid/console
    * 剩下就是在脚本中指定节点地址即可:
    <pre><code>
      driver = webdriver.Remote(
            command_executor=节点地址,
            desired_capabilities={
                'platform': 'ANY',
                'browserName': 指定浏览器,
                'version': '',
                'javascriptEnabled': True
            }
        )
    </pre></code>


# pytest_screenshots_pro
* control.py 控制执行文件
* 报告展示
![feature](https://github.com/linlin547/pytest_screenshots_pro/blob/master/worker/report_demo.png)
