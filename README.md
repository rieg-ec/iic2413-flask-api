# Flask + Mongo API

### Usage
---

### Environment Configuration:

Crear* archivo .env con las siguientes variables:

- ```MONGO_URI``` dirección de la base de datos *(mongodb://gray.ing.puc.cl)*
- ```MONGO_USER``` nombre de usuario
- ```MONGO_PASSWORD``` contraseña
- ```MONGO_DB``` nombre de la base de datos

*\*dentro de la carpeta de entrega ya se encuentra creado*

### Flask server:
1. ```python3 -m venv .venv```
2. ```source .venv/bin/activate```
3. ```pip install -r requirements.txt```
4. ```python3 main.py```

## Endpoints

### ```GET /messages```

response: array con todos los mensajes

```json
{
  "success": true,
  "payload": [
    {
      "mid": 1,
       "message": "Qué tal? Me gustó el hotel que reservé. 10 - 4.",
       "sender": 86,
       "receptant": 261,
       "lat": -51.729782,
       "long": -72.515097,
       "date": "2020-08-02"
    },
  ]
}
```
---

### ```GET /messages/:id```

response: mensaje con ```mid: id``` (ej: `/messages/13`)

```json
{
    "success": true,
    "payload": {
        "mid": 210,
        "message": "A todo esto, por qué magikarps y shrek? no habían códigos mejores?",
        "sender": 171,
        "receptant": 212,
        "lat": -20.736956,
        "long": -70.182595,
        "date": "2020-07-13"
    }
}
```
---

### ```POST /messages```

body:

```json
{
    "message": "Mensaje para probar el POST",
    "sender": 1,
    "receptant": 2,
    "lat": -46.059365,
    "long": -72.201691,
    "date": "2018-10-16"
}
```

response:
```json
{
    "success": true,
    "payload": "mensaje con mid 294 creado"
}
```

---

### ```DELETE /message/:id```

response:
```json
{
    "success": true,
    "payload": "mensaje con id 23 eliminado"
}
```

---

### ```GET /users```

response:
```json
{
  "success": true,
  "payload": [
    {
        "uid": 1,
        "name": "Nigel Dickens",
        "age": 36,
        "description": "Soy jefe de una instalacion en el puerto Caleta Coloso"
    },
  ]
}
```
---

### ```GET /users/:id```

response: información del usuario y todos los mensajes enviados por este

```json
{
  "success": true,
  "payload": {
    "user": {
        "uid": 12,
        "name": "Christie Zavala",
        "age": 55,
        "description": "Soy jefe de una instalacion en el puerto Puerto Angamos"
    },
    "messages": [
        {
            "mid": 125,
            "message": "Hola! Te quiero 3000. Cambio y fuera.",
            "sender": 12,
            "receptant": 455,
            "lat": -23.079884,
            "long": -70.385076,
            "date": "2020-10-29"
        },
    ]
  }
}
```

---

### ```GET /text-search```

body:

```json
{
    "userId": 212,
    "forbidden": ["no", "mala"],
    "required": ["viejo"],
    "desired": ["futuro"]
}
```

response:

```json
[
    {
        "mid": 68,
        "message": "jajajajaja. el futuro es hoy viejo",
        "sender": 212,
        "receptant": 250,
        "lat": -50.291406,
        "long": -90.276865,
        "date": "2020-09-20",
    }
]
```

---
