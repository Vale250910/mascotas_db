class Usuario:
    def __init__(self,id_usuario:int, nombre:str, apellido:str, email:str, contraseña:str,ciudad:str, direccion:str, telefono:str):
        self.__id_usuario=id_usuario
        self.__nombre = nombre
        self.__apellido= apellido
        self.__email=email
        self.__contraseña=contraseña
        self.__ciudad=ciudad
        self.__direccion= direccion
        self.__telefono=telefono
        
    def get_id_usuario(self):
        return self.__id_usuario
    
    def set_id_usuario(self,id_usuario):
         while True:
            id_usuario = int(id_usuario)
            if id_usuario >=1 and id_usuario <= 100000000:
                self.__id_usuario = id_usuario
                print("El ID esta correcto.")
                break
            else:
                id_usuario = int(input("Ingrese un ID válido. "))
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre=nombre   
    
    def get_apellido(self):
        return self.__apellido
    
    def set_apellido(self,apellido):
        if 3<= len(apellido) <=50:
            self.__apellido=apellido
            print("El apellido es correcto.")
        else:
            print("El apellido es incorrecto.")
   
    def get_email(self):
        return self.__email
    
    def set_email(self,email):
        self.__email =email
        if not isinstance(email, str):
            raise TypeError("El correo electrónico debe ser una cadena")
        if len(email) < 5:
            raise ValueError("El correo electrónico debe tener al menos 5 caracteres")
        if len(email) > 100:
            raise ValueError("El correo electrónico debe tener como máximo 100 caracteres")
        if "@" not in email:
            raise ValueError("El correo electrónico debe contener un arroba (@)")
        if "." not in email:
            raise ValueError("El correo electrónico debe contener un punto (.)")
        return email
        
    def get_contraseña(self):
        return self.__contraseña
    
    def set_contraseña(self,contraseña):
        if 5<= len(contraseña) <= 8:
            self.__contraseña = hash(contraseña)
            print("La contraseña esta correcta.")
        else:
            print("La contraseña debe tener entre 5 y 8 caracteres.")
    
    def get_ciudad(self):
        return self.__ciudad
    
    def set_ciudad(self,ciudad):
        if  3<= len (ciudad) <=50:
            self.__ciudad =ciudad
            print("La ciudad es correcta.")
        else:
            print("La ciudad es incorrecta.")
        
    def get_direccion(self):
        return self.__direccion
    
    def set_direccion(self,direccion):
        if  3<=  len(direccion) <=50:
            self.__direccion=direccion
            print("La dirección es correcta.")
        else:
            print("La dirección es incorrecta.")
          
          
    def get_telefono(self):
        return self.__telefono
    
    def set_telefono(self,telefono):
        
        if  7<=len (telefono) <=20:
            self.__telefono=telefono
            print("El teléfono es correcto.")
        else:
            print("El teléfono es incorrecto.")
    
    def iniciarSesion(self):
        pass
    
    def registrarse(self):
        pass
    
    def actualizarPerfil(self):
        pass