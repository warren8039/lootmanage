from django.urls import path
from django.views import generic
from . import views

app_name = 'lootmanage'
urlpatterns = [
    path('', views.TopPageView.as_view(), name='top'),
    path('edit/<str:pk>/', views.WantEditView.as_view(), name='want_edit'),
    path('drop/add/<str:f>', views.DropAdd, name='drop_add'),
]
