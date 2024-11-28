from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")), # Middleware para recarga automática de páginas
    path('auth/', include('authentication.urls')),
    path('landing/', include('landing.urls'))
]
