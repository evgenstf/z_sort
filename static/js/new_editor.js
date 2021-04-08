let current_article_json = {};

function set_author(author) {
  document.getElementById("author_textarea").value = author;
}

function get_author(author) {
}

function set_title(title) {
  document.getElementById("title_textarea").value = title;
}

function get_title(title) {
}

function get_editing_article_url() {
  let url = window.location.href.split('/');
  console.log("current_url:", url);
  let last_string = url[url.length - 2];
  if (last_string == 'editor') {
    return '';
  } else {
    return last_string;
  }
}

function load_sections_to_ui(sections) {

}

function get_sections_from_ui() {

}

function compile() {
  console.log('compile called');
}

function publish() {
  console.log('publish called');
}

function export_article() {
  console.log('export_article called');
}

function setup_section_button_listeners() {
  document.getElementById('add_markdown_section_button').onclick = function(){
    add_section('markdown');
  };
  document.getElementById('add_graph_section_button').onclick = function(){
    add_section('graph');
  };
  document.getElementById('add_steps_section_button').onclick = function(){
    add_section('steps');
  };
  document.getElementById('add_chart_section_button').onclick = function(){
    add_section('chart');
  };
}
setup_section_button_listeners();

count_sections = 1;
// TODO: refactor this shit
function add_section(section_class, content='') {
  function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
  }
  const section_title = capitalizeFirstLetter(section_class);

  let current_section = document.getElementById("editor_sections_div");

  let table = document.createElement("table");
  table.id = 'editor_form_header_' + String(count_sections);
  let row = document.createElement("tr");

  let cell = document.createElement("td");
  cell.classList.add('move_button_up_td');
  let new_section = document.createElement("div");
  new_section.classList.add('div_move_button');
  let button_up = document.createElement("button");
  button_up.innerHTML = '<img src="/sr/svg/move_up_active.svg" />';
  button_up.classList.add('move_button');
  button_up.id = 'move_up_button_' + String(count_sections);
  button_up.num = String(count_sections);
  button_up.onclick = function(){
    move_up_section(button_up.num);
  };
  new_section.appendChild(button_up);
  cell.appendChild(new_section);
  row.appendChild(cell);

  cell = document.createElement("td");
  new_section = document.createElement("div");
  new_section.classList.add('div_move_button');
  let button_down = document.createElement("button");
  button_down.innerHTML = '<img src="/sr/svg/move_down_active.svg" />';
  button_down.classList.add('move_button');
  button_down.id = 'move_down_button_' + String(count_sections);
  button_down.num = String(count_sections);
  button_down.onclick = function(){
    move_down_section(button_down.num);
  };
  new_section.appendChild(button_down);
  cell.appendChild(new_section);
  row.appendChild(cell);

  cell = document.createElement("td");
  cell.classList.add('section_name_td');
  new_section = document.createElement("div");
  new_section.classList.add('section_name');
  let section_name = document.createTextNode(section_title);
  new_section.appendChild(section_name);
  cell.appendChild(new_section);
  row.appendChild(cell);

  cell = document.createElement("td");
  new_section = document.createElement("div");
  new_section.classList.add('div_delete_section_button');
  let button = document.createElement("button");
  button.innerHTML = '<img src="/sr/svg/icon_delete.svg" />';
  button.classList.add('delete_section_button');
  button.id = 'delete_section_button_' + String(count_sections);
  button.num = String(count_sections);
  button.onclick = function(){
    delete_section(button.num);
  };
  new_section.appendChild(button);
  cell.appendChild(new_section);
  row.appendChild(cell);

  table.appendChild(row);
  current_section.appendChild(table);

  let form = document.createElement('form')
  form.method = 'post'
  form.id = 'editor_form_' + String(count_sections);
  form.classList.add('editor_form');
  form.name = section_class;

  let text_area = document.createElement('textarea');
  text_area.name = 'text_area';
  text_area.id = 'text_area_' + String(count_sections);
  text_area.classList.add('editor_text_area');
  text_area.placeholder = section_title;

  text_area.addEventListener('focus', autoResize, false);
  text_area.addEventListener('input', autoResize, false);

  function autoResize() {
    //this.style.height = 'auto';
    this.style.height = this.scrollHeight - 20 + 'px';
  }

  text_area.style.height = (content.match(/\n/g) || []).length * 25 + 'px';
  console.log("text_area.style.height", text_area.style.height);

  text_area.appendChild(document.createTextNode(content));

  form.appendChild(text_area);
  current_section.appendChild(form);

  count_sections++;
}
add_section('markdown');
