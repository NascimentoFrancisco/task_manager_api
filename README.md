# Desafio Django Rest Framework: API de de gerenciador de Tarefas

# Informações referentes a solução do desafio

* Documentação para uso do projeto [docs](docs.md)
* Para a autenticação da API usei o [djangorestframework-simplejwt](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) que faz autenticações por meio de tokens.

# Desafio proposto

Neste desafio, você precisará criar uma API RESTful de gerenciamento de tarefas, usando o [Django Rest Framework](https://www.django-rest-framework.org/).

> ## Requerimentos:

* Autenticação de usuário: os usuários precisam se registrar e fazer login antes de acessar as tarefas.
* CRUD de tarefas: os usuários podem criar, ler, atualizar e excluir tarefas através da API.
* Boas práticas de programação: o código deve ser claro, legível, e seguir as diretrizes da pep-8.
* Documentação da API: a API deve ser bem documentada, incluindo descrições claras de cada endpoint e exemplos de requisições e respostas.

> ## Instruções:

1. Crie um novo projeto Django com o nome "task_manager_api".
2. Instale o Django Rest Framework usando o comando "pip install djangorestframework".
3. Adicione as seguintes informações a cada tarefa: título, descrição, data de criação, data de conclusão e status (pendente/concluído).
4. Implemente a autenticação de usuários, permitindo que os usuários se registrem e façam login através da API.
5. Crie um endpoint para listar todas as tarefas, onde os usuários possam ver todas as tarefas que eles criaram.
6. Crie um endpoint para criar uma nova tarefa.
7. Crie um endpoint para editar uma tarefa existente.
8. Crie um endpoint para excluir uma tarefa existente.
9. Certifique-se de que o código siga as diretrizes da pep-8.
10. Documente sua API usando o recurso de documentação do Django Rest Framework.

**Obs.:** Não esqueça de fazer testes unitários para garantir a integridade da sua aplicação.

> ## Dicas:

* Você pode usar o Django's User model para a autenticação de usuários.
* Você pode usar o Django Rest Framework's Serializers para serializar os dados de tarefas.
* Você pode usar o Django Rest Framework's Viewsets e Routers para implementar as rotas da API.

**Boa sorte!**