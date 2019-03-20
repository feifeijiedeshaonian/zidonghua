import unittest
from HTMLTestRunner import HTMLTestRunner

casePath = "C:\\Users\\LENOVO\\Desktop\\python\\美腾\\zhiyou_guanli\\创建正式项目与子项目"
rule = "test*.py"
discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
print(discover)

reportPath = "E:\\html\\"+"report.html"

fp=open(reportPath,"wb")

runner =HTMLTestRunner(stream=fp,
                    title="baogao",
                    description="描述",
                    retry = 1)

runner.run(discover)
fp.close()