import cv2
import numpy as np

background = None
accumulated_weight = 0.5

ROI_top = 100
ROI_bottom = 300
ROI_right = 150
ROI_left = 350


def cal_accum_avg(frame, accumulated_weight):

    global background
    
    if background is None:
        background = frame.copy().astype("float")
        return None

    cv2.accumulateWeighted(frame, background, accumulated_weight)


def segment_hand(frame, threshold=25):
    global background
    
    diff = cv2.absdiff(background.astype("uint8"), frame)

    _ , thresholded = cv2.threshold(diff, threshold, 255, cv2.THRESH_BINARY)

    ## Saisir les contours externes de l'image
    contours, _= cv2.findContours(thresholded.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) == 0:
        return None
    else:
        
        hand_segment_max_cont = max(contours, key=cv2.contourArea)
        
        return (thresholded, hand_segment_max_cont)


cam = cv2.VideoCapture(0)

num_frames = 0
element = 10
num_imgs_taken = 0

while True:
    ret, frame = cam.read()

    # Retourne l'image pour que cela paraisse plus naturel
    frame = cv2.flip(frame, 1)

    frame_copy = frame.copy()

    roi = frame[ROI_top:ROI_bottom, ROI_right:ROI_left]

    gray_frame = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (9, 9), 0)

    #Pendant 120 images, on calcule l'arrière-plan moyen pour la soustraction d'arrière-plan
    if num_frames < 120:
        cal_accum_avg(gray_frame, accumulated_weight)
        if num_frames <= 119:
            
            cv2.putText(frame_copy, "Recuperation de l'arriere plan...", (80, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)
         
    #On laisse 300 images pour faire le signe voulu
    elif num_frames <= 300: 

        hand = segment_hand(gray_frame)
        
        cv2.putText(frame_copy, "Faites le signe voulu..." , (200, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        
        # Vérifie si la main est effectivement détectée en comptant le nombre de contours détectés...
        if hand is not None:
            
            thresholded, hand_segment = hand

            cv2.drawContours(frame_copy, [hand_segment + (ROI_right, ROI_top)], -1, (255, 0, 0),1)
            
            cv2.putText(frame_copy, str(num_frames), (70, 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

            cv2.imshow("Thresholded de l'image de la main", thresholded)
    
    # On commence à enregistrer les images des signes 
    else: 
        
        hand = segment_hand(gray_frame)
        
        # Vérifier si la main est effectivement détectée 
        if hand is not None:
            
            thresholded, hand_segment = hand

            cv2.drawContours(frame_copy, [hand_segment + (ROI_right, ROI_top)], -1, (255, 0, 0),1)
            
            cv2.putText(frame_copy, str(num_frames), (70, 45), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            cv2.putText(frame_copy, str(num_imgs_taken) + 'images' , (200, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            
            cv2.imshow("Thresholded de l'image de la main", thresholded)
            
            # On enregistre les images dans le dossier train
            if num_imgs_taken <= 1200:
                cv2.imwrite("C:/SignLanguage/gesture/train/10/" + str(num_imgs_taken) + '.jpg', thresholded)
            else:
                break
            num_imgs_taken +=1
        else:
            cv2.putText(frame_copy, 'Pas de main...', (200, 400), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.rectangle(frame_copy, (ROI_left, ROI_top), (ROI_right, ROI_bottom), (255,128,0), 3)
    
    cv2.putText(frame_copy, "Reconnaissance des signes de la main_ _ _", (10, 20), cv2.FONT_ITALIC, 0.5, (51,255,51), 1)
    
    # Increment du nombre d'images
    num_frames += 1

    cv2.imshow("Sign Detection", frame_copy)

    # Appuie sur "Exc" pour quitter
    k = cv2.waitKey(1) & 0xFF

    if k == 27:
        break

cv2.destroyAllWindows()
cam.release()