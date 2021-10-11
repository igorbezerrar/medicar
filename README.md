# medicar
Desafio: Medicar; Sistema para gestão de consultas em uma clínica médica
<h1>Medicar</h1>

Projeto realizado com Django e Rest Framework. Neste projeto, o desafio foi criar algo semelhante a um sistema de clínicas médicas.
Onde o usuário administrador loga em sua conta, podendo cadastrar especialidades médicas, médicos, agendas e marcar consultas.

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
> $ pip install -r requirements.txt

<h2>Iniciando</h2>

Considere as etapas anteriores da sessão PIP .
Seu banco de dados deve ser sincronizado, para fazer isso, digite o comando no terminal:
> $ python manage.py migrate

Você deve estar no mesmo nível de diretório do arquivo manage.py . Se houver algum problema, tente executar os dois comandos abaixo no terminal:

1º

> $ python manage.py makemigrations

2º

> $ python manage.py migrate

3º

Agora será necessário criar o usuario administrador, para isso, execute o seguinte comando no terminal:

> $ python manage.py createsuperuser

Será solicitado alguns dados, os mais importante é **Username** (nome de usuario) e **Password** (senha).

Agora com o banco de dados conectado e todas as tabelas criadas, inicie o servidor:
> $ python manage.py runserver

Se estiver usando, certifique-se de ter o ambiente virtual em execução e na mesma pasta do arquivo manage.py .

<h2>Como usar</h2>

Neste projeto, foram seguidas todas as orientações repassadas para o projeto em questao [README.md](https://github.com/Intmed-Software/desafio/blob/master/backend/README.md)

Usando a **Interface Administrativa do Django**, cadastre informações referente a **Especialidade** 
![Nova Especialidade](https://github.com/igorbezerra21/imagens_readme.md/blob/main/novaespecialidade.png)

cadastre tambem dados sobre o **Médico**.
![Novo Medico](https://github.com/igorbezerra21/imagens_readme.md/blob/main/novamedico.png)

Logo em seguida, será necessário criar uma **Agenda para o médico**
![Nova Agenda](https://github.com/igorbezerra21/imagens_readme.md/blob/main/novaagenda.png)



 
 
## Links
 
- Repositório: https://github.com/igorbezerra21/medicar
     - Em caso de dúvidas ou sugestões, fique à vontade para entrar em contato e/ou solicitar **pull requests**. 
 
 
## Criador
 
* **Igor Bezerra Reis**: @igorbezerra21 (https://github.com/igorbezerra21)
