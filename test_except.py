

def test_div(num1, num2):
    """ 当除数为0时 """
    return num1 / num2

def test_file():
    """ 读取文件"""
    try:
        f = open('testx.txt', 'r', encoding='utf-8')
        rest = f.read()
        print(rest)
    except Exception as err:
        print('error')
        print(err)
    finally:
        try:
            f.close()
            print('closed')
        except:
            pass



if __name__ == '__main__':
    # try:
    #     rest = test_div(5, 0)
    #     print(rest)
    # except (ZeroDivisionError, TypeError) as err:
    #     print(" 反正就是报错了")
    #     print(err)
    # except TypeError:
    #     print(" 报错了，请输入数字")

        # rest = test_div(5, 's')
        # print(rest)
    test_file()