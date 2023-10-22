import cv2
from pyzbar.pyzbar import decode
import time
import threading

# Memasukkan semua kode dalam satu bagian
my_qr_data = ["Potato 1", "Potato 2", "Potato 3", "Potato 4", "Potato 5", "Potato 6", "Potato 7"]

# Fungsi untuk menggambar kotak di sekitar barcode yang terdeteksi
def draw_barcode(frame, barcode):
    x, y, w, h = barcode.rect
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
# Fungsi untuk mendekode QR code
def decode_qr_code(frame):
    decoded_objects = decode(frame)
    
    if decoded_objects:
        for obj in decoded_objects:
            decoded_data = obj.data.decode("utf-8")
            if decoded_data in my_qr_data:
                # QR Code yang dikenali
                print(f'{decoded_data}')
                time.sleep(0.1)
            else:
                pass

# Fungsi untuk pengambilan gambar
def capture_frames():
    cam = cv2.VideoCapture(0)  # Kamera utama (indeks 0)
    cam.set(3, 320)
    cam.set(4, 240)

    # Aktifkan mode "adaptive" (mode ini mungkin tidak tersedia di semua library)
    cam.set(cv2.CAP_PROP_BRIGHTNESS, -1)  # Atur mode pencahayaan ke mode "adaptive"

    while True:
        success, frame = cam.read()

        # Panggil fungsi untuk mendekode QR code
        decode_qr_code(frame)

        # Tampilkan tampilan kamera
        cv2.imshow("QR Code Scanner", frame)

        # Tunggu selama 1 mili detik sebelum mengambil gambar berikutnya
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Tutup kamera
    cam.release()
    cv2.destroyAllWindows()

# Jalankan thread untuk pengambilan gambar
capture_thread = threading.Thread(target=capture_frames)
capture_thread.start()

# Tunggu hingga thread selesai
capture_thread.join()