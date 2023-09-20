


window.onload = function() {
  function loadChart(initial_date=null, end_date=null, coin='BRL', initial=false){
    // Função que irá montar o gráfico

    // Definindo url e parâmetros de consulta na api do sistema
    let url = '/api/quotationcoin-graphic/';
    let params = '';

    if (initial_date){
      if (params == ''){
        params += '?initial_date=' + initial_date
      } else {
        params += '&initial_date=' + initial_date
      }
    }

    if (end_date){
      if (params == ''){
        params += '?end_date=' + end_date
      } else {
        params += '&end_date=' + end_date
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
    .then((obj) => {
      // Após receber a Promisse é feito algumas iterações para montar objetos para serem usados na função Highcharts
      series_list = [];

      obj['coins'].forEach((obj_coin) => {
        let values_list_cotation = [];

        // filtra os valores de dados de acordo com o acronimo das siglas
        values = obj['graphic'].filter(val => (val['coin'] == obj_coin['acronym']));

        values.forEach((val) => {
          // monta uma lista dos valores que persiste na mesma ordenação das datas enviadas via sistema
          values_list_cotation.push(val['data']['value']);
        });

        // Dicionário com um obj da serie de elementos possiveis para visualização no gráfico
        dict_serie = {
          'name': obj_coin['name'],
          'data': values_list_cotation,
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
    });
  }

  setTimeout(() => {
    // Carregando o filtro dos ultimos 5 dias úteis com a cotação USD -> BRL por padrão
    loadChart(null, null, 'BRL', true);
  }, 500);

  function filtro() {
    // Função para executar o filtro que o usuário fizer na pagina para busca de uma determinada cotação

    // captura de informações os campos inputs
    let initial_date = document.getElementById('initial-date');
    let end_date = document.getElementById('end-date');
    let coin = document.getElementById('coin').value;

    if (initial_date.value && end_date.value && initial_date.valueAsDate > end_date.valueAsDate){
      alert('A data inicial não pode ser maior que a data final');
    } else {
      // loading botão filtro
      document.getElementById('loading-filter').setAttribute('class', 'spinner-grow spinner-grow-sm');
      // envia para a api
      loadChart(initial_date.value, end_date.value, coin);
    }
  }

  // capturar evento do click no botão do filtro
  document.getElementById("filtro").addEventListener("click", filtro, false);


  function changeDtInitial(){

  }
};