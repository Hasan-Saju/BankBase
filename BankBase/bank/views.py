from django.shortcuts import render
from bank.forms import UserForm, UserInfoForm,CreateNewAccount,LoanForm, TransactionForm,Deposite,Withdraw
from bank.models import UserInfo,Account,Transaction,Loan,Branch,AccountType
from django.contrib.auth.models import User
# module for authentication
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
import sweetify
from django.shortcuts import redirect

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
    dict={'branch':BTuple(),'actype':optionAccType()}
    # print(option())
    BTuple()
    
    if request.method=='POST':
        new_form=CreateNewAccount(request.POST)

        if new_form.is_valid():
            new_form.save(commit=True)
            # ok
            acname=new_form.cleaned_data['account_name']
            actype=new_form.cleaned_data['account_type']
            brID=new_form.cleaned_data['branch_name']
            id=Account.objects.filter(account_name=acname,account_type_id=actype,branch_name_id=brID).values_list('id',flat=True)[0]
            # print(id)
            # print(acname)
            # print(actype)
            # print(brID)
            vict={'id':id,'acname':acname,'actype':actype,'brID':brID}
            return render(request,'account_details.html',context=vict)
            # return HttpResponse("Account Created")
            # sweetify.success(request, 'Account Created Successfully!')
            # sweetify.sweetalert(request, 'Westworld is awesome', text='Really... if you have the chance - watch it!' persistent='I agree!')

            # return redirect('/')
        else:
            # return HttpResponse("Problem Occured")
            return render(request, 'new_account.html', {'form': new_form})
    
    return render(request,'new_account.html',context=dict)


def optionBranch():
    branch=Branch.objects.values('id')
    # print(branch)

    branchTuple=Branch.objects.values('id','location')
    for option in branchTuple:
        print(option['id'])
        print(option['location'])

    list=[]
    for option in branch:
        # print(option['id']) 
        list.append(option['id'])
    return list

def BTuple():
    branchTuple=Branch.objects.values('id','location')
    list=[]
    for option in branchTuple:
        list.append((option['id'],option['location']))
    return list
        


def optionAccType():
    actype=AccountType.objects.values('id','type')
    # print(branch)
    list=[]
    for option in actype:
        # print(option['id']) 
        list.append((option['id'],option['type']))
    return list



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
    dict={'account_info':accountInfo()}
    if request.method=='POST':
        new_form=LoanForm(request.POST)

        if new_form.is_valid():
            new_form.save(commit=True)
            return HttpResponse("Successfully created New Loan")

    
    return render(request,'loan_form.html',context=dict)

def accountInfo():
    info=Account.objects.values('id','account_name')
    list=[]
    for option in info:
        list.append((option['id'],option['account_name']))
    return list

def transaction_form(request):
    new_form=TransactionForm()

    if request.method=='POST':
        new_form=TransactionForm(request.POST)

        if new_form.is_valid():
            sourceAcc=int(new_form.cleaned_data['sourceAccount'])
            destAcc=int(new_form.cleaned_data['destAccount'])
            amount=int(new_form.cleaned_data['amount'])

            if credit(sourceAcc)-amount >= 0 :
                balance=Account.objects.values_list('currentBalance', flat=True).get(pk=sourceAcc)
                # print(balance)
                Account.objects.filter(pk=sourceAcc).update(currentBalance=balance-amount) 
                balance=Account.objects.values_list('currentBalance', flat=True).get(pk=destAcc)
                Account.objects.filter(pk=destAcc).update(currentBalance=balance+amount) 

                new_form.save(commit=True)
                return HttpResponse("Successfully created New Transaction")
            else:
                return HttpResponse("Don't have enough money to send")
    dict={}
    return render(request,'transaction_form.html',context=dict)


def deposite_form(request):
    new_form=Deposite()

    if request.method =='POST':
        new_form=Deposite(request.POST)

        if new_form.is_valid():
            destAcc=int(new_form.cleaned_data['destAccount'])
            amount=int(new_form.cleaned_data['amount'])

            balance=Account.objects.values_list('currentBalance', flat=True).get(pk=destAcc)
            Account.objects.filter(pk=destAcc).update(currentBalance=balance+amount) 
            
            new_form.save(commit=True)
            return HttpResponse("Successfully Deposited the Cash")

    dict={}
    return render(request,'deposite_form.html',context=dict)

def withdraw_form(request):
    new_form=Withdraw()

    if request.method =='POST':
        new_form=Withdraw(request.POST)

        if new_form.is_valid():

            sourceAcc=int(new_form.data['sourceAccount'])
            amount=int(new_form.data['amount'])

            if credit(sourceAcc)-amount >= 0 :
                balance=Account.objects.values_list('currentBalance', flat=True).get(pk=sourceAcc)
                Account.objects.filter(pk=sourceAcc).update(currentBalance=balance-amount)  

                new_form.save(commit=True)
                return HttpResponse("Witdrawal Successfull")
            else:
                return HttpResponse("Don't have enough money to withdraw")

    dict={}
    return render(request,'withdraw_form.html',context=dict)



def bank_statement(request,account_id):
    account_info_send=Transaction.objects.filter(sourceAccount=account_id)
    totalSend=0
    totalSend=sum(account_info_send.values_list('amount',flat=True))

    account_info_receive=Transaction.objects.filter(destAccount=account_id)
    totalReceive=0
    totalReceive=sum(account_info_receive.values_list('amount',flat=True))

    balance=totalReceive-totalSend

    diction={'send':account_info_send,'totalSend':totalSend,'receive':account_info_receive,'totalReceive':totalReceive,'balance':balance}
    return render(request,'statement.html',context=diction)

def loan_scheme(request):
    dict={}
    return render(request,'loan_scheme.html',context=dict)


def exchange_rate(request):
    dict={}
    return render(request,'exchange_rate.html',context=dict)
    


# internal functions
def debit(accountNumber):
    account_info_send=Transaction.objects.filter(sourceAccount=accountNumber)
    totalSend=0
    totalSend=sum(account_info_send.values_list('amount',flat=True))
    return int(totalSend)

def credit(accountNumber):
    account_info_receive=Transaction.objects.filter(destAccount=accountNumber)
    totalReceive=0
    totalReceive=sum(account_info_receive.values_list('amount',flat=True))
    return int(totalReceive)