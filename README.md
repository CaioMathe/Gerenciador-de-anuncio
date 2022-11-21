# Seazone-Code-Challenge

O projeto consiste no desenvolvimento de Api's com django rest para desenvolver um sistema de gerenciamento de imóveis, onde faz a integração de 3 tabelas distintas para a execução do sistema, onde pode criar um imóvel, vários anúncio para para esse imóvel e várias reservas para esse anúncio que está relacionado ao imóvel. Projeto com front-end que faz a execução de todas as api's: search, insert, updates e deletes.


Back-end: Django, Django Rest framework.
Front-end: Html, Css, Javascript, Ajax, Bootstrap.
Banco de dados: Sqlite3

Para executar: 

1° Fazer um git clone para a maquina de teste.

2° Realizar a instalação das bibliotecas utilizadas com o seguinte comando no terminal: "pip install -r requirements.txt".


3° Para iniciar o banco de dados primeiramente executar o comando: python manage.py makemigrations aplicativo, logo após executar: python manage.py migrate aplicativo


4° Para iniciar as fixures executar nessa sequencia os códigos: python manage.py loaddata imoveis_data.json, python manage.py loaddata anuncios_data.json, python manage.py loaddata reservas_data.json.


5° Após finalizar as instalações usar o comando: "python main.py runserver" para iniciar a aplicação.

