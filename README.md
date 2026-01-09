#Django Intro

## Entorno Virtual
```bash
python -m venv venv
venv\Scripts\activate # Windows
sourse venv/Scripts/activate #Gitbash
sourse venv/bin/activate #MacOS
```

### Instalacion

```bash
pip install django
```

### Crear Proyecto

```bash
python -m django startproject django_intro_g27 .
```

### Iniciar el proyecto

```bash
python manage.py runserver
```

### Migraciones

```Bash
#generar los documentos de migraciones
python manage.py makemigrations

#ejecutar las migraciones
python manage.py migrate

#ver el estado de los documentos de migraciones
python manage.py showmigrations
```

### Crear superusuario

```bash
python manage.py createsuperuser
```