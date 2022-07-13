#Carazas Quispe, Alessander Jesus
#Pardavé Espinoza Christian
#Nizama Cespedes Juan Carlos Antonio

from tkinter import*#IMPORTAMOS LIBRERIA TKINTER 
import matplotlib
import matplotlib.pyplot as plt
from datetime import date
from os import remove

import linecache
import aspose.words as aw


#Variables estadistica

Numero_clases=0#Variable para guardar el numero de clases

#Variables para el grafico de pastel
asistio=0
no_asist=0

#inicio con el porcentaje de asistencia
porcentaje_actual=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
inicio_porc = open("alum_porce.txt","r")
i=0
while(True):
    linea = inicio_porc.readline()
    if not linea:
        break
    if(linea[1]!='\n'):
           porcentaje_actual[i]=int(linea[:2])
    else:
         porcentaje_actual[i]=int(linea[0])
    i=i+1
inicio_porc.close()


# Guardado en txt
    
def txt(asignatura_r):#definimos funcion txt
    file = open("Asistencia.txt","a")#abre txt en caso no este creado se crea
    esp=" "#se da variable = espacio
    if(contador-1==1):# condicional de inicio(se imprime cabecera .txt)
        file.write("\nASISTENCIA: "+fecha+"\n"+"\nAPELLIDOS Y NOMBRES"+"\t\t\t"+"    ¿ASISTIÓ?"+"\t\n")#se imprime la cabecera
    file.write(str(contador-1))#imprime lista
    if(len(lista_alum[contador-2])<29):#si la longitud de l nombre es muy larga, se tabula de manera automatica
        file.write(". "+lista_alum[contador-2]+esp*(29-len(lista_alum[contador-2]))+"\t"+"|")#imprime tabullaciones, espacios
    else:
        file.write(". "+lista_alum[contador-2]+"\t"+"|")#de lo contrario solo tabula una vez
    file.write("\t")#define tab
    file.write(asignatura_r)#define asistencia
    file.write("\t|     ")#define tab + |
    file.write("\t\t\n")#impirme tabulacions mas salto de linea


    #guardar numero de clases
    
    if(contador==2):
        n_clases = open("Numero_clases.txt","r")
        global Numero_clases
        Numero_clases=int(n_clases.read())+1
        n_clases.close()
        clases = open("Numero_clases.txt","w")
        clases.write(str(Numero_clases))
        clases.close()
        
    #agregar porcentaje asistencia de cada alumno
    if(asignatura_r=="Si"):
        porcentaje_actual[contador-2]=porcentaje_actual[contador-2]+1

    
    file.close()#cierra ventana
    print("Asistencia Registrada.")#imprime asistencia registrada

def actualizar_porce():
    file = open("alum_porce.txt","w")
    for i in porcentaje_actual:
        file.write(str(i))
        file.write("\n")
    file.close



def total_alum():
        auxiliar=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        file = open("alum_porce.txt","r")
        i=0
        while(True):
            linea = file.readline()
            if not linea:
                break
            if(linea[1]!='\n'):
                auxiliar[i]=linea[:2]
            else:
                auxiliar[i]=linea[0]
            i=i+1
        file.close()

        n_clases = open("Numero_clases.txt","r")
        total_clases=int(n_clases.read())
        n_clases.close()
        #print(auxiliar)
        num_total=0
        num_falta=0
        for i in range(1,39,1):
            if(int(auxiliar[i])==total_clases):
                num_total+=1
                
        for i in range(0,39,1):
            if(int(auxiliar[i])!=total_clases):
                num_falta+=1
            
        total_alumnos = Tk()#sobrepone la ventana
        total_alumnos.geometry("350x300")#define dimensiones
        
        total_alumnos.title("Alumnos Que Asistieron y Faltaron en el Semestre")#titulo de la ventana
        total_alumnos.resizable(False,False)#hace que tenga un solo tamaño
        total_alumnos.config(background = "#213141")#define fondo
        main_title4 = Label(total_alumnos,text = "Asistieron todo el Semestre", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "200", height = "2")
        main_title4.pack()#ajusta los widgets a la ventana
        num=Label(total_alumnos,text=num_total, font= ("",20) )#label del alumno
        num.place(x = 150, y = 70)#ubicacion
        main_title5 = Label(total_alumnos,text = "Faltaron en el Semestre", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "35", height = "2")
        main_title5.place(x=0,y=110)
        num2=Label(total_alumnos,text=num_falta, font= ("",20) )#label del alumno
        num2.place(x = 150, y = 180)#ubicacion
        aceptar_btn= Button(total_alumnos,text = "Aceptar", width = "13", height = "2",command =lambda:[total_alumnos.destroy()],bg = "#00CD63")
        #imprime boton presencial, (lambda ejecuta funciones en cadena)
        aceptar_btn.place(x = 120, y = 210)#ubicacion en la ventana




def porce_alumno():
    actualizar_porce()
    valores=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    file = open("alum_porce.txt","r")
    i=0
    while(True):
        linea = file.readline()
        if not linea:
            break
        if(linea[1]!='\n'):
            valores[i]=linea[:2]
        else:
            valores[i]=linea[0]
        i=i+1
    file.close()

    
    eje_x = ["Apaza","ApazaQ","Benavente","Carazas","Castillo","Cayllahua","Ccama","Cerpa","Condori","Davis","Escarza","Gonzales","Gutierrez",
             "Hualpa","Huaman","Lazo","Lopez","Lupo","Maldonado","Maldonado","Mariños","Martínez","Mayorga","Mena","Mogollon","Montoya","Nizama",
             "Olazábal","Pardavé","Parizaca","Quilca","Quispe","Roque","Ruiz","Sucasaca","Taya","Yavar","Zamalloa","Zhong"]
    n_clases = open("Numero_clases.txt","r")
    numero_clases=int(n_clases.read())
    n_clases.close()
    eje_y=[int(valores[0])/numero_clases,int(valores[1])/numero_clases,int(valores[2])/numero_clases,int(valores[3])/numero_clases,
           int(valores[4])/numero_clases,int(valores[5])/numero_clases,int(valores[6])/numero_clases,int(valores[7])/numero_clases,
           int(valores[8])/numero_clases,int(valores[9])/numero_clases,int(valores[10])/numero_clases,int(valores[11])/numero_clases,
           int(valores[12])/numero_clases,int(valores[13])/numero_clases,int(valores[14])/numero_clases,int(valores[15])/numero_clases,
           int(valores[16])/numero_clases,int(valores[17])/numero_clases,int(valores[18])/numero_clases,int(valores[19])/numero_clases,
           int(valores[20])/numero_clases,int(valores[21])/numero_clases,int(valores[22])/numero_clases,int(valores[23])/numero_clases,
           int(valores[24])/numero_clases,int(valores[25])/numero_clases,int(valores[26])/numero_clases,int(valores[27])/numero_clases,
           int(valores[28])/numero_clases,int(valores[29])/numero_clases,int(valores[30])/numero_clases,int(valores[31])/numero_clases,
           int(valores[32])/numero_clases,int(valores[33])/numero_clases,int(valores[34])/numero_clases,int(valores[35])/numero_clases,
           int(valores[36])/numero_clases,int(valores[37])/numero_clases,int(valores[38])/numero_clases]
    plt.bar(eje_x, eje_y)
    plt.ylabel('Cantidad de asistencia')
    plt.xlabel('Estudiantes')
    plt.title('Porcentaje')
    plt.savefig('Porcentaje_Asistencia_Alumnos.png')
    plt.show()

def abandono_alumnos():
    if(contador-1==39):
        auxiliar=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        file = open("alum_porce.txt","r")
        i=0
        while(True):
            linea = file.readline()
            if not linea:
                break
            auxiliar[i]=linea[0]
            i=i+1
        file.close()
        num_aban=0
        for i in range(0,39,1):
            if(auxiliar[i]=='0'):
                num_aban+=1
        
        
        abandono = Tk()#sobrepone la ventana
        abandono.geometry("350x200")#define dimensiones
            
        abandono.title("Abandono de alumnos")#titulo de la ventana
        abandono.resizable(False,False)#hace que tenga un solo tamaño
        abandono.config(background = "#213141")#define fondo
        main_title3 = Label(abandono,text = "Alumnos que abandonaron", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "200", height = "2")#define label de la ventana
        main_title3.pack()#ajusta los widgets a la ventana
        aban=Label(abandono,text=num_aban, font= ("",20))#label del alumno
        aban.place(x = 150, y = 70)#ubicacion
        aceptar_btn= Button(abandono,text = "Aceptar", width = "13", height = "2",command =lambda:[abandono.destroy()],bg = "#00CD63")
        #imprime boton presencial, (lambda ejecuta funciones en cadena)
        aceptar_btn.place(x = 120, y = 110)#ubicacion en la ventana

    

def informe_a():
    remove("Asistencia_Final.txt")
    remove("asistencia_final2.txt") 
    contador_=2
    num_asis=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    file = open("alum_porce.txt","r")
    i=0
    while(True):
        linea = file.readline()
        if not linea:
            break
        if(linea[1]!='\n'):
            num_asis[i]=linea[:2]
        else:
            num_asis[i]=linea[0]
        i=i+1
    file.close()
    abandonaron=0;
    total_a=0
    total_falta=0
    n_clases = open("Numero_clases.txt","r")
    total_clases=int(n_clases.read())
    n_clases.close()
    file_main = open("Asistencia_Final.txt","a")
    file_2 = open("asistencia_final2.txt","a")
    for i in range (0,39):
        esp=" "
        if(contador_-1==1):
            file_main.write("\nASISTENCIA\nNÚMERO DE CLASES: "+str(total_clases)+"\n"+"\nAPELLIDOS Y NOMBRES"+"\t\t\t"+"   NÚMERO DE ASISTENCIAS"+"\t\n")
        file_main.write(str(contador_-1))
        if(len(lista_alum[contador_-2])<29):
            file_main.write(". "+lista_alum[contador_-2]+esp*(29-len(lista_alum[contador_-2]))+"\t\t"+"|")
        else:
            file_main.write(". "+lista_alum[contador_-2]+"\t\t"+"|")
        file_main.write("\t")
        file_main.write(str(num_asis[i]))
        file_main.write("\t|\n")
        file_2.write(str(num_asis[i]))
        file_2.write("\n")
        if(int(num_asis[i])==0):
            abandonaron+=1
        if(int(num_asis[i])==int(total_clases)):
            total_a+=1
        if(int(num_asis[i])!=int(total_clases)):
            total_falta+=1
        contador_+=1

    file_main.write("\n------------------------------------------------\n")
    file_main.write("\nCantidad de alumnos que abandonaron el curso: " + str(abandonaron) + "\n")
    file_main.write("\n------------------------------------------------\n")
    file_main.write("\nCantidad de alumnos que asistieron todo el semestre: " + str(total_a) + "\n")
    file_main.write("\n------------------------------------------------\n")
    file_main.write("\nCantidad de alumnos que falaron en el semestre: " + str(total_falta) + "\n")
    file_main.close()    
    file_2.close()
    
    doc = aw.Document("Asistencia_Final.txt")
    doc.save("Informe_Asistencia.pdf")


#Mostrar numero de clases

def num_clases():
    if(contador-1==39):
        global Numero_clases
        num_clases = Tk()#sobrepone la ventana
        num_clases.geometry("350x200")#define dimensiones
        
        num_clases.title("Número de Clases")#titulo de la ventana
        num_clases.resizable(False,False)#hace que tenga un solo tamaño
        num_clases.config(background = "#213141")#define fondo
        main_title2 = Label(num_clases,text = "Número de clases", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "200", height = "2")#define label de la ventana
        main_title2.pack()#ajusta los widgets a la ventana
        num=Label(num_clases,text=Numero_clases, font= ("",20) )#label del alumno
        num.place(x = 150, y = 70)#ubicacion
        aceptar_btn= Button(num_clases,text = "Aceptar", width = "13", height = "2",command =lambda:[num_clases.destroy()],bg = "#00CD63")
        #imprime boton presencial, (lambda ejecuta funciones en cadena)
        aceptar_btn.place(x = 120, y = 110)#ubicacion en la ventana
        pastel()
        porce_alumno()
        total_alum()

contador=1;#se da variable para poder inicializar

def imprimir():#funcion imprimir
    global contador#indicas variable global 
    etiqueta['text']=lista_alum[contador]#texto de etiqueta = nombre del alumno de acuerdo al index de la lista
    contador+=1#hace correr la lista

def cerrar():#funcion cerrar
    if(contador-1==39):#si llega al final de la lista(39 personas)
        mywindow.destroy()#cierra ventana

def asist(aux):
    global asistio,no_asist
    if(aux==0):
        asistio+=1
    elif(aux==1):
        no_asist+=1

def salir(var):
    var.destroy()

def switch(comp):
    if(comp["state"]=="normal"):
        comp["state"]="disabled"

#Grafico pastel de porcentaje de asistencia
def pastel():
    porcentaje_asist = ["Asistió","No Asitió"]
    sizes = [asistio,no_asist]
    explode = (0,0)

    fig1,ax1 = plt.subplots()

    ax1.pie(sizes,explode=explode,labels=porcentaje_asist,autopct='%1.1f%%',shadow=True,startangle=90)
    ax1.axis('equal')
    plt.title("Pocentaje de Asistencia de hoy")
    plt.legend()
    plt.savefig('asistencia_pastel.png')
    plt.show()

    

#Pantalla principal

mywindow = Tk()#inicia variable de la ventana
mywindow.geometry("300x450")#dimensiones de la ventana
mywindow.title("Formulario de Asistencia - Trabajo Interdisciplinar")#titulo de la ventana
mywindow.resizable(False,False)#tamaño constante
mywindow.config(background = "#213141")#color de fondo
main_title = Label(text = "Trabajo Interdisciplinar", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")#encabezado de la ventana (widget)
main_title.pack()#ajusta los widgets a la ventana

#Definimos lista de alumnos

lista_alum=["Apaza Apaza Nelzon Jorge",
"Apaza Quispe Angel Abraham",
"Benavente Aguirre Paolo Daniel",
"Carazas Quispe Alessander Jesus",
"Castillo Sancho Sergio",
"Cayllahua Gutierrez Diego Yampier",
"Ccama Marron Gustavo Alonso",
"Cerpa Garcia Jean Franco",
"Condori Casquino Ebert Luis",
"Davis Coropuna Leon Felipe",
"Escarza Pacori Alexander Raul",
"Gonzales Condori Alejandro Javier",
"Gutierrez Zevallos Jaime José",
"Hualpa Lopez Jose Mauricio",
"Huaman Coaquira Luciana Julissa",
"Lazo Paxi Natalie Marleny",
"Lopez Condori Andrea Del Rosario",
"Lupo Condori Avelino",
"Maldonado Casilla Braulio Nayap",
"Maldonado Parejo Roy Abel",
"Mariños Hilario Princce Yorwin",
"Martínez Choque Aldo Raúl",
"Mayorga Villena Jharold Alonso",
"Mena Quispe Sergio Sebastian Santos",
"Mogollon Caceres Sergio Daniel",
"Montoya Choque Leonardo",
"Nizama Cespedes Juan Carlos Antonio",
"Olazábal Chávez Neill Elverth",
"Pardavé Espinoza Christian",
"Parizaca Mozo Paul Antony",
"Quilca Huamani Bryan",
"Quispe Rojas Javier Wilber",
"Roque Sosa Owen Haziel",
"Ruiz Mamani Eduardo German",
"Sucasaca Chire Edward Henry",
"Taya Yana Samuel Omar",
"Yavar Guillen Roberto Gustavo",
"Zamalloa Molina Sebastian Agenor",
"Zhong Callasi Linghai Joaquin",""]


#labels

nombre=lista_alum[0]#muestra en pantalla el primer elemento de la lista


fecha = str(date.today().strftime('%A, %B %d, %Y'))#variable tipo cadena(recibe texto de label fecha)

asistencia_label = Label(text = "ASISTENCIA", font = ("Italic", 14,"bold"), bg = "#00FFFF", fg = "red", width = "18", height = "1")#indica label de la ASISTENCIA
asistencia_label.place(x = 30, y = 70)#ubicacion 

fecha_label = Label(text = "Fecha:", bg = "#00FFFF",font=("",13))#indica label de la fecha
fecha_label.place(x = 40, y = 120)#ubicacion 

fecha_entry = Label(text= fecha,font=("",11), width = "25")#label de entrada 
fecha_entry.place(x = 40, y = 150)#ubicacion

nombres_label = Label(text = "Apellidos y Nombres: ", bg = "#00FFFF",font =("",14))#label de nbombres(estetica)
nombres_label.place(x = 40, y = 180)#ubicacion

etiqueta=Label (text=nombre, font= ("",12) )#label del alumno
etiqueta.place(x = 40, y = 213)#ubicacion


#send_data

asistencia_label = Label(text = "¿Asistió?", bg = "#00FFFF",font=("",14))#label de la pregunta asistio
asistencia_label.place(x = 40, y = 250)#ubicacion

submit_btn = Button(mywindow,text = "Si", width = "9", height = "2", command =lambda:[imprimir(0),txt("Si"),cerrar(),num_clases(),asist(0),abandono_alumnos()],bg = "#00CD63")#label del boton si
submit_btn.place(x = 70, y = 290)#ubicacion

submit_btn = Button(mywindow,text = "No", width = "9", height = "2", command =lambda:[imprimir(),txt("No"),cerrar(),num_clases(),asist(1),abandono_alumnos()],bg = "#00CD63")#label boton no asistio
submit_btn.place(x = 150, y = 290)#ubicacion

cerrar_btn = Button(mywindow,text = "Salir",width="10",height = "2",command =lambda:[salir(mywindow)],bg = "#00CD63")#label del boton salir
cerrar_btn.place(x=110,y=400)#ubicacion

informe_asistencia = Button(mywindow,text = "INFORME ASISTENCIA",width="16",height = "2",command =lambda:[informe_a()],bg = "#00CD63")#label del boton salir
informe_asistencia.place(x=85,y=340)#ubicacion


mywindow.mainloop()#mantiene el programa en espera hasta que el usuario desea cerrarlo.
#Gracias :D



