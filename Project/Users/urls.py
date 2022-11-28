from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),

    path(
        'change_password/', views.ChangeUserPassword.as_view(),
        name='change_password'
        ),
    path(
        'password_change_done/', views.ChangeUserPasswordDone.as_view(),
        name='password_change_done'
        ),

    path(
        'reset_password/', views.ResetUserPassword.as_view(),
        name='reset_password'
        ),
    path(
        'reset_password_done/', views.ResetUserPasswordDone.as_view(),
        name='reset_password_done'
        ),
    path(
        'reset/<uidb64>/<token>/', views.UserPasswordResetConfirm.as_view(),
        name='reset_password_confirm'
        ),
    path(
        'reset/done/', views.UserPasswordResetComplete.as_view(),
        name='password_reset_done'
        ),


    path('profile/', views.UpdateUserProfile.as_view(), name='profile'),

    path('user_list/', views.UserList.as_view(), name='user_list'),
    path(
        'user/<int:user_id>/', views.UserDetail.as_view(), name='user_details'
        ),
]
