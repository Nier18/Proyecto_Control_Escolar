from django.shortcuts import render
from django.http import HttpResponse

# Importamos el archivo de servicios
try:
    from . import services
except ImportError:
    # Si services.py no existe, creamos funciones falsas
    class services:
        def get_home_content(): return HttpResponse("Error: 'services.py' no encontrado.", status=500)
        def get_prerequisitos_content(): return HttpResponse("Error: 'services.py' no encontrado.", status=500)
        def get_transcript_content(): return HttpResponse("Error: 'services.py' no encontrado.", status=500)
        def get_asesor_content(): return HttpResponse("Error: 'services.py' no encontrado.", status=500)
        def get_estudiantes_A_content(): return HttpResponse("Error: 'services.py' no encontrado.", status=500)
        def get_horario_profesor_content(): return HttpResponse("Error: 'services.py' no encontrado.", status=500)
        def get_asesor_resultado(student_id): return HttpResponse("Error: 'services.py' no encontrado.", status=500)

# --- Vista Principal (Controlador) ---
def index_view(request):
    """
    Controlador para la página principal (la "cáscara").
    Solo renderiza la plantilla 'index.html'.
    """
    return render(request, 'sistema_control_escolar/index.html')


# --- Endpoints de Contenido (Llamados por JavaScript) ---

def home_content_view(request):
    """
    Endpoint para cargar el contenido de bienvenida.
    """
    html_result = services.get_home_content()
    return HttpResponse(html_result)

def consulta_prerequisitos_view(request):
    """
    Endpoint para la Consulta 1 (Formulario).
    """
    html_result = services.get_prerequisitos_content()
    return HttpResponse(html_result)

def consulta_transcript_view(request):
    """
    Endpoint para la Consulta 2 (Formulario).
    """
    html_result = services.get_transcript_content()
    return HttpResponse(html_result)

def consulta_asesor_view(request):
    """
    Endpoint para la Consulta 3 (Formulario).
    """
    html_result = services.get_asesor_content()
    return HttpResponse(html_result)

def consulta_estudiantes_A_view(request):
    """
    Endpoint para la Consulta 4 (Formulario).
    """
    html_result = services.get_estudiantes_A_content()
    return HttpResponse(html_result)

def consulta_horario_profesor_view(request):
    """
    Endpoint para la Consulta 5 (Formulario).
    """
    html_result = services.get_horario_profesor_content()
    return HttpResponse(html_result)

# --- Endpoint de RESULTADOS (Llamado por JavaScript) ---

def consulta_asesor_resultado_view(request):
    """
    Endpoint que recibe el ID de estudiante y devuelve el resultado.
    """
    # Obtenemos el ID del estudiante desde los parámetros GET
    student_id = request.GET.get('student_id')
    html_result = services.get_asesor_resultado(student_id=student_id)
    return HttpResponse(html_result)

def consulta_prerequisitos_resultado_view(request):
    """
    Endpoint que recibe el ID del curso y devuelve sus prerrequisitos.
    """
    course_id = request.GET.get('course_id')
    html_result = services.get_prerequisitos_resultado(course_id=course_id)
    return HttpResponse(html_result)