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
    document.querySelector('#DisciplineTitleCreate').value = '';
    document.querySelector('#EventTitleCreate').value = '';
    document.querySelector('#SlugGameCreate').selectedIndex = 0;
    document.querySelector('#ParticipantTypeCreate').selectedIndex = 0;
    document.querySelector('#RankEqualCreate').selectedIndex = 0;
    document.querySelector('#RankPositionCreate').value = '';
    document.querySelector('#CountryNameCreate').value = '';
}

//per la modifica dell'atleta
function openUpdateModal(resultId) {
    document.querySelector('#resultIdInputUpdate').value = resultId;

    fetch("/results/getById/"+ resultId, {
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
    document.querySelector('#EventTitleUpdate').value = data.event_title;
    document.querySelector('#SlugGameUpdate').value = data.slug_game;
    document.querySelector('#ParticipantTypeUpdate').value = data.participant_type;
    document.querySelector('#RankEqualUpdate').value = data.rank_equal;
    document.querySelector('#RankPositionUpdate').value = data.rank_position;
    document.querySelector('#CountryNameUpdate').value = data.country_name;
}

//per l'eliminazione dell'atleta
function openDeleteModal(resultId) {
    document.querySelector('#resultIdInputDelete').value = resultId;
}

