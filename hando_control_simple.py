import cv2
import pyautogui
import time
from ultralytics import YOLO

model = YOLO('best.pt') 

cap = cv2.VideoCapture(0)

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

GESTURE_MAP = {
    'play_pause': 'space',
    'next': 'nexttrack',
    'previous': 'prevtrack'
}

COOLDOWN_SECONDS = 2
last_command_time = 0

while True:
    success, frame = cap.read()
    if not success:
        break
    
    frame_redimensionado = cv2.resize(frame, (WINDOW_WIDTH, WINDOW_HEIGHT))
    results = model(frame_redimensionado, verbose=False) 
    
    r = results[0]
    
    if len(r.boxes) > 0:
        # Pega a detecção com maior confiança
        best_detection_idx = r.boxes.conf.argmax()
        box = r.boxes[best_detection_idx]
        
        confidence = box.conf[0]
        class_id = int(box.cls[0])
        gesture_name = model.names[class_id]

        if confidence > 0.75:
            # Desenha a caixa e o rótulo na tela
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame_redimensionado, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame_redimensionado, f'{gesture_name} ({confidence:.2f})', (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

            # Verifica o cooldown
            current_time = time.time()
            if current_time - last_command_time > COOLDOWN_SECONDS:
                # Se o gesto for detectado 
                if gesture_name in GESTURE_MAP:
                    key_to_press = GESTURE_MAP[gesture_name]
                    pyautogui.press(key_to_press)
                    print(f"Comando executado: '{gesture_name}' -> Tecla '{key_to_press}'")
                    last_command_time = current_time 

    cv2.imshow("Controlador de Gestos", frame_redimensionado)

    # Encerra o loop se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera os recursos
cap.release()
cv2.destroyAllWindows()