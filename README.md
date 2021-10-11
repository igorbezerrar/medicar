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

> $ pip install -r requeriments.txt


ATENÇÃO: Considere estar na mesma pasta que 'requirements.txt'.

Se você usa ambiente virtual (recomendado):

Instale o ambiente virtual:
> $ python3 -m venv myvenv

Inicie o ambiente. Tenha o cuidado de colocar o caminho correto para o arquivo:
> $ source ./myvenv/bin/activate

Após clonar o repositório, instale as dependências com o arquivo 'requirements.txt':
> $ pip install -r requisitos.txt

<h2>Iniciando</h2>

Considere as etapas anteriores da sessão PIP .
Seu banco de dados deve ser sincronizado, para fazer isso, digite o comando no terminal:
> $ python manage.py migrate

Você deve estar no mesmo nível de diretório do arquivo manage.py . Se houver algum problema, tente executar os dois comandos abaixo no terminal:

1º

> $ python manage.py makemigrations

2º

> $ python manage.py migrate

Agora com o banco de dados conectado e todas as tabelas criadas, inicie o servidor:
> $ python manage.py runserver

Se estiver usando, certifique-se de ter o ambiente virtual em execução e na mesma pasta do arquivo manage.py .

<h2>Como usar</h2>

Foram seguidas todas as orientações repassadas para o projeto em questao [README.md](https://github.com/Intmed-Software/desafio/blob/master/backend/README.md)

Upon accessing the server link, you will see the *HOME* page for unlogged in users.  
![Home para usuários não logados](https://github.com/Jackie098/my-wallet/blob/master/images-readme/01.home_without_login.png)

Create an account in the respective session. Enter user and investor data.  
![Criar conta](https://github.com/Jackie098/my-wallet/blob/master/images-readme/02.new_account_form.png)

Then, *LOGIN* with the registered user data.  
![Login de usuário](https://github.com/Jackie098/my-wallet/blob/master/images-readme/03.login_view.png)

Now we can view *HOME* for logged in users. Note the new options released in *nav-bar* as much as the summary of operations and investor information.  
![Home para usuários logados](https://github.com/Jackie098/my-wallet/blob/master/images-readme/04.home_logged.png)

With the user logged in, register your operations and specify whether it is a purchase or sale.  
![Registro de Operações](https://github.com/Jackie098/my-wallet/blob/master/images-readme/05.new_operation.png)

You can also view your operations (their history).  
![Histórico de Operações](https://github.com/Jackie098/my-wallet/blob/master/images-readme/06.history_operations.png)
