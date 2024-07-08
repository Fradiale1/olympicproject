window.onload = function() {
    const datiDaPassare = getCookie('message');
    //const datiDaPassare = JSON.parse(localStorage.getItem('datiDaPassare'));
    
    console.log(datiDaPassare);
};

//per la creazione dell'host
function openCreateModal() {
    setCreateFieldModal();
}

function setCreateFieldModal(){
   // document.querySelector('#SlugCreate').value = '';
    document.querySelector('#EndDateCreate').value = '';
    document.querySelector('#BeginDateCreate').value = "";
    document.querySelector('#LocationCreate').value = "";
    document.querySelector('#GameNameCreate').value = "";
    document.querySelector('#SeasonCreate').value = "";
    document.querySelector('#GameYearCreate').value = '';
}

//per la modifica dell'host
function openUpdateModal(hostId) {
    document.querySelector('#hostIdInputUpdate').value = hostId;

    fetch("/hosts/getById/"+ hostId, {
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
    document.querySelector('#SlugUpdate').value = data.game_slug;
    document.querySelector('#BeginDateUpdate').value = data.game_start_date;
    document.querySelector('#EndDateUpdate').value = data.game_end_date;
    document.querySelector('#LocationUpdate').value = data.game_location;
    document.querySelector('#GameNameUpdate').value = data.game_name;
    document.querySelector('#SeasonUpdate').value = data.game_season;
    document.querySelector('#GameYearUpdate').value = data.game_year;
}

//per l'eliminazione dell'host
function openDeleteModal(hostId) {
    document.querySelector('#hostIdInputDelete').value = hostId;
}