import json

def process_database():
    print("Cargando exercises-es.json...")
    with open('api/exercises-es.json', 'r', encoding='utf-8') as f:
        exercises = json.load(f)

    base_url = "https://raw.githubusercontent.com/IgnacioPeralta00/overload-exercise-db/main/exercises/"
    
    print(f"Estandarizando {len(exercises)} ejercicios...")

    for exercise in exercises:
        if exercise.get('id'):
            exercise['id'] = exercise['id'].lower()
            
        if exercise.get('images'):
            formatted_images = []
            for img in exercise['images']:
                if not img.startswith("http"):
                    formatted_images.append(f"{base_url}{img}")
                else:
                    formatted_images.append(img)
            exercise['images'] = formatted_images

    print("Guardando cambios...")
    with open('api/exercises-es.json', 'w', encoding='utf-8') as f:
        json.dump(exercises, f, ensure_ascii=False, indent=4)

    print("JSON estandarizado con éxito")

if __name__ == "__main__":
    process_database()