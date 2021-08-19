# MCOC2021-P0

# Mi computador principal 

* Marca/modelo: HP OMEN 15-EN0002LA
* Tipo: Notebook
* Año adquisición: 2021
* Procesador:
  * Marca/Modelo: AMD Ryzen 7 4800H
  * Velocidad Base: 2.90 GHz
  * Velocidad Máxima: 4.20 GHz
  * Numero de núcleos: 8 
  * Numero de hilos: 16
  * Arquitectura: x86_64
  * Set de instrucciones: AMD64
* Tamaño de las cachés del procesador
  * L1: 512 KB
  * L2: 4.0 MB
  * L3: 8.0 MB
* Memoria 
  * Total: 16 GB
  * Tipo memoria: DDR4
  * Velocidad 3200 MHz
  * Numero de (SO)DIMM: 2
* Tarjeta Gráfica
  * Marca / Modelo: NVIDIA GeForce RTX 2060 
  * Memoria dedicada: 6.0 GB
  * Resolución: 1920 x 1080
* Disco 1: 
  * Marca: Western Digital
  * Tipo: SSD
  * Tamaño: 512 GB
  * Particiones: 1
  * Sistema de archivos: NTFS
  
* Dirección MAC de la tarjeta wifi: 90:0F:0C:42:F6:3D
* Dirección IP (Interna, del router): 192.168.1.106
* Dirección IP (Externa, del ISP): 190.161.68.7
* Proveedor internet: VTR Banda Ancha S.A.

# Desempeño MATMUL

A continuación se muestra el gráfico de rendimiento de la funcion matmul:

   ![Desempeño codigo](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/plot.png)
* **Preguntas:**
* ¿Cómo difiere del gráfico del profesor/ayudante?
  * R: El gráfico del profesor logra correr una matriz de tamaño 10000 en aproximadamente 10-20 segundos, mientras que en mi caso lo máximo que llego a correr es una matriz de tamaño 8000 en aproximadamente 65 segundos. El comportamiento de la curva superior es similar, es decir ambas poseen saltos aleatorios a medida que aumenta el tamaño N. La curva inferior es identica ya que el uso de memoria es el mismo independiente del computador y sus capacidades. Ademas esta la diferencia en memorias RAM de cada computador.

* ¿A qué se pueden deber las diferencias en cada corrida?
  * R: A diversos factores propios del computador usado, entre ellos el uso externo a SublimeText que se le esta dando al computador (Chrome, jugar, etc), la temperatura que alcanza el equipo en cada corrida puede ir aumentando generando posibles diferencias entre las corridas y los tiempos de estas. 

* El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
  * R: Porque al aumentar el tamaño de la matriz, estos datos se deben ir guardando en memoria y este aumento es lineal, ya que solo se guardan los valores. En cambio al aumentar el tamaño, las operaciones que debe hacer el computador no aumentan de manera lineal. Es por esto que las multplicaciones de matrices muy grandes demoran bastante. En otras palabras, la memoria que utiliza una matriz del doble de N equivale al doble de uso de memoria, sin embargo, una matriz con el doble de tamaño al realizar la multiplicación la cantidad de operaciones a realizar no es el doble, es un numero considerablemente mayor. Es por esto la no-linealidad del grafico superior.

* ¿Qué versión de python está usando?
  * R: Python 3.9.6

* ¿Qué versión de numpy está usando?
  * R: NumPy 1.21.1

* Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen (screenshot) de su uso de procesador durante alguna corrida para confirmar.
  * R: Se utilizan los 4 procesadores del notebook. Se puede ver como la CPU llega a una capacidad del 86%.
  
    ![Desempeño codigo](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/Screenshot%20CPU.PNG)

# Desempeño de INV

Para esta entrega se realizó un código para cada uno de los 12 casos pedidos. Cada código genera un archivo txt en donde se guarda la información correspondiente a 10 corridas del cálculo de la inversa de una matriz de tamaño N. Se utilizaron varios tamaños de N, en donde el máximo fue de 10000.

Se crearon 4 gráficos, cada uno representa un tipo de dato con sus 3 métodos de obtención de la inversa. 

* Caso half: Para el tipo de dato half, el método numpy no logra correr el código, el procesador no es capaz de trabjar con un float16 ni tampoco le hace un "upgrade" a float 32. En cuanto a los casos del método Scipy, en uso de memoria son idénticos. En cuanto a tiempo transcurrido se ve una pequeña diferencia, en donde al utilizar overwrite = True, el método logra generar la inversa con mayor rapidez. Esta tendencia se mantiene para todo el rango del tamaño N de la matriz. 

   ![plot_half](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/plot_half.png)


* Caso single: Para el tipo de dato single, los 3 métodos logran correr el código. En cuanto a memoria se mantiene idéntica para los 3 casos. En cuanto al tiempo transcurrido, ambos métodos scipy se ven muy similares, sin embargo el método numpy destaca ya que para el rango del tamaño de matrix N entre 50 y 500 posee osicilaciones bruscas en cuanto al tiempo de inversión. En casos es más rapido que Scipy y en casos es más lento. Ahora mirando el punto final donde N = 10000, se ve que el método más rápido fue Scipy con overwrite = True. 

   ![plot_single](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/plot_single.png)


* Caso double: Para el tipo de dato double, los 3 métodos logran correr el código. En cuanto a memoria se mantiene idéntica para los 3 casos. En cuanto al tiempo transcurrido, el método más rápido fue numpy, seguido de Scipy con overwrite = True. Se observan el mismo comportamiento aleatorio que para el caso anterior en un rango específico de N para el método Numpy. 

   ![plot_double](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/plot_double.png)


* Caso longdouble: Para el tipo de dato longdouble, el método numpy no logra correr el código. En cuanto a los casos del método Scipy se nota una mayor rapidez para el caso overwrite = True.

   ![plot_longdouble](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/plot_longdouble.png)
   
**Monitoreo del Computador**

En cuanto al uso de CPU, se ve como al correr el código se utiliza entre el 85% y el 100% de esta. Esto se repite para todos los casos.

   ![CPU caso1_single](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/Screenshot%20CPU%20caso1_single.png)
   ![CPU caso1_double](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/Screenshot%20CPU%20caso1_double.png)

En cuanto al uso de memoria RAM este oscilaba entre 5 a 7 GB para todos los casos

   ![RAM caso3_half](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/Screenshot%20RAM%20caso3_half.png)
   
   
¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)? Justifique claramente su respuesta. 
  * R: El método Scipy utiliza de soporte a los paquetes BLAS/LAPACK para compilar, los cuales mediante factoriación LU resuelven la inversa. El método Numpy va a depender de su instalación, para el caso Numpy funciona llamando a Scipy que luego hace la previamente explicado.

¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? Justifique su comentario en base al uso de procesadores y memoria observado durante las corridas.
  * R: El paralelismo indica que se pueden ejecutar tareas simultaneas en los distintos núcleos del procesador. Y la estructura de caché y su capacidad en memoria van a ser factores indicentes en la velocidad de procesamiento, ya que el acceso a memoria en cada nivel es considerablemente más rápido que por ejemplo acceder a datos de la RAM o del Disco Duro. Durante la corrida se muestran 16 CPU's trabajando en simultaneo al 100%. 

Conclusiones: el método Numpy tiene limitaciones en cuanto al uso de datos que utiliza, por el otro lado Scipy no tuvo estos límites para los 4 casos pedidos. Utilizar overwrite = True fue beneficioso en todos los casos en cuanto al tiempo de inversión. 

