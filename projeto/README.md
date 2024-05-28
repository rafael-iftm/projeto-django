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

### Comando `python manage.py collectstatic`

O comando `python manage.py collectstatic` é usado para coletar todos os arquivos estáticos do seu projeto em um único diretório, facilitando a sua gestão e disponibilização.

```python
python manage.py collectstatic
```

#### Arquivos Estáticos (CSS, JavaScript, Imagens)

Os arquivos estáticos, como CSS, JavaScript e imagens, são essenciais para a aparência e a funcionalidade do seu site. No Django, você configura e gerencia esses arquivos através de algumas variáveis no arquivo `settings.py`.

```python
# Configuração para arquivos estáticos
STATIC_URL = "static/"
STATICFILES_DIRS = [
    BASE_DIR / "base_static",
]
STATIC_ROOT = BASE_DIR / "static"
```

- **`STATIC_URL`**: Define a URL pública onde os arquivos estáticos serão acessíveis.
- **`STATICFILES_DIRS`**: Lista de diretórios onde o Django também deve procurar arquivos estáticos além das aplicações instaladas.
- **`STATIC_ROOT`**: Diretório onde todos os arquivos estáticos coletados serão armazenados.

Quando você executa o comando `python manage.py collectstatic`, o Django coleta todos os arquivos estáticos das suas aplicações e dos diretórios listados em `STATICFILES_DIRS`, copiando-os para o diretório definido em `STATIC_ROOT`. Isso é especialmente útil em ambientes de produção, onde um servidor web pode servir esses arquivos diretamente.

Para mais informações sobre a gestão de arquivos estáticos no Django, consulte a documentação oficial em [Django Static Files](https://docs.djangoproject.com/en/5.0/howto/static-files/).
