# Importamos los modelos de la base de datos
from .models import Student, Advisor, Instructor
# ¡IMPORTACIÓN NUEVA Y CLAVE!
from django.urls import reverse


# --- Servicio 0: Contenido de Bienvenida ---

def get_home_content():
    """
    Genera el HTML para la página de bienvenida.
    """
    # Usamos f-strings de triple comilla para HTML multilínea
    html = f"""
    <div class="p-4">
        <h2 class="text-2xl font-semibold mb-4 text-gray-800">Bienvenido al Sistema de Control Escolar</h2>
        <p class="text-gray-700">
            Este proyecto demuestra una arquitectura de Django MVT (Model-View-Template)
            separando la lógica de negocio en una <strong>Capa de Servicios</strong> (este archivo, <code>services.py</code>).
        </p>
        <p class="mt-4 text-gray-700">
            La interfaz utiliza JavaScript <code>fetch()</code> para cargar dinámicamente
            el contenido de cada consulta sin recargar la página.
        </p>
        <p class="mt-4 text-gray-700">
            Por favor, selecciona una consulta del menú de la izquierda para comenzar.
        </p>
    </div>
    """
    return html


# --- Servicio 1: Prerrequisitos (En Construcción) ---

def get_prerequisitos_content():
    html = """
    <h2 class="text-2xl font-semibold mb-4">Consulta 1: Prerrequisitos de un Curso</h2>
    <p class="text-yellow-700 bg-yellow-100 p-4 rounded-md">Esta funcionalidad está en construcción.</p>
    """
    return html


# --- Servicio 2: Transcript (En Construcción) ---

def get_transcript_content():
    html = """
    <h2 class="text-2xl font-semibold mb-4">Consulta 2: Transcript de Estudiante</h2>
    <p class="text-yellow-700 bg-yellow-100 p-4 rounded-md">Esta funcionalidad está en construcción.</p>
    """
    return html


# --- Servicio 3: Asesor de Estudiante (Formulario) ---

def get_asesor_content():
    """
    Genera el formulario HTML con un campo de texto para el ID del estudiante.
    """

    # --- ¡AQUÍ ESTÁ EL ARREGLO! ---
    # 1. Obtenemos la URL usando 'reverse' en Python.
    try:
        url_del_resultado = reverse('control_escolar:consulta_asesor_resultado')
    except Exception as e:
        # Si 'reverse' falla (ej. la URL no existe), mostramos un error
        return f'<p class_H="text-red-600">Error de configuración de URL: {e}</p>'

    # 2. Generamos el formulario completo e insertamos la variable.
    html = f"""
    <h2 class="text-2xl font-semibold mb-4">Consulta 3: Asesor de Estudiante</h2>

    <!-- 
      El 'action' ahora usa la variable 'url_del_resultado' de Python.
      Esto soluciona el SyntaxError.
    -->
    <form id="form-asesor" 
          action="{url_del_resultado}" 
          class="bg-gray-50 p-6 rounded-lg shadow-sm">

        <label for="student-id-input" class="block text-lg font-medium text-gray-700 mb-2">
            Introduce el ID del estudiante:
        </label>

        <input type="text" 
               id="student-id-input" 
               name="student_id" 
               class="w-full p-2 border border-gray-300 rounded-md"
               placeholder="Ej. 12345">

        <button type="submit" class="mt-4 bg-blue-600 text-white px-5 py-2 rounded-md hover:bg-blue-700 transition">
            Buscar Asesor
        </button>
    </form>

    <!-- Contenedor para los resultados -->
    <div id="resultado-asesor" class="mt-6"></div>
    """
    return html


# --- Servicio 3.1: Asesor de Estudiante (Resultado) ---

def get_asesor_resultado(student_id):
    """
    Recibe un ID de estudiante, consulta la BD y devuelve el resultado en HTML.
    """
    if not student_id:
        return '<p class="text-red-600">Por favor, introduce un ID de estudiante.</p>'

    try:
        # 1. Lógica de Consulta (ORM)
        # Buscamos al estudiante por el ID que nos pasaron
        asesoria = Advisor.objects.select_related('s', 'i').get(s_id=student_id)

        estudiante_nombre = asesoria.s.name
        asesor_nombre = asesoria.i.name

        # 2. Lógica de Presentación (Generar HTML)
        html = f"""
        <div class="bg-green-100 border border-green-400 text-green-800 px-4 py-3 rounded-lg">
            <p class="font-bold">Resultado:</p>
            <p>El asesor de <strong>{estudiante_nombre}</strong> es <strong>{asesor_nombre}</strong>.</p>
        </div>
        """
        return html

    except Advisor.DoesNotExist:
        # Manejo de caso donde el estudiante no tiene asesor
        try:
            # Buscamos al estudiante para mostrar su nombre
            estudiante = Student.objects.get(id=student_id)
            return f'<p class="text-yellow-700 bg-yellow-100 p-4 rounded-md">El estudiante <strong>{estudiante.name}</strong> no tiene un asesor asignado.</p>'
        except Student.DoesNotExist:
            return f'<p class="text-red-600">Error: No se encontró ningún estudiante con el ID <strong>{student_id}</strong>.</p>'
    except Exception as e:
        # Manejo de error general
        return f'<p class="text-red-600">Error en la consulta: {e}</p>'


# --- Servicio 4: Estudiantes con 'A' (En Construcción) ---

def get_estudiantes_A_content():
    html = """
    <h2 class="text-2xl font-semibold mb-4">Consulta 4: Estudiantes con Calificación 'A'</h2>
    <p class="text-yellow-700 bg-yellow-100 p-4 rounded-md">Esta funcionalidad está en construcción.</p>
    """
    return html


# --- Servicio 5: Horario de Profesor (En Construcción) ---

def get_horario_profesor_content():
    html = """
    <h2 class="text-2xl font-semibold mb-4">Consulta 5: Horario de un Profesor</h2>
    <p class="text-yellow-700 bg-yellow-100 p-4 rounded-md">Esta funcionalidad está en construcción.</p>
    """
    return html