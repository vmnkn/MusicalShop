from django.urls import path
from .views import ProductList, ProductDetailView, ProductCreate, ProductDelete, \
    ProductUpdate, ProductSearch, UserView, BasketView, basket_add, basket_delete, \
    StringsList, GuitarsList, KombosList, PedalsList, make_order, OrderView

app_name = 'musicshop'

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('search/', ProductSearch.as_view(), name='product_search'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreate.as_view(), name='create_product'),
    path('<int:pk>/update', ProductUpdate.as_view(), name='update_product'),
    path('<int:pk>/delete', ProductDelete.as_view(), name='delete_product'),

    path('account/', UserView.as_view(), name='user_view'),

    path('basket/', BasketView.as_view(), name='basket'),
    path('basket_add/<int:product_id>', basket_add, name='basket_add'),
    path('basket_delete/<int:id>', basket_delete, name='basket_delete'),

    path('guitars/', GuitarsList.as_view(), name='guitars_list'),
    path('strings/', StringsList.as_view(), name='strings_list'),
    path('pedals/', PedalsList.as_view(), name='pedals_list'),
    path('kombos/', KombosList.as_view(), name='kombos_list'),
    path('make_order/', make_order, name='make_order'),
    path('order/', OrderView.as_view(), name='order'),
]
