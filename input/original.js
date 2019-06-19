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

const n = codes.length;
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
