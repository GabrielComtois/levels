var counter = 1;
function addLevel1(clickedId) {
		counter++;
    var xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                var tab = document.getElementById('tableLevel1');
								var row = tab.insertRow(-1)
								row.innerHTML = xhr.responseText;
            } else {
                console.log('Erreur avec le serveur');
            }
        }
    };

    xhr.open("GET", "/level1/" + counter, true);
    xhr.send();

}

function removeLevel1(clickedId) {
		var elem = document.getElementById(clickedId).parentElement.parentElement;
		elem.parentNode.removeChild(elem);
}
