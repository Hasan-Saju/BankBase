from django.db import models
from django.contrib.auth.models import User
# Create your models here.
# user field er username,password,email, firstname,lastname


# for adding sth that isnt present in user model
class UserInfo(models.Model):
    # userinfo -one to one- user
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    facebook_id = models.URLField(blank=True)
    # profile_pics -directory- te save hobe
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


class Branch(models.Model):
    location = models.CharField(max_length=30)
    managerName = models.CharField(max_length=30)

    def __str__(self):
        return self.location+" Branch"


class AccountType(models.Model):
    type = models.CharField(max_length=20)
    InterestRate = models.FloatField()

    def __str__(self):
        return self.type


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    account_name = models.CharField(
        max_length=30, default="Blank. Set Account Name")
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    branch_name = models.ForeignKey(
        Branch, on_delete=models.CASCADE)
    password = models.CharField(max_length=15)
    currentBalance = models.IntegerField()
    # lastTransaction = models.DateTimeField()

    def __str__(self):
        return self.account_name+" and Account id: "+str(self.id)


class Loan(models.Model):
    accountNo = models.ForeignKey(Account, on_delete=models.CASCADE)
    loan_amount = models.IntegerField()
    interestRate = models.FloatField()
    loanPeriod = models.DateField()
    remainingTerms = models.IntegerField()

    def __str__(self):
        return str(self.accountNo)+" has loan of: "+str(self.loan_amount)+" taka"


class Transaction(models.Model):
    sourceAccount = models.BigIntegerField()
    destAccount = models.BigIntegerField()
    amount = models.IntegerField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.sourceAccount + " sends "+self.amount+" taka to "+self.destAccount


class Customer(models.Model):
    accountNum = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    email = models.EmailField()
    contactNo = models.BigIntegerField()
    address = models.CharField(max_length=40)

    def __str__(self):
        return self.name
