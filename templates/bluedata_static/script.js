
// Exibe a mensagem via toastr
//
function show_message(tag, message) {
    if(tag == 'success')
        toastr.success(message);
    else if(tag == 'info')
        toastr.info(message);
    else if(tag == 'warning')
        toastr.warning(message);
    else
        toastr.error(message);
}


// Modifica o is_active do registro
//
function toggle_active(url_str) {
    token = document.getElementsByName('csrfmiddlewaretoken')[0].value;

    $.ajax({
        type: 'POST',
        url: url_str,
        data: { csrfmiddlewaretoken: token },
        success: function(result) {
            location.reload();
        }
    });
}


/* customização do toastr */
toastr.options = {
  "closeButton": false,
  "debug": false,
  "newestOnTop": true,
  "progressBar": true,
  "positionClass": "toast-top-right",
  "preventDuplicates": true,
  "onclick": null,
  "showDuration": "300",
  "hideDuration": "1000",
  "timeOut": "4000",
  "extendedTimeOut": "1000",
  "showEasing": "swing",
  "hideEasing": "linear",
  "showMethod": "fadeIn",
  "hideMethod": "fadeOut"
};