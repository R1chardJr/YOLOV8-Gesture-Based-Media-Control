from dotenv import load_dotenv 

import cv2
import time
from ultralytics import YOLO

import spotipy
from spotipy.oauth2 import SpotifyOAuth

#Pegando as credenciais do Spotify do arquivo .env
load_dotenv() 
#Carregando o modelo treinado
model = YOLO('best.pt') 
# Inicia a webcam
cap = cv2.VideoCapture(0)
#Configurações da janela
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 405
#Definindo o scopo de permissões do Spotify
SCOPE = "user-read-playback-state user-modify-playback-state"

try:
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))
    print("Autenticação com Spotify bem-sucedida!")
except Exception as e:
    print(f"Erro ao autenticar com Spotify: {e}")
    exit()

#Configuracões de tempo entre os gestos
COOLDOWN_SECONDS = 2
last_command_time = 0

print("Programa iniciado, esperando por gestos...")
print("Pressione 'esc' para sair.")

while True:
    #Captura o frame da webcam
    success, frame = cap.read()
    #Caso não consiga capturar o frame encerra o loop
    if not success:
        break
    #Redimensiona o frame
    frame_redimensionado = cv2.resize(frame, (WINDOW_WIDTH, WINDOW_HEIGHT))
    results = model(frame_redimensionado, verbose=False) 
    # Pega o resultado da detecção do frame
    r = results[0]
    
    #Caso detecte algum gesto
    if len(r.boxes) > 0:
        best_detection_idx = r.boxes.conf.argmax()
        box = r.boxes[best_detection_idx]
        
        confidence = box.conf[0]
        class_id = int(box.cls[0])
        gesture_name = model.names[class_id]

        # Se a confiança for de pelo menos 80% é executado o comando
        if confidence > 0.8: 
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame_redimensionado, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame_redimensionado, f'{gesture_name} ({confidence:.2f})', (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            current_time = time.time()
            if current_time - last_command_time > COOLDOWN_SECONDS:
                try:
                    if gesture_name == 'play_pause':
                        # Verifica se há uma reprodução ativa
                        playback = sp.current_playback()
                        if playback and playback['is_playing']:
                            sp.pause_playback()
                            print("Comando: Pausar")
                        else:
                            sp.start_playback()
                            print("Comando: Play")

                    elif gesture_name == 'next':
                        sp.next_track()
                        print("Comando: Próxima Faixa")

                    elif gesture_name == 'previous':
                        sp.previous_track()
                        print("Comando: Faixa Anterior")

                    last_command_time = current_time # Reseta o timer
                
                except Exception as e:
                    print(f"Erro ao enviar comando para o Spotify: {e}")

    cv2.imshow("Controlador de Gestos Spotify", frame_redimensionado)
    
    # Encerra o loop se a tecla 'esc' for pressionada
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
