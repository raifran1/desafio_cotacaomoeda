


window.onload = function() {
  function loadChart(initialDate=null, endDate=null, coin='BRL', initial=false){
    // Função que irá montar o gráfico

    // Definindo url e parâmetros de consulta na api do sistema
    let url = '/api/quotationcoin-graphic/';
    let params = '';

    if (initialDate){
      if (params == ''){
        params += '?initial_date=' + initialDate
      } else {
        params += '&initial_date=' + initialDate
      }
    }

    if (endDate){
      if (params == ''){
        params += '?end_date=' + endDate
      } else {
        params += '&end_date=' + endDate
      }
    }

    if (coin){
      if (params == ''){
        params += '?coin_acronym=' + coin
      } else {
        params += '&coin_acronym=' + coin
      }
    }

    if (initial){
      // habilita o carregamento do grafico (efeito visual) -> Somente no primeiro carregamento do gráfico
      document.getElementById('div-graphic').setAttribute('class', 'col-lg-7 col-11 d-flex justify-content-center align-items-center');
      document.getElementById('graphic').setAttribute('class', 'd-none');
      document.getElementById('load-graphic').setAttribute('class', '');
    }

    // Fetch chamando a url de api com os parâmetros de filtro se houver
    fetch(url + params, {method: 'GET'})
      .then(response => response.json())
      .catch ((error) => {
        if (initial) {
          // executável somente no primeiro carregamento da pagina
          document.getElementById('load-graphic').setAttribute('class', 'd-none');
          document.getElementById('div-graphic').setAttribute('class', 'col-lg-7 col-11');
          document.getElementById('graphic').setAttribute('class', '');
        }
        // desabilita o loading do botão do filtro
        document.getElementById('loading-filter').setAttribute('class', 'spinner-grow spinner-grow-sm d-none');
      })
      .then((obj) => {
        // Após receber a Promisse é feito algumas iterações para montar objetos para serem usados na função Highcharts
        series_list = [];

        obj['coins'].forEach((objCoin) => {
          let valuesListCotation = [];

          // filtra os valores de dados de acordo com o acronimo das siglas
          values = obj['graphic'].filter(val => (val['coin'] == objCoin['acronym']));

          values.forEach((val) => {
            // monta uma lista dos valores que persiste na mesma ordenação das datas enviadas via sistema
            valuesListCotation.push(val['data']['value']);
          });

          // Dicionário com um obj da serie de elementos possiveis para visualização no gráfico
          dict_serie = {
            'name': objCoin['name'],
            'data': valuesListCotation,
            'color': '#1B6A5C'
          };

          series_list.push(dict_serie)
        });

        // desabilita o carregamento do grafico (efeito visual)
        setTimeout(() => {
          if (initial) {
            // executável somente no primeiro carregamento da pagina
            document.getElementById('load-graphic').setAttribute('class', 'd-none');
            document.getElementById('div-graphic').setAttribute('class', 'col-lg-7 col-11');
            document.getElementById('graphic').setAttribute('class', '');
          }
          // desabilita o loading do botão do filtro
          document.getElementById('loading-filter').setAttribute('class', 'spinner-grow spinner-grow-sm d-none');
        }, 300);

        // Instânciando o gráfico Highcharts do tipo Line usando os dataLabels
        Highcharts.chart('container', {
            chart: {
              type: 'line'
            },
            title: {
              text: ''
            },
            subtitle: {
              text: ''
            },
            xAxis: {
              categories: obj['dates']
            },
            yAxis: {
              title: {
                text: 'Cotação (1 USD)'
              }
            },
            plotOptions: {
              line: {
                dataLabels: {
                  enabled: true
                },
                enableMouseTracking: true
              }
            },
            series: series_list
        });
      })
  }

  setTimeout(() => {
    // Carregando o filtro dos ultimos 5 dias úteis com a cotação USD -> BRL por padrão
    loadChart(null, null, 'BRL', true);
  }, 500);

  function filtro() {
    // Função para executar o filtro que o usuário fizer na pagina para busca de uma determinada cotação

    // captura de informações os campos inputs

    //Nota: uso do jQuery em especifico para capturar a informação da data do datepicker
    let initialDate = null;
    let initialDateVal = $('#initial-date').datepicker().value();
    if (initialDateVal){
      let formatInitialDateList = initialDateVal.split('/');
      initialDate = formatInitialDateList[2] + '-' + formatInitialDateList[1] + '-' + formatInitialDateList[0];
    }

    let endDate = null;
    let endDateVal = $('#end-date').datepicker().value();
    if (endDateVal){
      let formatEndDateList = endDateVal.split('/');
      endDate = formatEndDateList[2] + '-' + formatEndDateList[1] + '-' + formatEndDateList[0];
    }

    let coin = document.getElementById('coin').value;

    // loading botão filtro
    document.getElementById('loading-filter').setAttribute('class', 'spinner-grow spinner-grow-sm');
    // envia para a api
    loadChart(initialDate, endDate, coin);
  }

  // capturar evento do click no botão do filtro
  document.getElementById("filtro").addEventListener("click", filtro, false);

};