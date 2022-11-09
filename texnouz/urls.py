from django.contrib import admin
from django.urls import path, include
from api.user.urls import router

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
