from . import views
from django.urls import path
app_name = 'food'
urlpatterns = [
    #/food/
    path('',views.IndexClassView.as_view(),name='index'),
    #/food/id(1 or 2)
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),
    path('item/',views.item,name='item'),
    #add item
    path('add',views.CreateItem.as_view(),name='create_item'),
    #edit
    path('update/<int:id>/',views.update_item,name='update_item'),
    #delete
    path('delete/<int:id>/',views.delete_item,name='delete_item'),
]