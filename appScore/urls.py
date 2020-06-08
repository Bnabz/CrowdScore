from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('my_profile/',views.my_profile, name='my_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('submit_project/', views.submit_project, name='submit_project'),
    # path('search/',views.search_results, name='search'),
]