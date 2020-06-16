from django.urls import path
from .views import register, login,  logout, quiz, result
urlpatterns = [
    path('', register, name= 'register_user')
    ,path('login/', login, name= 'login_user')
    # ,path('authenticate/', authenticate_user, name = 'authenticate_user')
    ,path('logout/', logout, name = 'logout_user')
    ,path('quiz/<category>/', quiz)
    ,path('result/', result)
    
]