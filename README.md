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