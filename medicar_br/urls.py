from django.contrib import admin
from django.urls import path, include

from home.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    # path('', include('home.urls')),
    path('', include(router.urls)),
]
