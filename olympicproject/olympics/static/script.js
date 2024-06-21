document.getElementById('yearForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const startYear = document.getElementById('startYear').value;
    const endYear = document.getElementById('endYear').value;

    fetch(`/api/frequent-fifas?start_year=${startYear}&end_year=${endYear}`)
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector('#resultsTable tbody');
            tableBody.innerHTML = '';  // Svuota la tabella
            data.forEach(fifa => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${fifa.destination}</td>
                    <td>${fifa.count}</td>
                `;
                tableBody.appendChild(row);
            });
        });
});
