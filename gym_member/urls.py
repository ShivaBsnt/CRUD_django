from django.urls import path
from . import views

urlpatterns = [
    path('', views.MemberList.as_view(), name='member_list'),
    path('view/<int:pk>', views.MemberDetail.as_view(), name='member_detail'),
    path('new', views.MemberCreate.as_view(), name='member_new'),
    path('edit/<int:pk>', views.MemberUpdate.as_view(), name='member_edit'),
    path('delete/<int:pk>', views.MemberDelete.as_view(), name='member_delete'),
]
