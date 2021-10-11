# medicar
Desafio: Medicar; Sistema para gestão de consultas em uma clínica médica
<h1 id='sobre'>Medicar</h1>

Projeto realizado com Django e Rest Framework. Neste projeto, o desafio foi criar algo semelhante a um sistema de clínicas médicas.
Onde o usuário administrador loga em sua conta, podendo cadastrar especialidades médicas, médicos, agendas e marcar consultas.

Tabela de conteúdos
=================
<!--ts-->
   * [Sobre](#sobre)
   * [Tecnologias](#tecnologias)
   * [PIP](#pip)
   * [Iniciando](#iniciando)
   * [Salvando dados](#salvando-dados)
   * [Requisições usando Insomnia](#insomnia)
      * [GET Especialidade](#get-especialidade)
      * [GET Medicos](#get-medicos)
      * [GET Consultas](#get-consultas)
      * [GET Agendas](#get-agendas)
      * [POST Nova Consulta](#post-consulta)
      * [DELETE Consulta](#delete-consulta)
   * [Link's](#links)
   * [Criador](#criador)
<!--te-->

<h2 id='tecnologias'>Tecnologias</h2>

* Python versão 3.7.0
* Django versão 2.2.0
* Django Rest Framework versão 3.12.4
* Django Multiselectfield versão 0.1.12
 
<h2 id='pip'>Pip</h2>

### Backend (API)

* Para baixar o projeto siga as instruções abaixo:

```
git clone https://github.com/igorbezerra21/medicar.git

```

Você precisará de algumas bibliotecas para executar o projeto. As dependências estarão no arquivo [requeriments.txt](https://github.com/igorbezerra21/medicar/blob/master/requirements.txt) .

Para instalar os requisitos, basta executar no terminal:
```
$ pip install -r requeriments.txt

```


ATENÇÃO: Considere estar na mesma pasta que 'requirements.txt'.

Se você usa ambiente virtual (recomendado):

Instale o ambiente virtual:
```
$ python3 -m venv myvenv

```

Inicie o ambiente. Tenha o cuidado de colocar o caminho correto para o arquivo:
```
$ source ./myvenv/bin/activate

```

Após clonar o repositório, instale as dependências com o arquivo 'requirements.txt':
```
$ pip install -r requirements.txt
```

<h2 id='iniciando'>Iniciando</h2>

Considere as etapas anteriores da sessão PIP .
Seu banco de dados deve ser sincronizado, para fazer isso, digite os seguintes comandos no terminal:<br/>

OBS: Você deve estar no mesmo nível de diretório do arquivo manage.py!

* 1º
```
$ python manage.py migrate

```

* 2º
```
$ python manage.py makemigrations

```

* 3º

Agora será necessário criar o usuario administrador, para isso, execute o seguinte comando no terminal:
```
$ python manage.py createsuperuser

```

Será solicitado alguns dados, os mais importante é **Username** (nome de usuario) e **Password** (senha).

Agora com o banco de dados conectado e todas as tabelas criadas, inicie o servidor:
```
$ python manage.py runserver

```

Se estiver usando, certifique-se de ter o ambiente virtual em execução e na mesma pasta do arquivo manage.py .

<h2 id='salvando-dados'>Salvando dados</h2>

Neste projeto, foram seguidas todas as orientações repassadas para o projeto em questão [README.md](https://github.com/Intmed-Software/desafio/blob/master/backend/README.md)

Antes de qualquer coisa, para que você consiga realizar qualquer tipo de requisição a API, será necessário criar um Token para seu usuário. 
Na **Interface Administrativa do Django**, crie um Token o vinculando com seu usuário:

![Novo Token](https://github.com/igorbezerra21/imagens_readme.md/blob/main/token.png)

O Token pode ser acessado nessa aba:
![Resultado Token](https://github.com/igorbezerra21/imagens_readme.md/blob/main/tokengerado.png)

Usando a **Interface Administrativa do Django**, cadastre informações referente a **Especialidade** 
![Nova Especialidade](https://github.com/igorbezerra21/imagens_readme.md/blob/main/novaespecialidade.png)

cadastre tambem dados sobre o **Médico**.
![Novo Medico](https://github.com/igorbezerra21/imagens_readme.md/blob/main/novamedico.png)

Logo em seguida, será necessário criar uma **Agenda para o médico**
![Nova Agenda](https://github.com/igorbezerra21/imagens_readme.md/blob/main/novaagenda.png)

<h2 id='insomnia'>Requisições usando Insomnia</h2>

Para facilitar sua vida, na tabela abaxo segue um link para o download de um arquivo .json. 
Acesse e salve o arquivo, logo em seguida importe o mesmo pelo Insomnia, será criado um Workspace com
todas as requisições configuradas. Seu único trabalho será o de adicionar o [Token gerado](#salvando-dados) para o usuario! 

| Requisição | Link |
| --- | --- |
| `Todas requisições` | Link https://raw.githubusercontent.com/igorbezerra21/imagens_readme.md/main/Insomnia_2021-10-11.json |

<h4>Adicionando o Token</h4>

Em cada requisição, acesse a aba `Header` e adicione token do usuário.

![Substituindo Token](https://github.com/igorbezerra21/imagens_readme.md/blob/main/insomnia_token.png)

Faça esse procedimento para todas as requisições!

<h4>GET Especialidades</h4>

Para consultar todas as especialidades basta usar a requisição `http://127.0.0.1:8000/especialidades/` 

![GET Especialidade](https://github.com/igorbezerra21/imagens_readme.md/blob/main/insomnia/todasespecialidades.png)

Para procurar uma especialidade específica, basta passar o paramêtro `search` -> `http://127.0.0.1:8000/especialidades/?search=car`

![GET Filtro Especialidade](https://github.com/igorbezerra21/imagens_readme.md/blob/main/insomnia/filtroespecialidade.png)

<h4>GET Médicos</h4>

Para consultar todos os médicos, basta usar a requisição `http://127.0.0.1:8000/medicos/` 

![GET Especialidade](https://github.com/igorbezerra21/imagens_readme.md/blob/main/insomnia/todososmedicos.png)

Para procurar um médico específico, você pode utilizar os paramêtros `search` e `especialidade` -> `http://127.0.0.1:8000/medicos/?search=igor&especialidade=2&especialidade=1`

![GET Filtro Especialidade](https://github.com/igorbezerra21/imagens_readme.md/blob/main/insomnia/filtromedico.png)

<h4>GET Consultas</h4>

Para buscar todas as consultas, use a requisição: `http://127.0.0.1:8000/consultas/` <br/>
OBS: Será mostrado apenas as consultas que pertecem ao usuário logado!

![GET Consulta](https://github.com/igorbezerra21/imagens_readme.md/blob/main/insomnia/todasconsultas.png)

<h4>GET Agendas</h4>

Todas as agendas disponivéis poderão ser acessadas a partir da requisição `http://127.0.0.1:8000/agenda/` 

![GET Agendas](https://github.com/igorbezerra21/imagens_readme.md/blob/main/insomnia/todasagendas.png)

Você poderá filtrar as agendas disponiveis utilizando alguns filtros: Por `medico` e/ou `especialidade`;<br/> 
Como tambem por intervalo de data: <br/>
`data_inicio` & `data_final` -> `http://127.0.0.1:8000/agenda/?medico=2&especialidade=2&data_inicio=2021-10-20&data_final=2021-10-31`

![GET Filtro Agenda](https://github.com/igorbezerra21/imagens_readme.md/blob/main/insomnia/filtroagenda.png)

Você poderá usar os quatros juntos, como no exemplo acima, como também separadamente:<br/>
Por `medico` -> `http://127.0.0.1:8000/agenda/?medico=2` <br/>
Por `especialidade` -> `http://127.0.0.1:8000/agenda/?especialidade=2` <br/>
Por `medico` & `especialidade` -> `http://127.0.0.1:8000/agenda/?medico=2&especialidade=2` <br/>
Por `data_inicio` & `data_final` -> `http://127.0.0.1:8000/agenda/?data_inicio=2021-10-20&data_final=2021-10-31` 

<h4>POST Consulta</h4>

Para marcar uma nova consulta, você usará uma requisicão do tipo `POST` passando o json com o `id_agenda`, junto com o `horario` disponível na respectiva agenda:

![POST Consulta](https://github.com/igorbezerra21/imagens_readme.md/blob/main/insomnia/novaconsulta.png)

<h4>DELETE Consulta</h4>

Para desmarcar uma consulta, envie uma requisição DELETE passando o id da consulta:
`http://127.0.0.1:8000/consultas/5`

![DELETE Consulta](https://github.com/igorbezerra21/imagens_readme.md/blob/main/insomnia/deletarconsulta.png)

<h2 id='link'>Link's</h2>
 
- Repositório: https://github.com/igorbezerra21/medicar
     - Em caso de dúvidas ou sugestões, fique à vontade para entrar em contato e/ou solicitar **pull requests**. 
 
 
<h2 id='criador'>Criador</h2>
  
* **Igor Bezerra Reis**: @igorbezerra21 (https://github.com/igorbezerra21)
