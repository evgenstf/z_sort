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

let num_section = 1;
function add_section() {
    let current_section = document.getElementById("editor_window");

    let table = document.createElement("table");
    let row = document.createElement("tr");

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
    button.onclick = delete_section;
    button.innerHTML = '<img src="/sr/svg/icon_delete.svg" />';
    button.classList.add('delete_section_button');
    new_section.appendChild(button);
    cell.appendChild(new_section);
    row.appendChild(cell);

    table.appendChild(row);
    current_section.appendChild(table);

    let form = document.createElement('form')
    form.method = 'post'
    form.id = 'editor_form_' + String(num_section);
    form.classList.add('editor_form');

    let text_area = document.createElement('textarea');
    text_area.name = 'text_area';
    text_area.id = 'text_area_' + String(num_section);
    text_area.classList.add('editor_text_area');

    form.appendChild(text_area);
    current_section.appendChild(form);

    num_section++;
}
add_section();

function compile() {
    let sections = []
    for (let index = 1; index < num_section; ++index) {
        let text = document.getElementById('text_area_' + String(index)).value;
        let section = {
            "type": "markdown",
            "content": text
        }
        sections.push(section)
    }

    $.ajax({
        type: 'post',
        url: '/editor/',
        data: JSON.stringify(sections),
        dataType: 'json',
        success: function (result) {
          console.log("editor result:", result)
          let article_preview = document.getElementById("view_window_background");

          article_preview.innerHTML = result['result'];
        }
    });
}

function delete_section() {
    let current_section = document.getElementById("editor_window");
    current_section.removeChild(current_section.lastElementChild);
    current_section.removeChild(current_section.lastElementChild);
}