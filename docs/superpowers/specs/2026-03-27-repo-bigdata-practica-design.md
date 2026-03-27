# Spec: Repositorio de Practica Big Data — BIY7131 DUOC

**Fecha:** 2026-03-27
**Estado:** Aprobado por el docente
**Contexto:** Repositorio para que los alumnos de Big Data (BIY7131, DUOC) puedan practicar localmente con PySpark, Kafka, Hive y Jupyter, complementando los labs de Google Cloud Skills Boost.

---

## 1. Problema

El curso BIY7131 se apoya en Google Cloud Skills Boost para laboratorios, pero los alumnos no pueden experimentar libremente fuera de esas sesiones. No tienen un entorno local donde practicar Spark, streaming, SQL distribuido ni pipelines ETL. El nivel tecnico es variado (desde principiantes en Python hasta intermedios) y las maquinas son mayoritariamente Windows con RAM limitada.

## 2. Solucion

Repositorio Git con entorno Docker Compose multi-servicio que los alumnos clonan y levantan localmente. Incluye notebooks de practica alineados a las 3 Experiencias de Aprendizaje (EA) del curso, datasets, documentacion teorica, y scripts de utilidad.

## 3. Enfoque: Docker Compose Multi-Servicio

### 3.1 Servicios

| Servicio | Imagen base | Perfil | Puerto |
|----------|------------|--------|--------|
| jupyter-spark | jupyter/pyspark-notebook:spark-3.5 | basico | 8888 |
| spark-master | bitnami/spark:3.5 | basico | 8080 |
| spark-worker | bitnami/spark:3.5 | basico | 8081 |
| zookeeper | bitnami/zookeeper:3.9 | completo | 2181 |
| kafka | bitnami/kafka:3.7 | completo | 9092 |
| hive-metastore | apache/hive:4.0 | completo | 9083 |
| hive-server | apache/hive:4.0 | completo | 10000 |
| postgres | postgres:16-alpine | completo | 5432 |

### 3.2 Perfiles

- **basico** (~2-3 GB RAM): jupyter-spark + spark-master + spark-worker. Suficiente para EA1 y EA2.
- **completo** (~6-8 GB RAM): todo lo anterior + Kafka + Zookeeper + Hive + PostgreSQL. Necesario para EA3 y Hive.

### 3.3 Compatibilidad

Todas las imagenes soportan linux/amd64 y linux/arm64:
- Windows (Docker Desktop con WSL2)
- Mac Intel y Apple Silicon
- Linux (Docker Engine)

### 3.4 Volumenes

```
./notebooks          -> /home/jovyan/notebooks
./notebooks_resueltos -> /home/jovyan/notebooks_resueltos  (solo lectura)
./datos              -> /home/jovyan/datos
./scripts            -> /home/jovyan/scripts
```

### 3.5 Variables de entorno (.env)

```
SPARK_WORKER_MEMORY=2g
SPARK_WORKER_CORES=2
JUPYTER_TOKEN=bigdata2026
KAFKA_BROKER_ID=1
POSTGRES_PASSWORD=hive_metastore
```

## 4. Estructura del Repositorio

```
proyecto_big_data/
├── README.md
├── GUIA_INSTALACION.md
├── docker-compose.yml
├── .env.example
├── .gitignore
│
├── docker/
│   ├── jupyter-spark/
│   │   ├── Dockerfile
│   │   └── requirements.txt
│   ├── kafka/
│   │   └── (customizacion si es necesaria)
│   └── hive/
│       └── (customizacion si es necesaria)
│
├── docs/
│   ├── temas/                         # 12 temas PDF de Manuel Padilla
│   │   ├── Tema_01_Introduccion_tecnologias_BigData.pdf
│   │   ├── Tema_02_HDFS_y_MapReduce.pdf
│   │   ├── Tema_03_Spark_I.pdf
│   │   ├── Tema_04_Spark_II.pdf
│   │   ├── Tema_05_Spark_III.pdf
│   │   ├── Tema_06_Apache_Kafka.pdf
│   │   ├── Tema_07_Hive_e_Impala.pdf
│   │   ├── Tema_08_Cloud_Computing_Conceptos.pdf
│   │   ├── Tema_09_Cloud_Computing_Azure.pdf
│   │   ├── Tema_10_Cloud_Computing_AWS.pdf
│   │   ├── Tema_11_Cloud_Computing_GCP.pdf
│   │   └── Presentacion_asignatura.pdf
│   ├── guias/
│   │   ├── despliegue_cluster_gcp.pdf
│   │   └── guia_visualizacion.pdf
│   └── referencias/
│       └── labs_google_skillsboost.md
│
├── datos/
│   ├── flights.csv
│   ├── sales.csv
│   ├── stores.csv
│   ├── netflix_titles.csv
│   ├── ufo_sightings.xlsx
│   ├── cartas_magic.csv
│   └── streaming/                     # Datos para streaming (generados)
│
├── notebooks/                         # Version alumno (con ejercicios)
│   ├── EA1_fundamentos/
│   │   ├── 01_introduccion_spark.ipynb
│   │   ├── 02_rdds_basico.ipynb
│   │   ├── 03_dataframes_intro.ipynb
│   │   └── 04_arquitecturas_bigdata.ipynb
│   ├── EA2_etl_batch/
│   │   ├── 01_ingesta_datos.ipynb
│   │   ├── 02_transformacion_limpieza.ipynb
│   │   ├── 03_spark_sql.ipynb
│   │   ├── 04_hive_metastore.ipynb
│   │   ├── 05_machine_learning_spark.ipynb
│   │   └── 06_visualizacion_datos.ipynb
│   ├── EA3_tiempo_real/
│   │   ├── 01_kafka_introduccion.ipynb
│   │   ├── 02_ingesta_tiempo_real.ipynb
│   │   ├── 03_spark_structured_streaming.ipynb
│   │   └── 04_dashboard_tiempo_real.ipynb
│   └── extras/
│       ├── actividad_vuelos.ipynb
│       ├── actividad_ventas.ipynb
│       ├── actividad_netflix.ipynb
│       ├── actividad_avistamientos.ipynb
│       └── actividad_cartas_magic.ipynb
│
├── notebooks_resueltos/               # Version docente (soluciones completas)
│   ├── EA1_fundamentos/
│   ├── EA2_etl_batch/
│   ├── EA3_tiempo_real/
│   └── extras/
│
└── scripts/
    ├── generar_datos_streaming.py
    ├── verificar_entorno.py
    ├── reset_entorno.sh
    └── reset_entorno.bat
```

## 5. Notebooks — Contenido detallado

### 5.1 EA1: Fundamentos (4 notebooks)

**01_introduccion_spark.ipynb**
- Que es Spark, arquitectura master/worker, SparkSession
- Leer CSV, show(), printSchema(), count()
- select(), filter(), operaciones basicas
- Dataset: flights.csv
- Ejercicios: leer datos, explorar schema, filtrar vuelos

**02_rdds_basico.ipynb**
- RDDs vs DataFrames, cuando usar cada uno
- Crear RDDs desde listas y archivos
- map(), filter(), reduce(), collect()
- Transformaciones lazy vs acciones
- persist() y cache()
- Dataset: flights.csv
- Ejercicios: transformaciones sobre RDDs, comparar rendimiento

**03_dataframes_intro.ipynb**
- Crear DataFrames, select, filter, withColumn
- groupBy + agg (sum, avg, count, min, max)
- Joins entre DataFrames
- Funciones de fecha (year, month, dayofweek)
- Columnas derivadas con when/otherwise
- Dataset: sales.csv + stores.csv
- Ejercicios: joins, agrupaciones, columnas calculadas

**04_arquitecturas_bigdata.ipynb**
- Notebook conceptual/interactivo
- Arquitectura Lambda vs Kappa (diagramas en markdown)
- Batch vs Streaming: cuando usar que
- Ecosistema Hadoop: HDFS, YARN, MapReduce
- Ecosistema moderno: Spark, Kafka, Hive
- On-premise vs Cloud
- Ejercicios: preguntas de analisis y diseño

### 5.2 EA2: ETL Batch (6 notebooks)

**01_ingesta_datos.ipynb**
- Leer CSV con opciones (header, inferSchema, delimiter, encoding)
- Leer JSON (single-line y multi-line)
- Leer Parquet
- Definir schemas manualmente (StructType)
- Manejo de datos corruptos (mode: PERMISSIVE, DROPMALFORMED, FAILFAST)
- Datasets: flights.csv, netflix_titles.csv, ufo_sightings (convertido a CSV)
- Ejercicios: leer multiples formatos, comparar schemas

**02_transformacion_limpieza.ipynb**
- Manejo de nulls: dropna(), fillna(), isNull()
- Eliminar duplicados: dropDuplicates()
- Cast de tipos: cast(), to_date(), to_timestamp()
- UDFs (User Defined Functions)
- when/otherwise para logica condicional
- Merge de multiples fuentes
- Dataset: sales.csv + stores.csv
- Ejercicios: limpiar dataset sucio, normalizar, mergear

**03_spark_sql.ipynb**
- createOrReplaceTempView()
- Queries SQL sobre DataFrames
- Subqueries y CTEs
- Window functions: ROW_NUMBER, RANK, LAG, LEAD
- Agregaciones avanzadas
- Dataset: sales.csv + stores.csv
- Ejercicios: queries progresivos de facil a complejo

**04_hive_metastore.ipynb** (requiere perfil completo)
- Conectar SparkSession a Hive metastore
- Crear bases de datos y tablas persistentes
- Tablas externas vs gestionadas
- Formato Parquet y particionamiento
- Consultas SQL sobre tablas Hive
- Dataset: flights.csv
- Ejercicios: crear tablas, insertar datos, consultar

**05_machine_learning_spark.ipynb**
- Pipeline de ML en Spark
- StringIndexer para variables categoricas
- VectorAssembler para features
- Binarizer para target binario
- DecisionTreeClassifier
- Evaluacion: accuracy, confusion matrix
- CrossValidator para hiperparametros
- Dataset: flights.csv (predecir retrasos)
- Ejercicios: construir pipeline, evaluar, mejorar modelo

**06_visualizacion_datos.ipynb**
- .toPandas() para conversion
- matplotlib: barras, lineas, histogramas
- seaborn: heatmaps, pairplots, boxplots
- Analisis visual de distribuciones y correlaciones
- Series temporales
- Dataset: sales.csv + stores.csv
- Ejercicios: crear visualizaciones especificas, interpretar resultados

### 5.3 EA3: Tiempo Real (4 notebooks)

**01_kafka_introduccion.ipynb** (requiere perfil completo)
- Conceptos: topics, particiones, producers, consumers, offsets
- Crear topics desde Python (kafka-python o confluent-kafka)
- Producir mensajes simples
- Consumir mensajes
- Ejercicios: crear topic, enviar y leer mensajes

**02_ingesta_tiempo_real.ipynb** (requiere perfil completo)
- Usar generar_datos_streaming.py como productor
- Tipos de datos: transacciones, logs, IoT
- Monitorear topic con consumer
- Verificar formato y contenido de mensajes
- Ejercicios: generar stream, consumir, analizar estructura

**03_spark_structured_streaming.ipynb** (requiere perfil completo)
- readStream desde Kafka
- Schema de mensajes Kafka (key, value, timestamp)
- Parsear JSON del value
- Agregaciones en ventanas (window, watermark)
- Modos de output: append, complete, update
- writeStream a consola y Parquet
- Ejercicios: crear pipeline streaming, agregar por ventana

**04_dashboard_tiempo_real.ipynb** (requiere perfil completo)
- Leer resultados de streaming procesados
- Visualizar con matplotlib en celdas que se refrescan
- Agregaciones acumuladas
- Metricas en tiempo real
- Ejercicios: crear panel con metricas clave

### 5.4 Extras (5 notebooks)

Actividades complementarias basadas en los datasets existentes. Cada una es autocontenida y puede usarse como tarea o practica adicional.

| Notebook | Habilidades practicadas |
|----------|------------------------|
| actividad_vuelos | Transformaciones, pivoting, Pipeline ML |
| actividad_ventas | SQL analytics, correlaciones, joins |
| actividad_netflix | EDA, filtrado por genero/pais/anio |
| actividad_avistamientos | Limpieza de datos, parsing de fechas, tendencias |
| actividad_cartas_magic | Estadisticas descriptivas, agrupaciones, filtros |

### 5.5 Formato de notebooks

**Version alumno:**
- Celda titulo + objetivos de aprendizaje
- Celda setup (imports, SparkSession)
- Bloques alternados: explicacion → ejemplo resuelto → ejercicio vacio con TODO
- Celda resumen
- Celda desafio extra (opcional)

**Version docente (notebooks_resueltos/):**
- Identico al alumno pero con soluciones completas
- Comentarios pedagogicos adicionales
- Outputs esperados visibles

## 6. Datasets

### 6.1 Existentes (a copiar al repo)

| Archivo | Origen | Tamano | Registros |
|---------|--------|--------|-----------|
| flights.csv | Manuel Padilla | 9.9 MB | 162,050 |
| sales.csv | Manuel Padilla | 13 MB | 421,570 |
| stores.csv | Manuel Padilla | 577 B | 45 |
| netflix_titles.csv | Curso DUOC | ~2 MB | ~8,800 |
| ufo_sightings.xlsx | Curso DUOC | variable | variable |
| cartas_magic.csv | Curso DUOC | variable | variable |

### 6.2 Nuevos (a generar para streaming)

Script `generar_datos_streaming.py` genera 3 tipos de eventos:

**Transacciones:**
```json
{"id": "tx_001", "timestamp": "2026-03-27T10:30:00", "monto": 45200, "tienda_id": 12, "producto": "Laptop", "metodo_pago": "tarjeta_credito"}
```

**Logs de servidor:**
```json
{"timestamp": "2026-03-27T10:30:01", "ip": "192.168.1.45", "endpoint": "/api/productos", "method": "GET", "status_code": 200, "response_time_ms": 145}
```

**Sensores IoT:**
```json
{"sensor_id": "sensor_042", "timestamp": "2026-03-27T10:30:02", "temperatura": 23.5, "humedad": 65.2, "ubicacion": "bodega_norte"}
```

## 7. Documentacion

### 7.1 README.md
- Descripcion, requisitos, inicio rapido (3 comandos)
- Estructura del repo explicada
- Guia por EA (que levantar, que notebooks abrir)
- FAQ y solucion de problemas comunes
- Contacto docente

### 7.2 GUIA_INSTALACION.md
- Paso a paso para Windows, Mac y Linux
- Instalacion Docker Desktop
- Clonar repo, configurar .env
- Levantar perfiles
- Verificar entorno
- Configuracion de recursos Docker

### 7.3 docs/temas/
- 12 PDFs teoricos de Manuel Padilla copiados al repo

### 7.4 docs/guias/
- Despliegue cluster GCP (PDF)
- Guia de visualizacion (PDF)

### 7.5 docs/referencias/labs_google_skillsboost.md
- Tabla de mapeo: notebook del repo ↔ lab de Google Skills Boost (codigo GSP)

## 8. Scripts

### 8.1 verificar_entorno.py
Ejecutar dentro de JupyterLab. Verifica:
- SparkSession se crea correctamente
- Puede leer flights.csv
- Puede hacer groupBy/agg
- Puede escribir/leer Parquet
- [perfil completo] Kafka accesible
- [perfil completo] Hive metastore accesible
- Librerias Python instaladas
- Output: reporte con checkmarks por verificacion

### 8.2 generar_datos_streaming.py
- Argumentos: --tipo (transacciones|logs|iot), --velocidad (eventos/seg), --kafka-topic, --duracion
- Genera datos aleatorios realistas
- Envia a Kafka o escribe a archivo

### 8.3 reset_entorno.sh / reset_entorno.bat
- Para contenedores, borra volumenes, reinicia limpio
- Versiones para Unix y Windows

## 9. Validacion y Testing

Cada notebook sera validado para asegurar que:
- Todas las celdas ejecutan sin error en el entorno Docker
- Los imports funcionan (pyspark, pandas, matplotlib, seaborn)
- Los paths a datasets son correctos (/home/jovyan/datos/...)
- Los ejercicios resueltos producen output coherente
- Las conexiones a Kafka y Hive funcionan en perfil completo
- Funciona identico en Windows (amd64) y Mac (arm64)

## 10. Decisiones de diseno

- **Spark 3.5**: ultima version estable con soporte amplio
- **jupyter/pyspark-notebook**: imagen oficial mantenida por Jupyter, incluye PySpark preconfigurado
- **bitnami/spark**: imagenes livianas y multi-arch para master/worker
- **Perfiles Docker Compose**: permite escalar recursos segun la EA y el equipo del alumno
- **Notebooks duales**: version alumno con TODOs + version resuelta para docente
- **Token fijo (bigdata2026)**: simplifica acceso en clase, no hay datos sensibles
- **Volumenes locales**: los notebooks persisten aunque se recreen los contenedores
