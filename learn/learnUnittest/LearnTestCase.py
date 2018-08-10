#coding:utf-8
import unittest
'''
定义了简单用例的创建，和执行
'''
class LearnTestCase(unittest.TestCase):
    #
    def setUp(self):
        pass

    #测试方法的方法名称都以 test打头。该命名规范用于告诉测试者哪些方法用于测试。
    def testCase1(self):
        print "\n"
        print "do test case 1"

    def testCase2(self):
        print "do test case 2"

    def testCase3(self):
        print "do test case 3"

    def tearDown(self):
        pass

if __name__ == '__main__':
    #unittest.main() 提供命令行接口的测试脚本，可直接从命令行运行该测试
    #unittest.main()

    #也可以用以下方法来控制测试用例的执行
    suite = unittest.TestLoader().loadTestsFromTestCase(LearnTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
