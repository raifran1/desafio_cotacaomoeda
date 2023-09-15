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