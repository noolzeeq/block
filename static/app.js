 let host = "http://127.0.0.1:8000";
 function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
    let csrf;
$("#submit-code").click(function (e) {
    e.preventDefault();
     $.ajax({
        url: host + "/make_order/",
        type: "POST",
         headers: {'X-CSRFToken': csrftoken},
        data: {"number": $("#amount").val(),
        "type": $("#type").val(),
        "weight": $("#weight").val(),
        "date_of_shipment": $("#date_of_shipment").val(),
        "date_of_shipping": $("#date_of_shipping").val()},
        success: function (data) {
            window.location.href='/orders/';
        ;}
    });
});