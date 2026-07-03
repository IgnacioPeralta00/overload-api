import json
# pyrefly: ignore [missing-import]
import deepl
 
DEEPL_AUTH_KEY = "49e43b30-6a0a-4523-b53e-2df43be3c6f6:fx"

def translate_database():
    translator = deepl.Translator(DEEPL_AUTH_KEY)

    print("Cargando archivo exercises-en.json...")
    with open('api/exercises-en.json', 'r', encoding='utf-8') as f:
        exercises = json.load(f)

    print(f"Iniciando traducción de {len(exercises)} ejercicios...")

    for index, exercise in enumerate(exercises):
        print(f"Traduciendo [{index + 1}/{len(exercises)}]: {exercise.get('name')}")

        try:
            if exercise.get('name'):
                translated_name = translator.translate_text(exercise['name'], target_lang="ES")
                exercise['name'] = translated_name.text

            if exercise.get('instructions') and len(exercise['instructions']) > 0:
                translated_instructions = translator.translate_text(exercise['instructions'], target_lang="ES")
                exercise['instructions'] = [res.text for res in translated_instructions]

        except Exception as e:
            print(f"Error traduciendo el ejercicio {exercise.get('name', 'Desconocido')}: {e}")

    print("Guardando resultados en exercises-es.json...")
    with open('exercises-es.json', 'w', encoding='utf-8') as f:
        json.dump(exercises, f, ensure_ascii=False, indent=4)

    print("Proceso completado con éxito")

if __name__ == "__main__":
    translate_database()