# Django Admin LTE v3 theme

1. [Instale o virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)
2. Crie um virtualenv chamado mpo: `mkvirtualenv djang-adminlte3`
3. Atualize o pip: `pip install --upgrade pip`
4. Instale os pacotes do projeto `pip install -r requirements.txt`
5. Migre o banco `python manage.py migrate`
7. Suba a aplicação (disponível em http://localhost:8000) `./manage.py runserver_plus`
8. Se você alterar algum plugin `python manage.py makemigrations`
9. Defina o ipdb como default breackpoint `export PYTHONBREAKPOINT=ipdb.set_trace`
10. Criar super usuário `python3 manage.py createsuperuser

### Como gerar uma nova release

1. No arquivo `setup.py`, incremente o número da versão
2. No arquivo `setup.py`, se foi criada uma nova pasta em `templates` ou em  `static`, adicione estas pastas usuando as demais como exemplo
3. Teste localmente:
    1. Crie a dist: `python setup.py sdist`
    2. Teste se está tudo lá: `untar dist/django-theme-adminlte3-3.2.0.*`
    3. Apague o lixo: `rm -rf dist django_theme_adminlte3.egg-info  django-theme-adminlte3-3.2.0.*`
4. Crie uma tag com o nome da igual à `version` do arquivo `setup.py`
5. Faça um push da tag
