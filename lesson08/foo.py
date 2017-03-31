import time 


STR = "hello!"

def foo():
    return time.localtime()


def boo():
    return time.timezone



if __name__ == "__main__":
    # print dir(time)   
    print foo()