# join-prova-tecnica

Requisitos para instalação
-----------------------------------
- Python 3.6+
## Setup
Clone o repositório
```sh
$ git clone https://github.com/gabrielmtararam/join-prova-tecnica.git
```
Crie o virtual environment and instale as dependencias
```sh
$ virtualenv --no-site-packages venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
Instale e configuere o banco de dados desejado, após isso insira
as configuracoes com o django no arquivo local_settings.py contido na 
mesma pasta que o settings, segue um exemplo abaixo para postgresql
```sh
$ nano ./prova/prova/local_settings.py
```
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'nome_do_banco',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': 'localhost',                     
        'PORT': '',                      
    }
}
```
Se desejar configure um servidor como apache ou nginx 
para servir a aplicação (ignore o ultimo comando) ou sirva conforme
abaixo
```sh
$ python manage.py migrate
$ python manage.py collectstatic
$ python manage.py runserver 
```
## Nota
Alguns recursos estão pendentes como passar a realizar as operações
de exclusão, atualização e cadastro de marcadores através de ajax
para poder exibir os possíveis erros no modal. Por enquanto o erros são tratados
no servidor, porem não são exibidos ao usuario.

Além disso existe o problema que caso a tela tenha suas dimensões alteradas a API de exibição de mapas exige que
a página seja recarregada para renderizar com novas dimensões.

Previsão para estar hospedado a partir de terça 11/01/2022 em:

[Exemplo](45.82.75.75:8001)
(Esse link será atualizado assim que o servidor estiver configurado)

