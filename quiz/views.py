from django.shortcuts import render,redirect,HttpResponse
from quiz.models import *
from django.contrib import messages
from django.contrib.auth import get_user, authenticate, login, password_validation, logout
from quiz.forms import Userform,loginform
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseRedirect
import json
# Create your views here.

global answerlist,result,pages
answerlist= {}

dummy=[]
def home(request):
    return render(request,'index.html',{'data':quiz.objects.filter(status=1).all()})

def registerpage(request):
        if request.method == 'POST':
            data = Userform(request.POST)
            if data.is_valid():
                createuser=User.objects.create(username=request.POST.get('username'),email=request.POST.get('email'))
                createuser.set_password(request.POST.get('password'))
                createuser.save()
                messages.success(request,'Account Successfully Created')
                return redirect('account')
            else:
                data = data.errors
        else:
            data = ''
        return render(request, 'login.html', {'data': data})


@csrf_exempt
def Loginauth(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        pwd=request.POST.get('password')
        try:
            user=authenticate(username=user,password=pwd)
            if user is not None:
                login(request,user)
                data = {'success': 'Your Account is Logined'}
            else:
                data = {'error': 'Invalid Account Details'}
        except:
            data={'error':'Invalid Details'}

        return JsonResponse(data)


def logout_view(request):
    logout(request)
    return redirect('index')


@csrf_exempt
@login_required(login_url='/account/')
def checkresult(request,pk,slug):
        qid=request.POST.get('qid')
        ans=request.POST.get('answer')
        data=question.objects.values('answer').get(id=qid)
        actualanswer=data['answer']
        if actualanswer == ans:
            data={'success':'Answer is Correct'}
        else:
            data = {'error': "Wrong Answer.The Answer is : "+actualanswer}
        query=useranswers.objects.get(quiz_id=pk,userid_id=request.user.id)
        if page_n == '1':
            query.q1=ans
        elif page_n == '2':
            query.q2 = ans
        elif page_n == '3':
            query.q3 = ans
        elif page_n == '4':
            query.q4 = ans
        elif page_n == '5':
            query.q5 = ans
        elif page_n == '6':
            query.q6 = ans
        elif page_n == '7':
            query.q7 = ans
        elif page_n == '8':
            query.q8 = ans
        elif page_n == '9':
            query.q9 = ans
        elif page_n == '10':
            query.q10 = ans
        else:
            print('novalue')
        query.save()
        return JsonResponse(data)

@login_required(login_url='/account/')
def quizpage(request,slug,pk):
    global page_n
    check=userinfo.objects.filter(question__quiz_id=pk,userid=request.user.id)
    if not check:
        checkdata=useranswers.objects.filter(quiz_id=pk,userid_id=request.user.id)
        if not checkdata:
            useranswers(quiz_id=pk,userid_id=request.user.id).save()
        data = question.objects.filter(quiz_id=pk).order_by('id').all()
        paginator = Paginator(data, 1)
        pages=paginator.num_pages
        if request.method == 'POST':
            global page_n
            page_n = request.POST.get('page_n')
            if paginator.num_pages >= int(page_n):
                results = list(
                    paginator.page(page_n).object_list.values('id', 'question', 'option1', 'option2', 'option3', 'option4'))
                return JsonResponse({"results": results})
    else:
        pages=0

    return render(request, 'quiz.html', {'pages': pages, })


@login_required(login_url='/account/')
def saveuserdata(request, pk,slug):
    result=0
    i=0
    data=useranswers.objects.values('q1','q2','q3','q4','q5','q6','q7','q8','q9','q10').get(userid_id=request.user.id,quiz_id=pk)
    answ=list(question.objects.values('answer').filter(quiz_id=int(pk)))
    for x in data:
        if data[x] == answ[i]['answer']:
            result=result+1
        i=i+1
    q=useranswers.objects.values('id').get(userid_id=request.user.id,quiz_id=pk)
    user=userinfo.objects.create(result=result)
    user.save()
    user.userid.add(request.user.id)
    user.question.add(q['id'])

    return redirect('result',pk,slug)

@login_required(login_url='/account/')
def showresultpage(request,pk,slug):
    try:
        result = userinfo.objects.get(userid=request.user.id, question__quiz_id=pk)
        qdata = question.objects.filter(quiz_id=pk)
        return render(request, 'quiz.html', {'result': result, 'qdata': qdata})
    except:
        return redirect('quiz',pk,slug)

@login_required(login_url='/account/')
def Showprofile(request):
    return render(request,'profile.html',{'data':userinfo.objects.filter(userid=request.user.id)})