


############################
#Borrar pantalla
import os
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')
############################

#####################################################################################################
# Funciones punto 1

import urllib
from bs4 import BeautifulSoup
#from urllib import request

def obtener_enlaces(url):
    html_pagina = urllib.request.urlopen(url)#devuelve la pagina formato html
    soup = BeautifulSoup(html_pagina, features="html.parser")
    etiquetas = soup('a') #en html los link estan referenciado por una etiqueta a
    #etiquetas es una tipo lista que devuelve 

    ### Aqui trabaja sobre cada una de las urls obtenidas
    lista_de_urls=[]
    for tag in etiquetas:
        url_html=tag.get('href') #devuelve una cadena de texto
        try:
            if url_html[0:4] == 'http':
                url_completa=str(tag.get('href'))#cadena de texto
            else :
                url_completa=(url+str(tag.get('href')))#concatena  la direccion relativa con la direccion original
            lista_de_urls.append(url_completa)
        except:
            print('')
    return lista_de_urls


import urllib.request

def obtener_enlaces_secundarios(lista_de_urls):
    dic_de_url = {}
    for url in lista_de_urls:
        lista_urls_secundarias = []
        print(f"Accediendo a los enlaces dentro de la página {url}")
        try:     
            html_pagina = urllib.request.urlopen(url)
            soup = BeautifulSoup(html_pagina, features="html.parser")
            etiquetas_secu = soup("a")  # devuelve todas las urls con etiqueta 'a' que están dentro de la página
            
            if len(etiquetas_secu) > 0: 
                #print(f"{len(etiquetas_secu)} enlaces que posee el link -----")
                for nueva_eti in etiquetas_secu:
                    url_html2 = nueva_eti.get("href")
                    try:
                        if url_html2.startswith("http"):
                            url_completa_secu = str(nueva_eti.get("href"))
                        else:
                            url_completa_secu = url + str(nueva_eti.get("href"))
                        lista_urls_secundarias.append(url_completa_secu)
                    except:
                        print("")

                lista_urls_secundarias = list(set(lista_urls_secundarias))
                lista_urls_secundarias = sorted(lista_urls_secundarias)
                dic_de_url[url] = lista_urls_secundarias
            else:
                print("No hay más enlaces")
        except:
                print("Algo ha fallado")  # si la petición al servidor falla, salta al except
            
    return dic_de_url

# Finaliza funciones punto 1
#####################################################################################################


# Main 

while True:
    clear_screen()
    print("Trabajo Practico N°3 Crawler y Scraper"+"\n\n")
    print("1. Punto 1: Desarrollo de Crawler para recolectar URLs de primer y segundo nivel de un sitio WEB")
    print("2. Punto 2: Web Scraping y Análisis Textual de las 10 Primeras Noticias de un sitio WEB")
    print("3. Punto 3: Identificación de Similitudes y Relaciones entre Noticias a través de Términos en Común")
    print("4. Salir\n")

    opcion = input("Ingrese una opción: ")
    if opcion == "1":


        """
        Planifique, diseñe y construya un crawler para recolectar todas las URLs de los primeros 
        2 niveles de profundidad del sitio web:https://www.fi.unju.edu.ar/
        Deberá crear una hoja de cálculo (Excel o Google SpreadSheet) para almacenar lo recolectado, 
        teniendo en cuenta de identificar las URLs de cada nivel de origen. Evite recolectar URLs repetidas, 
        para ello deberá almacenar de algún modo las URLs que vaya visitando.

        """
        clear_screen()

        url = "https://www.fi.unju.edu.ar/" #Defino la url del link a visitar
        lista_de_urls=obtener_enlaces(url) #Aqui obtiene todas las urls de primer nivel

        lista_de_urls = list(set(lista_de_urls)) # eliminar urls repetidas
        lista_de_urls = sorted(lista_de_urls) # ordenarlas


        print('Enlaces de página principal: \r\n')
        for tag in lista_de_urls:
            print(tag) 
        print('Tamaño de lista:', len(lista_de_urls))


        diccionario_de_urls = obtener_enlaces_secundarios(lista_de_urls)


###########################################################################
        import pandas as pd
        
        # Definir el diccionario
        diccionario=diccionario_de_urls

        # Crear un DataFrame a partir del diccionario
        df = pd.DataFrame.from_dict(diccionario, orient='index')

        # Transponer el DataFrame para que las claves sean filas y los valores sean columnas
        df = df.transpose()

        # Exportar el DataFrame a un archivo de Excel
        df.to_excel('archivo.xlsx', index=False)

##########################################################################3
        from openpyxl import load_workbook
        # Cargar el archivo existente
        book = load_workbook('archivo.xlsx')
        # Seleccionar la hoja a modificar
        sheet = book.active
        # Modificar el formato de las columnas
        for col in sheet.columns:
            max_length = 0
            column = col[0].column_letter
            for cell in col:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(cell.value)
                except:
                    pass
            adjusted_width = (max_length + 2) * 1.2
            sheet.column_dimensions[column].width = adjusted_width


        # Guardar los cambios en el archivo existente
        book.save('archivo.xlsx')
############################################################################
        #Dar color a la primer fila del excel

        from openpyxl.styles import PatternFill
        from openpyxl import load_workbook

        # Cargar el archivo Excel
        wb = load_workbook('archivo.xlsx')

        # Seleccionar la hoja de trabajo
        ws = wb.active

        # Definir el patrón de relleno
        fill = PatternFill(start_color='FFC7CE', end_color='FFC7CE', fill_type='solid')

        # Obtener la primera fila
        row = ws[1]

        # Aplicar el patrón de relleno a cada celda de la primera fila
        for cell in row:
            cell.fill = fill

        # Guardar el archivo Excel
        wb.save('archivo.xlsx')


        input("Presione enter para continuar...")
        pass

    elif opcion == "2":
       
        clear_screen()#Borra pantalla
        
        
        input("Presione enter para continuar...")

        pass


    elif opcion == "3":

        clear_screen()
        

        
        input("Presione enter para continuar...")

        pass

    elif opcion == "4":
        clear_screen()
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, por favor intente de nuevo.")
        input("Presione enter para continuar...")
