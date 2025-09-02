from django.urls import path

from recipes.views import about, contact, home

# dominio.com/recipes/...

urlpatterns = [
    path("", home),
    path("about/", about),
    path("contact/", contact),
]
