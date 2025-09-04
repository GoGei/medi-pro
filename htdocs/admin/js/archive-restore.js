$(document).on('click', '.action-archive, .action-restore', function (e) {
    e.preventDefault();
    const $btn = $(this);
    const isArchive = $btn.hasClass('action-archive');

    const title = $btn.data('title') || "Are you sure?";
    const text = $btn.data('text') || (isArchive ? "This object will be archived" : "This object will be restored");
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

                const $row = $btn.closest('tr');
                const $isActiveTd = $row.find('.table-is-active-field');

                if (response.is_active) {
                    $isActiveTd.html('<span class="true">✔</span>');
                    $btn.removeClass().addClass('btn btn-danger action-archive');
                    $btn.attr('href', $btn.attr('href').replace('restore', 'archive'));
                    $btn.html('<i class="fa fa-trash"></i>');
                } else {
                    $isActiveTd.html('<span class="false">✘</span>');
                    $btn.removeClass().addClass('btn btn-info action-restore');
                    $btn.attr('href', $btn.attr('href').replace('archive', 'restore'));
                    $btn.html('<i class="fa fa-refresh"></i>');
                }
            },
            error: function (response) {
                const text = response?.responseJSON?.msg || "Something went wrong";
                swal("Error", text, "error");
            }
        });
    });
});
