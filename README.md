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


* Caso double: Para el tipo de dato double, los 3 métodos logran correr el código. En cuanto a memoria se mantiene idéntica para los 3 casos. En cuanto al tiempo transcurrido, el método más rápido fue Numpy, seguido de Scipy con overwrite = True. Se observan el mismo comportamiento aleatorio que para el caso anterior en un rango específico de N para el método Numpy. 

   ![plot_double](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/plot_double.png)


* Caso longdouble: Para el tipo de dato longdouble, el método numpy no logra correr el código. En cuanto a los casos del método Scipy se nota una mayor rapidez para el caso overwrite = True.

   ![plot_longdouble](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/plot_longdouble.png)
   
**Monitoreo del Computador**

En cuanto al uso de CPU, se ve como al correr el código se utiliza entre el 85% y el 100% de esta. Esto se repite para todos los casos.

   ![CPU caso1_single](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/Screenshot%20CPU%20caso1_single.png)
   ![CPU caso1_double](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/Screenshot%20CPU%20caso1_double.png)

En cuanto al uso de memoria RAM este oscilaba entre 5 a 7 GB para todos los casos

   ![RAM caso3_half](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/Screenshot%20RAM%20caso3_half.png)
   
**Tamaños de Memoria**   

Para el caso de matriz con N = 10000 se tienen los siguientes valores de bytes utilizados en memoria para cada tipo de dato:
* Data Type "Half":       600000000 bytes
* Data Type "Single":     800000000 bytes 
* Data Type "Double":     1600000000 bytes
* Data Type "Longdouble": 1600000000 bytes

Aqui se nota como el dato longdouble fue descendido automáticamente por el computador a double, generando que su uso en memoria sea menor y su tiempo de procesamiento mayor.
   
**Preguntas**

¿Qué algoritmo de inversión cree que utiliza cada método (ver wiki)? Justifique claramente su respuesta. 
  * R: El método Scipy utiliza de soporte a los paquetes BLAS/LAPACK para compilar, los cuales mediante factoriación LU resuelven la inversa. El método Numpy va a depender de su instalación, para el caso Numpy funciona llamando a Scipy que luego hace la previamente explicado.

¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño en cada caso? Justifique su comentario en base al uso de procesadores y memoria observado durante las corridas.
  * R: El paralelismo indica que se pueden ejecutar tareas simultáneas en los distintos núcleos del procesador. Y la estructura de caché y su capacidad en memoria van a ser factores indicentes en la velocidad de procesamiento, ya que el acceso a memoria en cada nivel es considerablemente más rápido que por ejemplo acceder a datos de la RAM o del Disco Duro. Durante la corrida se muestran 16 CPU's trabajando en simultáneo al 100%. 

**Conclusiones**: el método Numpy tiene limitaciones en cuanto al uso de datos que utiliza, por el otro lado Scipy no tuvo estos límites para los 4 casos pedidos. Utilizar overwrite = True fue beneficioso en todos los casos en cuanto al tiempo de inversión. 

# Entrega 4: Desempeño de SOLVE y EIGH

Luego de ver los gráficos generados para la funcion SOLVE, existe una notoria diferencia en los tiempos de procesamiento. Para el caso del tipo de dato float32 se obtuvo que el método más rapido fue utilizando la funcion scipy.linalg.solve con assume_a="pos", y por el contrario el método en promedio más lento fue el proceso manual de obtener la inversa mediante scipy y luego multiplicarla por la matriz b. Mirando el gráfico se ven saltos aleatorios para el caso scipy.linalg.solve con assume_a="sym", mientras que para los demás métodos se nota una mayor homogeneidad en los tiempos de resolución. Para los tamaños N de matriz entre 10 y 1000 el método scipy.linalg.solve con assume_a="pos" es superior en rapidez al resto por una gran diferencia. 

![](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/Entrega%204/Plot%20Solve%20Float32.png)

Para el caso SOLVE pero con tipo de dato float64 se observa el mismo comportamiento descrito anteriormente, pero ahora con una mayor notoriedad en la lentidud del método x=inv(A)xb en comparación a los demás. Los tiempos aumentaron para todos los casos debido a usar un tipo de dato que utiliza más memoria, y por ende toma más tiempo de procesamiento.

![](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/Entrega%204/Plot%20Solve%20Float64.png)

Para el problema de encontrar valores y vectores propios se utilizó la funcion scipy.linalg.eigh con diferentes atributos en cada caso. Para el tipo de dato float32 los casos más rápidos fueron el caso III con overwrite_a=False y con overwrite_a=True. El caso eigh por defecto viene despues muy cercano. Luego el método que posee una considerable diferencia en tiempo fue el caso V. Se puede observar un gran salto en los tiempos de procesamiento entre los tamaños de matriz 20 y 50 para todos los métodos.

![](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/Entrega%204/Plot%20Eigh%20Float32.png)

Para EIGH con tipo de dato float64 se repite el mismo análisis y comportamiento de las curvas descrito anteriormente que para float32, con la salvedad de que los tiempos en general son mayores debido al cambio del tipo de dato. 

![](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/Entrega%204/Plot%20Eigh%20Float64.png)

**Rendimiento**

En cuanto al rendimiento para los casos A de resolver un sistema lineal, la CPU trabajo constantemente a su máxima capacidad durante las corridas. A continuación se muestra una captura del monitoreo: 

![](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/Entrega%204/Screenshot%20CPU%20Solve_%20caso2_float64.png)

Para el caso B del método EIGH se observó un comportamiento distinto y complejo. A continuación se muestra la CPU trabajando para el caso 1 de eigh para float32, Se ven saltos en cuanto al uso de procesador, no siempre estuvo trabajando a su máxima capacidad. 

![](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/Entrega%204/Screenshot%20CPU%20Eigh_caso1_float32.png)

Para el caso II de Eigh con overwrite_a=True y float32 se obtuvo el siguiente rendimiento, en el cual el procesador oscilaba entre un 5% y 20% de su capacidad. Y se observa que algunos nucleos a ratos daban saltos que los demas no hacian.

![](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/Entrega%204/Screenshot%20CPU%20Eigh_caso2_overwrite_True_float32.png)

El caso III de Eigh overwrite_a=False y float32 tuvo oscilaciones bruscas entre el 20% y 100% de la capacidad de la CPU. Para el caso IV se repite lo mismo. 

![](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/Entrega%204/Screenshot%20CPU%20Eigh_caso3_overwrite_False_float32.png)

El caso V de Eigh tuvo un comportamiento peculiar. Se mantuvo a ratos en capacidades muy bajas con algunos saltos de vez en cuando al operar las matrices de mayor tamaño. Su uso no fue parejo en todos los procesadores como lo fue en los casos anteriores. A continuacion se muestra el monitoreo para el caso V con overwrite=False para float64, seguido del caso V con overwrite=True para float32.

![](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/Entrega%204/Screenshot%20CPU%20Eigh_caso5_overwrite_False_float64.png)
![](https://github.com/VicenteOtaegui/MCOC2021-P0/blob/main/Entrega%204/Screenshot%20CPU%20Eigh_caso5_overwrite_True_float32.png)

En cuanto al uso de RAM en todos los casos oscilaba entre 5GB y 8 GB, por lo que no fue un factor determinante ni limitante para correr el programa. 



