"""
URL configuration for proyecto_final project.
"""
from django.contrib import admin
# ¡Importante! Asegúrate de que 'include' esté importado
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Esta línea le dice a Django que use las URLs de tu app
    # para la ruta raíz ('')
    path('', include('sistema_control_escolar.urls')),
]