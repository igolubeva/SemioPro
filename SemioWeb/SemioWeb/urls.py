from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('chants/', include('chants.urls')),
    path('StatisticModule/', include('StatisticModule.urls')),
]
