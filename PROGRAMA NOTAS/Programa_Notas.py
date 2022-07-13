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

def txt_notas():
    notas_info = nota_continua.get()
    comp=linecache.getline('auxiliar.txt',1).strip()
##    comp1=linecache.getline('continuas.txt',1).strip()
##    comp2=linecache.getline('continuas2.txt',1).strip()
##    comp3=linecache.getline('continuas3.txt',1).strip()
    if(int(comp)==0):
    #if(comp1=='-' or int(comp1)>=0):
        file1 = open("continuas.txt","a")
        file1.write(notas_info)
        file1.write("\n")
        file1.close()
        file_c=open("auxiliar.txt","w")
        file_c.write(str(1))
        file_c.close()
    if(int(comp)==1):
#    elif(comp2=='-' or int(comp2)>=0):
        file2 = open("continuas2.txt","a")
        file2.write(notas_info)
        file2.write("\n")
        file2.close()
        file_c=open("auxiliar.txt","w")
        file_c.write(str(2))
        file_c.close()
    if(int(comp)==2):
#    elif(comp3=='-' or int(comp3)>=0):
        file3 = open("continuas3.txt","a")
        file3.write(notas_info)
        file3.write("\n")
        file3.close()
        file_c=open("auxiliar.txt","w")
        file_c.write(str(3))
        file_c.close()


def txt_notas_parciales():
    notas_info = nota_parcial.get()
    comp=linecache.getline('auxiliar2.txt',1).strip()
    if(int(comp)==0):
        file1 = open("parciales.txt","a")
        file1.write(notas_info)
        file1.write("\n")
        file1.close()
        file_c=open("auxiliar2.txt","w")
        file_c.write(str(1))
        file_c.close()
    if(int(comp)==1):
        file2 = open("parciales2.txt","a")
        file2.write(notas_info)
        file2.write("\n")
        file2.close()
        file_c=open("auxiliar2.txt","w")
        file_c.write(str(2))
        file_c.close()
    if(int(comp)==2):
        file3 = open("parciales3.txt","a")
        file3.write(notas_info)
        file3.write("\n")
        file3.close()
        file_c=open("auxiliar2.txt","w")
        file_c.write(str(3))
        file_c.close()



def pdf_notas_final():
    remove("Notas_Finales.txt")
    remove("notas_finales2.txt")
    contador_=2
    promedio_final=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    file_min = open("nota_minima.txt","r")
    nota_minima = int(file_min.read())
    file_min.close()
    aprobados=0
    desaprobados=0
    quien_tuvo_mayor_nota=" "
    quien_tuvo_menor_nota=" "
    menor_nota=int(promedio_final[0])
    mayor_nota=int(promedio_final[0])

    
    for i in range (0,39):
        con_1=linecache.getline('continuas.txt',i+1).strip()
        con_2=linecache.getline('continuas2.txt',i+1).strip()
        con_3=linecache.getline('continuas3.txt',i+1).strip()
        par_1=linecache.getline('parciales.txt',i+1).strip()
        par_2=linecache.getline('parciales2.txt',i+1).strip()
        par_3=linecache.getline('parciales3.txt',i+1).strip()

        promedio_final[i]=(int(con_1)*0.1)+(int(con_2)*0.1)+(int(con_3)*0.3)+((int(par_1)*0.1)+(int(par_2)*0.1)+(int(par_3)*0.3))
        promedio_final[i]=round(promedio_final[i])
        file_main = open("Notas_Finales.txt","a")
        file_2 = open("notas_finales2.txt","a")
        esp=" "
        if(contador_-1==1):
            file_main.write("\nNOTAS DEL CURSO DE TRABAJO INTERDISCIPLINAR: "+"\n"+"\nAPELLIDOS Y NOMBRES"+"\t\t\t"+"    PROMEDIO"+"\t\n")
        file_main.write(str(contador_-1))
        if(len(lista_alum[contador_-2])<29):
            file_main.write(". "+lista_alum[contador_-2]+esp*(29-len(lista_alum[contador_-2]))+"\t"+"|")
        else:
            file_main.write(". "+lista_alum[contador_-2]+"\t"+"|")
        file_main.write("\t")
        file_main.write(str(promedio_final[i]))
        file_main.write("\t|\n")
        file_2.write(str(promedio_final[i]))
        file_2.write("\n")
        file_main.close()
        file_2.close()

        if(int(promedio_final[i])>=nota_minima):
            aprobados+=1
        if(int(promedio_final[i])<nota_minima):
            desaprobados+=1
        if(int(promedio_final[i])>mayor_nota):
            mayor_nota=int(promedio_final[i])
            quien_tuvo_mayor_nota=str(lista_alum[contador_-2])
        if(int(promedio_final[i])<menor_nota):
            menor_nota=int(promedio_final[i])
            quien_tuvo_menor_nota=str(lista_alum[contador_-2])
        contador_+=1

    file_main = open("Notas_Finales.txt","a")
    file_main.write("\n------------------------------------------------\n")
    file_main.write("\nAlumno con la mayor nota: " + str(quien_tuvo_mayor_nota) + "(" + str(mayor_nota) + ")" + "\n")
    file_main.write("\n------------------------------------------------\n")
    file_main.write("\nAlumno con la menor nota: " + str(quien_tuvo_menor_nota) + "(" + str(menor_nota) + ")" + "\n")
    file_main.write("\n------------------------------------------------\n")
    file_main.write("\nCantidad de alumnos que aprobaron el semestre: " + str(aprobados) + "\n")
    file_main.write("\n------------------------------------------------\n")
    file_main.write("\nCantidad de alumnos que desaprobaron el semestre: " + str(desaprobados) + "\n")
    file_main.close()    
    file_2.close()
    
    
    doc = aw.Document("Notas_Finales.txt")
    doc.save("Informe_Notas_Finales.pdf")

def peligro_jalar():
    contador_=2
    promedio_final=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range (0,38):
        con_1=linecache.getline('continuas.txt',i+1).strip()
        con_2=linecache.getline('continuas2.txt',i+1).strip()
        #con_3=linecache.getline('continuas3.txt',i+1).strip()
        par_1=linecache.getline('parciales.txt',i+1).strip()
        par_2=linecache.getline('parciales2.txt',i+1).strip()
        #par_3=linecache.getline('parciales3.txt',i+1).strip()

        promedio_final[i]=(((int(con_1)+int(con_2))+(int(par_1)+int(par_2)))/6)
        contador_+=1

    num_peligro=0
    for i in range(0,39,1):
        if(int(promedio_final[i])<=7):
            num_peligro+=1
    
    
    peligro = Tk()#sobrepone la ventana
    peligro.geometry("350x200")#define dimensiones
        
    peligro.title("Abandono de alumnos")#titulo de la ventana
    peligro.resizable(False,False)#hace que tenga un solo tamaño
    peligro.config(background = "#213141")#define fondo
    main_title6 = Label(peligro,text = "Alumnos que pueden jalar", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "200", height = "2")#define label de la ventana
    main_title6.pack()#ajusta los widgets a la ventana
    jalar=Label(peligro,text=num_peligro, font= ("",20))#label del alumno
    jalar.place(x = 150, y = 70)#ubicacion
    aceptar_btn= Button(peligro,text = "Aceptar", width = "13", height = "2",command =lambda:[peligro.destroy()],bg = "#00CD63")
    #imprime boton presencial, (lambda ejecuta funciones en cadena)
    aceptar_btn.place(x = 120, y = 110)#ubicacion en la ventana



#se da variable para poder inicializar
contador2=1
contador3=1

def imprimir(comp):#funcion imprimir
    global contador2,contador3#indicas variable global 
    if(comp==1):
        etiqueta2['text']=lista_alum[contador2]
        contador2+=1
        if(contador2-1==39):
            texto="Fin..."
            etiqueta2['text']==texto
            switch(submit_btn_guardar)
    elif(comp==2):
        etiqueta3['text']=lista_alum[contador3]
        contador3+=1
        if(contador3-1==39):
            texto2="Fin..."
            etiqueta3['text']==texto2
            switch(submit_btn_guardar2)

def cerrar():#funcion cerrar
    if(contador-1==39):#si llega al final de la lista(39 personas)
        mywindow.destroy()#cierra ventana


def salir(var):
    var.destroy()

def switch(comp):
    if(comp["state"]=="normal"):
        comp["state"]="disabled"


#Pantalla principal

mywindow = Tk()#inicia variable de la ventana
mywindow.geometry("500x400")#dimensiones de la ventana
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


#send_data
cerrar_btn = Button(mywindow,text = "Salir",width="10",height = "2",command =lambda:[salir(mywindow)],bg = "#00CD63")#label del boton salir
cerrar_btn.place(x=220,y=330)#ubicacion

#COLUMNA INGRESO DE NOTAS CONTINUAS

ingreso_notas_label = Label(text = "INGRESO DE NOTAS", font = ("Italic", 14,"bold"), bg = "#00FFFF", fg = "red", width = "18", height = "1")#indica label de la ASISTENCIA
ingreso_notas_label.place(x = 40, y = 70)#ubicacion 

continua_label = Label(text = "CONTINUA:", bg = "#00FFFF",font=("",13))#indica label de la fecha
continua_label.place(x = 40, y = 120)#ubicacion

nombres_label = Label(text = "Apellidos y Nombres: ", bg = "#00FFFF",font =("",14))#label de nbombres(estetica)
nombres_label.place(x = 40, y = 150)#ubicacion

etiqueta2=Label (text=nombre, font= ("",12) )#label del alumno
etiqueta2.place(x = 40, y = 185)#ubicacion

submit_btn_guardar = Button(mywindow,text = "GUARDAR",command =lambda:[imprimir(1),txt_notas( )], width = "9", height = "2",bg = "#00CD63")#label del boton guardar
submit_btn_guardar.place(x = 100, y = 290)#ubicacion

asistencia_label = Label(text = "Nota: ", bg = "#00FFFF",font=("",14))#label de la nota
asistencia_label.place(x = 40, y = 218)#ubicacion

nota_continua = StringVar()#variable tipo cadena(recibe texto de label nota)
nota_entry = Entry(textvariable = nota_continua, width = "30")#label de entrada 
nota_entry.place(x = 40, y = 250)#ubicacion


##NOTAS PARCIALES

parcial_label = Label(text = "PARCIAL:", bg = "#00FFFF",font=("",13))#indica label de la fecha
parcial_label.place(x = 280, y = 120)#ubicacion 

nombres2_label = Label(text = "Apellidos y Nombres: ", bg = "#00FFFF",font =("",14))#label de nbombres(estetica)
nombres2_label.place(x = 280, y = 150)#ubicacion

etiqueta3=Label(text=nombre, font= ("",12) )#label del alumno
etiqueta3.place(x = 280, y = 185)#ubicacion

asistencia_label = Label(text = "Nota: ", bg = "#00FFFF",font=("",14))#label de la nota
asistencia_label.place(x = 280, y = 218)#ubicacion

nota_parcial = StringVar()#variable tipo cadena(recibe texto de label nota)
nota2_entry = Entry(textvariable = nota_parcial, width = "30")#label de entrada 
nota2_entry.place(x = 280, y = 250)#ubicacion

submit_btn_guardar2 = Button(mywindow,text = "GUARDAR",command =lambda:[imprimir(2),txt_notas_parciales()], width = "9", height = "2",bg = "#00CD63")#label del boton guardar
submit_btn_guardar2.place(x = 310, y = 290)#ubicacion

#PDF

button_pdf_final = Button(mywindow,text="INFORME NOTAS",command=lambda:[pdf_notas_final()],width="16",height="1",bg="#00CD63")
button_pdf_final.place(x=40,y=360)

#PELIGRO DE JALAR
button_pdf_final = Button(mywindow,text="PUEDEN JALAR",command=lambda:[peligro_jalar()],width="16",height="1",bg="#00CD63")
button_pdf_final.place(x=340,y=360)

mywindow.mainloop()#mantiene el programa en espera hasta que el usuario desea cerrarlo.
#Gracias :D



