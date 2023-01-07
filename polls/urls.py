from django.urls import path

from . import views

# 添加url命名空间
app_name = "polls"

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('test/', views.test, name="test"),
    path('<int:pk>/', views.DetailView.as_view(), name="detail"),
    path('<int:pk>/results/', views.ResultsView.as_view(), name="results"),
    path('<int:question_id>/vote/', views.vote, name="vote"),
]

