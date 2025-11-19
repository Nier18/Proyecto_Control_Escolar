# Importamos los modelos de la base de datos
from .models import Student, Advisor, Instructor, Prereq, Course
# Ya no necesitamos 'reverse' aquí porque las URLs se manejan en los templates
# from django.urls import reverse 

# --- Servicio 0: Contenido de Bienvenida ---

def get_home_content():
    """
    No requiere datos, solo devolvemos un diccionario vacío o None.
    """
    return {}


# --- Servicio 1: Prerrequisitos ---

def get_prerequisitos_content():
    """
    No requiere datos para el formulario.
    """
    return {}

def get_prerequisitos_resultado(course_id):
    """
    Busca los prerrequisitos y devuelve un diccionario con los datos.
    """
    if not course_id:
        return {'error': 'Por favor, introduce un ID de curso.'}

    try:
        # Verificamos si el curso existe
        curso = Course.objects.get(course_id=course_id)
        
        # Buscamos sus prerrequisitos
        prerrequisitos = Prereq.objects.filter(course_id=course_id).select_related('prereq')

        if not prerrequisitos.exists():
             return {'curso': curso, 'no_prereqs': True}

        # Devolvemos el objeto curso y la lista de prerrequisitos
        return {
            'curso': curso,
            'prerrequisitos': prerrequisitos
        }

    except Course.DoesNotExist:
        return {'error': f'Error: No se encontró ningún curso con el ID {course_id}.'}
    except Exception as e:
        return {'error': f'Error en la consulta: {e}'}


# --- Servicio 2: Transcript (En Construcción) ---

def get_transcript_content():
    return {}


# --- Servicio 3: Asesor de Estudiante ---

def get_asesor_content():
    return {}

def get_asesor_resultado(student_id):
    """
    Busca el asesor y devuelve un diccionario con los datos.
    """
    if not student_id:
        return {'error': 'Por favor, introduce un ID de estudiante.'}

    try:
        # Buscamos la asesoría
        asesoria = Advisor.objects.select_related('s', 'i').get(s_id=student_id)
        return {'asesoria': asesoria}

    except Advisor.DoesNotExist:
        # Si no tiene asesor, buscamos al estudiante para mostrar su nombre
        try:
            estudiante = Student.objects.get(id=student_id)
            return {'estudiante': estudiante, 'no_asesor': True}
        except Student.DoesNotExist:
            return {'error': f'Error: No se encontró ningún estudiante con el ID {student_id}.'}
    except Exception as e:
        return {'error': f'Error en la consulta: {e}'}


# --- Servicio 4: Estudiantes con 'A' (En Construcción) ---

def get_estudiantes_A_content():
    return {}


# --- Servicio 5: Horario de Profesor (En Construcción) ---

def get_horario_profesor_content():
    return {}