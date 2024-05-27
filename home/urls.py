from django.urls import path

from home.views import contato, home, servicos, sobre

urlpatterns = [
    path("", home),  # /
    path("sobre/", sobre),  # /sobre
    path("servicos/", servicos),  # /servicos
    path("contato/", contato),  # /contato
]
