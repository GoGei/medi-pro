DEFAULT_PAGE_SIZE = 50;

function getQueryData(params) {
    return {
        search: params.term,
        page: params.page,
        limit: DEFAULT_PAGE_SIZE,
        offset: DEFAULT_PAGE_SIZE * params.page || 0,
        format: 'json'
    };
}


function processResults(data, params) {
    params.page = params.page || 1;
    return {
        pagination: {
            more: Boolean(data.next)
        },
        results: $.map(data.results, function (obj) {
            return {
                id: obj.id,
                text: obj.label
            };
        })
    }
}

function processResultsWithTags(data, params) {
    params.page = params.page || 1;
    let results = $.map(data.results, function (obj) {
        return {
            id: obj.id,
            text: obj.label
        };
    });

    // Check if the search term exists in the current results
    let termExists = data?.results?.length != 0;

    // If the search term doesn't exist, add it as a new tag
    if (!termExists && params.term.trim() !== '') {
        let txt = params.term.trim();
        results.push({
            id: txt,
            text: txt
        });
    }

    return {
        pagination: {
            more: Boolean(data.next)
        },
        results: results
    };
}


function constructSelect2($field, ajaxUrl, with_parent = false, process_data = getQueryData, process_result = processResults, ajaxAttrs = {}) {
    let select2Config = {
        allowClear: true,
        placeholder: $field.attr('placeholder'),
        width: '100%',
        ajax: {
            url: ajaxUrl,
            method: 'GET',
            dataType: 'json',
            delay: 250,
            ...ajaxAttrs,
            data: function (params) {
                return process_data(params);
            },
            processResults: function (data, params) {
                return process_result(data, params);
            }
        }
    };

    if (with_parent) {
        select2Config['dropdownParent'] = $('#modal-form .modal-body');
    }

    $field.select2(select2Config);
}