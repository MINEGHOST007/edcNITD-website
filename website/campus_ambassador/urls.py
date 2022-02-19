from django.urls import path
from campus_ambassador.views import *

app_name = "cap"

urlpatterns = [
    path("",home,name="cap_home_page"),
    path("login/",cap_login,name='login'),
    path("register/",register,name='register'),
    path("logout/",cap_logout,name="logout"),
    path("profile/",profile,name='profile'),
    path("profile/edit",edit_profile,name='edit_profile'),
    path('score_task/',score_task,name='score_task'),
    path('subtask_completed/<str:amb_uid>',completed_subtask,name='subtask_completed'),
    path('remove_subtask_completed/<str:amb_uid>',remove_comp_subtask,name='remove_completed_subtask'),
]