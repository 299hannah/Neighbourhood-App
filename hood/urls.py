from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.index, name="index"),

    path("accounts/profile/", views.profile, name="profile"),
    path("new_post/", views.new_post, name='new_post'),
    path('update/', views.update, name='update'),
    path('update_profile/', views.update_profile, name='update_profile'),

    path('delete/<int:pk>/', views.delete_post, name='delete'),
    path('category', views.category, name='category'),
    path('newhood', views.create_hood, name='newhood'),
    path('post', views.post, name='post'),
    path('business/', views.business, name='business'),

    path('detail', views.detail, name='detail'),
    # path('<hood_id>/members', views.hood_members, name='members'),
    path('search', views.search_business, name='search'),
    # path('join_hood/<id>', views.join_hood, name='join-hood'),
    # path('leave_hood/<id>', views.leave_hood, name='leave-hood'),
    path('new_business/', views.new_business, name='new_business'),

    path('update_post/<int:pk>/', views.update_post, name='update_post'),

    


]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 