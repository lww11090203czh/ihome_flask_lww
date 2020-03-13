#  coding:utf-8

# 装饰器demo

import functools



def login_required(func):

    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        pass

    return wrapper


@login_required
def itcast():
    """itcast python"""
    pass

print(itcast.__name__)  #wrapper.__name__
print(itcast.__doc__)   #wrapper.__doc__











