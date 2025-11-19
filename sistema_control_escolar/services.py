# Importamos los modelos de la base de datos
from .models import Student, Advisor, Instructor, Prereq, Course, Takes, Teaches, TimeSlot
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


# --- Servicio 2: Transcript ---

def get_transcript_content():
    return {}

def get_transcript_resultado(student_id):
    """
    Busca el transcript de un estudiante.
    """
    if not student_id:
        return {'error': 'Por favor, introduce un ID de estudiante.'}

    try:
        # Verificamos si el estudiante existe
        estudiante = Student.objects.get(id=student_id)

        # Buscamos los cursos que ha tomado (Takes)
        # Necesitamos llegar a Course para el titulo: Takes -> Section (course) -> Course (course)
        # Ordenamos por Año (descendente) y Semestre para que parezca un historial
        transcript = Takes.objects.filter(id=student_id).select_related('course__course').order_by('-year', 'semester')

        if not transcript.exists():
            return {'estudiante': estudiante, 'no_transcript': True}

        return {
            'estudiante': estudiante,
            'transcript': transcript
        }

    except Student.DoesNotExist:
        return {'error': f'Error: No se encontró ningún estudiante con el ID {student_id}.'}
    except Exception as e:
        return {'error': f'Error en la consulta: {e}'}


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

def get_estudiantes_A_resultado(course_id):
    """
    Busca estudiantes con calificación 'A', 'A-' o 'A+' en un curso específico.
    """
    if not course_id:
        return {'error': 'Por favor, introduce un ID de curso.'}

    try:
        # Verificamos si el curso existe (buscando en Section o Course, 
        # pero Takes se relaciona con Section, así que buscaremos coincidencias en Takes directamente 
        # o validaremos el curso primero).
        # Para ser consistentes con la lógica anterior, intentamos buscar el curso primero.
        try:
            curso = Course.objects.get(course_id=course_id)
        except Course.DoesNotExist:
             return {'error': f'Error: No se encontró ningún curso con el ID {course_id}.'}

        # Buscamos en Takes: course_id coincide Y grade está en la lista
        # Nota: En el modelo Takes, 'course' es una FK a Section. 
        # Pero Section tiene 'course' que es FK a Course.
        # Django permite hacer takes__course__course_id = course_id
        
        estudiantes = Takes.objects.filter(
            course__course__course_id=course_id,
            grade__in=['A', 'A-', 'A+']
        ).select_related('id', 'course__course').order_by('id__name')

        if not estudiantes.exists():
            return {'curso': curso, 'no_students': True}

        return {
            'curso': curso,
            'estudiantes': estudiantes
        }

    except Exception as e:
        return {'error': f'Error en la consulta: {e}'}


# --- Servicio 5: Horario de Profesor (En Construcción) ---

def get_horario_profesor_content():
    return {}

def get_horario_profesor_resultado(instructor_id):
    """
    Busca el horario de clases de un profesor específico.
    """
    if not instructor_id:
        return {'error': 'Por favor, introduce un ID de profesor.'}

    try:
        # Verificamos si el profesor existe
        try:
            instructor = Instructor.objects.get(id=instructor_id)
        except Instructor.DoesNotExist:
             return {'error': f'Error: No se encontró ningún profesor con el ID {instructor_id}.'}

        # Buscamos en Teaches: id (Instructor) coincide
        # Usamos select_related para traer datos de Section (course), Course (course__course) y TimeSlot (course__time_slot_id)
        # Nota: Section tiene time_slot_id, pero TimeSlot es otro modelo. 
        # Section.time_slot_id es un CharField en el modelo Section, pero debería ser FK a TimeSlot si queremos los detalles.
        # Revisando models.py: 
        # Section.time_slot_id = models.CharField(max_length=4)
        # TimeSlot.time_slot_id = models.CharField(primary_key=True, max_length=4)
        # No hay FK explícita en el modelo Section hacia TimeSlot, es una relación lógica.
        # Tendremos que hacer un "join manual" o buscar los TimeSlots aparte, o confiar en que Django pueda seguirlo si lo definimos (pero está managed=False).
        # Dado que no hay FK en el modelo Section hacia TimeSlot, no podemos usar select_related('course__time_slot_id').
        # Tendremos que iterar y buscar los detalles del horario o modificar el modelo (pero no debemos modificar models.py si no es necesario).
        
        # Estrategia: Traemos los Teaches con sus Sections y Courses.
        clases = Teaches.objects.filter(id=instructor_id).select_related('course', 'course__course')
        
        # Para mostrar los detalles del horario (días, horas), necesitamos cruzar con TimeSlot.
        # Como no hay FK, lo haremos en Python o modificamos el template para mostrar solo el ID del slot si es muy complejo.
        # Pero el usuario pidió "horario", así que intentaremos enriquecer los datos.
        
        resultados = []
        for clase in clases:
            # Buscamos el TimeSlot correspondiente
            try:
                # TimeSlot tiene PK compuesta (time_slot_id, day, start_hr, start_min)
                # Pero Section solo tiene time_slot_id. Esto implica que un time_slot_id puede tener múltiples entradas (días distintos).
                slots = TimeSlot.objects.filter(time_slot_id=clase.course.time_slot_id)
            except Exception:
                slots = []
            
            resultados.append({
                'clase': clase,
                'slots': slots
            })

        if not resultados:
            return {'instructor': instructor, 'no_classes': True}

        return {
            'instructor': instructor,
            'resultados': resultados
        }

    except Exception as e:
        return {'error': f'Error en la consulta: {e}'}