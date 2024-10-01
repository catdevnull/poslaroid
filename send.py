import socket
from PIL import Image
import io
import sys

def send_image(host, port, image_path):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        
        # Open and convert the image to PNG
        with Image.open(image_path) as img:
            img_byte_arr = io.BytesIO()
            img.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()
        
        # Send the size of the image
        s.sendall(len(img_byte_arr).to_bytes(4, byteorder='big'))
        
        # Send the image data
        s.sendall(img_byte_arr)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python send.py <host> <port> <image_path>")
        sys.exit(1)
    
    host = sys.argv[1]
    port = int(sys.argv[2])
    image_path = sys.argv[3]
    
    send_image(host, port, image_path)