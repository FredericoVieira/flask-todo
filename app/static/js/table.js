$(document).ready(function() {
    var table = $('#todo-table').DataTable( {
        "sAjaxSource": "/all",
        "sAjaxDataProp": "tasks",
        "aoColumnsDefs": [
            { "data": "id" },
            { "data": "name" },
            { "data": "description" },
            { "data": "status" }
        ],
        "columns": [
            {"width": "5%"},
            {"width": "25%"},
            null,
            {"width": "13%"},
        ]
    });

    $('#todo-table tbody').on('click', 'tr', function(){
        if ($(this).hasClass('selected')){
            $(this).removeClass('selected');
        }
        else {
            table.$('tr.selected').removeClass('selected');
            $(this).addClass('selected');
        }
    });

    $('#delete').click(function(){
        table_line = table.row('.selected')[0]
        row_id = table.data()[table_line][0]

        $.post("/delete/"+row_id,
            function(){
                alert("Tarefa deletada com sucesso!");
            }
        );
        table.row('.selected').remove().draw(false);
    });

    $('#edit').click(function(){
        table_line = table.row('.selected')[0]
        row_id = table.data()[table_line][0]

        window.location.href = "/edit/"+row_id;
    });

    $('#show').click(function(){
        table_line = table.row('.selected')[0]
        row_id = table.data()[table_line][0]

        window.location.href = "/show/"+row_id;
    });
});