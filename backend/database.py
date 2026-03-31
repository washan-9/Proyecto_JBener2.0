import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Cargar variables de entorno (útil si se ejecuta localmente sin docker-compose envs)
load_dotenv()

# Obtener credenciales de Supabase
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

if not SUPABASE_URL or not SUPABASE_KEY:
    raise ValueError("Faltan configurar las variables de entorno SUPABASE_URL o SUPABASE_KEY")

# Inicializar cliente de Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_supabase() -> Client:
    """
    Dependencia opcional para inyectar el cliente de base de datos en las rutas, 
    o puede importarse directamente donde se requiera.
    """
    return supabase
