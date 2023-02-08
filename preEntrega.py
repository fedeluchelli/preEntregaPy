###################################################################################
###############################       ENTREGA       ###############################
###################################################################################


import json

users = {}

def set_user(username, password):
    users[username] = password
    print("Usuario registrado exitosamente.")

def login(username, password):
    if username in users:
        if users[username] == password:
            print(f"Bienvenido {username} !") 
        else:
            print("Error en la contraseña")
    else:
        print("Error en inicio de sesión")   

def get_users():
    print("Usuarios registrados:")
    for username in users:
        print(username)
               
def menu():
    opcion = "1"
    while opcion == "1":
        
            print("""
                --------------------------------------------
                Escriba el número de la opción que desee :
                
                1- Ingresar usuario
                2- Log In
                3- Visualizar información
                4- Exportar base de datos a texto
                
                Presione 'enter' para salir
                --------------------------------------------
                """)
            
            opcion = int(input())
        

    if (opcion == 1):
        set_user(input("Cree su usuario: "), input("Cree su contraseña: ")),
        menu()
        
    if (opcion == 2):
        login(input("Usuario de acceso: "), input("Ingrese su contraseña: ")) 
        menu()
        
    if (opcion == 3):
        get_users()
        menu()
        
    if (opcion == 4):
        with open("./experimento.txt", 'w') as file:
            json.dump(users, file, indent=4)
        menu()
    

menu()


###################################################################################
#####################################################       Fede Luchelli       ###