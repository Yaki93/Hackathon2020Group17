    # accounts/urls.py
from django.urls import path

from .views import SignUpView,grades,bulletin_board,calendar,presence,schedule,Username_Recovery


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('grades/',grades,name='grades'),
    path('bulletinboard/',bulletin_board,name='bulletin_board'),
    path('calendar/', calendar, name='calendar'),
    path('presence/', presence, name='presence'),
    path('schedule/', schedule, name='schedule'),
    path('UsernameRecovery/', Username_Recovery, name='UsernameRecovery'),
]