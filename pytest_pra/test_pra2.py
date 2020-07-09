import pytest,os,subprocess


class TestFun(object):

    def setup_method(self):
        print('setup_method')

    def teardown_method(self):
        print('setup_method')

    def test_1(self):
        print('运行test1')
        assert 1==1

    def test_2(self):
        print('运行test2')
        assert 1 == 2

    def test_3(self):
        print('运行test3')
        assert 1 == 1


if __name__ == '__main__':
    # pytest.main(["-s","test_pra.py"])
    # os.system('python --html=report.html')
    # subprocess.run('python --html=report.html')
    pytest.main(["-s",
                 str(__file__),
                 "--html=report.html"
                 ])