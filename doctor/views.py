from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from functions.decorators import login_required
from patient.models import Doctor, Questions


# 在线接诊展示问诊情况
@login_required
def index(request):
    if request.method == "GET":
        # 获取医生id
        doctor_id = request.session.get('passport_id')
        # 获取问题列表
        questions = Questions.objects.filter(doctor_id=doctor_id)
        # 获取评论列表
        print("questions------------", questions)
        return render(request, 'doctor/index.html', locals())
    elif request.method == 'POST':
        question_id = int(request.POST.get('question_id'))
        doctor_id = int(request.POST.get('doctor_id'))
        comment = request.POST.get('comment').strip(' ')
        print("comment------------", comment)

        if comment:
            question = Questions.objects.get(id=question_id)
            question.comment = comment
            question.save()
        else:
            return HttpResponse("回复不能为空")
        return redirect("doctor:index")


# 医生个人主页
@login_required
def user(request):
    id = request.session.get('passport_id')
    doctor = Doctor.objects.get(id=id)
    return render(request, 'doctor/user_center_info.html', locals())


# 医生接诊记录
@login_required
def treatment_record(request):
    # 获取医生id
    doctor_id = request.session.get('passport_id')
    # 获取接诊记录
    questions = Questions.objects.filter(doctor_id=doctor_id)
    return render(request, 'doctor/treatment_record.html', locals())
