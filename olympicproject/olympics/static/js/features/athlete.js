window.onload = function() {
    const datiDaPassare = getCookie('message');
    //const datiDaPassare = JSON.parse(localStorage.getItem('datiDaPassare'));
    
    console.log(datiDaPassare);
};

//per la creazione dell'atleta
function openCreateModal() {
    setCreateFieldModal();
}

function setCreateFieldModal(){
    document.querySelector('#FullnameCreate').value = '';
    document.querySelector('#NPartCreate').value = '';
    document.querySelector('#FirstGameCreate').selectedIndex = 0;
    document.querySelector('#YearBirthCreate').value = '';
    document.querySelector('#MedalsCreate').value = '';
}

//per la modifica dell'atleta
function openUpdateModal(athleteId) {
    document.querySelector('#athleteIdInputUpdate').value = athleteId;

    fetch("/athletes/getById/"+ athleteId, {
        method: 'GET',
        /*headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(json)*/
    })
    .then(response => {
        if (response.ok) {
          return response.text();
        } else {
          throw new Error('Errore nella richiesta.');
        }
    })
    .then(data => {
        data = JSON.parse(data);
        setUpdateFieldModal(data);
    })
    .catch(error => {
        console.error(error);
    });
}

function setUpdateFieldModal(data){
    document.querySelector('#FullnameUpdate').value = data.athlete_full_name;
    document.querySelector('#NPartUpdate').value = data.games_participations;
    document.querySelector('#FirstGameUpdate').value = data.first_game;
    document.querySelector('#YearBirthUpdate').value = data.athlete_year_birth;
    document.querySelector('#MedalsUpdate').value = data.athlete_medals;
}

//per l'eliminazione dell'atleta
function openDeleteModal(athleteId) {
    document.querySelector('#athleteIdInputDelete').value = athleteId;
}