// toastr.options = {
//     positionClass: "toast-top-center toast-top-full-width",
//     preventDuplicates: true
// };

toastr.options = {
  closeButton: false,
  debug: false,
  newestOnTop: true,
  progressBar: true,
  positionClass: "toast-top-right",
  preventDuplicates: false,
  onclick: null,
  showDuration: 300,
  hideDuration: 1000,
  timeOut: 5000,
  extendedTimeOut: 1000,
  showEasing: "swing",
  hideEasing: "linear",
  showMethod: "fadeIn",
  hideMethod: "fadeOut"
}

// проверка данных формы
function validate_all() {
    let email = $("#emailInput").val();
    let login = $("#loginInput").val();
    let password = $("#passwordInput").val();

    let arr = {'email': email, 'login': login, 'password': password}

    // отправка json посредством XMLHttpRequest на бекенд
    let request = new XMLHttpRequest();
    request.open("POST", "check_registration", false);
    request.send(JSON.stringify(arr));

    // обработка данных с бекенда
    if (request.status === 200) {
        let data = JSON.parse(request.responseText);
        if ('status' in data && data.status === 'ok') {
            return true;
        } else if ('error' in data) {
            toastr.warning(data.error); // отображение ошибки в браузере
        }
    }
    return false;
}