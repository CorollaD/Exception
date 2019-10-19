

class MyException(Exception):
    """ 我的自定义异常"""
    pass


class InvalidCtrlExec(Exception):
    """ 当参数不合法时触发"""
    def __init__(self, err_code, err_msg):
        """

        :param err_code:
        :param err_msg:
        """
        self.err_code = err_code
        self.err_msg = err_msg

    def __str__(self):
        return 'Error: {0} - {1}'.format(self.err_code, self.err_msg)



def test_exec(num1, num2):
    """ 除法的实现"""
    if isinstance()
