# Data QR Code yang dihasilkan oleh program
my_qr_data = "Potato Busuk"

# Decode QR Code
def decode_qr_code(frame):
    decoded_objects = decode(frame)
    
    if decoded_objects:
        for obj in decoded_objects:
            decoded_data = obj.data.decode("utf-8")
            if decoded_data == my_qr_data:
                # QR Code yang dikenali
                print(f'QR Code dikenali: {decoded_data}')
                # Lakukan tindakan sesuai dengan QR Code yang dikenali
            else:
                # QR Code tidak dikenali
                print(f'QR Code tidak dikenali: {decoded_data}')
    else:
        pass