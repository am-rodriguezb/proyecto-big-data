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
