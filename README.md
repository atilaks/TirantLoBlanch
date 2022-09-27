### TirantLoBlanch

## Objetivo
El objetivo de esta herramienta de Web Scrapyng es extraer los valores de fecha y título en el portal de contratación de Navarra para datos de tipo acuerdo en el año 2020.

## Herramientas 
Se ha hecho uso de bibliotecas como "requests" y "BeautifulSoup" para la extracción de datos, y de la biblioteca "json" para la modelización de un archivo tipo JSON. 

## Contenido
  - WebExtractor: Se ocupa de extraer el enlace y modelizarlo con un archivo tipo BeautifulSoup para poder trabajar.
  - ContentExtractor: Se ocupa de extraer el contenido de la página objetivo. En este caso fecha y título.
  - Tracker: Función main que coordina las funciones para extraer un archivo final de tipo JSON.
  - agreements_2020: Resultado (output) de la herramienta con los datos de los acuerdos de 2020.
  
## Propuesta de mejora
  - Creación de una hoja de estilo para dar un formato más amigable al archivo final "agreements_2020".
  
## Comentarios
  - La documentación se ha sido escrita en castellano, ya que su ámbito de aplicación es para un entorno de trabajo de habla hispana.
  - El código se ha creado para un caso concreto. Por lo que no es estandarizable, no siendo útil para cualquier entorno que no comparta la hoja HTML sobre la que se trabaja.
  - Se ha utilizado la versión 3.9 de Python.
