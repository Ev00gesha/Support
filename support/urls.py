from django.urls import path

from . import views

urlpatterns = [
    path('', views.SupportListView.as_view(), name='home'),
    path('my_account/', views.MyAccountView.as_view(), name='my_account'),
    path('request/<int:pk>/edit/', views.ReqUpdateView.as_view(), name='update'),
    path('request/<int:pk>/delete/', views.ReqDeleteView.as_view(), name='delete'),
    path('request/<int:pk>/answer/', views.AnswerView.as_view(), name='answer'),
    path('print/', views.AnswerListView.as_view(), name='print'),
]
