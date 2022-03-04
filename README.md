# web_scrapper

O site está disponível em https://scrapper-el.herokuapp.com

Essa aplicação Django realiza scrapping no site `http://free-proxy.cz/en/main/` trazendo os proxys e as informações sobre eles.

## Para rodar a aplicação:

Caso você possua docker-compose:
* ```docker-compose run --service-ports app bash``` para criar o container e iniciá-lo;
* ```python manage.py migrate``` para criar as tabelas no DB;
* ```python manage.py runserver 0.0.0.0:80000``` para rodar a aplicação no server

Caso você queira rodar localmente sem Docker:
* ```pip install -r requirements.txt```
* ```python manage.py migrate``` para criar as tabelas no DB;
* ```python manage.py runserver 0.0.0.0:80000``` para rodar a aplicação no server

## A aplicação:


Ela é bem simples, na página inicial você terá dois menus:
* O primeiro (a esquerda), corresponde ao commando para popular o DB (Bulk Create) ou para apagar todos os dados do DB (Bulk Delete), você seleciona a opção e clica em ```Do!```. O bulk create realizará o scrapping na página referida e após finalizado, carregará na tela inicial a tabela com os registros.

* O segundo formuláro é para cadastrar o usuário, para ter acesso ao admin panel. No admin panel, será possível acessar os registros salvos, editá-los, excluí-los, ou inserir algum novo manualmente.

## Pontos a melhorar:

* O scrapping consome um tempo considerável até finalizar (por volta de 1 minuto), seria interessante adicionar uma thread para que ele rode no background e a pessoa possa sair da página, enquanto a tarefa é realizada.

* Adicionar filtros na página inicial, atualmente a página incial renderiza todos os registros contidos no banco de dados, fazendo com que quanto mais registros, mais lenta a resposta do site. Seria bom adicionar filtros e particionar a tabela para que não sejam todos carregados ao mesmo tempo.