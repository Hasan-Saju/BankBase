from django import forms
from django.contrib.auth.models import User
from bank.models import UserInfo,Account,Loan,Transaction


class UserForm(forms.ModelForm):
    # override for showing ** in pass
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'password', 'email')


class UserInfoForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields = ('LinkedIn_ID', 'Employee_Photo')


class CreateNewAccount(forms.ModelForm):
    class Meta:
        model=Account
        exclude=('id','currentBalance')

class LoanForm(forms.ModelForm):
    class Meta:
        model=Loan
        fields='__all__'

class TransactionForm(forms.ModelForm):
    class Meta:
        model=Transaction
        # fields='__all__'
        exclude=('timestamp',)

class Deposite(forms.ModelForm):
    class Meta:
        model=Transaction
        exclude=('sourceAccount','timestamp',)

class Withdraw(forms.ModelForm):
    class Meta:
        model=Transaction
        exclude=('destAccount','timestamp',)

