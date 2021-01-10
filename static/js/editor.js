let num_section = 1;
function add_section() {
let current_div = document.getElementById("editor_window");
let newDiv = document.createElement("div");
let  newContent = document.createTextNode("Section " + num_section);
num_section++;

newDiv.appendChild(newContent);
current_div.appendChild(newDiv);

let form = document.createElement('form');
form.name='myForm';
// my_form.method = 'POST';
// my_form.action = 'http://z-sort.com';

let input = document.createElement('INPUT');
input.type='TEXT';
input.name='myInput';
input.value='z-sort editor input';
form.appendChild(input);

current_div.appendChild(form);
// form.submit();
}
add_section();
