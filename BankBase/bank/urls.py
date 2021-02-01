from django.conf.urls import url
from django.urls import path
from bank import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

app_name = 'bank'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('new_account/', views.new_account, name='new_account'),
    path('transaction/', views.transaction_list.as_view(), name='transaction'),
    path('transaction_form/', views.transaction_form, name='transaction_form'),
    path('loan_form/', views.loan_form, name='loan_form'),
    path('loan/', views.loan_list.as_view(), name='loan'),
]

# image processing
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
