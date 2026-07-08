# 
# Overload Exercise API

Overload Exercise API es una API REST estática y de solo lectura que provee un catálogo base de ejercicios físicos en español. Está construida como una Serverless Function y diseñada para ser consumida de forma pública.

## Base URL
```text
https://overload-api.vercel.app/api/exercises
```


## Endpoint: Obtener Catálogo de Ejercicios

Devuelve la lista completa de ejercicios físicos disponibles.

- **Método:** `GET`
- **Autenticación:** No requerida
- **CORS:** Habilitado para cualquier origen (`*`)

### Ejemplo de Petición (cURL)
```bash
curl -X GET https://overload-api.vercel.app/api/exercises
```

### Ejemplo de Respuesta (JSON)
El servidor devuelve un arreglo de objetos, donde cada objeto representa un ejercicio. Código de éxito: `200 OK`.

```json
[
  {
    "name": "3/4 de abdominales",
    "force": "pull",
    "level": "beginner",
    "mechanic": "compound",
    "equipment": "body only",
    "primaryMuscles": [
      "abdominals"
    ],
    "secondaryMuscles": [],
    "instructions": [
      "Túmbate en el suelo y sujeta bien los pies. Las piernas deben estar flexionadas por las rodillas.",
      "Coloca las manos detrás o a los lados de la cabeza. Empezarás tumbado boca arriba en el suelo. Esta será tu posición inicial.",
      "..."
    ],
    "category": "strength",
    "images": [
      "https://raw.githubusercontent.com/IgnacioPeralta00/overload-exercise-db/main/exercises/3_4_Sit-Up/0.jpg",
      "https://raw.githubusercontent.com/IgnacioPeralta00/overload-exercise-db/main/exercises/3_4_Sit-Up/1.jpg"
    ],
    "id": "3_4_sit-up"
  }
]
```

### Diccionario de Datos (Modelo de Ejercicio)

Cada objeto de ejercicio contiene las siguientes propiedades:

| Campo | Tipo | Descripción |
| :--- | :--- | :--- |
| `id` | `String` | Identificador único del ejercicio (formato snake_case o kebab-case). |
| `name` | `String` | Nombre del ejercicio en español. |
| `force` | `String` | Tipo de fuerza aplicada (ej. `pull`, `push`, `static`). |
| `level` | `String` | Nivel de dificultad sugerido (ej. `beginner`, `intermediate`, `expert`). |
| `mechanic` | `String` | Tipo de movimiento (ej. `compound` para compuestos, `isolation` para aislamiento). |
| `equipment` | `String` | Equipo necesario (ej. `body only`, `barbell`, `dumbbell`, `machine`). |
| `primaryMuscles` | `Array<String>` | Lista de los músculos principales trabajados. |
| `secondaryMuscles` | `Array<String>` | Lista de los músculos secundarios o estabilizadores involucrados. |
| `instructions` | `Array<String>` | Guía paso a paso sobre cómo ejecutar el movimiento correctamente. |
| `category` | `String` | Categoría del entrenamiento (ej. `strength`, `stretching`, `cardio`). |
| `images` | `Array<String>` | URLs absolutas hacia las imágenes demostrativas del ejercicio alojadas remotamente. |

## Origen de las Imágenes y Recursos (Créditos)

Tanto la **base de datos original (JSON)** como los recursos visuales de este proyecto provienen del excelente proyecto de código abierto [yuhonas/free-exercise-db](https://github.com/yuhonas/free-exercise-db).

Para la construcción de esta API:
1. Se realizó un *fork* de dicho repositorio original con el fin de **traducir y adaptar** todo el catálogo de ejercicios (nombres, músculos, equipo e instrucciones) al idioma español.
2. Para mantener la API serverless lo más rápida y ligera posible, las imágenes no se sirven a través de la función de Vercel. En su lugar, se sirven de forma estática directamente desde la infraestructura global de GitHub utilizando enlaces crudos (`raw.githubusercontent.com`) apuntando al *fork*
