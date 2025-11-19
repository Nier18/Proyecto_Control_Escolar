from django.shortcuts import render


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
    context = services.get_home_content()
    return render(request, 'sistema_control_escolar/home_content.html', context)

def consulta_prerequisitos_view(request):
    """
    Endpoint para la Consulta 1 (Formulario).
    """
    context = services.get_prerequisitos_content()
    return render(request, 'sistema_control_escolar/prerequisitos_form.html', context)

def consulta_transcript_view(request):
    """
    Endpoint para la Consulta 2 (Formulario).
    """
    context = services.get_transcript_content()
    return render(request, 'sistema_control_escolar/transcript_form.html', context)

def consulta_asesor_view(request):
    """
    Endpoint para la Consulta 3 (Formulario).
    """
    context = services.get_asesor_content()
    return render(request, 'sistema_control_escolar/asesor_form.html', context)

def consulta_estudiantes_A_view(request):
    """
    Endpoint para la Consulta 4 (Formulario).
    """
    context = services.get_estudiantes_A_content()
    return render(request, 'sistema_control_escolar/estudiantes_A_form.html', context)

def consulta_horario_profesor_view(request):
    """
    Endpoint para la Consulta 5 (Formulario).
    """
    context = services.get_horario_profesor_content()
    return render(request, 'sistema_control_escolar/horario_profesor_form.html', context)

# --- Endpoint de RESULTADOS (Llamado por JavaScript) ---

def consulta_asesor_resultado_view(request):
    """
    Endpoint que recibe el ID de estudiante y devuelve el resultado.
    """
    student_id = request.GET.get('student_id')
    context = services.get_asesor_resultado(student_id=student_id)
    return render(request, 'sistema_control_escolar/asesor_resultado.html', context)

def consulta_prerequisitos_resultado_view(request):
    """
    Endpoint que recibe el ID del curso y devuelve sus prerrequisitos.
    """
    course_id = request.GET.get('course_id')
    context = services.get_prerequisitos_resultado(course_id=course_id)
    return render(request, 'sistema_control_escolar/prerequisitos_resultado.html', context)

def consulta_transcript_resultado_view(request):
    """
    Endpoint que recibe el ID del estudiante y devuelve su transcript.
    """
    student_id = request.GET.get('student_id')
    context = services.get_transcript_resultado(student_id=student_id)
    return render(request, 'sistema_control_escolar/transcript_resultado.html', context)