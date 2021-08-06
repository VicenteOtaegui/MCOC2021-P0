# MCOC2021-P0

# Mi computador principal 

* Marca/modelo: ASUS R510IU-DM023T 
* Tipo: Notebook
* Año adquisición: 2018
* Procesador:
  * Marca/Modelo: AMD FX-9830P
  * Velocidad Base: 3.00 GHz
  * Velocidad Máxima: 3.70 GHz
  * Numero de núcleos: 4 
  * Numero de hilos: 4
  * Arquitectura: x86_64
  * Set de instrucciones: FMA4
* Tamaño de las cachés del procesador
  * L1: 2 x 96 KB 3-way set associative shared instruction caches
        4 x 32 KB 8-way set associative data caches
  * L2: 2 x 1 MB 16-way set associative shared caches
  * L3: None
* Memoria 
  * Total: 12 GB
  * Tipo memoria: DDR4
  * Velocidad 2133 MHz
  * Numero de (SO)DIMM: 4
* Tarjeta Gráfica
  * Marca / Modelo: AMD RADEON RX 560 Series
  * Memoria dedicada: 2048 MB
  * Resolución: 1920 x 1080
* Disco 1: 
  * Marca: SK Hynix
  * Tipo: SSD
  * Tamaño: 128GB
  * Particiones: 1
  * Sistema de archivos: NTFS
* Disco 2: 
  * Marca: Samsung
  * Tipo: HDD
  * Tamaño: 750GB
  * Particiones: 1
  * Sistema de archivos: NTFS
  
* Dirección MAC de la tarjeta wifi: F0:03:8C:D8:84:B1
* Dirección IP (Interna, del router): 192.168.1.110
* Dirección IP (Externa, del ISP): 190.161.68.7
* Proveedor internet: VTR Banda Ancha S.A.

# Desempeño MATMUL

![Desempeño codigo](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/plot.png)
* **Preguntas:**
* ¿Cómo difiere del gráfico del profesor/ayudante?
  * R: El gráfico del profesor logra correr una matriz de tamaño 10000 en aproximadamente 10-20 segundos, mientras que en mi caso lo máximo que llego a correr es una matriz de tamaño 8000 en aproximadamente 65 segundos. El comportamiento de la curva superior es similar, es decir ambas poseen saltos aleatorios a medida que aumenta el tamaño N. La curva inferior es identica ya que el uso de memoria es el mismo independiente del computador y sus capacidades. Ademas esta la diferencia en memorias RAM de cada computador.

* ¿A qué se pueden deber las diferencias en cada corrida?
  * R: A diversos factores propios del computador usado, entre ellos el uso externo a SublimeText que se le esta dando al computador (Chrome, jugar, etc), la temperatura que alcanza el equipo en cada corrida puede ir aumentando generando posibles diferencias entre las corridas y los tiempos de estas. 

* El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
  * R: Porque al aumentar el tamaño de la matriz, estos datos se deben ir guardando en memoria y este aumento es lineal, ya que solo se guardan los valores. En cambio al aumentar el tamaño, las operaciones que debe hacer el computador no aumentan de manera lineal. Es por esto que las multplicaciones de matricez muy grandes demoran bastante. En otras palabras, la memoria que utiliza una matriz del doble de N equivale al doble de uso de memoria, sin embargo, una matriz con el doble de tamaño al realizar la multiplicación la cantidad de operaciones a realizar no es el doble, es un numero considerablemente mayor. Es por esto la no-linealidad del grafico superior.

* ¿Qué versión de python está usando?
  * R: Python 3.9.6

* ¿Qué versión de numpy está usando?
  * R: NumPy 1.21.1

* Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen (screenshot) de su uso de procesador durante alguna corrida para confirmar.
  * R: Se utilizan los 4 procesadores del notebook. Se puede ver como la CPU llega a una capacidad del 86%.
    ![Desempeño codigo](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/Screenshot%20CPU.PNG)


