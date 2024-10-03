import cv2
import os

# Demander le chemin de la vidéo à l'utilisateur
video_path = input("Path of video : ")

# Demander le dossier de sortie pour stocker les frames extraites
output_folder = input("Path for extracted frame folder (default 'extracted_frames') : ")
if output_folder.strip() == "":
    output_folder = 'extracted_frames'

# Ouvrir la vidéo
cap = cv2.VideoCapture(video_path)

# Créer un dossier pour stocker les frames extraites s'il n'existe pas
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Obtenir le nombre d'images par seconde (fps) de la vidéo
fps = cap.get(cv2.CAP_PROP_FPS)

# Définir le nombre d'images à extraire par seconde
images_per_second = int(input("How many frames per second to extract ?"))  # Modifiez cette valeur selon vos besoins
frame_name = input("Frames names ?")
# Calculer l'intervalle de frames en fonction des images par seconde désirées
frame_interval = int(fps / images_per_second)

# Initialiser un compteur de frames
frame_count = 0

# Boucle pour lire la vidéo et extraire les frames
while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break  # Si la vidéo est terminée, on sort de la boucle

    if frame_count % frame_interval == 0:
        # Générer le nom du fichier pour la frame
        frame_filename = f"{output_folder}/{frame_name}_{frame_count // frame_interval}.png"
        # Sauvegarder la frame en PNG
        cv2.imwrite(frame_filename, frame)

    # Incrémenter le compteur de frames
    frame_count += 1

# Libérer les ressources de la vidéo
cap.release()

print(f'Frames saved in : {output_folder}')
