let num_section = 1;
function add_section() {
    let current_div = document.getElementById("editor_window");
    let new_div = document.createElement("div");
    let new_content = document.createTextNode("Section " + num_section);

    new_div.appendChild(new_content);
    current_div.appendChild(new_div);

    let form = document.createElement('form')
    form.method = 'post'
    form.id = 'editor_form_' + String(num_section);
    form.classList.add('editor_form');

    let text_area = document.createElement('textarea');
    text_area.name = 'text_area';
    text_area.id = 'text_area_' + String(num_section);
    text_area.classList.add('editor_text_area');

    form.appendChild(text_area);
    current_div.appendChild(form);

    num_section++;
}
add_section();

function compile() {
    for (let index = 1; index < num_section; ++index) {
        let text = document.getElementById('text_area_' + String(index)).value;
        let json_file = {
            "type": "markdown",
            "content": ""
        }
        json_file["content"] += text;
        json_file = JSON.stringify(json_file);
        console.log(json_file);

        $.ajax({
            url: '/editor/',
            data: {
                "type": "markdown",
                "content": text
            },
            dataType: 'json',
        });
    }
}

