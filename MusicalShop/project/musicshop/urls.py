from django.urls import path
from .views import GuitarList, GuitarDetailView, guitar_create

urlpatterns = [
    path('', GuitarList.as_view()),
    path('<int:pk>', GuitarDetailView.as_view()),
    path('create/', guitar_create, name='create_guitar'),
]
