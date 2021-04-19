from django.urls import path
from gateway.views import LoginView, RegisterView, setNewPasswordView, verifyEmailView, passwordResetView, ChangePasswordView, PasswordTokenCheckView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("register/", RegisterView.as_view(), name="register"),
    path("verify-email/", verifyEmailView.as_view(), name="verify-email"),
    # path("refresh/", RefreshTokenView.as_view(), name="refresh"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
    path("password-reset-request/", passwordResetView.as_view(), name="password-reset-request"),
    path("password-reset/<uidb64>/<token>/", PasswordTokenCheckView.as_view(), name="password-reset"),
    path("password-reset-confirmed/", setNewPasswordView.as_view(), name="password-reset-confirmed")

]

