# Medicar API
Sistema para gestão de consultas em uma clínica médica

## Instalação

* Crie e ative a virtualenv:

```console

python3 -m venv venv

.\venv\Scripts\activate

```
* Faça o download do projeto:

```console

git clone https://github.com/caikesilva/medicar_api.git

```

* Execute:

```console

cd .\backend\

```

* Instale as dependências:

```console

pip install -r requirements.txt

```

* Execute:

```console

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

```

**Administração**
``` 
http://127.0.0.1:8000/admin/

```

**API**
```
http://127.0.0.1:8000/

```
## Usuarios
Cadastro e login de usuarios

### login de usuario
**POST**  /accounts/login/

Exemplo requisição:
```json
{
	"username": "admin",
	"password": "admin"
}
```

Retorno:
```json
{
	"key": "5bd7a66f4e96ca8d44615948df8136e3ddb21022"
} 
```


### Cadastrar um usuário
**POST**  /accounts/registration/

Exemplo requisição:
```json
{
	"username": "testando",
	"email": "testando@gmail.com",
	"password1": "testando#",
	"password2": "testando#"
}
```
Retorno:
```json
{
	"key": "35c6f81a7b9ffec26378efa103760dc3e79a113a"
}
```

## Especialidades
### Lista todas as especialidades médicas disponíveis na clínica

Obs: Endpoint protegido por autenticação.

Exemplo de requisição:

**GET**  /especialidades/

Authorization: Token 35c6f81a7b9ffec26378efa103760dc3e79a113a

Retorno:

```json
[
    {
        "id": 1,
        "nome": "Pediatria"
    },
    {
        "id": 2,
        "nome": "Cardiologia"
    }
]
```
#### Filtros
* Filtro pelo nome da especialidade

Exemplo requisição:

**GET**  /especialidades/?search=ped

Authorization: Token 35c6f81a7b9ffec26378efa103760dc3e79a113a

Retorno: 
```json
[
    {
        "id": 1,
        "nome": "Pediatria"
    }
]
```
## Medicos
### Lista todos os médicos que atendem pela clínica

Obs: Endpoint protegido por autenticação.

Exemplo de requisição:

**GET**  /medicos/

Authorization: Token 35c6f81a7b9ffec26378efa103760dc3e79a113a

Retorno:
```json
[
    {
        "id": 1,
        "crm": 3711,
        "nome": "Drauzio Varella",
        "especialidade": {
            "id": 1,
            "nome": "Pediatria"
        }
    },
    {
        "id": 2,
        "crm": 2544,
        "nome": "Gregory House",
        "especialidade": {
            "id": 2,
            "nome": "Cardiologia"
        }
    },
    {
        "id": 3,
        "crm": 3087,
        "nome": "Tony Tony Chopper",
        "especialidade": {
            "id": 1,
            "nome": "Pediatria"
        }
    }
]
```
### Filtros
* Filtro por nome
* Filtro por especialidade

Exemplo de requisição:

**GET**  /medicos/?search=Drauzio&especialidade=1

Authorization: Token 35c6f81a7b9ffec26378efa103760dc3e79a113a

Retorno:
```json
[
    {
        "id": 1,
        "crm": 3711,
        "nome": "Drauzio Varella",
        "especialidade": {
            "id": 1,
            "nome": "Pediatria"
        }
    }
]
```
## Agendas
### Lista todas as agendas disponíveis na clínica

Obs: Endpoint protegido por autenticação.

Exemplo de requisição:

**GET**  /agendas/

Authorization: Token 35c6f81a7b9ffec26378efa103760dc3e79a113a

Retorno:
```json
[
    {
        "id": 5,
        "medico": {
            "id": 2,
            "crm": 2544,
            "nome": "Gregory House",
            "especialidade": {
                "id": 2,
                "nome": "Cardiologia"
            }
        },
        "dia": "2021-05-03",
        "horarios": [
            "08:00:00"
        ]
    },
    {
        "id": 10,
        "medico": {
            "id": 1,
            "crm": 3711,
            "nome": "Drauzio Varella",
            "especialidade": {
                "id": 1,
                "nome": "Pediatria"
            }
        },
        "dia": "2021-05-07",
        "horarios": [
            "14:00:00",
            "14:15:00",
            "16:00:00"
        ]
    },
    {
        "id": 11,
        "medico": {
            "id": 3,
            "crm": 3087,
            "nome": "Tony Tony Chopper",
            "especialidade": {
                "id": 1,
                "nome": "Pediatria"
            }
        },
        "dia": "2021-05-07",
        "horarios": [
            "14:00:00",
            "16:00:00"
        ]
    }
]
```
### Filtros
* Filtro por medico
* Filtro por especialidade
* Filtro por intervalo de datas

Exemplo de requisição:

**GET** /agendas/?medico=2&especialidade=2&data_inicio=2021-05-11&data_final=2021-05-13

Authorization: Token 35c6f81a7b9ffec26378efa103760dc3e79a113a

Retorno:
```json
	[
    {
        "id": 13,
        "medico": {
            "id": 2,
            "crm": 2544,
            "nome": "Gregory House",
            "especialidade": {
                "id": 2,
                "nome": "Cardiologia"
            }
        },
        "dia": "2021-05-11",
        "horarios": [
            "08:00:00",
            "08:30:00",
            "09:00:00"
        ]
    },
    {
        "id": 14,
        "medico": {
            "id": 2,
            "crm": 2544,
            "nome": "Gregory House",
            "especialidade": {
                "id": 2,
                "nome": "Cardiologia"
            }
        },
        "dia": "2021-05-12",
        "horarios": [
            "14:00:00",
            "09:00:00",
            "09:30:00"
        ]
    }
]
```
## Consultas
### Marcar uma consulta para o usuário logado

Obs: Endpoint protegido por autenticação.

Exemplo de requisição:

**POST**  /consultas/

Authorization: Token 35c6f81a7b9ffec26378efa103760dc3e79a113a

Body:
```json
{
    "agenda_id": 10,
    "horario": "14:15"
}
```

Retorno:
```json
{
    "id": 38,
    "dia": "2021-05-07",
    "horario": "14:15",
    "data_agendamento": "2021-05-03T01:14:27.387201-03:00",
    "medico": {
        "id": 1,
        "crm": 3711,
        "nome": "Drauzio Varella",
        "especialidade": {
            "id": 1,
            "nome": "Pediatria"
        }
    }
}
```

### Listar consultas do usuário logado

Obs: Endpoint protegido por autenticação.

Exemplo de requisição:

**GET**  /consultas/

Authorization: Token 35c6f81a7b9ffec26378efa103760dc3e79a113a


Retorno:
```json
[
    {
        "id": 36,
        "dia": "2021-05-07",
        "horario": "14:00:00",
        "data_agendamento": "2021-05-03T00:47:50.831396-03:00",
        "medico": {
            "id": 1,
            "crm": 3711,
            "nome": "Drauzio Varella",
            "especialidade": {
                "id": 1,
                "nome": "Pediatria"
            }
        }
    },
    {
        "id": 37,
        "dia": "2021-05-07",
        "horario": "16:00:00",
        "data_agendamento": "2021-05-03T00:48:36.595055-03:00",
        "medico": {
            "id": 1,
            "crm": 3711,
            "nome": "Drauzio Varella",
            "especialidade": {
                "id": 1,
                "nome": "Pediatria"
            }
        }
    }
]
```
### Desmarcar uma consulta do usuário logado

Obs: Endpoint protegido por autenticação.

Exemplo de requisição:

**DELETE**  /consultas/30/

Authorization: Token 35c6f81a7b9ffec26378efa103760dc3e79a113a

Retorno:
```json
[]
```
