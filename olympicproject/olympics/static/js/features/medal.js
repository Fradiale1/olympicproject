window.onload = function() {
    const datiDaPassare = getCookie('message');
    //const datiDaPassare = JSON.parse(localStorage.getItem('datiDaPassare'));
    
    console.log(datiDaPassare);
};

//per la creazione della medaglia
function openCreateModal() {
    setCreateFieldModal();
}

function setCreateFieldModal(){
    document.querySelector('#DisciplineTitleCreate').value = '';
    document.querySelector('#SlugGameCreate').selectedIndex = 0;
    document.querySelector('#EventTitleCreate').value = '';
    document.querySelector('#EventGenderCreate').selectedIndex = 0;
    document.querySelector('#MedalTypeCreate').selectedIndex = 0;
    document.querySelector('#ParticipantTypeCreate').selectedIndex = 0;
    document.querySelector('#ParticipantTitleCreate').value = '';
    document.querySelector('#AthleteNameCreate').value = '';
    document.querySelector('#CountryNameCreate').value = '';
}

//per la modifica della medaglia
function openUpdateModal(medalId) {
    document.querySelector('#medalIdInputUpdate').value = medalId;

    fetch("/medals/getById/"+ medalId, {
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
    document.querySelector('#DisciplineTitleUpdate').value = data.discipline_title;
    document.querySelector('#SlugGameUpdate').value = data.slug_game;
    document.querySelector('#EventTitleUpdate').value = data.event_title;
    document.querySelector('#EventGenderUpdate').value = data.event_gender;
    document.querySelector('#MedalTypeUpdate').value = data.medal_type;
    document.querySelector('#ParticipantTypeUpdate').value = data.participant_type;
    document.querySelector('#ParticipantTitleUpdate').value = data.participant_title;
    document.querySelector('#AthleteNameUpdate').value = data.athlete_full_name;
    document.querySelector('#CountryNameUpdate').value = data.country_name;
}

//per l'eliminazione della medaglia
function openDeleteModal(medalId) {
    document.querySelector('#medalIdInputDelete').value = medalId;
}