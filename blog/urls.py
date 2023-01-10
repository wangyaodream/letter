from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    # post views
    path('', views.post_list, name="post_list"),
    path('<int:year>/<int:month>/<int:day>/<slug:post>',
         views.post_detail, name="post_detail"),
    # path('', views.PostListView.as_view(), name="post_list"),  # 使用基本视图
    path('<int:post_id>/share/', views.post_share, name='post_share'),
    path('tag/<slug:tag_slug>/', views.post_list, name='post_list_by_tag')
]

