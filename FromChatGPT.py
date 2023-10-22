import cv2
from pyzbar.pyzbar import decode
import time

#memasukkan semua kodenya dalam 1 bagian
my_qr_data = ["Potato 1", "Potato 2", "Potato 3", "Potato 4", "Potato 5", "Potato 6", "Potato 7"]

# Decode QR Code 
def decode_qr_code(frame):
    decoded_objects = decode(frame)
    
    if decoded_objects:
        for obj in decoded_objects:
            decoded_data = obj.data.decode("utf-8")
            if decoded_data in my_qr_data:
                # QR Code yang dikenali
                print(f'{decoded_data}')
            else:
                pass
    else:
        pass

# Camer Inilization
cam = cv2.VideoCapture(1)  # kamera utama (indeks 0)
cam.set(3, 320)
cam.set(4, 240)

# Aktifkan mode "adaptive" (mode ini mungkin tidak tersedia di semua library)
cam.set(cv2.CAP_PROP_BRIGHTNESS, -1)  # Atur mode pencahayaan ke mode "adaptive"

while True:
    success, frame = cam.read()

    # Calling The Decode fuction
    decode_qr_code(frame)

    # Shows The Camera Frame
    cv2.imshow("QR Code Scanner", frame)

    # Wait for 1 MiliSecond to rake another picture
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close Camera and Tab
cam.release()
cv2.destroyAllWindows()
