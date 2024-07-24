$(document).ready(function() {
    $('#disciplineSelect').change(function() {
        const selectedDiscipline = $(this).val();

        if (!selectedDiscipline) {
            $('#eventSelect').prop('disabled', true);
            return;
        }

        $.ajax({
            url: "/results/get_event_by_discipline",
            method: 'GET',
            data: { discipline: selectedDiscipline},
            dataType: 'json',
            success: function(data) {
                $('#eventSelect').empty().append('<option value="">Seleziona il genere</option>');
                $.each(data, function(index, single_data) {
                    $('#eventSelect').append('<option value="'+ single_data.event_title +'">'+ single_data.event_title +'</option>');
                });

                $('#eventSelect').prop('disabled', false);
            },
            error: function(xhr, textStatus, errorThrown) {
                console.error('Errore durante la richiesta:', errorThrown);
                $('#eventSelect').prop('disabled', true);
            }
        });
    });
});