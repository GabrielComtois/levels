var counterLevel1 = 1;
var counterLevel2 = 1;
var counterLevel3 = 1;
var counterLevel4 = 1;


function addLevel1(clickedId) {
		counterLevel1++;
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE) {
            if (xhr.status === 200) {
                var table = document.createElement('table');
								table.id = "table" + counterLevel1 + "Level1";
								var response = xhr.responseText.split('ici');
								var row1 = table.insertRow(0);
								row1.innerHTML = response[0];
								var row2 = table.insertRow(1);
								row2.innerHTML = response[1];
								document.getElementById(clickedId).parentElement.parentElement.parentElement.parentElement.parentElement.appendChild(table);
            } else {
                console.log('Erreur avec le serveur');
            }
        }
    };
    xhr.open("GET", "/level1/" + counterLevel1, true);
    xhr.send();
}


function addLevel2(clickedId) {
		counterLevel2++;
		var lvl1 = clickedId.charAt(0);
		var xhr = new XMLHttpRequest();
		xhr.onreadystatechange = function() {
				if (xhr.readyState === XMLHttpRequest.DONE) {
						if (xhr.status === 200) {
								var index = document.getElementById(clickedId).parentElement.parentElement.rowIndex;
								var response = xhr.responseText.split('ici');
								var tab = document.getElementById(clickedId).parentElement.parentElement.parentElement.parentElement;
								var row1 = tab.insertRow(index);
								row1.innerHTML = response[0];
								var row2 = tab.insertRow(index + 1);
								row2.innerHTML = response[1];

						} else {
								console.log('Erreur avec le serveur');
						}
				}
		};
		xhr.open("GET", "/level2/" + lvl1 + "/" + counterLevel2, true);
    xhr.send();
}


function addLevel3(clickedId) {
		counterLevel3++;
		var lvl1 = clickedId.charAt(0);
		var lvl2 = clickedId.replace(/\b[0-9]+Level[0-9]/, '');
		lvl2 = lvl2.replace(/Level[0-9]addbtn\b/, '');
		var xhr = new XMLHttpRequest();
		xhr.onreadystatechange = function() {
				if (xhr.readyState === XMLHttpRequest.DONE) {
						if (xhr.status === 200) {
								var index = document.getElementById(clickedId).parentElement.parentElement.rowIndex;
								var response = xhr.responseText.split('ici');
								var tab = document.getElementById(clickedId).parentElement.parentElement.parentElement.parentElement;
								var row1 = tab.insertRow(index);
								row1.innerHTML = response[0];
								var row2 = tab.insertRow(index + 1);
								row2.innerHTML = response[1];
						} else {
								console.log('Erreur avec le serveur');
						}
				}
		};
		xhr.open("GET", "/level3/" + lvl1 + "/" + lvl2 + "/" + counterLevel3, true);
    xhr.send();
}


function addLevel4(clickedId) {
		counterLevel4++;
		var lvl1 = clickedId.charAt(0);
		var lvl2 = clickedId.replace(/\b[0-9]+Level[0-9]/, '');
		lvl2 = lvl2.replace(/Level[0-9]+Level[0-9]addbtn\b/, '');
		var lvl3 = clickedId.replace(/\b[0-9]+Level[0-9]+Level[0-9]/, '');
		lvl3 = lvl3.replace(/Level[0-9]addbtn\b/, '')
		console.log(lvl2);
		console.log(lvl3);
		var xhr = new XMLHttpRequest();
		xhr.onreadystatechange = function() {
				if (xhr.readyState === XMLHttpRequest.DONE) {
						if (xhr.status === 200) {
								var index = document.getElementById(clickedId).parentElement.parentElement.rowIndex;
								var tab = document.getElementById(clickedId).parentElement.parentElement.parentElement.parentElement;
								var row1 = tab.insertRow(index);
								row1.innerHTML = xhr.responseText;

						} else {
								console.log('Erreur avec le serveur');
						}
				}
		};
		xhr.open("GET", "/level4/" + lvl1 + "/" + lvl2 + "/" + lvl3 + "/" + counterLevel4 , true);
    xhr.send();
}


function rmvLevel1(clickedId) {
		var elem = document.getElementById(clickedId).parentElement.parentElement.parentElement.parentElement;
		elem.parentNode.removeChild(elem);
}
