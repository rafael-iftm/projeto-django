# Home App

Este diretório contém o código do app `home` do projeto Django. O app `home` é responsável por gerenciar as páginas principais do site, incluindo as páginas de contato, serviços, sobre, e a página inicial.

## Estrutura do Diretório

A estrutura do diretório `home` é organizada da seguinte forma:

```plaintext
📦home
 ┣ 📂migrations
 ┃ ┗ 📜__init__.py
 ┣ 📂static
 ┃ ┣ 📂contato
 ┃ ┃ ┣ 📜contato.css
 ┃ ┃ ┗ 📜contato.js
 ┃ ┣ 📂home
 ┃ ┃ ┣ 📜home.css
 ┃ ┃ ┗ 📜home.js
 ┃ ┣ 📂servicos
 ┃ ┃ ┣ 📜servicos.css
 ┃ ┃ ┗ 📜servicos.js
 ┃ ┗ 📂sobre
 ┃ ┃ ┣ 📜sobre.css
 ┃ ┃ ┗ 📜sobre.js
 ┣ 📂templates
 ┃ ┣ 📜contato.html
 ┃ ┣ 📜home.html
 ┃ ┣ 📜servicos.html
 ┃ ┗ 📜sobre.html
 ┣ 📜admin.py
 ┣ 📜apps.py
 ┣ 📜models.py
 ┣ 📜tests.py
 ┣ 📜urls.py
 ┣ 📜views.py
 ┗ 📜__init__.py
```

## Descrição dos Arquivos e Diretórios

- **migrations/**: Contém arquivos de migração do banco de dados.
- **static/**: Contém arquivos estáticos (CSS e JS) organizados por páginas.
  - **contato/**: Arquivos estáticos para a página de contato.
  - **home/**: Arquivos estáticos para a página inicial.
  - **servicos/**: Arquivos estáticos para a página de serviços.
  - **sobre/**: Arquivos estáticos para a página sobre.
- **templates/**: Contém arquivos HTML das páginas.
  - **contato.html**: Template para a página de contato.
  - **home.html**: Template para a página inicial.
  - **servicos.html**: Template para a página de serviços.
  - **sobre.html**: Template para a página sobre.
- **admin.py**: Configurações do administrador do Django para o app `home`.
- **apps.py**: Configurações da aplicação `home`.
- **models.py**: Definições dos modelos do banco de dados.
- **tests.py**: Testes automatizados para o app `home`.
- **urls.py**: Rotas do app `home`.
- **views.py**: Lógicas de visualização (views) para o app `home`.
- **__init__.py**: Arquivo que torna o diretório um módulo Python.

## Inicializando o App Django

Para inicializar um novo app no Django, você pode usar o seguinte comando:

```bash
python manage.py startapp nome_do_app
```