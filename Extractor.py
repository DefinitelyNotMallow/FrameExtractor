import cv2
import os

video_path = input("Path of video : ")
output_folder = input("Path for extracted frame folder (default 'extracted_frames') : ")

if output_folder.strip() == "":
    output_folder = 'extracted_frames'

cap = cv2.VideoCapture(video_path)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

fps = cap.get(cv2.CAP_PROP_FPS)

images_per_second = int(input("How many frames per second to extract ?"))
frame_name = input("Frames names ?")
frame_interval = int(fps / images_per_second)
frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break

    if frame_count % frame_interval == 0:
        frame_filename = f"{output_folder}/{frame_name}_{frame_count // frame_interval}.png"
        cv2.imwrite(frame_filename, frame)
    frame_count += 1

cap.release()
print(f'Frames saved in : {output_folder}')
