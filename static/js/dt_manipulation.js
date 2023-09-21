// iniciando campo de data final
$('#initial-date').datepicker({
  showOtherMonths: true,
  format: 'dd/mm/yyyy',
  maxDate: new Date(),
  disableDaysOfWeek: [0, 6]
});

// iniciando campo de data final
$('#end-date').datepicker({
  showOtherMonths: true,
  format: 'dd/mm/yyyy',
  maxDate: new Date(),
  disableDaysOfWeek: [0, 6]
});

// função para travar a mudança de datas no formulario para 5 dias úteis capturado pelo evento de edição de uma data
// no filtro de data inicial
$('#initial-date').change(function () {
  // valor inicial
  let valorInicial = $(this).val();

  // transforma em lista para facilitar a manipulação
  let formatDateWithList = valorInicial.split('/');

  // captura o dia em inteiro
  let day = parseInt(formatDateWithList[0]);
  let month = parseInt(formatDateWithList[1]);

  let lastDateOfMonth = new Date(formatDateWithList[2], formatDateWithList[1], 0).getDate();
  let iterouMes = false;

  // verifica e calcula qual seria a data limite para o campo de data final do formulário
  for(let i=0; i <= 4; i++){

    // iterador de mês para acrescentar quando a data ultrapassar certas regras de dias do mês
    if (lastDateOfMonth == 28 && !iterouMes && day == 28){
      console.log('itera mês 28');
      month += 1;
      day = 1;
      iterouMes = true;
    }else if (lastDateOfMonth == 31 && !iterouMes && day == 31) {
      console.log('itera mês 31');
      month += 1;
      day = 1;
      iterouMes = true;
    }else if (lastDateOfMonth == 30 && !iterouMes && day == 30) {
      console.log('itera mês 30');
      month += 1;
      day = 1;
      iterouMes = true;
    } else {
      // valida se o dia atual ta no limite da iteração de dias, se nao tiver incrementa
      day += 1;
    }

    // puxa a nova data
    let date = new Date(month + '/' +  day + '/' + formatDateWithList[2]);

    // valida se não é um fim de semana, caso seje final de semana é necessário ignorar
    if (date.getDay() in [0, 6]){
      day += 1;
    }
  }

  let dateFormat = new Date(month + '/' + day + '/' + formatDateWithList[2]);

  // reinicia o formulário de data final para adaptar as datas de inicio e fim
  $('#end-date').datepicker().destroy();

  $('#end-date').datepicker({
    showOtherMonths: true,
    format: 'dd/mm/yyyy',
    minDate: valorInicial,
    maxDate: dateFormat,
    disableDaysOfWeek: [0, 6]
  });
});

// função para travar a mudança de datas no formulario para 5 dias úteis capturado pelo evento de edição de uma data
// no filtro de data final
$('#end-date').change(function () {
  // valor inicial
  let valorEnd = $(this).val();

  // transforma em lista para facilitar a manipulação
  let formatDateWithList = valorEnd.split('/');

  // captura o dia em inteiro
  let day = parseInt(formatDateWithList[0]);
  let month = parseInt(formatDateWithList[1]);

  // captura o dia atual em inteiro
  let dayToday = new Date().getDate();

  let lastDateOfMonth = new Date(formatDateWithList[2], formatDateWithList[1], 0).getDate();
  let iterouMes = false;

  // verifica e calcula qual seria a data limite para o campo de data final do formulário
  for(let i=0; i <= 4; i++){

    if (!iterouMes && day == 1) {
      month -= 1;
      day = lastDateOfMonth;
      iterouMes = true;
    } else {
      // valida se o dia atual ta no limite da iteração de dias, se nao tiver incrementa
      day -= 1;
    }

    // puxa a nova data
    let date = new Date(month + '/' +  day + '/' + formatDateWithList[2]);

    // valida se não é um fim de semana, caso seje final de semana é necessário ignorar
    if (date.getDay() in [0, 6]){
      day -= 1;
    }
  }

  let dateFormat = new Date(month + '/' + day + '/' + formatDateWithList[2]);

  // reinicia o formulário de data final para adaptar as datas de inicio e fim
  $('#initial-date').datepicker().destroy();

  $('#initial-date').datepicker({
    showOtherMonths: true,
    format: 'dd/mm/yyyy',
    minDate: dateFormat,
    maxDate: valorEnd,
    disableDaysOfWeek: [0, 6]
  });
});
