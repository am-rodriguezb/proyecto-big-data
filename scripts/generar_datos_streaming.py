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
