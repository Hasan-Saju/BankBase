from django.shortcuts import render
from bank.forms import UserForm, UserInfoForm,CreateNewAccount,LoanForm, TransactionForm,Deposite,Withdraw
from bank.models import UserInfo,Account,Transaction,Loan
from django.contrib.auth.models import User
# module for authentication
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.

def login_page(request):
    dict = {}
    return render(request, 'login.html', context=dict)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:  # will check authentication ok or not
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('bank:index'))
            else:
                return HttpResponse("Account is not active!!")
        else:
            return HttpResponse("Credentials are wrong")

    else:
        return HttpResponseRedirect(reverse('bank:login'))


@login_required  # this view will be called if user is in login state
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('bank:index'))


def index(request):
    dict = {}
    if request.user.is_authenticated:
        current_user = request.user
        user_id = current_user.id
        user_basic_info = User.objects.get(pk=user_id)
        user_more_info = UserInfo.objects.get(
            user__pk=user_id)  # relationship er jonno, shob relation a same, user bridge of relation
        # cz eita diye model a 1-1 korsi
        dict = {'user_basic_info': user_basic_info,
                'user_more_info': user_more_info}

    return render(request, 'index.html', context=dict)


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        user_info_form = UserInfoForm(data=request.POST)

        if user_form.is_valid() and user_info_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)  # password encryption
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user  # user table connects userinfo

            # check if pp exists or not
            if 'profile_pic' in request.FILES:  # this is for img,pdf,static files
                user_info.profile_pic = request.FILES['profile_pic']

            user_info.save()
            registered = True
    else:
        user_form = UserForm()
        user_info_form = UserInfoForm()

    dict = {'user_form': user_form,
            'user_info_form': user_info_form, 'registered': registered}
    return render(request, 'register.html', context=dict)

def new_account(request):
    new_form=CreateNewAccount()
    
    if request.method=='POST':
        new_form=CreateNewAccount(request.POST)

        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request)
    
    dict={}
    return render(request,'new_account.html',context=dict)



class transaction_list(ListView):
    context_object_name = 'transaction_list'
    model = Transaction
    template_name = 'transaction.html'

class loan_list(ListView):
    context_object_name = 'loan_list'
    model = Loan
    template_name = 'loan.html'


def loan_form(request):
    new_form=LoanForm()

    if request.method=='POST':
        new_form=LoanForm(request.POST)

        if new_form.is_valid():
            new_form.save(commit=True)
            return HttpResponse("Successfully created New Loan")

    dict={}
    return render(request,'loan_form.html',context=dict)

def transaction_form(request):
    new_form=TransactionForm()

    if request.method=='POST':
        new_form=TransactionForm(request.POST)

        if new_form.is_valid():
            new_form.save(commit=True)
            return HttpResponse("Successfully created New Transaction")

    dict={}
    return render(request,'transaction_form.html',context=dict)

def deposite_form(request):
    new_form=Deposite()

    if request.method =='POST':
        new_form=Deposite(request.POST)

        if new_form.is_valid():
            new_form.save(commit=True)
            return HttpResponse("Successfully Deposited the Cash")
    dict={}
    return render(request,'deposite_form.html',context=dict)

def withdraw_form(request):
    new_form=Withdraw()

    if request.method =='POST':
        new_form=Withdraw(request.POST)

        if new_form.is_valid():
            new_form.save(commit=True)
            return HttpResponse("Successfully Cash Withdrawn")

    dict={}
    return render(request,'withdraw_form.html',context=dict)



def bank_statement(request,account_id):
    account_info_send=Transaction.objects.filter(sourceAccount=account_id)
    totalSend=0
    totalSend=sum(account_info_send.values_list('amount',flat=True))

    account_info_receive=Transaction.objects.filter(destAccount=account_id)
    totalReceive=0
    totalReceive=sum(account_info_receive.values_list('amount',flat=True))

    diction={'send':account_info_send,'totalSend':totalSend,'receive':account_info_receive,'totalReceive':totalReceive}
    return render(request,'statement.html',context=diction)

def loan_scheme(request):
    dict={}
    return render(request,'loan_scheme.html',context=dict)


def exchange_rate(request):
    dict={}
    return render(request,'exchange_rate.html',context=dict)
    

