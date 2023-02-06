from django.urls import path
from .views import GuitarList, GuitarDetailView, GuitarCreate, GuitarDelete, GuitarUpdate, GuitarSearch, UserView

urlpatterns = [
    path('', GuitarList.as_view(), name='guitar_list'),
    path('search/', GuitarSearch.as_view(), name='guitar_search'),
    path('<int:pk>', GuitarDetailView.as_view(), name='guitar_detail'),
    path('create/', GuitarCreate.as_view(), name='create_guitar'),
    path('<int:pk>/update', GuitarUpdate.as_view(), name='update_guitar'),
    path('<int:pk>/delete', GuitarDelete.as_view(), name='delete_guitar'),
    path('account/', UserView.as_view(), name='user_view'),
]
