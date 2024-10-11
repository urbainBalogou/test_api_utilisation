import requests
import base64
import json

# Fonction pour encoder l'image en base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return f"data:image/jpg;base64,{encoded_string}"

# Chemin de l'image à tester
image_path = "OIP.jpeg"  # Assurez-vous que le fichier est dans le répertoire courant

# URL de l'API
url = "https://plant.id/api/v3/health_assessment"

# Préparer les données de la requête
data = {
    "images": [encode_image(image_path)],
    "latitude": 49.207,
    "longitude": 16.608,
    "similar_images": True
}

# En-têtes de la requête
headers = {
    "Api-Key": "MHR9QctkXxZqATsGMSxn65haSqPjqgUwWFfFjlAlrd5IsAr82z",  # Remplacez par votre clé API
    "Content-Type": "application/json"
}

# Envoyer la requête POST
response = requests.post(url, headers=headers, data=json.dumps(data))

# Afficher la réponse
if response.status_code in (200, 201):
    data = response.json()  # Charger la réponse JSON

    # Vérifier la santé de la plante
    is_healthy = data['result']['is_healthy']['binary']
    health_probability = data['result']['is_healthy']['probability']

    # Afficher le résultat de la santé
    print("État de santé de la plante :")
    if is_healthy:
        print(f"La plante est considérée comme saine (Probabilité : {health_probability:.2f}%)")
    else:
        print(f"La plante n'est pas considérée comme saine (Probabilité : {health_probability:.2f}%)")

    # Afficher les suggestions de maladies
    print("\nSuggestions de maladies :")
    if 'disease' in data['result'] and 'suggestions' in data['result']['disease']:
        for disease in data['result']['disease']['suggestions']:
            name = disease['name']
            probability = disease['probability']
            similar_images = ", ".join([img['url'] for img in disease['similar_images']])
            print(f"- {name} : Probabilité de {probability:.2f}% (Images similaires : {similar_images})")
    else:
        print("Aucune maladie suggérée.")

else:
    print("Erreur:", response.status_code, response.text)
