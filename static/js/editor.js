function add_article_tittle() {
    let current_section = document.getElementById("editor_window");
    let article_tittle = document.createElement("div");
    article_tittle.id = 'article_tittle';
    let section_name = document.createTextNode("Article tittle");

    article_tittle.appendChild(section_name);
    current_section.appendChild(article_tittle);

    let form = document.createElement('form')
    form.method = 'post'
    form.id = 'article_tittle_form';

    let text_area = document.createElement('textarea');
    text_area.name = 'text_area';
    text_area.id = 'article_tittle_text_area';

    form.appendChild(text_area);
    current_section.appendChild(form);
}
add_article_tittle();

function add_article_section(current_section) {
    let article_section = document.createElement("div");
    article_section.id = 'article_section';
    let section_name = document.createTextNode("Section");

    article_section.appendChild(section_name);
    current_section.appendChild(article_section);

    let form = document.createElement('form')
    form.method = 'post'
    form.id = 'article_section_form';

    let text_area = document.createElement('textarea');
    text_area.name = 'text_area';
    text_area.id = 'article_section_text_area';

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

count_sections = 1;
function add_section() {
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
    let section_name = document.createTextNode("Markdown");
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

    let text_area = document.createElement('textarea');
    text_area.name = 'text_area';
    text_area.id = 'text_area_' + String(count_sections);
    text_area.classList.add('editor_text_area');

    form.appendChild(text_area);
    current_section.appendChild(form);

    count_sections++;
}
add_section();

function get_sections_from_editor() {
    let sections = []
    for (let index = 1; index < count_sections; ++index) {
        let text = document.getElementById('text_area_' + String(index)).value;
        let section = {
            "type": "markdown",
            "content": text
        }
        sections.push(section)
    }
    return sections;
}

function compile() {
    let sections = get_sections_from_editor();
    $.ajax({
        type: 'post',
        url: '/editor/',
        data: JSON.stringify(sections),
        dataType: 'json',
        success: function (result) {
          article_preview = document.getElementById("view_window_background");
          article_preview.innerHTML = result['result'];
        }
    });
}

function export_article() {
    let sections = get_sections_from_editor();
    let json_sections = JSON.stringify(sections);
    let a = document.createElement("a");
    let file = new Blob([json_sections], {type: 'text/plain'});
    a.href = URL.createObjectURL(file);
    a.download = 'sections.json';
    a.click();
}

function delete_section(num_section) {
    let editor_form = document.getElementById("editor_form_" + num_section);
    editor_form.remove();
    let editor_form_header = document.getElementById("editor_form_header_" + num_section);
    editor_form_header.remove();
    update_sections_id_after_delete(num_section);
    --count_sections;
}

function update_sections_id_after_delete(num_section) {
    let editor_sections_list = get_editor_sections();
    for (let i = num_section + 1; i <= editor_sections_list.length; ++i) {
        let button_up = document.getElementById('move_up_button_' + String(num_section));
        let button_down = document.getElementById('move_down_button_' + String(num_section));
        let text_area = document.getElementById('text_area_' + String(num_section));
        button_up.id = 'move_up_button_' + String(num_section - 1);
        button_down.id = 'move_down_button_' + String(num_section - 1);
        text_area.id = 'text_area_' + String(num_section - 1);
    }
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

function move_up_section(section_num) {
    let move_up_section_num = parseInt(section_num);
    if (move_up_section_num === 1) {
        return false;
    }
    let editor_sections_list = get_editor_sections();
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
    update_editor_section_id_after_move_up(section_num);
}

function move_down_section(section_num) {
    let move_down_section_num = parseInt(section_num);
    let editor_sections_list = get_editor_sections();
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
    update_editor_section_id_after_move_down(section_num);
}

function update_editor_section_id_after_move_down(section_num) {
    let next_button_up = document.getElementById('move_up_button_' + String(parseInt(section_num) + 1));
    let next_button_down = document.getElementById('move_down_button_' + String(parseInt(section_num) + 1));
    let next_text_area = document.getElementById('text_area_' + String(parseInt(section_num) + 1));
    let button_up = document.getElementById('move_up_button_' + section_num);
    let button_down = document.getElementById('move_down_button_' + section_num);
    let text_area = document.getElementById('text_area_' + section_num);
    next_button_up.num = section_num;
    next_button_up.id = 'move_up_button_' + next_button_up.num;
    next_button_down.num = section_num;
    next_button_down.id = 'move_down_button_' + next_button_down.num;
    next_text_area.id = 'text_area_' + next_button_down.num;
    button_up.num = String(parseInt(section_num) + 1);
    button_up.id = 'move_up_button_' + button_up.num;
    button_down.num = String(parseInt(section_num) + 1);
    button_down.id = 'move_down_button_' + button_up.num;
    text_area.id = 'text_area_' + button_up.num;
}

function update_editor_section_id_after_move_up(section_num) {
    let next_button_up = document.getElementById('move_up_button_' + String(parseInt(section_num) - 1));
    let next_button_down = document.getElementById('move_down_button_' + String(parseInt(section_num) - 1));
    let next_text_area = document.getElementById('text_area_' + String(parseInt(section_num) - 1));
    let button_up = document.getElementById('move_up_button_' + section_num);
    let button_down = document.getElementById('move_down_button_' + section_num);
    let text_area = document.getElementById('text_area_' + section_num);
    next_button_up.num = section_num;
    next_button_up.id = 'move_up_button_' + next_button_up.num;
    next_button_down.num = section_num;
    next_button_down.id = 'move_down_button_' + next_button_down.num;
    next_text_area.id = 'text_area_' + next_button_down.num;
    button_down.num = String(parseInt(section_num) - 1);
    button_down.id = 'move_down_button_' + button_down.num;
    button_up.num = String(parseInt(section_num) - 1);
    button_up.id = 'move_up_button_' + button_down.num;
    text_area.id = 'text_area_' + button_down.num;
}
