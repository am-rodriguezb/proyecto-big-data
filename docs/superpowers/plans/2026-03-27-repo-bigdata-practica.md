# Repositorio de Practica Big Data — Plan de Implementacion

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Crear un repositorio completo con Docker Compose, notebooks de practica PySpark, datasets, documentacion teorica, y scripts de utilidad para el curso Big Data BIY7131 de DUOC.

**Architecture:** Docker Compose multi-servicio con perfiles (basico: Jupyter+Spark, completo: +Kafka+Hive). Notebooks organizados por Experiencia de Aprendizaje (EA1-EA3) con version alumno y docente. Datasets copiados de fuentes existentes + generador de streaming.

**Tech Stack:** Docker Compose, PySpark 3.5, JupyterLab, Apache Kafka, Apache Hive, Python 3.11, pandas, matplotlib, seaborn

---

## File Map

### Infrastructure
- Create: `.gitignore`
- Create: `.env.example`
- Create: `docker-compose.yml`
- Create: `docker/jupyter-spark/Dockerfile`
- Create: `docker/jupyter-spark/requirements.txt`

### Documentation
- Create: `README.md`
- Create: `GUIA_INSTALACION.md`
- Create: `docs/referencias/labs_google_skillsboost.md`

### Datasets (copy from existing)
- Copy: `datos/flights.csv`
- Copy: `datos/sales.csv`
- Copy: `datos/stores.csv`
- Copy: `datos/netflix_titles.csv`
- Copy: `datos/ufo_sightings.xlsx`
- Copy: `datos/cartas_magic.csv`

### Documentation PDFs (copy from existing)
- Copy: `docs/temas/*.pdf` (12 files)
- Copy: `docs/guias/despliegue_cluster_gcp.pdf`
- Copy: `docs/guias/guia_visualizacion.pdf`

### Scripts
- Create: `scripts/verificar_entorno.py`
- Create: `scripts/generar_datos_streaming.py`
- Create: `scripts/reset_entorno.sh`
- Create: `scripts/reset_entorno.bat`

### Notebooks — EA1 Fundamentos (alumno + resuelto)
- Create: `notebooks/EA1_fundamentos/01_introduccion_spark.ipynb`
- Create: `notebooks/EA1_fundamentos/02_rdds_basico.ipynb`
- Create: `notebooks/EA1_fundamentos/03_dataframes_intro.ipynb`
- Create: `notebooks/EA1_fundamentos/04_arquitecturas_bigdata.ipynb`
- Create: `notebooks_resueltos/EA1_fundamentos/01_introduccion_spark.ipynb`
- Create: `notebooks_resueltos/EA1_fundamentos/02_rdds_basico.ipynb`
- Create: `notebooks_resueltos/EA1_fundamentos/03_dataframes_intro.ipynb`
- Create: `notebooks_resueltos/EA1_fundamentos/04_arquitecturas_bigdata.ipynb`

### Notebooks — EA2 ETL Batch (alumno + resuelto)
- Create: `notebooks/EA2_etl_batch/01_ingesta_datos.ipynb`
- Create: `notebooks/EA2_etl_batch/02_transformacion_limpieza.ipynb`
- Create: `notebooks/EA2_etl_batch/03_spark_sql.ipynb`
- Create: `notebooks/EA2_etl_batch/04_hive_metastore.ipynb`
- Create: `notebooks/EA2_etl_batch/05_machine_learning_spark.ipynb`
- Create: `notebooks/EA2_etl_batch/06_visualizacion_datos.ipynb`
- Create: `notebooks_resueltos/EA2_etl_batch/01_ingesta_datos.ipynb`
- Create: `notebooks_resueltos/EA2_etl_batch/02_transformacion_limpieza.ipynb`
- Create: `notebooks_resueltos/EA2_etl_batch/03_spark_sql.ipynb`
- Create: `notebooks_resueltos/EA2_etl_batch/04_hive_metastore.ipynb`
- Create: `notebooks_resueltos/EA2_etl_batch/05_machine_learning_spark.ipynb`
- Create: `notebooks_resueltos/EA2_etl_batch/06_visualizacion_datos.ipynb`

### Notebooks — EA3 Tiempo Real (alumno + resuelto)
- Create: `notebooks/EA3_tiempo_real/01_kafka_introduccion.ipynb`
- Create: `notebooks/EA3_tiempo_real/02_ingesta_tiempo_real.ipynb`
- Create: `notebooks/EA3_tiempo_real/03_spark_structured_streaming.ipynb`
- Create: `notebooks/EA3_tiempo_real/04_dashboard_tiempo_real.ipynb`
- Create: `notebooks_resueltos/EA3_tiempo_real/01_kafka_introduccion.ipynb`
- Create: `notebooks_resueltos/EA3_tiempo_real/02_ingesta_tiempo_real.ipynb`
- Create: `notebooks_resueltos/EA3_tiempo_real/03_spark_structured_streaming.ipynb`
- Create: `notebooks_resueltos/EA3_tiempo_real/04_dashboard_tiempo_real.ipynb`

### Notebooks — Extras (alumno + resuelto)
- Create: `notebooks/extras/actividad_vuelos.ipynb`
- Create: `notebooks/extras/actividad_ventas.ipynb`
- Create: `notebooks/extras/actividad_netflix.ipynb`
- Create: `notebooks/extras/actividad_avistamientos.ipynb`
- Create: `notebooks/extras/actividad_cartas_magic.ipynb`
- Create: `notebooks_resueltos/extras/actividad_vuelos.ipynb`
- Create: `notebooks_resueltos/extras/actividad_ventas.ipynb`
- Create: `notebooks_resueltos/extras/actividad_netflix.ipynb`
- Create: `notebooks_resueltos/extras/actividad_avistamientos.ipynb`
- Create: `notebooks_resueltos/extras/actividad_cartas_magic.ipynb`

---

## Task 1: Scaffolding del repositorio

**Files:**
- Create: `.gitignore`
- Create: `.env.example`

- [ ] **Step 1: Crear .gitignore**

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.egg-info/
.eggs/
dist/
build/

# Jupyter
.ipynb_checkpoints/
*.ipynb_checkpoints

# Entorno
.env
.venv/
venv/

# IDE
.idea/
.vscode/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
desktop.ini

# Docker
docker/jupyter-spark/tmp/

# Spark
spark-warehouse/
metastore_db/
derby.log

# Datos temporales generados
datos/streaming/output/
datos/tmp/

# Logs
*.log
logs/
```

Write this to `/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data/.gitignore`

- [ ] **Step 2: Crear .env.example**

```env
# ============================================
# Configuracion del Entorno Big Data
# ============================================
# Copiar este archivo a .env:  cp .env.example .env
# Ajustar valores segun los recursos de tu equipo

# --- Spark ---
SPARK_WORKER_MEMORY=2g
SPARK_WORKER_CORES=2
SPARK_MASTER_WEBUI_PORT=8080
SPARK_WORKER_WEBUI_PORT=8081

# --- Jupyter ---
JUPYTER_TOKEN=bigdata2026
JUPYTER_PORT=8888

# --- Kafka ---
KAFKA_BROKER_ID=1
KAFKA_PORT=9092

# --- PostgreSQL (Hive Metastore) ---
POSTGRES_USER=hive
POSTGRES_PASSWORD=hive_metastore
POSTGRES_DB=metastore

# --- Recursos minimos recomendados ---
# Perfil basico: 4 GB RAM, 2 CPUs en Docker Desktop
# Perfil completo: 6-8 GB RAM, 4 CPUs en Docker Desktop
```

Write this to `/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data/.env.example`

- [ ] **Step 3: Crear estructura de directorios**

```bash
cd "/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
mkdir -p docker/jupyter-spark
mkdir -p docs/temas docs/guias docs/referencias
mkdir -p datos/streaming
mkdir -p notebooks/EA1_fundamentos notebooks/EA2_etl_batch notebooks/EA3_tiempo_real notebooks/extras
mkdir -p notebooks_resueltos/EA1_fundamentos notebooks_resueltos/EA2_etl_batch notebooks_resueltos/EA3_tiempo_real notebooks_resueltos/extras
mkdir -p scripts
```

- [ ] **Step 4: Commit**

```bash
cd "/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
git add .gitignore .env.example
git commit -m "chore: scaffolding inicial del repositorio"
```

---

## Task 2: Infraestructura Docker

**Files:**
- Create: `docker/jupyter-spark/Dockerfile`
- Create: `docker/jupyter-spark/requirements.txt`
- Create: `docker-compose.yml`

- [ ] **Step 1: Crear requirements.txt**

```txt
# Analisis de datos
pandas>=2.1.0
numpy>=1.26.0
openpyxl>=3.1.0

# Visualizacion
matplotlib>=3.8.0
seaborn>=0.13.0
plotly>=5.18.0

# Kafka
kafka-python-ng>=2.0.2

# Utilidades
tqdm>=4.66.0
Faker>=22.0.0
```

Write to `docker/jupyter-spark/requirements.txt`

- [ ] **Step 2: Crear Dockerfile**

```dockerfile
FROM jupyter/pyspark-notebook:spark-3.5.3

USER root

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

USER ${NB_UID}

# Copiar e instalar dependencias Python
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Configurar Spark para conectar a cluster externo y Hive
ENV SPARK_MASTER_URL=spark://spark-master:7077
ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=python3

# Directorio de trabajo
WORKDIR /home/jovyan
```

Write to `docker/jupyter-spark/Dockerfile`

- [ ] **Step 3: Crear docker-compose.yml**

```yaml
version: "3.8"

x-spark-common: &spark-common
  image: bitnami/spark:3.5
  networks:
    - bigdata-net
  restart: unless-stopped

services:
  # ============================================
  # PERFIL BASICO — EA1 y EA2
  # ============================================

  jupyter-spark:
    build:
      context: ./docker/jupyter-spark
      dockerfile: Dockerfile
    container_name: bigdata-jupyter
    profiles: ["basico", "completo"]
    ports:
      - "${JUPYTER_PORT:-8888}:8888"
    environment:
      - JUPYTER_TOKEN=${JUPYTER_TOKEN:-bigdata2026}
      - SPARK_MASTER=spark://spark-master:7077
      - JUPYTER_ENABLE_LAB=yes
    volumes:
      - ./notebooks:/home/jovyan/notebooks
      - ./notebooks_resueltos:/home/jovyan/notebooks_resueltos:ro
      - ./datos:/home/jovyan/datos
      - ./scripts:/home/jovyan/scripts
      - jupyter-work:/home/jovyan/work
    networks:
      - bigdata-net
    depends_on:
      - spark-master
    restart: unless-stopped

  spark-master:
    <<: *spark-common
    container_name: bigdata-spark-master
    profiles: ["basico", "completo"]
    ports:
      - "${SPARK_MASTER_WEBUI_PORT:-8080}:8080"
    environment:
      - SPARK_MODE=master
      - SPARK_MASTER_HOST=spark-master

  spark-worker:
    <<: *spark-common
    container_name: bigdata-spark-worker
    profiles: ["basico", "completo"]
    ports:
      - "${SPARK_WORKER_WEBUI_PORT:-8081}:8081"
    environment:
      - SPARK_MODE=worker
      - SPARK_MASTER_URL=spark://spark-master:7077
      - SPARK_WORKER_MEMORY=${SPARK_WORKER_MEMORY:-2g}
      - SPARK_WORKER_CORES=${SPARK_WORKER_CORES:-2}
    depends_on:
      - spark-master

  # ============================================
  # PERFIL COMPLETO — EA3 + Hive
  # ============================================

  zookeeper:
    image: bitnami/zookeeper:3.9
    container_name: bigdata-zookeeper
    profiles: ["completo"]
    environment:
      - ALLOW_ANONYMOUS_LOGIN=yes
    networks:
      - bigdata-net
    restart: unless-stopped

  kafka:
    image: bitnami/kafka:3.7
    container_name: bigdata-kafka
    profiles: ["completo"]
    ports:
      - "${KAFKA_PORT:-9092}:9092"
    environment:
      - KAFKA_CFG_ZOOKEEPER_CONNECT=zookeeper:2181
      - KAFKA_CFG_LISTENERS=PLAINTEXT://:29092,EXTERNAL://:9092
      - KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://kafka:29092,EXTERNAL://localhost:9092
      - KAFKA_CFG_LISTENER_SECURITY_PROTOCOL_MAP=PLAINTEXT:PLAINTEXT,EXTERNAL:PLAINTEXT
      - KAFKA_CFG_INTER_BROKER_LISTENER_NAME=PLAINTEXT
      - KAFKA_CFG_AUTO_CREATE_TOPICS_ENABLE=true
      - ALLOW_PLAINTEXT_LISTENER=yes
    networks:
      - bigdata-net
    depends_on:
      - zookeeper
    restart: unless-stopped

  postgres:
    image: postgres:16-alpine
    container_name: bigdata-postgres
    profiles: ["completo"]
    environment:
      - POSTGRES_USER=${POSTGRES_USER:-hive}
      - POSTGRES_PASSWORD=${POSTGRES_PASSWORD:-hive_metastore}
      - POSTGRES_DB=${POSTGRES_DB:-metastore}
    volumes:
      - postgres-data:/var/lib/postgresql/data
    networks:
      - bigdata-net
    restart: unless-stopped

  hive-metastore:
    image: apache/hive:4.0.1
    container_name: bigdata-hive-metastore
    profiles: ["completo"]
    ports:
      - "9083:9083"
    environment:
      - SERVICE_NAME=metastore
      - DB_DRIVER=postgres
      - SERVICE_OPTS=-Djavax.jdo.option.ConnectionDriverName=org.postgresql.Driver -Djavax.jdo.option.ConnectionURL=jdbc:postgresql://postgres:5432/metastore -Djavax.jdo.option.ConnectionUserName=${POSTGRES_USER:-hive} -Djavax.jdo.option.ConnectionPassword=${POSTGRES_PASSWORD:-hive_metastore}
    networks:
      - bigdata-net
    depends_on:
      - postgres
    restart: unless-stopped

  hive-server:
    image: apache/hive:4.0.1
    container_name: bigdata-hive-server
    profiles: ["completo"]
    ports:
      - "10000:10000"
      - "10002:10002"
    environment:
      - SERVICE_NAME=hiveserver2
      - HIVE_SERVER2_THRIFT_PORT=10000
      - SERVICE_OPTS=-Dhive.metastore.uris=thrift://hive-metastore:9083
    networks:
      - bigdata-net
    depends_on:
      - hive-metastore
    restart: unless-stopped

networks:
  bigdata-net:
    driver: bridge

volumes:
  jupyter-work:
  postgres-data:
```

Write to `docker-compose.yml`

- [ ] **Step 4: Commit**

```bash
cd "/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
git add docker/ docker-compose.yml
git commit -m "feat: infraestructura Docker Compose con perfiles basico y completo"
```

---

## Task 3: Copiar datasets y documentacion

**Files:**
- Copy: all datasets to `datos/`
- Copy: all PDFs to `docs/temas/` and `docs/guias/`

- [ ] **Step 1: Copiar datasets de Manuel Padilla**

```bash
REPO="/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
MATLAB="/Users/giocrisraigodoy/Documents/MATLAB/Ingenieria para el procesado masico de datos"

cp "$MATLAB/Actividad 1/actividad_1/flights.csv" "$REPO/datos/"
cp "$MATLAB/Actividad 2/actividad_2/sales.csv" "$REPO/datos/"
cp "$MATLAB/Actividad 2/actividad_2/stores.csv" "$REPO/datos/"
```

- [ ] **Step 2: Copiar datasets de DUOC**

```bash
REPO="/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
DUOC="/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/BIY7131 - Big Data/PDA_BIY7131_69a86e5161b5e/Recursos PDA_BIY7131_AVY1101/Propuesta actividades extra BigData"

# Netflix (descomprimir)
unzip -o "$DUOC/Actividad Netflix/netflix_titles.csv.zip" -d "$REPO/datos/"

# UFO sightings
cp "$DUOC/Actividad Avistamientos/ufo_sighting.xlsx" "$REPO/datos/ufo_sightings.xlsx"

# Magic cards
cp "$DUOC/Actividad Cartas Magic/cartas_magic.csv" "$REPO/datos/"
```

- [ ] **Step 3: Copiar PDFs de temas (Manuel Padilla)**

```bash
REPO="/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
TEMAS="/Users/giocrisraigodoy/Documents/MATLAB/Ingenieria para el procesado masico de datos/Documentación Manuel Padilla-20260309/Temas"

cp "$TEMAS/Presentación de la asignatura.pdf" "$REPO/docs/temas/"
cp "$TEMAS/Tema 1. Introducción a las tecnologías Big Data.pdf" "$REPO/docs/temas/"
cp "$TEMAS/Tema 2. HDFS y MapReduce.pdf" "$REPO/docs/temas/"
cp "$TEMAS/Tema 3. Spark I.pdf" "$REPO/docs/temas/"
cp "$TEMAS/Tema 4. Spark II.pdf" "$REPO/docs/temas/"
cp "$TEMAS/Tema 5. Spark III.pdf" "$REPO/docs/temas/"
cp "$TEMAS/Tema 6. Apache Kafka.pdf" "$REPO/docs/temas/"
cp "$TEMAS/Tema 7. Hive e Impala.pdf" "$REPO/docs/temas/"
cp "$TEMAS/Tema 8. Cloud Computing. Conceptos generales.pdf" "$REPO/docs/temas/"
cp "$TEMAS/Tema 9. Cloud Computing. Microsoft Azure.pdf" "$REPO/docs/temas/"
cp "$TEMAS/Tema 10. Cloud Computing. AWS.pdf" "$REPO/docs/temas/"
cp "$TEMAS/Tema 11. Cloud Computing. Google Cloud Platform.pdf" "$REPO/docs/temas/"
```

- [ ] **Step 4: Copiar guias complementarias**

```bash
REPO="/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
MATLAB="/Users/giocrisraigodoy/Documents/MATLAB/Ingenieria para el procesado masico de datos"
DUOC="/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/BIY7131 - Big Data/PDA_BIY7131_69a86e5161b5e/Recursos PDA_BIY7131_AVY1101/Propuesta actividades extra BigData"

cp "$MATLAB/Despliegue de clúster Google Cloud.pdf" "$REPO/docs/guias/despliegue_cluster_gcp.pdf"
cp "$DUOC/Guía Visualización/guia_visualitzacio_es.pdf" "$REPO/docs/guias/guia_visualizacion.pdf"
```

- [ ] **Step 5: Verificar que todos los archivos se copiaron**

```bash
cd "/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
echo "=== DATOS ==="
ls -lh datos/
echo "=== TEMAS ==="
ls -lh docs/temas/
echo "=== GUIAS ==="
ls -lh docs/guias/
```

Expected: 6 archivos en datos/, 12 PDFs en docs/temas/, 2 PDFs en docs/guias/

- [ ] **Step 6: Commit**

```bash
cd "/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
git add datos/ docs/temas/ docs/guias/
git commit -m "feat: agregar datasets y documentacion teorica"
```

---

## Task 4: Scripts de utilidad

**Files:**
- Create: `scripts/verificar_entorno.py`
- Create: `scripts/generar_datos_streaming.py`
- Create: `scripts/reset_entorno.sh`
- Create: `scripts/reset_entorno.bat`

- [ ] **Step 1: Crear verificar_entorno.py**

```python
#!/usr/bin/env python3
"""
Script de verificacion del entorno Big Data.
Ejecutar dentro de JupyterLab para confirmar que todo funciona.

Uso:
    %run /home/jovyan/scripts/verificar_entorno.py
"""

import sys
import os


def check(nombre, funcion):
    """Ejecuta una verificacion y muestra el resultado."""
    try:
        resultado = funcion()
        if resultado:
            print(f"  [PASS] {nombre}")
            return True
        else:
            print(f"  [FAIL] {nombre}")
            return False
    except Exception as e:
        print(f"  [FAIL] {nombre} -> {e}")
        return False


def verificar_python():
    """Verifica version de Python."""
    version = sys.version_info
    return version.major == 3 and version.minor >= 10


def verificar_pyspark():
    """Verifica que PySpark esta instalado y puede crear SparkSession."""
    from pyspark.sql import SparkSession
    spark = SparkSession.builder \
        .appName("verificacion_entorno") \
        .master("local[*]") \
        .getOrCreate()
    version = spark.version
    spark.stop()
    return version.startswith("3.5")


def verificar_librerias():
    """Verifica librerias Python necesarias."""
    librerias = ["pandas", "numpy", "matplotlib", "seaborn", "openpyxl", "plotly"]
    faltantes = []
    for lib in librerias:
        try:
            __import__(lib)
        except ImportError:
            faltantes.append(lib)
    if faltantes:
        print(f"    Faltantes: {', '.join(faltantes)}")
        return False
    return True


def verificar_datasets():
    """Verifica que los datasets estan accesibles."""
    datos_dir = "/home/jovyan/datos"
    archivos = [
        "flights.csv", "sales.csv", "stores.csv",
        "netflix_titles.csv", "ufo_sightings.xlsx", "cartas_magic.csv"
    ]
    faltantes = [a for a in archivos if not os.path.exists(os.path.join(datos_dir, a))]
    if faltantes:
        print(f"    Faltantes: {', '.join(faltantes)}")
        return False
    return True


def verificar_spark_csv():
    """Verifica que Spark puede leer un CSV."""
    from pyspark.sql import SparkSession
    spark = SparkSession.builder \
        .appName("verificacion_csv") \
        .master("local[*]") \
        .getOrCreate()
    df = spark.read.csv("/home/jovyan/datos/flights.csv", header=True, inferSchema=True)
    count = df.count()
    spark.stop()
    return count > 0


def verificar_spark_operaciones():
    """Verifica operaciones basicas de Spark."""
    from pyspark.sql import SparkSession
    from pyspark.sql import functions as F
    spark = SparkSession.builder \
        .appName("verificacion_ops") \
        .master("local[*]") \
        .getOrCreate()
    df = spark.read.csv("/home/jovyan/datos/stores.csv", header=True, inferSchema=True)
    resultado = df.groupBy("Type").agg(F.count("*").alias("total"))
    count = resultado.count()
    spark.stop()
    return count > 0


def verificar_parquet():
    """Verifica escritura y lectura de Parquet."""
    from pyspark.sql import SparkSession
    spark = SparkSession.builder \
        .appName("verificacion_parquet") \
        .master("local[*]") \
        .getOrCreate()
    parquet_path = "/tmp/verificacion_parquet"
    df = spark.createDataFrame([(1, "test"), (2, "ok")], ["id", "valor"])
    df.write.mode("overwrite").parquet(parquet_path)
    df_leido = spark.read.parquet(parquet_path)
    count = df_leido.count()
    spark.stop()
    return count == 2


def verificar_kafka():
    """Verifica conexion a Kafka."""
    from kafka import KafkaProducer
    producer = KafkaProducer(
        bootstrap_servers="kafka:29092",
        request_timeout_ms=5000,
        max_block_ms=5000
    )
    producer.close()
    return True


def verificar_hive():
    """Verifica conexion a Hive Metastore."""
    from pyspark.sql import SparkSession
    spark = SparkSession.builder \
        .appName("verificacion_hive") \
        .master("local[*]") \
        .config("hive.metastore.uris", "thrift://hive-metastore:9083") \
        .enableHiveSupport() \
        .getOrCreate()
    spark.sql("SHOW DATABASES").show()
    spark.stop()
    return True


def main():
    print("=" * 55)
    print("  VERIFICACION DEL ENTORNO BIG DATA")
    print("  Curso BIY7131 - DUOC 2026-1")
    print("=" * 55)

    total = 0
    pasados = 0

    # --- Verificaciones basicas (perfil basico) ---
    print("\n--- Verificaciones basicas ---")
    basicas = [
        ("Python >= 3.10", verificar_python),
        ("PySpark 3.5.x instalado", verificar_pyspark),
        ("Librerias Python (pandas, numpy, matplotlib, etc.)", verificar_librerias),
        ("Datasets accesibles", verificar_datasets),
        ("Spark puede leer CSV", verificar_spark_csv),
        ("Spark groupBy/agg funciona", verificar_spark_operaciones),
        ("Spark escribe/lee Parquet", verificar_parquet),
    ]

    for nombre, func in basicas:
        total += 1
        if check(nombre, func):
            pasados += 1

    # --- Verificaciones perfil completo ---
    print("\n--- Verificaciones perfil completo (opcional) ---")
    avanzadas = [
        ("Kafka accesible", verificar_kafka),
        ("Hive Metastore accesible", verificar_hive),
    ]

    for nombre, func in avanzadas:
        total += 1
        if check(nombre, func):
            pasados += 1

    # --- Resumen ---
    print("\n" + "=" * 55)
    print(f"  RESULTADO: {pasados}/{total} verificaciones pasaron")
    if pasados >= 7:
        print("  Entorno basico OK - listo para EA1 y EA2")
    if pasados == total:
        print("  Entorno completo OK - listo para EA3")
    elif pasados < 7:
        print("  ATENCION: hay problemas en el entorno basico")
        print("  Revisa la GUIA_INSTALACION.md para soluciones")
    print("=" * 55)


if __name__ == "__main__":
    main()
```

Write to `scripts/verificar_entorno.py`

- [ ] **Step 2: Crear generar_datos_streaming.py**

```python
#!/usr/bin/env python3
"""
Generador de datos de streaming para practicas de Kafka.
Produce eventos simulados a un topic de Kafka.

Uso:
    python generar_datos_streaming.py --tipo transacciones --velocidad 5 --duracion 60
    python generar_datos_streaming.py --tipo logs --velocidad 20 --duracion 120
    python generar_datos_streaming.py --tipo iot --velocidad 10 --duracion 60
    python generar_datos_streaming.py --tipo transacciones --archivo datos/streaming/transacciones.jsonl --cantidad 1000
"""

import argparse
import json
import random
import time
import sys
from datetime import datetime


# --- Generadores de datos ---

PRODUCTOS = [
    ("Laptop", 450000, 1200000),
    ("Mouse", 5000, 25000),
    ("Teclado", 15000, 65000),
    ("Monitor", 150000, 650000),
    ("Audifonos", 10000, 120000),
    ("Webcam", 20000, 80000),
    ("Disco SSD", 30000, 150000),
    ("Memoria RAM", 25000, 90000),
    ("Cable USB", 2000, 8000),
    ("Cargador", 8000, 35000),
]

METODOS_PAGO = ["tarjeta_credito", "tarjeta_debito", "efectivo", "transferencia"]

ENDPOINTS = [
    "/api/productos", "/api/usuarios", "/api/ventas", "/api/login",
    "/api/carrito", "/api/checkout", "/api/buscar", "/api/categorias",
    "/", "/health", "/api/reportes", "/api/inventario"
]

METODOS_HTTP = ["GET", "GET", "GET", "GET", "POST", "POST", "PUT", "DELETE"]
STATUS_CODES = [200, 200, 200, 200, 200, 201, 301, 400, 404, 500]

UBICACIONES = [
    "bodega_norte", "bodega_sur", "bodega_central",
    "planta_1", "planta_2", "oficina_central",
    "exterior_patio", "sala_servidores"
]


def generar_transaccion(seq_id):
    """Genera un evento de transaccion de venta."""
    producto, precio_min, precio_max = random.choice(PRODUCTOS)
    return {
        "id": f"tx_{seq_id:06d}",
        "timestamp": datetime.now().isoformat(),
        "monto": random.randint(precio_min, precio_max),
        "tienda_id": random.randint(1, 45),
        "producto": producto,
        "cantidad": random.randint(1, 5),
        "metodo_pago": random.choice(METODOS_PAGO),
    }


def generar_log(seq_id):
    """Genera un evento de log de servidor web."""
    endpoint = random.choice(ENDPOINTS)
    status = random.choice(STATUS_CODES)
    # Requests lentos correlacionan con errores
    base_time = 50 if status == 200 else 500
    return {
        "id": f"log_{seq_id:06d}",
        "timestamp": datetime.now().isoformat(),
        "ip": f"192.168.{random.randint(1,10)}.{random.randint(1,254)}",
        "endpoint": endpoint,
        "method": random.choice(METODOS_HTTP),
        "status_code": status,
        "response_time_ms": max(10, int(random.gauss(base_time, base_time * 0.4))),
        "user_agent": random.choice(["Chrome/120", "Firefox/121", "Safari/17", "Edge/120"]),
    }


def generar_iot(seq_id):
    """Genera un evento de sensor IoT."""
    ubicacion = random.choice(UBICACIONES)
    # Temperatura base segun ubicacion
    temp_base = 22.0 if "oficina" in ubicacion or "sala" in ubicacion else 18.0
    if "exterior" in ubicacion:
        temp_base = 15.0
    return {
        "sensor_id": f"sensor_{random.randint(1, 50):03d}",
        "timestamp": datetime.now().isoformat(),
        "temperatura": round(random.gauss(temp_base, 3.0), 1),
        "humedad": round(random.gauss(60.0, 15.0), 1),
        "presion_hpa": round(random.gauss(1013.0, 5.0), 1),
        "ubicacion": ubicacion,
    }


GENERADORES = {
    "transacciones": generar_transaccion,
    "logs": generar_log,
    "iot": generar_iot,
}


def enviar_a_kafka(tipo, velocidad, duracion, topic):
    """Envia eventos a Kafka."""
    try:
        from kafka import KafkaProducer
    except ImportError:
        print("ERROR: kafka-python-ng no instalado. Ejecuta: pip install kafka-python-ng")
        sys.exit(1)

    producer = KafkaProducer(
        bootstrap_servers="kafka:29092",
        value_serializer=lambda v: json.dumps(v).encode("utf-8"),
    )

    generador = GENERADORES[tipo]
    intervalo = 1.0 / velocidad
    fin = time.time() + duracion
    seq = 0

    print(f"Enviando eventos '{tipo}' a topic '{topic}' ({velocidad} eventos/seg, {duracion}s)...")
    print("Presiona Ctrl+C para detener\n")

    try:
        while time.time() < fin:
            seq += 1
            evento = generador(seq)
            producer.send(topic, value=evento)
            if seq % 50 == 0:
                print(f"  Enviados: {seq} eventos", end="\r")
            time.sleep(intervalo)
    except KeyboardInterrupt:
        print("\nDetenido por el usuario")
    finally:
        producer.flush()
        producer.close()
        print(f"\nTotal enviados: {seq} eventos al topic '{topic}'")


def escribir_a_archivo(tipo, cantidad, archivo):
    """Escribe eventos a un archivo JSONL (un JSON por linea)."""
    generador = GENERADORES[tipo]

    print(f"Generando {cantidad} eventos '{tipo}' en '{archivo}'...")

    with open(archivo, "w") as f:
        for i in range(1, cantidad + 1):
            evento = generador(i)
            f.write(json.dumps(evento) + "\n")
            if i % 500 == 0:
                print(f"  Generados: {i}/{cantidad}", end="\r")

    print(f"\nArchivo generado: {archivo} ({cantidad} eventos)")


def main():
    parser = argparse.ArgumentParser(description="Generador de datos de streaming para Big Data")
    parser.add_argument("--tipo", choices=["transacciones", "logs", "iot"],
                        required=True, help="Tipo de datos a generar")

    # Modo Kafka
    parser.add_argument("--velocidad", type=int, default=10,
                        help="Eventos por segundo (modo Kafka, default: 10)")
    parser.add_argument("--duracion", type=int, default=60,
                        help="Duracion en segundos (modo Kafka, default: 60)")
    parser.add_argument("--topic", type=str, default=None,
                        help="Topic de Kafka (default: bigdata-<tipo>)")

    # Modo archivo
    parser.add_argument("--archivo", type=str, default=None,
                        help="Ruta del archivo de salida (modo archivo)")
    parser.add_argument("--cantidad", type=int, default=1000,
                        help="Cantidad de eventos (modo archivo, default: 1000)")

    args = parser.parse_args()

    if args.archivo:
        escribir_a_archivo(args.tipo, args.cantidad, args.archivo)
    else:
        topic = args.topic or f"bigdata-{args.tipo}"
        enviar_a_kafka(args.tipo, args.velocidad, args.duracion, topic)


if __name__ == "__main__":
    main()
```

Write to `scripts/generar_datos_streaming.py`

- [ ] **Step 3: Crear reset_entorno.sh**

```bash
#!/bin/bash
# Reset completo del entorno Big Data
# Detiene contenedores, borra volumenes y datos temporales

echo "============================================"
echo "  Reset del Entorno Big Data"
echo "============================================"
echo ""

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR"

echo "1. Deteniendo contenedores..."
docker-compose --profile completo down -v 2>/dev/null
docker-compose --profile basico down -v 2>/dev/null

echo "2. Eliminando datos temporales..."
rm -rf datos/streaming/output/ 2>/dev/null
rm -rf datos/tmp/ 2>/dev/null

echo "3. Limpiando checkpoints de Spark..."
rm -rf spark-warehouse/ metastore_db/ derby.log 2>/dev/null

echo ""
echo "Reset completado. Para volver a iniciar:"
echo "  docker-compose --profile basico up -d"
echo ""
```

Write to `scripts/reset_entorno.sh`

- [ ] **Step 4: Crear reset_entorno.bat**

```batch
@echo off
REM Reset completo del entorno Big Data
REM Detiene contenedores, borra volumenes y datos temporales

echo ============================================
echo   Reset del Entorno Big Data
echo ============================================
echo.

cd /d "%~dp0\.."

echo 1. Deteniendo contenedores...
docker-compose --profile completo down -v 2>nul
docker-compose --profile basico down -v 2>nul

echo 2. Eliminando datos temporales...
if exist datos\streaming\output rd /s /q datos\streaming\output
if exist datos\tmp rd /s /q datos\tmp

echo 3. Limpiando checkpoints de Spark...
if exist spark-warehouse rd /s /q spark-warehouse
if exist metastore_db rd /s /q metastore_db
if exist derby.log del derby.log

echo.
echo Reset completado. Para volver a iniciar:
echo   docker-compose --profile basico up -d
echo.
pause
```

Write to `scripts/reset_entorno.bat`

- [ ] **Step 5: Hacer ejecutables los scripts**

```bash
chmod +x "/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data/scripts/reset_entorno.sh"
chmod +x "/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data/scripts/generar_datos_streaming.py"
chmod +x "/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data/scripts/verificar_entorno.py"
```

- [ ] **Step 6: Commit**

```bash
cd "/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
git add scripts/
git commit -m "feat: scripts de verificacion, generador de streaming y reset"
```

---

## Task 5: Notebooks EA1 — Fundamentos (version alumno)

**Files:**
- Create: `notebooks/EA1_fundamentos/01_introduccion_spark.ipynb`
- Create: `notebooks/EA1_fundamentos/02_rdds_basico.ipynb`
- Create: `notebooks/EA1_fundamentos/03_dataframes_intro.ipynb`
- Create: `notebooks/EA1_fundamentos/04_arquitecturas_bigdata.ipynb`

Todos los notebooks se crean como archivos .ipynb (formato JSON de Jupyter). Usar la estructura estandar:

```
Celda 1 (markdown): Titulo, numero de EA/actividad, objetivos de aprendizaje
Celda 2 (markdown): Conceptos clave resumidos
Celda 3 (code): Setup - imports y SparkSession
Celdas 4-N: Bloques de {explicacion markdown → codigo ejemplo → ejercicio con TODO}
Celda N+1 (markdown): Resumen de lo aprendido
Celda N+2 (markdown): Desafio extra (opcional)
```

La SparkSession en todos los notebooks EA1/EA2 debe crearse asi (modo local, compatible con perfil basico):

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("nombre_del_notebook") \
    .master("local[*]") \
    .getOrCreate()

print(f"Spark version: {spark.version}")
```

Los paths a datos siempre deben ser: `/home/jovyan/datos/nombre_archivo.ext`

- [ ] **Step 1: Crear 01_introduccion_spark.ipynb**

Notebook introductorio. Contenido requerido:

**Conceptos:** Que es Apache Spark, arquitectura (driver, executors, cluster manager), SparkSession, diferencia con MapReduce.

**Ejemplos y ejercicios con `flights.csv`:**
1. Crear SparkSession y verificar version
2. Leer flights.csv con `spark.read.csv()` (header=True, inferSchema=True)
3. Explorar: `df.show(5)`, `df.printSchema()`, `df.count()`, `df.columns`
4. `df.describe().show()` para estadisticas basicas
5. **Ejercicio:** seleccionar columnas especificas con `df.select()`
6. **Ejercicio:** filtrar vuelos con retraso > 0 usando `df.filter()`
7. **Ejercicio:** contar vuelos por aerolinea con `df.groupBy().count()`
8. **Desafio:** encontrar el top 5 de rutas (origen-destino) mas frecuentes

- [ ] **Step 2: Crear 02_rdds_basico.ipynb**

**Conceptos:** RDDs (Resilient Distributed Datasets), transformaciones lazy vs acciones, lineage, persist/cache.

**Ejemplos y ejercicios:**
1. Crear RDD desde lista: `sc.parallelize([1,2,3,4,5])`
2. Transformaciones: `map()`, `filter()`, `flatMap()`
3. Acciones: `collect()`, `count()`, `take()`, `reduce()`
4. Crear RDD desde archivo: `sc.textFile("datos/flights.csv")`
5. **Ejercicio:** usar map + filter para procesar lineas del CSV
6. **Ejercicio:** contar palabras (word count clasico) con flatMap + map + reduceByKey
7. **Ejercicio:** comparar rendimiento RDD vs DataFrame para la misma operacion
8. **Desafio:** implementar un join manual entre dos RDDs

- [ ] **Step 3: Crear 03_dataframes_intro.ipynb**

**Conceptos:** DataFrames, Column API, funciones de agregacion, joins, funciones de fecha.

**Ejemplos y ejercicios con `sales.csv` + `stores.csv`:**
1. Leer ambos CSVs y explorar schemas
2. `select()`, `withColumn()`, `withColumnRenamed()`
3. `filter()` / `where()` con condiciones multiples
4. `groupBy()` + `agg()`: sum, avg, count, min, max
5. Join entre sales y stores: `df_sales.join(df_stores, "Store")`
6. Funciones de fecha: extraer anio, mes, dia de semana
7. `when()` / `otherwise()` para crear columnas condicionales
8. **Ejercicio:** calcular ventas totales por tipo de tienda
9. **Ejercicio:** encontrar la tienda con mayor venta promedio semanal
10. **Ejercicio:** crear columna "temporada" basada en el mes (verano/invierno/etc.)
11. **Desafio:** calcular el crecimiento porcentual mes a mes por tienda

- [ ] **Step 4: Crear 04_arquitecturas_bigdata.ipynb**

**Contenido conceptual (mayormente markdown, pocas celdas de codigo):**
1. Ecosistema Hadoop: HDFS, YARN, MapReduce (diagrama en markdown)
2. Ecosistema moderno: Spark, Kafka, Hive, Presto
3. Arquitectura Lambda (batch + speed + serving layers)
4. Arquitectura Kappa (streaming-first)
5. Comparativa Lambda vs Kappa (tabla markdown)
6. On-premise vs Cloud (pros/contras)
7. Servicios cloud equivalentes: GCP vs AWS vs Azure (tabla comparativa)
8. **Ejercicio reflexivo:** dado un caso de uso, disenar la arquitectura apropiada
9. **Ejercicio reflexivo:** identificar componentes de una arquitectura Lambda para e-commerce
10. **Desafio:** proponer arquitectura para sistema de deteccion de fraude en tiempo real

- [ ] **Step 5: Commit**

```bash
cd "/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
git add notebooks/EA1_fundamentos/
git commit -m "feat: notebooks EA1 fundamentos (version alumno)"
```

---

## Task 6: Notebooks EA1 — Fundamentos (version docente)

**Files:**
- Create: `notebooks_resueltos/EA1_fundamentos/01_introduccion_spark.ipynb`
- Create: `notebooks_resueltos/EA1_fundamentos/02_rdds_basico.ipynb`
- Create: `notebooks_resueltos/EA1_fundamentos/03_dataframes_intro.ipynb`
- Create: `notebooks_resueltos/EA1_fundamentos/04_arquitecturas_bigdata.ipynb`

Copiar cada notebook de la version alumno y completar TODOS los ejercicios marcados con TODO. Agregar comentarios pedagogicos explicando la solucion. Incluir los outputs esperados como texto en celdas markdown debajo de cada solucion.

- [ ] **Step 1: Crear versiones resueltas de los 4 notebooks EA1**

Para cada notebook en `notebooks/EA1_fundamentos/`:
- Copiar el contenido completo
- Reemplazar cada celda con `# TODO:` por el codigo de la solucion completa
- Agregar celda markdown despues de cada solucion: `> **Nota docente:** explicacion de por que se resuelve asi`
- Mantener los desafios tambien resueltos

- [ ] **Step 2: Commit**

```bash
cd "/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
git add notebooks_resueltos/EA1_fundamentos/
git commit -m "feat: notebooks EA1 fundamentos (version docente resuelta)"
```

---

## Task 7: Notebooks EA2 — ETL Batch parte 1 (version alumno)

**Files:**
- Create: `notebooks/EA2_etl_batch/01_ingesta_datos.ipynb`
- Create: `notebooks/EA2_etl_batch/02_transformacion_limpieza.ipynb`
- Create: `notebooks/EA2_etl_batch/03_spark_sql.ipynb`

- [ ] **Step 1: Crear 01_ingesta_datos.ipynb**

**Conceptos:** Formatos de datos (CSV, JSON, Parquet), schemas, inferSchema vs manual, opciones de lectura, datos corruptos.

**Ejemplos y ejercicios:**
1. Leer CSV basico: flights.csv con header e inferSchema
2. Leer CSV con schema manual usando StructType/StructField
3. Opciones de lectura: delimiter, encoding, nullValue, dateFormat
4. Leer archivo Excel: ufo_sightings.xlsx con pandas + convertir a Spark DataFrame
5. Escribir y leer Parquet (explicar ventajas columnar)
6. Modos de manejo de datos corruptos: PERMISSIVE, DROPMALFORMED, FAILFAST
7. **Ejercicio:** leer netflix_titles.csv definiendo schema manual
8. **Ejercicio:** leer cartas_magic.csv y explorar el schema inferido vs real
9. **Ejercicio:** convertir flights.csv a Parquet y comparar tamano
10. **Desafio:** leer multiples archivos CSV de un directorio con un solo read

- [ ] **Step 2: Crear 02_transformacion_limpieza.ipynb**

**Conceptos:** Calidad de datos, valores nulos, duplicados, casting, UDFs, normalizacion.

**Ejemplos y ejercicios con `sales.csv` + `stores.csv`:**
1. Detectar nulls: `df.filter(col("x").isNull())`, `df.summary()`
2. Manejar nulls: `dropna()`, `fillna()`, estrategias por columna
3. Detectar y eliminar duplicados: `dropDuplicates()`
4. Cast de tipos: `cast("int")`, `to_date()`, `to_timestamp()`
5. `when()` / `otherwise()` para transformaciones condicionales
6. Crear UDF para transformacion personalizada
7. Merge de DataFrames: union, join
8. **Ejercicio:** limpiar flights.csv (quitar filas con NA en columnas criticas)
9. **Ejercicio:** normalizar nombres de columnas (snake_case, sin espacios)
10. **Ejercicio:** crear UDF que categorice montos en "bajo/medio/alto"
11. **Desafio:** pipeline completo de limpieza de netflix_titles.csv

- [ ] **Step 3: Crear 03_spark_sql.ipynb**

**Conceptos:** Spark SQL, vistas temporales, SQL nativo sobre DataFrames, window functions.

**Ejemplos y ejercicios con `sales.csv` + `stores.csv`:**
1. `createOrReplaceTempView("ventas")` y `spark.sql("SELECT ...")`
2. WHERE, GROUP BY, HAVING, ORDER BY
3. Joins en SQL: INNER, LEFT, RIGHT
4. Subqueries: IN, EXISTS, subquery en FROM
5. CTEs: WITH clause
6. Window functions: ROW_NUMBER(), RANK(), DENSE_RANK()
7. Window functions: LAG(), LEAD(), SUM() OVER
8. **Ejercicio:** top 5 tiendas por ventas totales usando SQL
9. **Ejercicio:** calcular ranking de departamentos dentro de cada tienda
10. **Ejercicio:** usar LAG para calcular diferencia de ventas semana a semana
11. **Desafio:** query complejo combinando CTEs, window functions y joins

- [ ] **Step 4: Commit**

```bash
cd "/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
git add notebooks/EA2_etl_batch/01_ingesta_datos.ipynb notebooks/EA2_etl_batch/02_transformacion_limpieza.ipynb notebooks/EA2_etl_batch/03_spark_sql.ipynb
git commit -m "feat: notebooks EA2 batch parte 1 - ingesta, transformacion, SQL (version alumno)"
```

---

## Task 8: Notebooks EA2 — ETL Batch parte 2 (version alumno)

**Files:**
- Create: `notebooks/EA2_etl_batch/04_hive_metastore.ipynb`
- Create: `notebooks/EA2_etl_batch/05_machine_learning_spark.ipynb`
- Create: `notebooks/EA2_etl_batch/06_visualizacion_datos.ipynb`

- [ ] **Step 1: Crear 04_hive_metastore.ipynb**

**IMPORTANTE:** Este notebook requiere perfil completo. Incluir celda de advertencia al inicio.

**Conceptos:** Hive como data warehouse, metastore, tablas gestionadas vs externas, particionamiento, formato Parquet.

SparkSession para Hive:
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("hive_metastore") \
    .master("local[*]") \
    .config("hive.metastore.uris", "thrift://hive-metastore:9083") \
    .enableHiveSupport() \
    .getOrCreate()
```

**Ejemplos y ejercicios con `flights.csv`:**
1. Verificar conexion: `spark.sql("SHOW DATABASES").show()`
2. Crear base de datos: `spark.sql("CREATE DATABASE IF NOT EXISTS bigdata")`
3. Crear tabla gestionada desde DataFrame
4. Crear tabla externa apuntando a directorio Parquet
5. Insertar datos y consultar
6. Particionar tabla por columna (ej: mes o aerolinea)
7. **Ejercicio:** crear tabla de vuelos particionada por mes
8. **Ejercicio:** ejecutar queries SQL sobre las tablas Hive
9. **Desafio:** disenar schema de data warehouse para datos de ventas

- [ ] **Step 2: Crear 05_machine_learning_spark.ipynb**

**Conceptos:** Pipeline ML en Spark, feature engineering, clasificacion, evaluacion.

**Ejemplos y ejercicios con `flights.csv` (predecir retrasos):**
1. Exploracion inicial: distribucion de retrasos
2. StringIndexer: codificar columnas categoricas (aerolinea, origen, destino)
3. VectorAssembler: combinar features en vector
4. Binarizer: crear target binario (retraso > 15 min = 1)
5. Train/test split: `randomSplit([0.8, 0.2])`
6. DecisionTreeClassifier: entrenar modelo
7. Evaluacion: accuracy, confusion matrix con MulticlassClassificationEvaluator
8. Pipeline: encapsular todo en Pipeline
9. CrossValidator: busqueda de hiperparametros
10. **Ejercicio:** agregar mas features al modelo (hora, dia de semana, distancia)
11. **Ejercicio:** comparar DecisionTree vs RandomForest
12. **Desafio:** mejorar el modelo hasta superar 70% accuracy

- [ ] **Step 3: Crear 06_visualizacion_datos.ipynb**

**Conceptos:** Visualizacion desde Spark, toPandas(), matplotlib, seaborn, mejores practicas.

**Ejemplos y ejercicios con `sales.csv` + `stores.csv`:**
1. Convertir a pandas: `df_spark.toPandas()` (cuidado con tamano)
2. matplotlib basico: barras, lineas, histogramas
3. seaborn: heatmap de correlacion, boxplot, pairplot
4. Grafico de barras: ventas por tipo de tienda
5. Serie temporal: ventas semanales a lo largo del tiempo
6. Heatmap: correlacion entre variables numericas
7. **Ejercicio:** crear grafico de barras horizontales con top 10 departamentos
8. **Ejercicio:** crear boxplot comparando ventas por tipo de tienda
9. **Ejercicio:** crear grafico de lineas con tendencia mensual
10. **Desafio:** dashboard con 4 graficos en una sola figura (subplots 2x2)

- [ ] **Step 4: Commit**

```bash
cd "/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
git add notebooks/EA2_etl_batch/04_hive_metastore.ipynb notebooks/EA2_etl_batch/05_machine_learning_spark.ipynb notebooks/EA2_etl_batch/06_visualizacion_datos.ipynb
git commit -m "feat: notebooks EA2 batch parte 2 - Hive, ML, visualizacion (version alumno)"
```

---

## Task 9: Notebooks EA2 — Version docente completa

**Files:**
- Create: `notebooks_resueltos/EA2_etl_batch/01_ingesta_datos.ipynb`
- Create: `notebooks_resueltos/EA2_etl_batch/02_transformacion_limpieza.ipynb`
- Create: `notebooks_resueltos/EA2_etl_batch/03_spark_sql.ipynb`
- Create: `notebooks_resueltos/EA2_etl_batch/04_hive_metastore.ipynb`
- Create: `notebooks_resueltos/EA2_etl_batch/05_machine_learning_spark.ipynb`
- Create: `notebooks_resueltos/EA2_etl_batch/06_visualizacion_datos.ipynb`

- [ ] **Step 1: Crear versiones resueltas de los 6 notebooks EA2**

Para cada notebook en `notebooks/EA2_etl_batch/`:
- Copiar contenido completo
- Completar todos los ejercicios con TODO
- Agregar notas docente despues de cada solucion
- Incluir outputs esperados como texto descriptivo

- [ ] **Step 2: Commit**

```bash
cd "/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
git add notebooks_resueltos/EA2_etl_batch/
git commit -m "feat: notebooks EA2 batch (version docente resuelta)"
```

---

## Task 10: Notebooks EA3 — Tiempo Real (version alumno)

**Files:**
- Create: `notebooks/EA3_tiempo_real/01_kafka_introduccion.ipynb`
- Create: `notebooks/EA3_tiempo_real/02_ingesta_tiempo_real.ipynb`
- Create: `notebooks/EA3_tiempo_real/03_spark_structured_streaming.ipynb`
- Create: `notebooks/EA3_tiempo_real/04_dashboard_tiempo_real.ipynb`

**TODOS los notebooks EA3 requieren perfil completo.** Incluir advertencia al inicio de cada uno.

- [ ] **Step 1: Crear 01_kafka_introduccion.ipynb**

**Conceptos:** Mensajeria distribuida, topics, particiones, producers, consumers, offsets, consumer groups.

**Ejemplos y ejercicios:**
1. Verificar conexion a Kafka
```python
from kafka import KafkaProducer, KafkaConsumer
from kafka.admin import KafkaAdminClient, NewTopic

admin = KafkaAdminClient(bootstrap_servers="kafka:29092")
print("Conexion OK. Topics existentes:", admin.list_topics())
```
2. Crear topic:
```python
topic = NewTopic(name="test-bigdata", num_partitions=3, replication_factor=1)
admin.create_topics([topic])
```
3. Producir mensajes con KafkaProducer
4. Consumir mensajes con KafkaConsumer
5. Enviar JSON serializado
6. **Ejercicio:** crear topic "ventas-stream", enviar 10 transacciones JSON
7. **Ejercicio:** consumir y mostrar los mensajes del topic
8. **Desafio:** crear producer que envie datos cada 2 segundos en un loop

- [ ] **Step 2: Crear 02_ingesta_tiempo_real.ipynb**

**Conceptos:** Generacion de datos en tiempo real, simulacion de streams, monitoreo de topics.

**Ejemplos y ejercicios:**
1. Ejecutar generador de datos:
```python
%run /home/jovyan/scripts/generar_datos_streaming.py --tipo transacciones --archivo /home/jovyan/datos/streaming/transacciones_sample.jsonl --cantidad 500
```
2. Leer archivo JSONL generado con Spark
3. Explorar estructura de los datos generados
4. Enviar datos a Kafka usando el generador (desde otra celda o terminal)
5. Consumir y verificar formato de mensajes
6. **Ejercicio:** generar datos de tipo "logs" y explorar su estructura
7. **Ejercicio:** generar datos de tipo "iot" y calcular estadisticas basicas
8. **Desafio:** modificar el generador para agregar un nuevo tipo de evento

- [ ] **Step 3: Crear 03_spark_structured_streaming.ipynb**

**Conceptos:** Structured Streaming, readStream, writeStream, watermarks, window aggregations, output modes.

SparkSession para streaming:
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("structured_streaming") \
    .master("local[*]") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.3") \
    .getOrCreate()
```

**Ejemplos y ejercicios:**
1. Leer stream desde Kafka:
```python
df_stream = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:29092") \
    .option("subscribe", "bigdata-transacciones") \
    .option("startingOffsets", "earliest") \
    .load()
```
2. Parsear JSON del campo value
3. Agregar watermark y window
4. Output modes: complete, append, update
5. writeStream a consola (para debug)
6. writeStream a Parquet (para persistencia)
7. **Ejercicio:** crear streaming pipeline que cuente transacciones por tienda en ventanas de 1 minuto
8. **Ejercicio:** calcular monto promedio por metodo de pago en streaming
9. **Desafio:** pipeline que detecte anomalias (montos inusualmente altos)

- [ ] **Step 4: Crear 04_dashboard_tiempo_real.ipynb**

**Conceptos:** Visualizacion de datos de streaming, metricas en tiempo real, actualizacion de graficos.

**Ejemplos y ejercicios:**
1. Leer resultados de streaming procesados (desde Parquet)
2. Calcular metricas acumuladas
3. Crear graficos con matplotlib que muestren datos actualizados
4. Usar `IPython.display.clear_output()` para refrescar
5. Crear funcion de monitoreo con loop de actualizacion
6. **Ejercicio:** crear panel con 3 metricas: total transacciones, monto total, promedio
7. **Ejercicio:** grafico de barras actualizable con ventas por tienda
8. **Desafio:** dashboard completo con 4 graficos y refresco automatico

- [ ] **Step 5: Commit**

```bash
cd "/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
git add notebooks/EA3_tiempo_real/
git commit -m "feat: notebooks EA3 tiempo real (version alumno)"
```

---

## Task 11: Notebooks EA3 — Version docente

**Files:**
- Create: `notebooks_resueltos/EA3_tiempo_real/01_kafka_introduccion.ipynb`
- Create: `notebooks_resueltos/EA3_tiempo_real/02_ingesta_tiempo_real.ipynb`
- Create: `notebooks_resueltos/EA3_tiempo_real/03_spark_structured_streaming.ipynb`
- Create: `notebooks_resueltos/EA3_tiempo_real/04_dashboard_tiempo_real.ipynb`

- [ ] **Step 1: Crear versiones resueltas de los 4 notebooks EA3**

Copiar y completar todos los ejercicios. Agregar notas docente.

- [ ] **Step 2: Commit**

```bash
cd "/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
git add notebooks_resueltos/EA3_tiempo_real/
git commit -m "feat: notebooks EA3 tiempo real (version docente resuelta)"
```

---

## Task 12: Notebooks Extras (ambas versiones)

**Files:**
- Create: `notebooks/extras/actividad_vuelos.ipynb`
- Create: `notebooks/extras/actividad_ventas.ipynb`
- Create: `notebooks/extras/actividad_netflix.ipynb`
- Create: `notebooks/extras/actividad_avistamientos.ipynb`
- Create: `notebooks/extras/actividad_cartas_magic.ipynb`
- Create: `notebooks_resueltos/extras/` (mismos 5 notebooks resueltos)

- [ ] **Step 1: Crear actividad_vuelos.ipynb**

Basado en la Actividad 1 de Manuel Padilla. Ejercicios:
1. Leer flights.csv y explorar
2. Crear columna fecha combinando campos
3. Crear columna dia de la semana
4. Pivoting: organizar datos por dia
5. Calcular retrasos medios por periodo del dia (manana/tarde/noche)
6. Pipeline ML: predecir retrasos usando DecisionTreeClassifier

- [ ] **Step 2: Crear actividad_ventas.ipynb**

Basado en la Actividad 2 de Manuel Padilla. Ejercicios:
1. Leer sales.csv y stores.csv, hacer join
2. Vista general de ventas por tienda
3. Analisis de desempleo vs ventas
4. Evolucion mensual de ventas
5. Tamano de tienda vs ventas
6. Analisis por departamento
7. Temperatura vs ventas

- [ ] **Step 3: Crear actividad_netflix.ipynb**

Ejercicios con netflix_titles.csv:
1. Leer y explorar el dataset
2. Distribucion de contenido: peliculas vs series
3. Top 10 paises productores de contenido
4. Evolucion temporal del catalogo (contenido agregado por anio)
5. Analisis de generos/categorias mas comunes
6. Duracion promedio por tipo de contenido

- [ ] **Step 4: Crear actividad_avistamientos.ipynb**

Ejercicios con ufo_sightings.xlsx:
1. Leer Excel con pandas y convertir a Spark DataFrame
2. Limpiar datos: fechas, coordenadas, textos
3. Distribucion geografica de avistamientos
4. Tendencias temporales (por anio, mes, dia de semana)
5. Analisis de duracion de avistamientos
6. Tipos de formas reportadas mas comunes

- [ ] **Step 5: Crear actividad_cartas_magic.ipynb**

Ejercicios con cartas_magic.csv:
1. Leer y explorar el dataset
2. Estadisticas descriptivas de atributos numericos
3. Distribucion por color/tipo de carta
4. Analisis de coste de mana
5. Filtros y agrupaciones avanzadas
6. Visualizacion de distribuciones

- [ ] **Step 6: Crear versiones resueltas de los 5 extras**

Copiar y completar todos los ejercicios en `notebooks_resueltos/extras/`

- [ ] **Step 7: Commit**

```bash
cd "/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
git add notebooks/extras/ notebooks_resueltos/extras/
git commit -m "feat: notebooks extras con actividades complementarias (alumno + docente)"
```

---

## Task 13: Documentacion principal

**Files:**
- Create: `README.md`
- Create: `GUIA_INSTALACION.md`
- Create: `docs/referencias/labs_google_skillsboost.md`

- [ ] **Step 1: Crear README.md**

```markdown
# Big Data — Repositorio de Practica

**Curso:** BIY7131 - Big Data | **Institucion:** DUOC UC | **Semestre:** 2026-1

Repositorio con entorno de practica local para el curso de Big Data. Incluye notebooks interactivos con PySpark, Apache Kafka, Apache Hive, y datasets reales para aprender procesamiento de datos a escala.

## Inicio Rapido

```bash
# 1. Clonar el repositorio
git clone <URL_DEL_REPO>
cd proyecto_big_data

# 2. Configurar entorno
cp .env.example .env

# 3. Levantar el entorno (primera vez descarga ~3GB)
docker-compose --profile basico up -d

# 4. Abrir JupyterLab
# Ir a http://localhost:8888 (token: bigdata2026)
```

## Requisitos

- **Docker Desktop** 4.0+ ([Windows](https://docs.docker.com/desktop/install/windows-install/) | [Mac](https://docs.docker.com/desktop/install/mac-install/) | [Linux](https://docs.docker.com/desktop/install/linux/))
- **Git** para clonar el repositorio
- **RAM disponible:** minimo 4 GB para perfil basico, 6-8 GB para perfil completo
- **Disco:** ~5 GB libres para imagenes Docker

> Ver [GUIA_INSTALACION.md](GUIA_INSTALACION.md) para instrucciones detalladas paso a paso.

## Estructura del Repositorio

```
proyecto_big_data/
├── README.md                    # Esta guia
├── GUIA_INSTALACION.md          # Instalacion paso a paso
├── docker-compose.yml           # Servicios Docker
├── .env.example                 # Variables de entorno
│
├── docker/                      # Configuracion Docker
│   └── jupyter-spark/           # Imagen personalizada de Jupyter + Spark
│
├── docs/                        # Documentacion teorica
│   ├── temas/                   # Material de estudio (PDFs)
│   ├── guias/                   # Guias complementarias
│   └── referencias/             # Links a labs de Google
│
├── datos/                       # Datasets para practicas
│   ├── flights.csv              # Datos de vuelos (162K registros)
│   ├── sales.csv                # Ventas semanales (421K registros)
│   ├── stores.csv               # Informacion de tiendas (45)
│   ├── netflix_titles.csv       # Catalogo Netflix
│   ├── ufo_sightings.xlsx       # Avistamientos UFO
│   ├── cartas_magic.csv         # Cartas Magic: The Gathering
│   └── streaming/               # Datos generados para streaming
│
├── notebooks/                   # Notebooks de practica (version alumno)
│   ├── EA1_fundamentos/         # Introduccion a Spark y Big Data
│   ├── EA2_etl_batch/           # Pipelines ETL y procesamiento batch
│   ├── EA3_tiempo_real/         # Kafka y streaming
│   └── extras/                  # Actividades complementarias
│
├── notebooks_resueltos/         # Notebooks con soluciones (docente)
│
└── scripts/                     # Utilidades
    ├── verificar_entorno.py     # Verifica que todo funciona
    ├── generar_datos_streaming.py # Genera datos para Kafka
    ├── reset_entorno.sh         # Reset (Linux/Mac)
    └── reset_entorno.bat        # Reset (Windows)
```

## Guia por Experiencia de Aprendizaje

### EA1: Fundamentos de Big Data (Perfil basico)

```bash
docker-compose --profile basico up -d
```

| Notebook | Tema | Dataset |
|----------|------|---------|
| `01_introduccion_spark` | SparkSession, leer datos, operaciones basicas | flights.csv |
| `02_rdds_basico` | RDDs, transformaciones, acciones | flights.csv |
| `03_dataframes_intro` | DataFrames, joins, agregaciones | sales.csv + stores.csv |
| `04_arquitecturas_bigdata` | Lambda, Kappa, ecosistema | Conceptual |

### EA2: ETL Batch (Perfil basico + completo para Hive)

```bash
# Para notebooks 01-03, 05-06:
docker-compose --profile basico up -d

# Para notebook 04 (Hive):
docker-compose --profile completo up -d
```

| Notebook | Tema | Dataset |
|----------|------|---------|
| `01_ingesta_datos` | CSV, JSON, Parquet, schemas | Multiples |
| `02_transformacion_limpieza` | Nulls, duplicados, UDFs | sales.csv + stores.csv |
| `03_spark_sql` | SQL, window functions, CTEs | sales.csv + stores.csv |
| `04_hive_metastore` | Hive, tablas, particiones | flights.csv |
| `05_machine_learning_spark` | Pipeline ML, clasificacion | flights.csv |
| `06_visualizacion_datos` | matplotlib, seaborn | sales.csv + stores.csv |

### EA3: Tiempo Real (Perfil completo)

```bash
docker-compose --profile completo up -d
```

| Notebook | Tema | Dataset |
|----------|------|---------|
| `01_kafka_introduccion` | Topics, producers, consumers | Generado |
| `02_ingesta_tiempo_real` | Generacion y consumo de streams | Generado |
| `03_spark_structured_streaming` | readStream, ventanas, watermarks | Stream Kafka |
| `04_dashboard_tiempo_real` | Visualizacion en tiempo real | Stream procesado |

### Actividades Extra

| Notebook | Descripcion |
|----------|-------------|
| `actividad_vuelos` | Analisis de vuelos + ML |
| `actividad_ventas` | SQL analytics + correlaciones |
| `actividad_netflix` | EDA del catalogo Netflix |
| `actividad_avistamientos` | Limpieza datos + tendencias |
| `actividad_cartas_magic` | Estadisticas descriptivas |

## Comandos Utiles

```bash
# Levantar entorno basico
docker-compose --profile basico up -d

# Levantar entorno completo
docker-compose --profile completo up -d

# Ver estado de los contenedores
docker-compose ps

# Ver logs de un servicio
docker-compose logs jupyter-spark
docker-compose logs kafka

# Apagar todo
docker-compose down

# Reset total (borra volumenes)
docker-compose down -v
# O usar el script:
./scripts/reset_entorno.sh        # Linux/Mac
scripts\reset_entorno.bat         # Windows
```

## Puertos y URLs

| Servicio | URL | Descripcion |
|----------|-----|-------------|
| JupyterLab | http://localhost:8888 | Interfaz de notebooks (token: bigdata2026) |
| Spark Master UI | http://localhost:8080 | Monitoreo de Spark |
| Spark Worker UI | http://localhost:8081 | Estado del worker |
| Hive Server | localhost:10000 | Conexion JDBC a Hive |

## Material Teorico

En la carpeta `docs/temas/` encontraras PDFs con la teoria de cada tema:

1. Introduccion a las tecnologias Big Data
2. HDFS y MapReduce
3. Spark I — RDDs
4. Spark II — DataFrames y Spark SQL
5. Spark III — MLlib y GraphX
6. Apache Kafka
7. Hive e Impala
8. Cloud Computing — Conceptos generales
9. Cloud Computing — Microsoft Azure
10. Cloud Computing — AWS
11. Cloud Computing — Google Cloud Platform

## Solucion de Problemas

### Docker no arranca en Windows
- Verificar que WSL2 esta habilitado: `wsl --install`
- Verificar virtualizacion en BIOS (VT-x / AMD-V)
- Reiniciar Docker Desktop

### Puerto 8888 ocupado
```bash
# Cambiar puerto en .env
JUPYTER_PORT=8889
# Reiniciar
docker-compose --profile basico up -d
```

### Spark se queda sin memoria
```bash
# Reducir memoria del worker en .env
SPARK_WORKER_MEMORY=1g
SPARK_WORKER_CORES=1
```

### Kafka no conecta
- Verificar que el perfil completo esta levantado: `docker-compose ps`
- Esperar 30 segundos despues de levantar (Kafka tarda en inicializar)
- Ver logs: `docker-compose logs kafka`

### Los notebooks no aparecen
- Verificar que la carpeta `notebooks/` esta en el mismo directorio que `docker-compose.yml`
- Verificar que Docker tiene permisos para montar volumenes

## Verificacion del Entorno

Dentro de JupyterLab, abrir un notebook y ejecutar:

```python
%run /home/jovyan/scripts/verificar_entorno.py
```

Esto verificara que todos los componentes estan funcionando correctamente.
```

Write to `README.md`

- [ ] **Step 2: Crear GUIA_INSTALACION.md**

Guia detallada paso a paso con secciones para:
1. Requisitos del sistema (tabla con minimos por OS)
2. Paso 0: Verificar requisitos (WSL2 en Windows, virtualizacion)
3. Paso 1: Instalar Docker Desktop (links oficiales por OS, configurar RAM/CPU)
4. Paso 2: Instalar Git (links por OS)
5. Paso 3: Clonar repositorio
6. Paso 4: Configurar .env (copiar .env.example, explicar cada variable)
7. Paso 5: Levantar perfil basico (comando, que esperar, cuanto tarda)
8. Paso 6: Verificar entorno (abrir JupyterLab, ejecutar verificacion)
9. Paso 7: Levantar perfil completo (cuando se necesite)
10. Apendice A: Configurar recursos Docker Desktop (capturas textuales)
11. Apendice B: Desinstalar todo limpiamente

- [ ] **Step 3: Crear docs/referencias/labs_google_skillsboost.md**

```markdown
# Laboratorios Google Cloud Skills Boost

Tabla de correspondencia entre los notebooks del repositorio y los laboratorios de Google Cloud Skills Boost.

## EA1: Fundamentos

| Notebook | Lab Google Skills Boost | Codigo |
|----------|------------------------|--------|
| 01_introduccion_spark | Getting Started with Cloud Shell and gcloud | GSP002 |
| 01_introduccion_spark | Creating a Virtual Machine | GSP001 |
| 02_rdds_basico | Introduction to Cloud Dataproc: Hadoop and Spark on Google Cloud | GSP123 |
| 04_arquitecturas_bigdata | Cloud IAM: Qwik Start | GSP064 |

## EA2: ETL Batch

| Notebook | Lab Google Skills Boost | Codigo |
|----------|------------------------|--------|
| 01_ingesta_datos | Cloud Storage: Qwik Start | GSP073 |
| 01_ingesta_datos | Dataflow: Qwik Start - Python | GSP207 |
| 02_transformacion_limpieza | Dataprep: Qwik Start | GSP105 |
| 02_transformacion_limpieza | Dataprep: Working with Dataprep | GSP050 |
| 03_spark_sql | Introduccion a SQL para BigQuery y Cloud SQL | GSP281 |
| 03_spark_sql | BigQuery: Qwik Start - Console | GSP072 |
| 03_spark_sql | BigQuery: Qwik Start - Command Line | GSP071 |
| 03_spark_sql | Explore Your Ecommerce Dataset with SQL in BigQuery | GSP407 |
| 03_spark_sql | BigQuery: Build a Data Warehouse | GSP413 |
| 04_hive_metastore | BigQuery: Using BigQuery | GSP406 |
| 05_machine_learning_spark | Getting Started with BigQuery ML | GSP247 |
| 06_visualizacion_datos | Looker Studio: Qwik Start | GSP136 |
| 06_visualizacion_datos | Explore and Create Reports with Looker Studio | GSP409 |
| 06_visualizacion_datos | Looker Data Explorer: Qwik Start | GSP718 |

## EA3: Tiempo Real

| Notebook | Lab Google Skills Boost | Codigo |
|----------|------------------------|--------|
| 01_kafka_introduccion | Creating a Streaming Data Pipeline With Apache Kafka | GSP730 |
| 01_kafka_introduccion | Get Started with Pub/Sub | (Curso) |
| 02_ingesta_tiempo_real | Stream Processing with Cloud Pub/Sub and Dataflow: Qwik Start | GSP903 |
| 02_ingesta_tiempo_real | Introduccion a las APIs en Google | GSP294 |
| 03_spark_structured_streaming | Dataflow: Qwik Start - Templates | GSP192 |
| 04_dashboard_tiempo_real | Looker: Filtering and Sorting Data | GSP855 |
| 04_dashboard_tiempo_real | Looker: Functions and Operators | GSP857 |

## Otros Labs Relevantes

| Lab | Codigo | Tema |
|-----|--------|------|
| Cloud Storage: Store Image and Video Files | GSP185 | Almacenamiento |
| BigQuery Soccer Data Ingestion | GSP848 | Ingesta |
| BigQuery: Billing Data Analysis | GSP621 | Analisis |
| Cloud Composer: Qwik Start | GSP261 | Orquestacion |
| BigLake | GSP1040 | Data Lake |
| Implement a Chatbot with BigQuery ML | GSP431 | ML aplicado |
| Datos meteorologicos en BigQuery | GSP009 | Analisis |
| Dataprep: Data Preparation Using Dataprep | GSP823 | Preparacion |

## Como usar los labs

1. Acceder a [Google Cloud Skills Boost](https://www.cloudskillsboost.google/)
2. Buscar el lab por codigo (ej: GSP123)
3. Iniciar el lab (proporciona credenciales temporales de GCP)
4. Seguir las instrucciones del lab
5. Comparar con lo practicado localmente en los notebooks

> **Nota:** Los labs de Google Skills Boost se ejecutan en la nube con credenciales temporales. Los notebooks de este repositorio replican conceptos similares en un entorno local con Docker.
```

Write to `docs/referencias/labs_google_skillsboost.md`

- [ ] **Step 4: Commit**

```bash
cd "/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
git add README.md GUIA_INSTALACION.md docs/referencias/
git commit -m "docs: README, guia de instalacion y mapeo de labs Google Skills Boost"
```

---

## Task 14: Validacion completa

- [ ] **Step 1: Verificar estructura del repositorio**

```bash
cd "/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
find . -not -path './.git/*' -not -path './docs/superpowers/*' | sort
```

Verificar que existen todos los archivos del file map.

- [ ] **Step 2: Validar docker-compose.yml**

```bash
cd "/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
docker-compose config --profiles basico
docker-compose config --profiles completo
```

Expected: YAML valido sin errores.

- [ ] **Step 3: Build de la imagen Jupyter**

```bash
cd "/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
docker-compose build jupyter-spark
```

Expected: Build exitoso sin errores.

- [ ] **Step 4: Levantar perfil basico y verificar**

```bash
cd "/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
cp .env.example .env
docker-compose --profile basico up -d
sleep 30
docker-compose ps
```

Expected: 3 servicios running (jupyter-spark, spark-master, spark-worker).

- [ ] **Step 5: Verificar JupyterLab accesible**

Abrir http://localhost:8888?token=bigdata2026 y verificar que:
- JupyterLab carga correctamente
- Se ven las carpetas notebooks/, datos/, scripts/
- notebooks_resueltos/ esta visible (read-only)

- [ ] **Step 6: Ejecutar verificar_entorno.py dentro de Jupyter**

Abrir un notebook nuevo y ejecutar:
```python
%run /home/jovyan/scripts/verificar_entorno.py
```

Expected: Todas las verificaciones basicas pasan (7/7 o 7/9 sin perfil completo).

- [ ] **Step 7: Ejecutar un notebook de prueba**

Abrir `notebooks_resueltos/EA1_fundamentos/01_introduccion_spark.ipynb` y ejecutar todas las celdas.

Expected: Todas las celdas ejecutan sin error, outputs visibles.

- [ ] **Step 8: Levantar perfil completo y verificar**

```bash
cd "/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
docker-compose --profile completo up -d
sleep 60
docker-compose ps
```

Expected: 8 servicios running.

- [ ] **Step 9: Verificar Kafka y Hive**

Ejecutar verificar_entorno.py de nuevo — ahora deberia dar 9/9.

- [ ] **Step 10: Ejecutar notebook de streaming de prueba**

Abrir `notebooks_resueltos/EA3_tiempo_real/01_kafka_introduccion.ipynb` y ejecutar las celdas de conexion y envio de mensajes.

Expected: Conexion exitosa, mensajes enviados y recibidos.

- [ ] **Step 11: Apagar y limpiar**

```bash
cd "/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
docker-compose --profile completo down
```

- [ ] **Step 12: Commit final**

```bash
cd "/Users/giocrisraigodoy/Documents/DUOC/2026-1/BIG DATA/proyecto_big_data"
git add -A
git commit -m "chore: validacion completa del entorno"
```

---

## Orden de ejecucion y dependencias

```
Task 1 (Scaffolding)
  └──> Task 2 (Docker)
  └──> Task 3 (Datasets + Docs) [paralelo con Task 2]
         └──> Task 4 (Scripts) [depende de Task 3 por paths de datos]
                └──> Task 5 (EA1 alumno) [depende de Task 4 por verificar_entorno]
                │      └──> Task 6 (EA1 docente) [depende de Task 5]
                └──> Task 7 (EA2 p1 alumno) [paralelo con Task 5]
                │      └──> Task 8 (EA2 p2 alumno)
                │             └──> Task 9 (EA2 docente)
                └──> Task 10 (EA3 alumno) [paralelo con Task 5]
                │      └──> Task 11 (EA3 docente)
                └──> Task 12 (Extras) [paralelo con Task 5]
                └──> Task 13 (Documentacion) [paralelo con Task 5]
                       └──> Task 14 (Validacion) [depende de TODOS los anteriores]
```

Tasks que pueden ejecutarse en paralelo:
- Tasks 2 y 3 (Docker e importar datos)
- Tasks 5, 7, 10, 12, 13 (notebooks EA1, EA2 p1, EA3, extras, docs)
- Tasks 6, 8 (despues de sus respectivos alumno)
