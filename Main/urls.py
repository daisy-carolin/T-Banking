from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('h', views.register, name='register'),
    path('register/', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('login_user', views.login_user, name='login'),
    path('add_member/', views.add_member, name='add_member'),
    path('view_member/', views.view_member, name='view_member'),
    path('join_group/', views.join_group, name='join_group'),
    path('view_groups/<str:id>/', views.view_groups, name='view_groups'),
    path('group_set_up/', views.group_set_up, name='group_set_up'),
    path('create_group/', views.create_group, name='create_group'),
    path('proceed/', views.proceed, name='proceed'),
    path('member_contribution/', views.member_contribution, name='member_contribution'),
    path('view_member_contribution/', views.view_member_contribution, name='view_member_contribution'),

    path('borrow_loan/', views.borrow_loan, name='borrow_loan'),
    path('fund_loan/', views.fund_loan, name='fund_loan'),
    path('fund_loan_add/', views.fund_loan_add, name='fund_loan_add'),

    path('repay_loan/', views.repay_loan, name='repay_loan'),


    # path('join_group/<int:group_id>/', views.join_group, name='join_group'),

]
