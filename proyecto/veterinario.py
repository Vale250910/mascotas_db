from datetime import datetime
class Veterinario:
    
    def __init__(self, id_vet:int, nombre:str,cargo:str, especialidad:str, horario:str,fecha_ingreso:datetime):
        self.__id_vet =id_vet
        self.__nombre=nombre
        self.__cargo =cargo
        self.__especialidad =especialidad
        self.__horario=horario
        self.__fecha_ingreso=fecha_ingreso
        
    def get_id_vet(self):
        return self.__id_vet
    
    def set_id_vet(self,id_vet):
        while True:
            id_vet = int(id_vet)
            if id_vet >= 1 and id_vet <= 100000000:
                self.__id_vet = id_vet
                print("El ID esta correcto")
                break
            else:
                id_us = int(input("Ingrese un ID válido: "))
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre =nombre
    
    def get_cargo(self):
        return self.__cargo
    
    def set_cargo(self,cargo):
        if 3<= len(cargo)  <=50:
            self.__cargo =cargo
            print("El cargo es correcto.")
        else:
            print("El cargo es incorrecto.")
        

    def get_especialidad(self):
        return self.__especialidad
    
    def set_especialidad(self,especialidad):
        if 5<=  len(especialidad) <=50:
            self.__especialidad =especialidad
            print("La especialidad es correcta.")
        else:
            print("La especialidad es incorrecta.")
        
        
    def get_horario(self):
        return self.__horario
    
    def set_horario(self,horario):
        if 3<=  len(horario) <=50:
            self.__horario =horario
            print("El horario es correcto.")
        else:
            print("El horario es incorrecto.")
        
    
    def get_fecha_ingreso(self):
        return self.__fecha_ingreso
    
    def set_fecha_ingreso(self,fecha_ingreso):
          self.__fecha_ingreso = fecha_ingreso

          while True:
            try:
                fecha_ingreso = datetime.strptime(fecha_ingreso, "%Y-%m-%d")
                if fecha_ingreso >= datetime(1950, 1, 1):
                    break  
                else:
                    print("La fecha debe ser igual o posterior al 01/01/1950. Intente nuevamente.")
            except ValueError:
                print("Formato de fecha inválido. Intente nuevamente.")
                break

    def verCalendario(self):
        pass
    
    def actualizarDisponibilidad(self):
        pass