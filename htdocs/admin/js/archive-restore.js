$('.action-archive').click(function (e) {
    e.preventDefault();
    const $btn = $(this);

    const title = $btn.data('title') || "Are you sure?";
    const text = $btn.data('text') || "This object will be archived";
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
            success: function () {
                swal(complete, completeText, "success");
            },
            error: function (xhr) {
                swal("Error", "Something went wrong", "error");
            }
        });
    });
});
