# coding=utf-8
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
# 如果未登陆，则转到登陆界面
def login(func):
    def login_fun(request,*args, **kwargs):
        if login_fun.session.has_key('user_id'):
            return func(request,*args, **kwargs)
        else:
            red = HttpResponseRedirect('/user/login')
            red.set_cookie('url',request.get_full_path)
            return red
    return login_fun

