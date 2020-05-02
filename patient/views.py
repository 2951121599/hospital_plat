from itertools import chain

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from functions.decorators import login_required
from hospital_plat import settings
from patient.models import Doctor, Symptom, Department, Medicine, Questions, MedicineRecord


# 主页
def index(request):
    return render(request, 'patient/index.html', locals())


# 在线问诊
@login_required
def online_inquiry(request):
    if request.method != 'GET':
        return HttpResponse("请使用GET请求数据! ")
    # 获取科室分类
    departments = Department.objects.all()
    # 获取症状特征分类
    symptoms = Symptom.objects.all()
    # 获取医生列表
    doctors = Doctor.objects.all()
    # 取出筛选科室分类
    department = request.GET.get('department')
    print('department-------------', department)
    # 在结果集里面筛选
    if department:
        department = Department.objects.filter(department_name=department)[0]
        department_id = department.id
        doctors = Doctor.objects.filter(department_id=department_id)
        print('doctors_department---------', doctors)
    # 取出筛选症状特征
    symptom = request.GET.get('symptom')
    print('symptom-------------', symptom)
    # 在结果集里面筛选
    if symptom:
        symptom = Symptom.objects.filter(symptom_name=symptom)[0]
        symptom_id = symptom.id
        doctors = Doctor.objects.filter(symptom_id=symptom_id)
        print('doctors_symptom---------', doctors)
    return render(request, 'patient/online_inquiry.html', locals())


# 在线购药
@login_required
def online_shopping(request):
    if request.method == 'GET':
        # 获取药品信息
        medicines = Medicine.objects.all()
        return render(request, 'patient/online_shopping.html', locals())
    elif request.method == 'POST':
        return render(request, 'patient/online_shopping.html', locals())


# 医生详情页
@login_required
def detail(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    print('doctor_detail--------------', doctor)
    return render(request, 'patient/detail.html', locals())


# 搜索医生
@login_required
def search(request):
    search_word = request.GET.get('search_word', '')
    try:
        # 部分匹配
        search_doctor = Doctor.objects.filter(name__icontains=search_word)
        # 获得搜索的类型
        search_name = search_doctor[0].name
        print('search_name------------', search_name)
    except Exception as e:
        print(e)
        return HttpResponse('没有搜索到符合的结果! ')
    return render(request, 'patient/search.html', locals())


# 咨询内容
@login_required
def inquiry(request):
    doctor_id = request.POST.get('doctor_id')
    print("doctor_id------------", doctor_id)
    if request.method == 'GET':
        return render(request, 'patient/detail.html')
    elif request.method == 'POST':
        try:
            content = request.POST.get('content')
            # 1.获取上传的图片
            img = request.FILES['pic']
            # 2.创建一个新文件
            save_path = '%s/img/%s' % (settings.MEDIA_ROOT, img.name)
            with open(save_path, 'wb') as f:
                # 3.获取上传文件的内容并写到创建的文件中
                for i in img.chunks():
                    f.write(i)
            print("pic.name------------", img.name)
            
            if content:
                passport_id = request.session.get('passport_id')
                # 4.存储到数据库
                Questions.objects.create(content=content, user_id=passport_id, doctor_id=doctor_id, image_url='img/%s' % img.name)
                return HttpResponse("咨询成功, 请等待回复!!!")
            else:
                return HttpResponse("数据为空!!!")
        except Exception as e:
            print("e------------", e)
            return HttpResponse("数据提交失败!!!")


# 问诊记录
@login_required
def inquiry_record(request):
    if request.method != 'GET':
        return HttpResponse("请使用GET方式请求数据!")
    # 从问诊表中取出数据
    id = request.session.get('passport_id')
    print('id--------------', id)
    # 有2条咨询记录
    questions = Questions.objects.filter(user_id=id)
    print("questions------------", questions)
    return render(request, 'patient/inquiry_record.html', locals())


# 购药记录
@login_required
def shopping_record(request):
    if request.method != 'GET':
        return HttpResponse("请使用GET方式请求数据!")
    # 从问诊表中取出数据
    id = request.session.get('passport_id')
    print('id--------------', id)
    # 有2条购药记录
    medicine_records = MedicineRecord.objects.filter(user_id=id)
    return render(request, 'patient/shopping_record.html', locals())


# 查看回复
@login_required
def reply(request, question_id):
    id = request.session.get('passport_id')
    try:
        question = Questions.objects.filter(user_id=id, id=question_id)[0]
        print("question------------", question)

        return render(request, 'patient/reply.html', locals())
    except Exception as e:
        print("e------------", e)
        return HttpResponse("出错了!")


# 查找药品
@login_required
def search_medicine(request):
    global medicine_name, medicine_num
    medicine_name = request.POST.get('medicine_name')
    try:
        d = Medicine.objects.filter(medicine_name=medicine_name).first()
        medicine_name = d.medicine_name
        medicine_num = int(d.medicine_num)
        name1 = d.medicine_name
        num1 = int(d.medicine_num)
        medicines = Medicine.objects.all()
        print("medicine_name, medicine_num------------", medicine_name, medicine_num)

    except Exception as e:
        print("e------------", e)
        return HttpResponse("没有搜索到相关药品信息!")
    return render(request, 'patient/online_shopping.html', locals())


# 购药
@login_required
def take_medicine(request):
    medicines = Medicine.objects.all()
    global medicine_name, medicine_num
    id = request.session.get('passport_id')
    if request.method == "GET":
        try:
            name1 = medicine_name
            num1 = int(medicine_num)
        except Exception as e:
            print("e------------", e)
            return HttpResponse("有错误")
        return render(request, 'patient/take_medicine.html', locals())
    elif request.method == 'POST':
        number = request.POST.get("number")
        medicine_name = medicine_name
        M = Medicine.objects.filter(medicine_name=medicine_name).first()
        numbers = M.medicine_num
        num_result = numbers - int(number)
        if num_result < 0:
            return HttpResponse("取药失败, 药品数量不足!")
        else:
            Medicine.objects.filter(medicine_name=medicine_name).update(medicine_num=num_result)
            num = number
            medicine_ = medicine_name
            MedicineRecord.objects.create(medicine_name=medicine_, medicine_num=num, user_id=id)
            return redirect('patient:online_shopping')


# 二维码
def erweima(request):
    return render(request, 'patient/erweima.html')


# 药品详情页
def product_details(request):
    return render(request, 'patient/product_details.html')


# 购物车
def cart(request):
    return render(request, 'patient/cart.html')


# 药品列表页
def product_list(request):
    return render(request, 'patient/product_list.html')
