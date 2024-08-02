import socket

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket: #AF_INET IPv4 y SOCK_STREAM implica protocolo TCP con verificacion seguro y robusto.
        HOST = "127.0.0.1"
        PORT = 3000
        BUFFER = 1024
        server_socket.bind((HOST, PORT))
        server_socket.listen(1) #Número de conexiones no aceptadas que el sistema permite antes de empezar a rechazarlas
        print("Servidor esperando conexiones en el puerto 3000...")
        
        while True:
            client_conn, client_addr = server_socket.accept() #Se bloquea ejecución hasta que cliente se conecta, devuelve client_address (IP cliente y puerto cliente) y client_socket ()
            with client_conn:
                print(f"Conexión establecida con {client_addr}")

                while True:
                    data = client_conn.recv(BUFFER).decode() #decode() 
                    if not data: #Se verifica cuando cliente cierra conexión
                        break
                    print(f"Recibido del cliente mensaje hexadecimal: {data}")
                    response = f"Servidor recibió: {data}"
                    client_conn.send(response.encode())
            print(f"Conexión cerrada con {client_addr}")
            break

if __name__ == "__main__": #Si ejecuto el script directamente ejecuto la funcion que abre el servidor, me permite importar la función si quiero.
    start_server()
