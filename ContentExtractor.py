"""
EXTRACTOR DE CONTENIDO

Recibiendo como parámetro el resultado de WebExtractor
(soup). Toma como raíz de búsqueda el resultado de "root_items".

Teniendo como referencia la raíz de objetos, recorre con un bucle,
inspeccionando los valores de título y fecha mediante el uso de anclas. 
Después de cada vuelta registra los dos valores en la lista.

Devuelve los valores de título y fecha almacenados en un array
inicializado al principio de la función ("clean_data")
"""

def ContentExtractor(soup):
    root_items = soup.find_all("div", class_="asset-full-content clearfix mb-5 no-title")
    clean_data = []
    for root in root_items:
        title_value = root.find('h2').get_text()
        date_value = root.findAll("input", class_="field form-control")[2].get('value')
        clean_data.append({"date":date_value, "title":title_value})
    return clean_data