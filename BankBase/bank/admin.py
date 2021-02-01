from django.contrib import admin
from bank.models import UserInfo
from bank import models

# Register your models here.

admin.site.register(UserInfo)
admin.site.register(models.Branch)
admin.site.register(models.AccountType)
admin.site.register(models.Account)
admin.site.register(models.Customer)
admin.site.register(models.Loan)
admin.site.register(models.Transaction)
