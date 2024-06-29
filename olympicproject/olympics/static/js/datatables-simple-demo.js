window.addEventListener('DOMContentLoaded', event => {
    $(document).ready(function() {
        var table = $('#datatablesSimple').DataTable({
            initComplete: function () {
                // Clona la riga dell'intestazione e la aggiunge sotto l'intestazione originale
                $('#datatablesSimple thead tr').clone(true).addClass('search-row').appendTo('#datatablesSimple thead');

                this.api()
                    .columns()
                    .every(function (index) {
                        var column = this;

                        // Nella seconda riga di intestazione (index 1) aggiungi l'input di ricerca
                        $('thead tr.search-row th:eq(' + index + ')').html('<input type="text" placeholder="Search ' + $(column.header()).text() + '" />');

                        // Aggiungi il listener per la ricerca
                        $('thead tr.search-row th:eq(' + index + ') input').on('keyup change clear', function () {
                            if (column.search() !== this.value) {
                                column.search(this.value).draw();
                            }
                        });

                        // Ferma la propagazione del click sugli input di ricerca
                        $('thead tr.search-row th:eq(' + index + ') input').on('click', function (e) {
                            e.stopPropagation();
                        });
                    });
            }
        });
    });
});