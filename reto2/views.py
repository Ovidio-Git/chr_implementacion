from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .models import concesionesMaritimas
from time import sleep
from json import dump




datos_tabla = []
numeros_navegacion_tabla = []


def get_concesiones(request):
    
    #Declaracion de variables
    url = "https://www.concesionesmaritimas.cl/C_ConcesionesVigentes.jsp?ind=9&cons=1&variable=0&maritimas=0&acuicolas=0&permisos=0&carga=0"
    xpath_seleccione_region="/html/body/font/form/center/table[1]/tbody/tr[2]/td[1]/select"
    xpath_seleccione_gobernacion_maritima="/html/body/font/form/center/table[1]/tbody/tr[4]/td[1]/select"
    xpath_seleccione_capitania_puerto="/html/body/font/form/center/table[1]/tbody/tr[6]/td/select"
    xpath_boton_listado="/html/body/font/form/table[2]/tbody/tr[1]/td/img[2]"
    xpath_tabla_listado="/html/body/font/form/div/center/table/tbody"
    
    # Configuración del navegador
    options = Options()
    #options.add_argument("--headless")  # Ejecución sin ventana del navegador
    browser = webdriver.Chrome(executable_path='./chromedriver_linux64/chromedriver', options=options)
    
    
    # Consulta a pagina con la tabla
    browser = webdriver.Chrome(executable_path='./chromedriver_linux64/chromedriver')
    browser.get(url)
    browser.refresh()
    
    try:
        sleep(1)
        #Seleccionar valor II para el filtro region
        lista_desplagable_region = Select(browser.find_element(by=By.XPATH, value=xpath_seleccione_region))
        lista_desplagable_region.select_by_value("2")
        sleep(1)
        #Selecionar valor Gobernación Marítima Antofagasta para el filtro gobernacion maritima
        lista_desplagable_gobernacion_maritima = Select(browser.find_element(by=By.XPATH, value=xpath_seleccione_gobernacion_maritima))
        lista_desplagable_gobernacion_maritima.select_by_value("12")
        #Selecionar valor Antofagasta para el filtro Capitanía de Puerto
        sleep(1)
        lista_desplagable_capitania_puerto = Select(browser.find_element(by=By.XPATH, value=xpath_seleccione_capitania_puerto))
        lista_desplagable_capitania_puerto.select_by_value("13") 
        #Realizar click en el boton ver listado y esperar a que muestre la tabla con los datos
        boton_element_listado = browser.find_element(by=By.XPATH, value=xpath_boton_listado).click()
        wait = WebDriverWait(browser,20)
        wait.until(EC.presence_of_element_located((By.XPATH, xpath_tabla_listado)))
        
        #Extraer datos de la tabla con los datos filtrados
        
        # extraer datos de paginacion
        navegacion_tabla = browser.find_element(by=By.XPATH,value="/html/body/font/form/p[4]/font/table/tbody")
        
        for objetivo in navegacion_tabla.find_elements_by_tag_name('td'):
            numeros_navegacion_tabla.append(objetivo.text)
        numeros_navegacion_tabla.pop(0)

        ###################################
        
        ### extraccion de datos primera pagina
        thead = browser.find_element(by=By.XPATH, value=xpath_tabla_listado)
        for tr in thead.find_elements(by=By.TAG_NAME, value='tr'):
            datos_fila = []
            for td in tr.find_elements(by=By.TAG_NAME, value='td'):
                datos_celda = td.text  # Separar cada columna en elementos individuales
                datos_fila.append(datos_celda)
            datos_tabla.append(datos_fila)
        datos_tabla.pop(0)
        #######################################

        # Navegando en las paginas de la tabla
        for i in numeros_navegacion_tabla:
            browser.find_element(by=By.XPATH,value=f"/html/body/font/form/p[4]/font/table/tbody/tr/td[{i}]/font/a").click()

            ### extraccion de datos de la vista
            thead = browser.find_element(by=By.XPATH, value=xpath_tabla_listado)
            for tr in thead.find_elements(by=By.TAG_NAME, value='tr')[1:]:
                datos_fila = []
                for td in tr.find_elements(by=By.TAG_NAME, value='td'):
                    datos_celda = td.text  # Separar cada columna en elementos individuales
                    datos_fila.append(datos_celda)
                datos_tabla.append(datos_fila)
        #########################################    
            
            
        browser.quit()
            
        
        # Creacion de archivo .json
        nombre_archivo = "output_datos_tabla.json"
        with open(nombre_archivo, "w") as archivo_json:
            dump(datos_tabla, archivo_json)

        #insercion de datos a tabla reto2_concesionesmaritimas
        for fila in datos_tabla:
            instancia_concesion = concesionesMaritimas(numero_id=int(fila[0]), 
                                        numero_concesion=int(fila[1]), 
                                        tipo_de_concesion=fila[2],
                                        comuna=fila[3], 
                                        lugar=fila[4],
                                        numero_rs_ds=fila[5], 
                                        tipo_tramite=fila[6],
                                        concersionario=fila[7],
                                        tipo_vigencia=fila[8])
            instancia_concesion.save()

    
    
        return HttpResponse(datos_tabla)
         
    except Exception as exception:
        return HttpResponse('[ERROR] ' + f'{exception.__class__.__name__}: {exception}')
    
    finally:
        browser.quit()

    

