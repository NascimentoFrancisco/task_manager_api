# Desafio Django: Aplicação de Tarefas

## Principais tecnologias usadas
- Python 3.8.10
- Django 4.1.4
- djangorestframework 3.14.0
- djangorestframework-simplejwt 5.2.2

## Instruções para usar esse projeto em sua máquina local

1º) Clone o repositŕorio com o seguinte comando:
~~~
https://github.com/NascimentoFrancisco/task_manager_api.git
~~~

2º) Abra oprojeto em seu editor de texto de preferência para criar e ativar o virtualenv
> Windows:

Criação
~~~
python -m venv venv
~~~
Ativação
~~~
venv\Scripts\activate
~~~

> Linux:

Criação
~~~
python3 -m venv venv
~~~
Ativação
~~~
. venv/bin/activate
~~~

3º) Instale as dependências
~~~
pip install -r requirements.txt
~~~

4º) Faça as migrations e o migrate

~~~
python manage.py makemigrations
~~~
~~~
python manage.py migrate
~~~

5º) Inicie o servidor e acesse o seguinte link para ver a documentação dos endpoints da API.

~~~
python manage.py runserver
~~~
~~~
http://127.0.0.1:8000/api/v1/docs
~~~