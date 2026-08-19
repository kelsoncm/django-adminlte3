# Django Admin LTE v3 Theme 🎨

[![PyPI version](https://badge.fury.io/py/django-admintheme-adminlte3.svg)](https://badge.fury.io/py/django-admintheme-adminlte3)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Tema moderno baseado no **AdminLTE 3** adaptado nativamente para a interface de administração do Django Admin.

> 📚 **Documentação Oficial e Suíte**: Para guias completos, visão geral de arquitetura e outros temas da organização, visite [django-adminthemes.github.io](https://django-adminthemes.github.io).

---

## Como Usar

### 1. Instalação via pip

```bash
pip install django-admintheme-adminlte3
```

### 2. Configuração no `settings.py`

Adicione `'adminlte3'` ao `INSTALLED_APPS` **antes** de `'django.contrib.admin'`:

```python
INSTALLED_APPS = [
    'adminlte3',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # ...
]
```

### 3. Coleta de Arquivos Estáticos

```bash
python manage.py collectstatic --noinput
python manage.py runserver
```

---

## Desenvolvimento Local (Workspace Privado)

Para contribuir ou testar alterações neste repositório em conjunto com o ecossistema **Django Admin Themes**, utilize o ambiente orquestrado do `workspace`:

```bash
# 1. Clone o repositório workspace privado
git clone git@github.com:django-adminthemes/workspace.git ~/projetos/PESSOAL/django-adminthemes/workspace
cd ~/projetos/PESSOAL/django-adminthemes/workspace

# 2. Inicialize o ambiente (clona repositórios e configura atalhos)
./dbkw setup

# 3. Suba o container do AdminLTE3 em modo de desenvolvimento
dbkw launch adminlte3
```

Para mais detalhes sobre o workflow de desenvolvimento e atalhos CLI, consulte a documentação do [workspace/README.md](https://github.com/django-adminthemes/workspace).

---

## 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE.md` para mais informações.
