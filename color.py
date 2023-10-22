import cv2
from pyzbar.pyzbar import decode

# Fungsi untuk menggambar kotak di sekitar barcode yang terdeteksi
def draw_barcode(frame, barcode):
    x, y, w, h = barcode.rect
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Membuka kamera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    # Konversi gambar ke grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Decode barcode
    barcodes = decode(gray)

    for barcode in barcodes:
        # Mendapatkan data dari barcode
        barcode_data = barcode.data.decode('utf-8')

        # Menggambar kotak di sekitar barcode yang terdeteksi
        draw_barcode(frame, barcode)

        # Menampilkan data barcode
        cv2.putText(frame, barcode_data, (barcode.rect[0], barcode.rect[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Menampilkan frame dengan barcode yang terdeteksi
    cv2.imshow('Barcode Scanner', frame)

    if cv2.waitKey(1) & 0xFF == 27:  # Tekan tombol 'Esc' untuk keluar
        break

# Menutup kamera dan jendela tampilan
cap.release()
cv2.destroyAllWindows()
