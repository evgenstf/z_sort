let num_section = 1;
function add_section() {
    let current_section = document.getElementById("editor_window");
    let new_section = document.createElement("div");
    new_section.classList.add('section_name');
    let section_name = document.createTextNode("Markdown ");

    new_section.appendChild(section_name);
    current_section.appendChild(new_section);

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

