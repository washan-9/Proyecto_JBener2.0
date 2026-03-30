# Proyecto JBener

Plataforma de gestión financiera personal orientada a construir patrimonio, trackear criptomonedas y dar control tributario SUNAT. 

## Requisitos

- [Docker](https://www.docker.com/) y [Docker Compose](https://docs.docker.com/compose/)
- Base de datos en [Supabase](https://supabase.com/).

## Instalación y Ejecución Local

1. Clonar este repositorio.
2. Copiar `.env.example` a `.env` y configurar las credenciales correctas:
   ```bash
   cp .env.example .env
   ```
3. Construir y levantar el contenedor usando Docker Compose:
   ```bash
   docker compose up --build -d
   ```
4. La API y Aplicación estarán disponibles en `http://localhost:8000`.
   La documentación interactiva de la API está en `http://localhost:8000/docs`.

## Desarrollo y Metodología

Por favor consulta la carpeta `eve/` para ver los lineamientos operativos, documentos de análisis, sistema de diseño y registro de mejoras progresivas.
