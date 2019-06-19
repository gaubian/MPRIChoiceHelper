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

    constructor() {
	super();

	this.addEventListener('click', e => {
	    this.selecter(!this.isselected);
	});
    }
}

const fs = require('fs') 
  
fs.readFile('test.txt', (err, data) => { 
    if (err) throw err; 
  
    console.log(data.toString()); 
}) 

customElements.define('selectable-row', SelectableRow);

var ref_table = document.getElementById("table");
var template = document.querySelector("#row");
for(var i = 0; i < 10; i++) {
    var clone = document.importNode(template.content, true);
    var li = document.createElement("li");
    li.appendChild(clone);
    ref_table.appendChild(li);
}
