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
    console.log(getCookie('csrftoken'));
    const $breadcrumb = $("ol.breadcrumb");
    $breadcrumb.find("li").last().addClass("active");

    const $lastLink = $("ol.breadcrumb li").last().find("a");
    $lastLink.wrapInner("<strong></strong>");
});

$.ajaxSetup({
    xhrFields: {withCredentials: true},
    headers: {'X-CSRFToken': getCookie('csrftoken')},
});
