import socket
import time

def start_client(hex_code, repetitions, delay):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        HOST = "127.0.0.1"
        PORT = 3000
        BUFFER = 1024
        client_socket.connect((HOST, PORT))
        
        for i in range(repetitions):
            client_socket.send(hex_code.encode())
            response = client_socket.recv(BUFFER).decode()
            print(f"Respuesta del servidor: {response}")
            time.sleep(delay)
    print("Conexión cerrada con el servidor")

if __name__ == "__main__":
    hex_code = input("Introduzca el código hexadecimal de 4 cifras que desea enviar al servidor: ")
    repetitions = int(input("Introduzca el número de veces que desea enviar la información: "))
    delay = float(input("Introduzca el delay que desea entre transmisiones: " ))
    
    #Verificación de errores de inserción
    if len(hex_code) != 4 or not all(c in '0123456789ABCDEF' for c in hex_code):
        print("Código hexadecimal inválido. Debe tener 4 caracteres y estar en el rango 0-9, A-F.")
    start_client(hex_code, repetitions, delay)
