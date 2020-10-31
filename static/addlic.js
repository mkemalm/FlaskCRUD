$(function () {
    $("#licstart").datepicker();
});

$(function () {
    $("#licend").datepicker();
});

$(document).ready(function () {
    $("#submitlic").click(function (e) {
        if(!$.isNumeric($("#licprice").val())) {
            $('.warningdiv').text('Enter a valid price!');
            e.preventDefault(e);
        }
        if(!$.isNumeric($("#licnumber").val())) {
            $('.warningdiv').text('Enter a valid number!');
            e.preventDefault(e);
        }
    });
});