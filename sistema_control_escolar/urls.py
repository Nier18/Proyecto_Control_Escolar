from django.urls import path
from . import views

# app_name nos permite usar {% url 'control_escolar:index' %}
app_name = 'control_escolar'

urlpatterns = [
    # 1. La URL para la página "cáscara" (index.html)
    path('', views.index_view, name='index'),

    # 2. Los "endpoints" que el JavaScript llamará con fetch()

    # Endpoint para el contenido de bienvenida
    path('contenido/inicio/', views.home_content_view, name='home_content'),

    # Endpoints para las 5 consultas
    path('consulta/prerequisitos/', views.consulta_prerequisitos_view, name='consulta_prerequisitos'),
    path('consulta/transcript/', views.consulta_transcript_view, name='consulta_transcript'),
    path('consulta/asesor/', views.consulta_asesor_view, name='consulta_asesor'),
    path('consulta/estudiantes-A/', views.consulta_estudiantes_A_view, name='consulta_estudiantes_A'),
    path('consulta/horario-profesor/', views.consulta_horario_profesor_view, name='consulta_horario_profesor'),
]