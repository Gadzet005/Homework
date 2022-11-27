from django.views.generic import CreateView
import django.contrib.auth.views as AuthViews


class RegisterUser(CreateView):
    pass


class LoginUser(AuthViews.LoginView):
    pass


class LogoutUser(AuthViews.LogoutView):
    pass


class ChangeUserPassword(AuthViews.PasswordChangeView):
    pass


class ChangeUserPasswordDone(AuthViews.PasswordChangeDoneView):
    pass


class ResetUserPassword(AuthViews.PasswordResetView):
    pass


class ResetUserPasswordDone(AuthViews.PasswordResetDoneView):
    pass


class UserPasswordResetConfirm(AuthViews.PasswordResetConfirmView):
    pass


class UserPasswordResetComplete(AuthViews.PasswordResetCompleteView):
    pass
