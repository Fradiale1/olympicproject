function deleteAthlete(athleteId) {
    {
        fetch(`/athletes/delete/${athleteId}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => {
            if (response.ok) {
                // Remove the athlete row from the table
                document.querySelector(`tr[data-athlete-id="${athleteId}"]`).remove();
            } else {
                alert('Failed to delete the athlete.');
            }
        });
    }
}