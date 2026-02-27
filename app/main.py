from fastapi import FastAPI, HTTPException #Vamos a usar Fast API 
from pydantic import BaseModel
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_READ_COMMITTED

# 1. Inicializamos la aplicación FastAPI
app = FastAPI(title="Pagila Rental API - Persona A")

# --- MODELOS DE DATOS (Esquemas para Postman) ---

class RentalData(BaseModel):
    customer_id: int
    inventory_id: int
    staff_id: int

# Aquí después agregaremos los modelos para Devoluciones y Pagos...

# --- CONFIGURACIÓN DE BASE DE DATOS ---
def get_db_connection():
    """
    Establece la conexión con PostgreSQL y configura el nivel
    de aislamiento requerido para el manejo de concurrencia.
    """
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="pagila",
            user="postgres",       
            password="postgres" 
        )
        # El aislamiento para transacciones seguras
        conn.set_isolation_level(ISOLATION_LEVEL_READ_COMMITTED)
        return conn
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error de conexión con la Base de Datos: {str(e)}")

# --- ENDPOINTS ---
@app.get("/")
def health_check():
    return {"status": "Lista para recibir transacciones."}
