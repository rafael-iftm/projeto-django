## Estrutura da Pasta `projeto`

A pasta `projeto` é um módulo do seu projeto Django. Abaixo está a descrição de cada arquivo e pasta dentro desse módulo:

### Criando o Projeto Django

Para criar um novo projeto Django, execute o seguinte comando no terminal:

```bash
django-admin startproject projeto .
```

## Estrutura da pasta `projeto`
```
📦projeto
 ┣ 📜asgi.py
 ┣ 📜README.md
 ┣ 📜settings.py
 ┣ 📜urls.py
 ┣ 📜wsgi.py
```

### asgi.py
- **Função**: Ponto de entrada para o servidor ASGI (Asynchronous Server Gateway Interface).
- **Detalhes**: Configura a aplicação ASGI para o projeto, permitindo suporte a operações assíncronas.

### settings.py
- **Função**: Arquivo de configuração principal do projeto Django.
- **Detalhes**: Contém todas as configurações essenciais, como banco de dados, aplicações instaladas, middleware, URLs estáticas e de mídia, e configurações de segurança.

### urls.py
- **Função**: Mapeamento de URLs para as visualizações correspondentes.
- **Detalhes**: Define as rotas do projeto, indicando quais funções de visualização (views) devem ser chamadas para diferentes caminhos de URL.

### wsgi.py
- **Função**: Ponto de entrada para o servidor WSGI (Web Server Gateway Interface).
- **Detalhes**: Configura a aplicação WSGI para o projeto, permitindo que ele seja servido em servidores compatíveis com WSGI, como Gunicorn.

Cada um desses arquivos desempenha um papel crucial no funcionamento e na organização do seu projeto Django, ajudando a manter o código estruturado, configurado e pronto para desenvolvimento e implantação.
