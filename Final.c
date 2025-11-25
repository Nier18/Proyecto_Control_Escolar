

#include <stdio.h>
#include <stdlib.h>

// Estructura del circulo
struct Circulo {
  int id;
  struct Circulo *siguiente;
};

// Función que imprime dos veces el círculo
void mostrar_dos_veces(struct Circulo *primer_elemento) {
  if (primer_elemento == NULL) {
    printf("(Círculo vacío)\n");
    return;
  }

  struct Circulo *temp = primer_elemento;
  printf("Círculo: [ ");
  for (int i = 0; i < 2; i++) {
    do {
      printf("%d ", temp->id);
      temp = temp->siguiente;
    } while (temp != primer_elemento);
    temp = primer_elemento;
  }
  printf("]\n");
}

int main() {
  int n, s;
  int num_elementos;

  struct Circulo *primer_elemento = NULL;
  struct Circulo *ultimo_del_circulo = NULL;
  struct Circulo *ultimo_recien_llegado = NULL;

  printf("--- Círculo  ---\n");

  // --- 1. Preguntar cuántos soldados ---
  printf("¿Cuántos elementos hay en el círculo? ");
  scanf("%d", &num_elementos);

  if (num_elementos <= 0) {
    printf("Debe haber al menos un elemento.\n");
    return 1;
  }

  // --- 2. Crear la lista circular pidiendo los IDs ---
  printf("Introduce el numero de los %d elementos:\n", num_elementos);
  for (int i = 1; i <= num_elementos; i++) {

    int id_actual;
    printf("ID del elemento #%d: ", i);
    scanf("%d", &id_actual);

    // Crear el nuevo soldado (vagón)
    ultimo_recien_llegado = (struct Circulo *)malloc(sizeof(struct Circulo));
    if (ultimo_recien_llegado == NULL) {
      printf("Error: No se pudo asignar memoria.\n");
      return 1;
    }

    ultimo_recien_llegado->id = id_actual;

    // ---- Lógica de la "Fila de Conga" ----
    if (primer_elemento == NULL) {
      // Si la fila está vacía, él es el primero
      primer_elemento = ultimo_recien_llegado;
    } else {
      // Si no, el que era último le da la mano al nuevo
      ultimo_del_circulo->siguiente = ultimo_recien_llegado;
    }
    // El recién llegado es SIEMPRE el último de la fila
    ultimo_del_circulo = ultimo_recien_llegado;
    // ----------------------------------------
  }

  // Cerrar el círculo: el último le da la mano al primero
  if (ultimo_del_circulo != NULL) {
    ultimo_del_circulo->siguiente = primer_elemento;
  }

  printf("\nLos elementos iniciales son:\n");
  mostrar_dos_veces(primer_elemento);
  printf("\n");
}
