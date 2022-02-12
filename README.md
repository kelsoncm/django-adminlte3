# My pet on-line #

1. Instale o virtualenvwrapper
2. Crie um virtualenv chamado mpo: `mkvirtualenv adminlte3`
3. Atualize o pip: `pip install --upgrade pip`
4. Instale os pacotes do projeto `pip install -r requirements.txt`
5. Migre o banco `python manage.py migrate`
7. Suba a aplicação (disponível em http://localhost:8000) `./manage.py runserver`
8. Se você alterar algum plugin `python manage.py makemigrations`
9. Para usar a interface REST
   1. http://localhost:8000/api/1.0/ ou http://localhost:8000/api/1.0/redoc/ ou http://localhost:8000/api/1.0/docs
   2. Para acessar via CLI será necessário um token que deve ser criado em http://localhost:8000/admin/authtoken/tokenproxy/
   3. Exemplo usando curl `curl -X GET "http://localhost:8000/api/1.0/users/" -H "accept: application/json" -H  "Authorization: Token 2b4c5da55199324d7c4500fcb01e975012577510"`, onde `2b4c5da55199324d7c4500fcb01e975012577510` que é importado no passo 6.
   4. Falta estudar estas outras autenticações https://www.django-rest-framework.org/api-guide/authentication/

```
export PYTHONBREAKPOINT=ipdb.set_trace
```