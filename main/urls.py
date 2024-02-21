from django.urls import path
from .views import home, blogpost_create, blogpost_update, blogpost_delete

urlpatterns = [
    path('', home),
    path('create/', blogpost_create, name='blogpost_create'),
    path('update/<int:pk>/', blogpost_update, name='blogpost_update'),
    path('delete/<int:pk>/', blogpost_delete, name='blogpost_delete'),
]
