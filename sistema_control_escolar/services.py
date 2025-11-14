# Importamos los modelos de Django
from .models import Student, Instructor, Course, Prereq, Takes, Advisor, Teaches

# Importamos pandas para procesar datos si es necesario
import pandas as pd


# -----------------------------------------------
# LÓGICA PARA LA PÁGINA DE INICIO
# -----------------------------------------------

def get_home_content():
    """
    Genera el HTML para la vista de bienvenida inicial.
    """
    # Esta es una "plantilla" de HTML simple como string.
    # En un futuro, podrías renderizar un template de Django aquí.
    html_content = """
        <h2 class="text-2xl font-semibold mb-4">Bienvenido</h2>
        <p class="text-gray-700">
            Selecciona una consulta del menú de la izquierda para comenzar.
        </p>
        <p class="mt-4 text-gray-700">
            Esta aplicación utiliza una arquitectura desacoplada. La interfaz (HTML) carga los datos de forma asíncrona (con `fetch`) desde *endpoints* de Django, los cuales obtienen su lógica de una capa de servicios (`services.py`).
        </p>
    """
    return html_content


# -----------------------------------------------
# STUBS PARA LAS 5 CONSULTAS
# -----------------------------------------------
# Dejaremos las funciones listas para ser implementadas.
# Por ahora, solo devolverán un HTML simple.
# -----------------------------------------------

def get_prerequisitos_content():
    """
    Servicio para la Consulta 1: Prerrequisitos de un curso.
    """
    # TODO: Implementar lógica de consulta
    # 1. Crear formulario HTML para seleccionar un curso.
    # 2. Si se envía el formulario (POST/GET), buscar en Prereq.objects.filter(...)
    # 3. Generar tabla HTML con los resultados.

    html_content = """
        <h2 class="text-2xl font-semibold mb-4">Consulta 1: Prerrequisitos de Curso</h2>
        <p class="text-gray-700">Esta funcionalidad está en construcción.</p>
        <!-- Aquí irá el formulario de selección de curso -->
    """
    return html_content


def get_transcript_content():
    """
    Servicio para la Consulta 2: Transcript de un estudiante.
    """
    # TODO: Implementar lógica de consulta
    html_content = """
        <h2 class="text-2xl font-semibold mb-4">Consulta 2: Transcript de Estudiante</h2>
        <p class="text-gray-700">Esta funcionalidad está en construcción.</p>
        <!-- Aquí irá el formulario de selección de estudiante -->
    """
    return html_content


def get_asesor_content():
    """
    Servicio para la Consulta 3: Asesor de un estudiante.
    """
    # TODO: Implementar lógica de consulta
    html_content = """
        <h2 class="text-2xl font-semibold mb-4">Consulta 3: Asesor de Estudiante</h2>
        <p class="text-gray-700">Esta funcionalidad está en construcción.</p>
        <!-- Aquí irá el formulario de selección de estudiante -->
    """
    return html_content


def get_estudiantes_A_content():
    """
    Servicio para la Consulta 4: Estudiantes con 'A' en un curso.
    """
    # TODO: Implementar lógica de consulta
    html_content = """
        <h2 class="text-2xl font-semibold mb-4">Consulta 4: Estudiantes con 'A'</h2>
        <p class="text-gray-700">Esta funcionalidad está en construcción.</p>
        <!-- Aquí irá el formulario de selección de curso -->
    """
    return html_content


def get_horario_profesor_content():
    """
    Servicio para la Consulta 5: Horario de un profesor.
    """
    # TODO: Implementar lógica de consulta
    html_content = """
        <h2 class="text-2xl font-semibold mb-4">Consulta 5: Horario de Profesor</h2>
        <p class="text-gray-700">Esta funcionalidad está en construcción.</p>
        <!-- Aquí irá el formulario de selección de profesor -->
    """
    return html_content