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
    $('.tagsinput').tagsinput({
        tagClass: $(this).data('tagClass') || 'label label-primary'
    });
    $('.input-group.date').datepicker({
        startView: 1,
        todayBtn: "linked",
        keyboardNavigation: false,
        forceParse: false,
        autoclose: true,
        format: "dd/mm/yyyy"
    });
    $('.input-daterange').datepicker({
        keyboardNavigation: false,
        forceParse: false,
        autoclose: true
    });
    $('.i-checks').iCheck({
        checkboxClass: 'icheckbox_square-green',
        radioClass: 'iradio_square-green'
    });
    $('.colorpicker').colorpicker();
    $('.clockpicker').clockpicker();
    $(".select2").select2({
        theme: 'bootstrap4',
    });
    $(".touchspin").TouchSpin({
        buttondown_class: 'btn btn-white',
        buttonup_class: 'btn btn-white'
    });
    $('.dual_select').bootstrapDualListbox({
        selectorMinimalHeight: 160
    });
});

$.ajaxSetup({
    xhrFields: {withCredentials: true},
    headers: {'X-CSRFToken': getCookie('csrftoken')},
});
