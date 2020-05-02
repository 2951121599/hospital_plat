from django.http import JsonResponse
from django.shortcuts import *
from .models import User, UserDoc
from functions.decorators import login_required


def register(request):
    return render(request, 'user/register.html')


# 提交注册页的表单
def register_handle(request):
    # 获取数据
    username = request.POST.get('username')
    password = request.POST.get('password')
    print("username,password:------------", username, password)
    # 校正数据
    # 数据有空
    if not all([username, password]):
        return render(request, 'user/register.html', {'errmsg': '参数不能为空'})

    # 业务处理，向系统中添加账户
    try:
        User.objects.add_one_passport(
            username=username,
            password=password,
        )
    # 打印异常
    except Exception as e:
        print("e:", e)
        return render(request, 'user/register.html', {'errmsg': '用户名已存在'})
    # 注册完返回登录页
    return render(request, 'user/login.html')


# 显示登录页面
def login(request):
    # 如果能从cookies中获取到username则表示点击过“保存用户名”
    if request.COOKIES.get('username'):
        username = request.COOKIES.get('username')
    else:
        username = ''
    context = {
        'username': username,
    }
    return render(request, 'user/login.html', context)


# 验证登录
def login_check(request):
    # 1.获取数据
    username = request.POST.get('username')
    password = request.POST.get('password')

    # 2.验证数据
    if not all([username, password]):
        # 有数据为空
        return JsonResponse({"res": 2})

    # 3.进行处理：根据用户名和密码查找账户信息
    passport = User.objects.get_one_passport(username=username, password=password)
    if passport:
        turn_to = reverse('patient:index')
        jres = JsonResponse({"res": 1, "turn_to": turn_to})

        # 记住用户的登录状态
        request.session['islogin'] = True
        request.session['username'] = username
        request.session['passport_id'] = passport.id
        return jres
    else:
        # 用户名密码错误
        return JsonResponse({"res": 0})


# 登出
def logout(request):
    # 清除session信息
    request.session.flush()
    return redirect(reverse('patient:index'))


@login_required
def user(request):
    if request.method == 'GET':
        passport_id = request.session.get('passport_id')  # 数据表中的id
        user = User.objects.get(id=passport_id)
        return render(request, 'user/user_center_info.html', locals())
    else:
        return HttpResponse("请使用GET请求数据!")


# 医生登录
# 显示登录页面
def login2(request):
    # 如果能从cookies中获取到username则表示点击过“保存用户名”
    if request.COOKIES.get('username'):
        username = request.COOKIES.get('username')
    else:
        username = ''
    context = {
        'username': username,
    }
    return render(request, 'user/login.html', context)


# 验证登录
def login2_check(request):
    # 1.获取数据
    username = request.POST.get('username')
    password = request.POST.get('password')

    # 2.验证数据
    if not all([username, password]):
        # 有数据为空
        return JsonResponse({"res": 2})

    # 3.进行处理：根据用户名和密码查找账户信息
    passport = UserDoc.objects.get_one_passport(username=username, password=password)
    if passport:
        turn_to = reverse('doctor:index')
        jres = JsonResponse({"res": 1, "turn_to": turn_to})

        # 记住用户的登录状态
        request.session['islogin'] = True
        request.session['username'] = username
        request.session['passport_id'] = passport.id
        return jres
    else:
        # 用户名密码错误
        return JsonResponse({"res": 0})


# 登出
def log2out(request):
    # 清除session信息
    request.session.flush()
    return redirect(reverse('doctor:index'))


# 用户中心
@login_required
def user(request):
    if request.method == 'GET':
        passport_id = request.session.get('passport_id')  # 数据表中的id
        user = User.objects.get(id=passport_id)
        return render(request, 'user/user_center_info.html', locals())
    else:
        return HttpResponse("请使用GET请求数据!")


# 修改个人信息
@login_required
def user_change(request):
    if request.method == 'GET':
        return render(request, 'user/change_user_info.html')
    elif request.method == 'POST':
        # 添加用户信息
        passport_id = request.session.get('passport_id')
        print("passport_id：---------------", passport_id)  # 数据表中的id
        user = User.objects.get(id=passport_id)
        if not user:
            return HttpResponse('Sorry~~~ user is not exist')
        phone = request.POST.get('phone')
        nickname = request.POST.get('nickname')
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        # 保存数据
        user.phone = phone
        user.nickname = nickname
        user.name = name
        user.description = desc
        user.save()
        # return render(request, 'user/user_center_info.html')
        return redirect(reverse('user:user'))
