# PataLog 🐾

Sistema de registro de vacunas para mascotas desarrollado con Django.

## Características
- Registro de mascotas (perros y gatos)
- Historial de vacunas por mascota
- Control de próximas dosis
- Panel administrativo
- CRUD completo
- Vistas genéricas de Django

## Instalación local

```bash
# Crear entorno virtual
python -m venv patalog-env
patalog-env\Scripts\activate  # Windows

# Instalar dependencias
pip install -r requirements.txt

# Migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Correr servidor
python manage.py runserver
```

## Acceder
- App: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/
