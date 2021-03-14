function add_article_title() {
  let current_section = document.getElementById("editor_window");
  let article_title = document.createElement("div");
  article_title.id = 'article_title';
  let section_name = document.createTextNode("Article title");

  article_title.appendChild(section_name);
  current_section.appendChild(article_title);

  let form = document.createElement('form')
  form.method = 'post'
  form.id = 'article_title_form';

  let text_area = document.createElement('textarea');
  text_area.name = 'text_area';
  text_area.id = 'article_title_text_area';
  text_area.placeholder = 'Title';

  form.appendChild(text_area);
  current_section.appendChild(form);
}
add_article_title();

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


function add_article_section(current_section) {
  let article_section = document.createElement("div");
  article_section.id = 'article_section';
  let section_name = document.createTextNode("Category");

  article_section.appendChild(section_name);
  current_section.appendChild(article_section);

  let form = document.createElement('form')
  form.method = 'post'
  form.id = 'article_section_form';

  let text_area = document.createElement('textarea');
  text_area.name = 'text_area';
  text_area.id = 'article_category_text_area';
  text_area.placeholder = 'Category';

  form.appendChild(text_area);
  current_section.appendChild(form);
  return current_section;
}

function add_author_name(current_section) {
  let author_name = document.createElement("div");
  author_name.id = 'author_name';
  let section_name = document.createTextNode("Author");

  author_name.appendChild(section_name);
  current_section.appendChild(author_name);

  let form = document.createElement('form')
  form.method = 'post'
  form.id = 'author_name_form';

  let text_area = document.createElement('textarea');
  text_area.name = 'text_area';
  text_area.id = 'author_name_text_area';
  text_area.placeholder = 'Author name';

  form.appendChild(text_area);
  current_section.appendChild(form);
  return current_section;
}

function add_article_section_and_author_name() {
  let body = document.getElementById("editor_window");
  let table = document.createElement("table");
  let row = document.createElement("tr");

  let article_section_cell = document.createElement("td");
  article_section_cell = add_article_section(article_section_cell);
  row.appendChild(article_section_cell);

  let author_name_cell = document.createElement("td");
  author_name_cell = add_author_name(author_name_cell);
  row.appendChild(author_name_cell);

  table.appendChild(row);
  body.appendChild(table);
}
add_article_section_and_author_name();

function add_sections_buttons() {
  let body = document.getElementById("editor_window");
  let section_buttons = document.createElement("div");
  section_buttons.id = 'add_section_buttons';

  let section_buttons_title = document.createElement("p");
  section_buttons_title.id = 'add_section_title';
  let section_name = document.createTextNode('add section');
  section_buttons_title.appendChild(section_name);
  section_buttons.appendChild(section_buttons_title);

  section_buttons.appendChild(document.createElement("br"));


  let button = document.createElement("button");
  button.classList.add('add_section_button');
  button.onclick = function(){
    add_section('Markdown', 'markdown');
  };
  button.innerHTML = '<img src="/sr/svg/icon_markdown.svg" />';
  section_name = document.createTextNode('markdown');
  button.appendChild(section_name);
  section_buttons.appendChild(button);

  button = document.createElement("button");
  button.classList.add('add_section_button');
  button.onclick = function(){
    add_section('Graph', 'graph');
  };
  button.innerHTML = '<img src="/sr/svg/icon_graph.svg" />';
  section_name = document.createTextNode('graph');
  button.appendChild(section_name);
  section_buttons.appendChild(button);

  button = document.createElement("button");
  button.classList.add('add_section_button');
  button.onclick = function(){
    add_section('Chart', 'chart');
  };
  button.innerHTML = '<img src="/sr/svg/icon_chart.svg" />';
  section_name = document.createTextNode('chart');
  button.appendChild(section_name);
  section_buttons.appendChild(button);

  button = document.createElement("button");
  button.classList.add('add_section_button');
  button.onclick = function(){
    add_section('Steps', 'steps');
  };
  button.innerHTML = '<img src="/sr/svg/icon_steps.svg" />';
  section_name = document.createTextNode('steps');
  button.appendChild(section_name);
  section_buttons.appendChild(button);

  body.appendChild(section_buttons);
}
add_sections_buttons();

count_sections = 1;
function add_section(section_title, section_class) {
  let current_section = document.getElementById("editor_window");

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

  let text = '';
  if (section_class == 'graph') {
    text = "{\n            \"type\": \"dot\",\n            \"node_color\": \"#D3D3D3\",\n            \"edge_color\": \"#909090\",\n            \"node_count\": 7,\n            \"node_attributes\": {\n                    \"0\": {\"label\":\"12\", \"color\":\"yellow\"}\n            },\n            \"edges\": [\n                    {\"from\": 0, \"to\":1},\n                    {\"from\": 0, \"to\":2},\n                    {\"from\": 1, \"to\":3},\n                    {\"from\": 1, \"to\":4},\n                    {\"from\": 2, \"to\":5},\n                    {\"from\": 2, \"to\":6}\n            ]\n}";
  }
  else if (section_class == 'chart') {
    text = "{\n            \"type\": \"line\",\n            \"color\": \"#1e4a76\",\n            \"line_smooth\": true,\n            \"show_grid\": true,\n            \"x-axis\": [\n                    0,\n                    1,\n                    2,\n                    3,\n                    4,\n                    5\n            ],\n            \"y-axis\": [\n                    4,\n                    5,\n                    0,\n                    3,\n                    0,\n                    1\n            ]\n}";
  }
  else if (section_class == 'steps') {
    text = "[\n      [\n        {\n          \"type\":\"markdown\",\n          \"content\":\"#Ициализация\"\n        },\n        {\n          \"type\":\"markdown\",\n          \"content\":\"Начать стоит с того, что добавить в дерево первый элемент, он будет являться корнем и уже образует упорядоченную кучу сам по себе.\"\n        },\n        {\n          \"type\": \"graph\",\n          \"content\": {\n            \"type\": \"dot\",\n            \"node_color\": \"#D3D3D3\",\n            \"edge_color\": \"#909090\",\n            \"node_count\": 7,\n            \"node_attributes\": {\n              \"0\": {\"label\":\"12\", \"color\":\"yellow\"}\n            },\n            \"edges\": [\n              {\"from\": 0, \"to\":1},\n              {\"from\": 0, \"to\":2},\n              {\"from\": 1, \"to\":3},\n              {\"from\": 1, \"to\":4},\n              {\"from\": 2, \"to\":5},\n              {\"from\": 2, \"to\":6}\n            ]\n          }\n        }\n      ],\n      [\n        {\n          \"type\":\"markdown\",\n          \"content\":\"#Добавление элемента\"\n        },\n        {\n          \"type\":\"markdown\",\n          \"content\":\"Далее добавляем следующий элемент в первый незянятый слот в порядке BFS обхода.\"\n        },\n        {\n          \"type\": \"graph\",\n          \"content\": {\n            \"type\": \"dot\",\n            \"node_color\": \"#D3D3D3\",\n            \"edge_color\": \"#909090\",\n            \"node_count\": 7,\n            \"node_attributes\": {\n              \"0\": {\"label\":\"12\", \"color\":\"yellow\"},\n              \"1\": {\"label\":\"1\", \"color\":\"green\"}\n            },\n            \"edges\": [\n              {\"from\": 0, \"to\":1},\n              {\"from\": 0, \"to\":2},\n              {\"from\": 1, \"to\":3},\n              {\"from\": 1, \"to\":4},\n              {\"from\": 2, \"to\":5},\n              {\"from\": 2, \"to\":6}\n            ]\n          }\n        }\n]\n      \n      \n]";
  }

  text_area.style.height = (text.match(/\n/g) || []).length * 25 + 'px';
  console.log("text_area.style.height", text_area.style.height);

  section_name = document.createTextNode(text);
  text_area.appendChild(section_name);

  form.appendChild(text_area);
  current_section.appendChild(form);

  let sections_buttons = document.getElementById('add_section_buttons');
  sections_buttons.remove();
  add_sections_buttons();

  count_sections++;
}
add_section('Markdown', 'markdown');

function get_today_date() {
  return (new Date()).toString().split(' ').splice(1,3).join(' ');
}

function get_sections_from_editor() {
  let sections = [];
  let sections_to_export = get_editor_sections();
  for (let index = 1; index < sections_to_export.length; index += 2) {
    let form = sections_to_export[index];
    let text = form.childNodes[0].value;
    let section = {
      "type": form.name,
      "content": text,
    }
    sections.push(section)
  }
  return sections;
}

function get_article_json_from_editor() {
  let article_json = {
    "date": get_today_date(),
    "header": ["<h1>" + document.getElementById('article_title_text_area').value + "</h1>"],
    "authors":[document.getElementById('author_name_text_area').value],
    "sections": get_sections_from_editor(),
    "url": get_editing_article_url(),
    "category": document.getElementById('article_category_text_area').value,
  }
  return article_json;
}

function compile() {
  let article = JSON.stringify(get_article_json_from_editor());
  $.ajax({
      type: 'post',
      url: '/editor/',
      data: JSON.stringify(`{"type":"compile","article":${article}}`),
      dataType: 'json',
      success: function (result) {
        let article_preview = document.getElementById("view_window_background");
        article_preview.innerHTML = result['html'];
      }
  });
}

function publish() {
  let article = JSON.stringify(get_article_json_from_editor());
  $.ajax({
      type: 'post',
      url: '/editor/',
      data: JSON.stringify(`{"type":"publish","article":${article}}`),
      dataType: 'json',
      success: function (result) {
        console.log('article published:', result);
        window.location.href = '/article/' + result['url'];
      }
  });
}

function export_article() {
  let article = document.getElementById("view_window").cloneNode(true);
  article.childNodes[1].style.padding = "40px";
  let opt = {
    margin:       0,
    pagebreak:    { mode: ['avoid-all', 'css', 'legacy'] },
    filename:     'article.pdf',
    html2canvas:  { scale: 4, windowWidth: 2000 },
    jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
  };
  html2pdf().set(opt).from(article).save();

  // let sections = get_sections_from_editor();
  // let json_sections = JSON.stringify(sections);
  // let a = document.createElement("a");
  // let file = new Blob([json_sections], {type: 'text/plain'});
  // a.href = URL.createObjectURL(file);
  // a.download = 'sections.json';
  // a.click();
}

function reverse_string(string) {
  let split_string = string.split("");
  let reverse_array = split_string.reverse();
  let reverse_string = reverse_array.join("");
  return reverse_string;
}

function get_id_num_from_id(id) {
  let reverses_id = reverse_string(id);
  let reversed_id_num = String(parseInt(reverses_id));
  let id_num = reverse_string(reversed_id_num);
  return parseInt(id_num);
}

function delete_section(num_section) {
  let editor_form = document.getElementById("editor_form_" + num_section);
  editor_form.remove();
  let editor_form_header = document.getElementById("editor_form_header_" + num_section);
  editor_form_header.remove();
}

function get_editor_sections() {
  let editor_section = document.getElementById("editor_window");
  let editor_node_list = [].slice.call(editor_section.childNodes);
  editor_node_list =  editor_node_list.slice(3);
  return editor_node_list;
}

function update_editor_section(new_editor_section_list) {
  let editor_section = document.getElementById("editor_window");
  let editor_sections_list = get_editor_sections();
  for (let i = 0; i < editor_sections_list.length - 3; ++i) {
    editor_section.removeChild(editor_section.lastElementChild);
  }
  for (let child of new_editor_section_list) {
    editor_section.appendChild(child);
  }
}

function get_section_pos_by_num(section_num, editor_sections) {
  for (let i = 0; i < editor_sections.length; i += 2) {
    let id_num = get_id_num_from_id(editor_sections[i].id)
    if (id_num === parseInt(section_num)) {
      return (i + 2) / 2;
    }
  }
}

function move_up_section(section_num) {
  let editor_sections_list = get_editor_sections();
  let move_up_section_num = get_section_pos_by_num(section_num, editor_sections_list);

  if (move_up_section_num === 1) {
    return false;
  }
  let new_editor_section_list = [];
  for (let i = 0; i < 2 * (move_up_section_num - 2); ++i) {
    new_editor_section_list.push(editor_sections_list[i]);
  }
  new_editor_section_list.push(editor_sections_list[(move_up_section_num - 1) * 2]);
  new_editor_section_list.push(editor_sections_list[(move_up_section_num - 1) * 2 + 1]);
  new_editor_section_list.push(editor_sections_list[(move_up_section_num - 2) * 2]);
  new_editor_section_list.push(editor_sections_list[(move_up_section_num - 2) * 2 + 1]);
  for (let i = move_up_section_num * 2; i < editor_sections_list.length; ++i) {
    new_editor_section_list.push(editor_sections_list[i]);
  }
  update_editor_section(new_editor_section_list);
}

function move_down_section(section_num) {
  let editor_sections_list = get_editor_sections();
  let move_down_section_num = get_section_pos_by_num(section_num, editor_sections_list);

  if (move_down_section_num >= editor_sections_list.length / 2) {
    return;
  }
  let new_editor_section_list = [];
  for (let i = 0; i < 2 * (move_down_section_num - 1); ++i) {
    new_editor_section_list.push(editor_sections_list[i]);
  }
  new_editor_section_list.push(editor_sections_list[(move_down_section_num) * 2]);
  new_editor_section_list.push(editor_sections_list[(move_down_section_num) * 2 + 1]);
  new_editor_section_list.push(editor_sections_list[(move_down_section_num - 1) * 2]);
  new_editor_section_list.push(editor_sections_list[(move_down_section_num - 1) * 2 + 1]);
  for (let i = (move_down_section_num + 1) * 2; i < editor_sections_list.length; ++i) {
    new_editor_section_list.push(editor_sections_list[i]);
  }
  update_editor_section(new_editor_section_list);
}

function get_sections_from_server() {
  article_url = get_editing_article_url();
  console.log("article_url:", article_url);
  $.ajax({
      type: 'post',
      url: '/editor/',
      data: JSON.stringify(`{"type":"get_sections","article_url":"${article_url}"}`),
      dataType: 'json',
      success: function (result) {
        console.log("received sections from server:", result);
      }
  });
}

get_sections_from_server();
