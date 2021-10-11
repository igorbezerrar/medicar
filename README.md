# medicar
Desafio: Medicar; Sistema para gestão de consultas em uma clínica médica
<h1>Medicar</h1>

Projeto realizado com Django e Rest Framework. Neste projeto, o desafio foi criar algo semelhante a um sistema de clínicas médicas.
Onde o usuário administrador loga em sua conta, podendo cadastrar especialidades médicas, médicos, agendas e consultas.

<h2>Tecnologias</h2>

* Python versão 3.7.0
* Django versão 2.2.0
* Django Rest Framework versão 3.12.4
* Django Multiselectfield versão 0.1.12

<h2>Pip</h2>

Você precisará de algumas bibliotecas para executar o projeto. As inscrições estarão no arquivo [requeriments.txt](https://github.com/igorbezerra21/medicar/blob/master/requirements.txt) .

Para instalar os requisitos, basta executar no terminal:

"""
$ pip install -r requeriments.txt
"""

ATENÇÃO: Considere estar na mesma pasta que 'requirements.txt'.

Se você usa ambiente virtual (recomendado):

Instale o ambiente virtual:
$ python3 -m venv myvenv

Inicie o ambiente. Tenha o cuidado de colocar o caminho correto para o arquivo:
$ source ./myvenv/bin/activate

Após clonar o repositório, instale as dependências com o arquivo 'requirements.txt':
$ pip install -r requisitos.txt

<h2>Iniciando</h2>

Considere as etapas anteriores da sessão PIP .
Seu banco de dados deve ser sincronizado, para fazer isso, digite o comando no terminal:
$ python manage.py migrate

Você deve estar no mesmo nível de diretório do arquivo manage.py . Se houver algum problema, tente executar os dois comandos abaixo no terminal:
1º

$ python manage.py makemigrations

2º

$ python manage.py migrate

Agora com o banco de dados conectado e todas as tabelas criadas, inicie o servidor:
$ python manage.py runserver

Se estiver usando, certifique-se de ter o ambiente virtual em execução e na mesma pasta do arquivo manage.py .

<h2>Como usar</h2>
