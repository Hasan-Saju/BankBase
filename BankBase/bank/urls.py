from django.conf.urls import url
from django.urls import path
from bank import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

app_name = 'bank'

urlpatterns = [
    
    path('', views.login_page, name='login'),
    path('user_login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('home/', views.index, name='index'),
    path('new_account/', views.new_account, name='new_account'),
    path('transaction/', views.transaction_list.as_view(), name='transaction'),
    path('transaction_form/', views.transaction_form, name='transaction_form'),
    path('loan_scheme/', views.loan_scheme, name='loan_scheme'),
    path('loan_form/', views.loan_form, name='loan_form'),
    path('loan/', views.loan_list.as_view(), name='loan'),
    path('statement/<int:account_id>/', views.bank_statement, name='statement'),
    path('exchange_rate/', views.exchange_rate, name='exchange_rate'),
    path('deposite/', views.deposite_form, name='deposite'),
    path('withdraw/', views.withdraw_form, name='withdraw'),
]

# image processing
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
