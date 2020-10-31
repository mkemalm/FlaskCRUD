$(function () {
    $("#warrantystart").datepicker();
});

$(function () {
    $("#warrantyend").datepicker();
});

$(document).ready(function () {
    $("#submithw").click(function (e) {
        if(!$.isNumeric($("#price").val())) {
            $('.warningdiv').text('Enter a valid price!');
            e.preventDefault(e);
        }
    });
});