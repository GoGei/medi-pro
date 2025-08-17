$(document).ready(function () {
    const $breadcrumb = $("ol.breadcrumb");
    $breadcrumb.find("li").last().addClass("active");

    const $lastLink = $("ol.breadcrumb li").last().find("a");
    $lastLink.wrapInner("<strong></strong>");
});
