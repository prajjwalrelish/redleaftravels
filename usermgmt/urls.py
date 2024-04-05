from django.urls import path
from .views import user_login,user_logout,user_signup,activate
from django.contrib.auth import views as auth_views
from home.forms import EmailValidationOnForgotPassword

urlpatterns = [
        path("login", user_login, name="login"),
        path("logout", user_logout, name="logout"),
        path("signup",user_signup, name="signup"),
        
        path('activate/<uidb64>/<token>/',activate, name='activate') ,
        path('password-reset',auth_views.PasswordResetView.as_view(form_class=EmailValidationOnForgotPassword,template_name='reset_pass/password_reset.html'), name='password_reset'),
        path('password-reset-confirm/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='reset_pass/password_reset_confirm.html'), name='password_reset_confirm'),
        path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='reset_pass/password_reset_done.html'), name='password_reset_done'),
        path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='reset_pass/password_reset_complete.html'), name='password_reset_complete'),
    
]
