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

### Libraries used:
1. [**Marshmallow**](https://marshmallow.readthedocs.io/en/stable/): para validar los parametros del body de las requests

2. [**Flask-restful**](https://flask-restful.readthedocs.io/en/latest/quickstart.html#a-minimal-api): para construir la api de manera organizada y simple

3. [**PyMongo**](https://pymongo.readthedocs.io/en/stable/): mongo driver para la base de datos


## Endpoints

### ```GET /messages```

response: array con todos los mensajes

```json
[
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
```
---

### ```GET /messages/:id```

response: mensaje con ```mid: id``` (ej: `/messages/13`)

```json
{
    "mid": 13,
    "message": "Te cuento que: Me encanta el metal. Me despido, saludos.",
    "sender": 393,
    "receptant": 392,
    "lat": -27.374641,
    "long": -90.97999,
    "date": "2020-09-16"
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

response: ```204 NO CONTENT```

---

```DELETE /message/:id```

response: ```204 NO CONTENT```

---

```GET /users```

```GET /users/:id```

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

response: array con todos los mensajes y el ```score``` asociado al número de matchs con ```desired```

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
        "score": 1
    }
]
```

---
