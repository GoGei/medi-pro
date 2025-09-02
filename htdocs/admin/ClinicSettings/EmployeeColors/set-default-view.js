$(document).on('click', '.set-default-view', function (e) {
    e.preventDefault();
    const $btn = $(this);

    const title = $btn.data('title') || "Are you sure?";
    const text = $btn.data('text') || "This object will be set as default";
    const complete = $btn.data('complete') || "Completed!";
    const completeText = $btn.data('complete_text') || "Action was successfully performed";

    swal({
        title: title,
        text: text,
        type: "warning",
        showCancelButton: true,
        confirmButtonColor: "#DD6B55",
        closeOnConfirm: false
    }, function () {
        $.ajax({
            url: $btn.attr('href'),
            type: "POST",
            success: function (response) {
                swal(complete, completeText, "success");

                if (response.is_default) {
                    $('#is-default').html('<span class="label label-primary">Default</span>');
                }
            },
            error: function () {
                swal("Error", "Something went wrong", "error");
            }
        });
    });
});