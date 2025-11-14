from django.shortcuts import render
from django.http import HttpResponse

# Importamos el archivo de servicios (que crearemos a continuación)
# Usamos un try/except para evitar errores si el archivo no existe
try:
    from . import services
except ImportError:
    # Si services.py no existe, creamos funciones falsas
    # para evitar que la app crashee en la importación.
    class services:
        def get_home_content(): return HttpResponse("Error: 'services.py' no encontrado. Por favor, crea el archivo.", status=500)
        def get_prerequisitos_content(): return HttpResponse("Error: 'services.py' no encontrado.", status=500)
        def get_transcript_content(): return HttpResponse("Error: 'services.py' no encontrado.", status=500)
        def get_asesor_content(): return HttpResponse("Error: 'services.py' no encontrado.", status=500)
        def get_estudiantes_A_content(): return HttpResponse("Error: 'services.py' no encontrado.", status=500)
        def get_horario_profesor_content(): return HttpResponse("Error: 'services.py' no encontrado.", status=500)

# --- Vista Principal (Controlador) ---
def index_view(request):
    """
    Controlador para la página principal (la "cáscara").
    Solo renderiza la plantilla 'index.html'.
    """
    # Esta vista SÍ debe renderizar 'index.html'
    return render(request, 'sistema_control_escolar/index.html')


# --- Endpoints de Contenido (Llamados por JavaScript) ---
# Estas vistas solo llaman al servicio y devuelven el HTML.

def home_content_view(request):
    """
    Endpoint para cargar el contenido de bienvenida.
    """
    html_result = services.get_home_content()
    return HttpResponse(html_result)

def consulta_prerequisitos_view(request):
    """
    Endpoint para la Consulta 1.
    """
    html_result = services.get_prerequisitos_content()
    return HttpResponse(html_result)

def consulta_transcript_view(request):
    """
    Endpoint para la Consulta 2.
    """
    html_result = services.get_transcript_content()
    return HttpResponse(html_result)

def consulta_asesor_view(request):
    """
    Endpoint para la Consulta 3.
    """
    html_result = services.get_asesor_content()
    return HttpResponse(html_result)

def consulta_estudiantes_A_view(request):
    """
    Endpoint para la Consulta 4.
    """
    html_result = services.get_estudiantes_A_content()
    return HttpResponse(html_result)

def consulta_horario_profesor_view(request):
    """
    Endpoint para la Consulta 5.
    """
    html_result = services.get_horario_profesor_content()
    return HttpResponse(html_result)