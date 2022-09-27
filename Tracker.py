import json
from ContentExtractor import ContentExtractor
from WebExtractor import WebExtractor

"""
Variables:
    - incomplete_url: URL sin el identificativo final de página.
    - website_content: Array con los datos sacados de la página web.

El método principal comienza recorriendo un bucle FOR mediante un objeto
de tipo BeautifulSoup (soup), el cual va cambiando a cada vuelta, 
provocando un salto de página. Tras cada vuelta, además, registra los 
datos sacados en la variable "website_content".

En la segunda parte se construye el objeto JSON desde la variable "file",
la cual es un diccionario con la key "contents" y como value los registros
exportados. Utilizo la biblioteca de json para dar formato a la variable 
"json_file".

Finalmente se construye un archivo de tipo .json, abriendo el archivo, 
escribiendo y cerrándolo, en el cual se pueden observar los registros de
tipo fecha y título de los acuerdos de 2020 ("agreements_2020.json").

*Me he ceñido a la petición de recorrer 4 páginas, aunque cabe destacar 
que el apartado "Acuerdos 2020" dispone de 6.
"""

if __name__ == "__main__":
    incomplete_url = 'https://portalcontratacion.navarra.es/es/acuerdos-2020?p_p_id=com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_BbD7OO7VreZ1&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_BbD7OO7VreZ1_delta=20&p_r_p_resetCur=false&_com_liferay_asset_publisher_web_portlet_AssetPublisherPortlet_INSTANCE_BbD7OO7VreZ1_cur='
    website_content = []

    for page in range(4):
        soup = WebExtractor(incomplete_url, page)
        website_content.extend(ContentExtractor(soup))

    file = {"contents": website_content}
    json_file = json.dumps(file)

    file = open("agreements_2020.json", "w")
    file.write(json_file)
    file.close()
