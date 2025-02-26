



from django.contrib import admin
from django.urls import path, include
from .views import (home_view,
                    login_page,
                    register_view,
                    log_out_view,
                    profiles_list_view,
                    profile_details_view,
                    change_password,
                    update_profile,
                    emailConfirm_view,
                    send_email,
                    project_view,
                    )

urlpatterns = [
    path('', home_view, name="home"),
    path('login/', login_page, name="login"),
    path('logout/', log_out_view, name="logout"),
    path('profiles/', profiles_list_view, name="profiles"),
    path('profiles/<slug:slug>', profile_details_view, name="profile_details"),
    path('profiles/edit/<slug:slug>/', update_profile, name="edit_profile"),
    path('register/', register_view, name="register"),
    path('login/change_password/', change_password, name="change_password"),
    path('emailsuccess/', emailConfirm_view, name="emailsuccess"),
    path('send-email/', send_email, name="send_email"),
    path('projects/', project_view, name="projects")
]

































# from django.urls import path

# from .views import (
#     ActivateView,
#     ChangeEmailActivateView,
#     ChangeEmailView,
#     ChangePasswordView,
#     ChangeProfileView,
#     LogInView,
#     LogOutConfirmView,
#     LogOutView,
#     RemindUsernameView,
#     ResendActivationCodeView,
#     RestorePasswordConfirmView,
#     RestorePasswordDoneView,
#     RestorePasswordView,
#     SignUpView,
# )

# app_name = "accounts"

# urlpatterns = [
#     path("log-in/", LogInView.as_view(), name="log_in"),
#     path("log-out/confirm/", LogOutConfirmView.as_view(), name="log_out_confirm"),
#     path("log-out/", LogOutView.as_view(), name="log_out"),
#     path(
#         "resend/activation-code/",
#         ResendActivationCodeView.as_view(),
#         name="resend_activation_code",
#     ),
#     path("sign-up/", SignUpView.as_view(), name="sign_up"),
#     path("activate/<code>/", ActivateView.as_view(), name="activate"),
#     path("restore/password/", RestorePasswordView.as_view(), name="restore_password"),
#     path(
#         "restore/password/done/",
#         RestorePasswordDoneView.as_view(),
#         name="restore_password_done",
#     ),
#     path(
#         "restore/<uidb64>/<token>/",
#         RestorePasswordConfirmView.as_view(),
#         name="restore_password_confirm",
#     ),
#     path("remind/username/", RemindUsernameView.as_view(), name="remind_username"),
#     path("change/profile/", ChangeProfileView.as_view(), name="change_profile"),
#     path("change/password/", ChangePasswordView.as_view(), name="change_password"),
#     path("change/email/", ChangeEmailView.as_view(), name="change_email"),
#     path(
#         "change/email/<code>/",
#         ChangeEmailActivateView.as_view(),
#         name="change_email_activation",
#     ),
# ]