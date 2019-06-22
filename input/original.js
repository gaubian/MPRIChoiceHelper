const n = codes.length;

function updateRight() {
    const tab = document.querySelectorAll('selectable-row');
    const areselected = new Array(n);
    const deg = new Array(n);
    const tak = new Array(n);
    for(var i = 0; i < n; i++) {
        deg[i] = 0;
	tak[i] = 0;
	areselected[i] = tab[i].isselected;
    }
    for(var i = 0; i < edges.length; i++) {
	const u = edges[i][0];
	const v = edges[i][1];
	deg[u] += 1;
	deg[v] += 1;
        if(areselected[u] || areselected[v]) {
	    tak[u] += 1;
	    tak[v] += 1;
	}
    }
    const to_sort = new Array(0);
    for(var i = 0; i < n; i++) {
	if(!areselected[i] && deg[i] > 0) {
            to_sort.push([tak[i]/deg[i],i]);
	}
    }
    to_sort.sort();
    var ul = document.getElementById("rightcolumn");
    ul.innerHTML = '';
    for(var i = 0; i < 10 && to_sort.length - 1 - i >= 0; i++) {
	var li = document.createElement("tr");
	const ii = to_sort[to_sort.length - i - 1][1];
	const x = Math.floor(to_sort[to_sort.length - i - 1][0] * 100);
	var firstcell = document.createElement("td");
	var secondcell = document.createElement("td");
	var thirdcell = document.createElement("td");
	firstcell.setAttribute("id", "firstcell");
	firstcell.innerHTML = x + ' %';
	secondcell.innerHTML = codes[ii];
	secondcell.setAttribute("id", "secondcell");
	thirdcell.innerHTML = names[ii]; 
	li.appendChild(firstcell);
	li.appendChild(secondcell);
	li.appendChild(thirdcell);
        ul.appendChild(li);
    }
    var ref_ects = document.getElementById("ECTS");
    var ects = 0;
    for(var i = 0; i < n; ++i) {
	if(areselected[i]) {
	    ects += nb_ects[i];
	}
    }
    ref_ects.innerHTML = "Nombre d'ECTS : " +  ects;
}

class SelectableRow extends HTMLElement {	
    get isselected() {
	return this.hasAttribute('isselected');
    }

    selecter(val) {
	if(val) {
            this.setAttribute('isselected', '');
	}
	else {
	    this.removeAttribute('isselected');
	}
	updateRight();
    }

    get index() {
	this.getAttribute('index');
    }

    index(val) {
	console.log(i);
        this.setAttribute('index',val);
	this.innerHTML = codes[i] + ' ' + names[i];
    }

    constructor() {
	super();
	this.innerHTML = "TEST";

	this.addEventListener('click', e => {
	    this.selecter(!this.isselected);
	});
    }
}

customElements.define('selectable-row', SelectableRow);

var ref_table = document.getElementById("table");
var template = document.querySelector("#row");
for(var i = 0; i < n; i++) {
    var clone = document.importNode(template.content, true);
    var li = document.createElement("li");
    li.appendChild(clone);
    ref_table.appendChild(li);
}
const tab = document.querySelectorAll('selectable-row');
for(var i = 0; i < n; i++) {
    tab[i].index(i);
}
updateRight();

// Get the modal
var modal = document.getElementById("myModal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementById("myImg");
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");
img.onclick = function(){
  modal.style.display = "block";
  modalImg.src = this.src;
  captionText.innerHTML = this.alt;
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}
