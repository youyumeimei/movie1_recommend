"""movierecomend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from movie import views

urlpatterns = [
                  path('', views.index, name='index'),
                  path('single/<int:id>/', views.single, name='single'),
                  path('search', views.search, name='search'),
                  path('tags', views.tags, name='tags'),
                  path('tag_movie/<int:tag_id>', views.tag_movie, name='tag_movie'),
                  path('admin/', admin.site.urls),
                  path('login/', views.rlogin, name="login"),
                  path('register/', views.register, name="register"),
                  path('logout/', views.rlogout, name="logout"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

admin.site.site_header = '推荐系统后台管理'
admin.site.index_title = '首页-推荐系统'
admin.site.site_title = '推荐系统'
