## Projeto cotação de moedas online (desafio_cotacaomoeda)

- Desenvolvedor Raifran Lucas (github: @raifran1)

### O projeto consiste basicamente em uma página de cotação entre a moeda USD ($) para as moedas EUR / BRL / JPY

#### Escopo
``` 
Preciso de um sistema que guarde as cotações do dólar versus real, euro e iene(JPY) e que as exibe em um gráfico, 
respeitando as seguintes especificações:

* Deve ser possível informar uma data de início e de fim para consultar qualquer período de tempo, contanto que o período informado seja de no máximo 5 dias úteis.
* Deve ser possível variar as moedas (real, euro e iene).
```

#### Regras de negócio
```
* Os dados das cotações devem ser coletados utilizando a api do https://www.vatcomply.com/documentation (Você vai precisar usar Dólar como base).
* O código deve ser desenvolvido utilizando um repositório git no seu perfil do Github ou BitBucket;
* Backend: deve ser implementado em python utilizando o framework django.
* Frontend: o único requisito é usar o highcharts para apresentação dos dados.
* Não precisa de login, usuário, autenticação ou qualquer coisa. Só a página carregando o gráfico.
```

#### Extras
```
* Deploy no heroku ou em outro servidor de sua preferência.
* Criar uma api para realizar leitura das cotações persistidas no banco de dados.
```


## Sistema
### Admin
```
O sistema do admin foi customizado utilizando o django-jet, e com umas customizações específicas a mais como jet-sidebar 
que é uma biblioteca de autoria minha que usa o django-jet como base. Junto a ela coloquei dentro da aplicação um arquivo css e html,
que é uma atualização desse front que está sendo trabalhada ainda para ser lançada em versão futura do jet-sidebar.

url da biblioteca: https://pypi.org/project/jet-sidebar/
gihub: https://github.com/raifran1/jet-sidebar
```

### Frontend 
```
Foi utilizado um frontend integrado com o django usando o framework bootstrap para montagem do layout, teve o uso de javascript
para carregar dados da api do próprio sistema e gerar o gráfico do Highcharts. Nos filtros foi usado a biblioteca datepicker 
e jQuery e Javascript para manipulação das regras de negócio de apresentação das datas.
```

- Para modelagem do frontend foi feito um esboço no figma ```https://www.figma.com/file/NlbN3m4fB46e7hEZOlvSje/CotaON?type=design&node-id=0%3A1&mode=design&t=dmyH9iqJmCxPLRTS-1```

### Backend
```
Foi utilizado Python e Django como a base do sistema, MySQL como banco de dados do sistema para persistir os dados, Django Rest Framework para API
e por fim a workdays para ajuda no calculo de dias úteis por padrão no carregamento do gráfico.
```

- Para modelagem do banco de dados foi feito um esboço no Diagrams ```https://drive.google.com/file/d/1aNlHnfQf_zfXjdd6eaiRiBV33jjy7Eh9/view?usp=sharing```

- Banco de dados: é persistido o cadastro de todas as moedas, e todas as suas cotações separado por data.

- Scripts: Foi-se criado scripts no manage do django para auxiliar na população do banco de dados e atualização do mesmo. Sendo os dois ```python manage.py import_coins``` esse comando importará todas as moedas, siglas e simbolos e persistirá em banco de dados, e ```python manage.py import_cotation``` importa a cotação do dia, segundo documentação do vatcomply a mesma atualiza às 11h (Horário de Brasília), porém esse comando não é obrigatoriamente necessária sua execução via cron ou algo agendado pois o sistema foi feito para se auto alimentar e persistir de acordo com o uso e filtros feitos pelo usuário no frontend ou API.

- API 
  - Link da documentação ```https://documenter.getpostman.com/view/6751701/2s9YCARAgj```

  - ```https://cotaon.raifranlucas.dev/api/coins/```: lista todas as moedas persistidas em banco de dados
  - ```https://cotaon.raifranlucas.dev/api/quotationcoin-graphic/```: lista todas as cotações em um período e moeda específica, por padrão ele retorna as cotações dos últimos 5 dias e o Real Brasileiro;
    - initial_date (aaaa-mm-dd): captura a data inicial que a API deve utilizar para retornar os dados
    - end_date (aaaa-mm-dd): captura a data final que a API deve utilizar para retornar os dados
    - coin_acronym: moedas que a api pode retornar, para isso é usado a sigla da moeda (BRL) nesse filtro. Também é possivel carregar multiplas moedas passando elas separado por virgula (BRL,USD)
  

