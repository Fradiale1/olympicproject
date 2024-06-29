const setCookie = (name, value, days = 7, path = '/') => {
    const expires = new Date(Date.now() + days * 864e5).toUTCString()
    document.cookie = name + '=' + encodeURIComponent(value) + '; expires=' + expires + '; path=' + path
}
  
const getCookie = (name) => {
    return document.cookie.split('; ').reduce((r, v) => {
        const parts = v.split('=')
        return parts[0] === name ? decodeURIComponent(parts[1]) : r
    }, '')
}
  
const deleteCookie = (name, path) => {
    setCookie(name, '', -1, path)
}


window.onload = function() {
    const datiDaPassare = getCookie('message');
    //const datiDaPassare = JSON.parse(localStorage.getItem('datiDaPassare'));
    
    console.log(datiDaPassare);
};

function openDeleteModal(athleteId) {
    document.querySelector('#athleteIdInputDelete').value = athleteId;
}

function openDeleteModal(athleteId) {
    document.querySelector('#athleteIdInputUpdate').value = athleteId;
}
