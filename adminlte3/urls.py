from django.urls import path
from .views import dashboard, contacts, register, term_of_use
from .apps import AdminLTE3Config


app_name = AdminLTE3Config.name


urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('contacts/', contacts, name="contacts"),
    path('register/', register, name="register"),
    path('term_of_use/', term_of_use, name="term_of_use"),
]
