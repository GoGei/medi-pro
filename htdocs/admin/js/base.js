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

$(document).ready(function () {
    const $breadcrumb = $("ol.breadcrumb");
    $breadcrumb.find("li").last().addClass("active");

    const $lastLink = $("ol.breadcrumb li").last().find("a");
    $lastLink.wrapInner("<strong></strong>");

    bsCustomFileInput.init();

    // Form init
    $('.timepicker').datetimepicker({format: 'HH:mm:ss'});
    $('.datepicker').datetimepicker({format: 'YYYY-MM-DD'});
    $('.datetimepicker').datetimepicker({format: 'YYYY-MM-DD HH:mm:ss'});
    $('.uuid-inputmask').each(function () {
        const maskObj = $(this).data('mask');
        $(this).mask(maskObj.mask, {
            translation: {
                'h': {pattern: /[0-9a-fA-F]/}
            }
        });
    });
    $(".select2").select2({
        theme: 'bootstrap4',
    });
    $('.tagsinput').tagsinput({
        tagClass: 'label label-primary'
    });
    $('.i-checks').iCheck({
        checkboxClass: 'icheckbox_square-green',
        radioClass: 'iradio_square-green'
    });
    $('.colorpicker').colorpicker();
});

$.ajaxSetup({
    xhrFields: {withCredentials: true},
    headers: {'X-CSRFToken': getCookie('csrftoken')},
});
