$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})
$(document).ready(function () {
    $('#sistem-table').DataTable({
        "columnDefs": [
            { "orderable": false, "targets": 4 }
        ]
    });
});