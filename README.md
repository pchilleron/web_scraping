# web_scraping
M2.851 Tipología y ciclo de vida de los datos

Práctica 1

Pablo Chillerón Beviá
Evgeny Muzarev Gevorgian


Scraping de booking.com

Primera aproximación.

Ejecutar main.py en PyCharm o booking_scrap1.ipynb en jupyter notebook.

El script tarda en ejecutarse 2-3 minutos, hay que tener un poco de paciencia. Al terminar, mostrará la dimensión del dataframe resultante y creará fichero booking.csv en el mismo directorio.

Lo que hace este script es extraer los resultados de la búsqueda en booking.com: Benidrom, 1º quincena de agosto(1/08/2022 - 15/08/2022) de 2022, 2 adultos sin niños.

Se extraen y se guardan en un dataframe los siguientes campos: Name(nombre del hotel/apartamento), Stars(nº de estrellas), From_Centre(la distancia del centro en km), From_Beach(la distancia de la playa en km), Reviews(nº de reviews), Rating, Comfort(el nivel de confort), Img(link a la imagen) y Price(el precio en euros).

Aquellos valores que por algún motivo no se han podido extraer, se sustituyen por NaN.

Luego, se guarda este dataframe en formato .csv(booking.csv).

Con cada ejecución se carga diferente número de registros(resultados). De momento, no se entiende porqué.
