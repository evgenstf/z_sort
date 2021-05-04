const EDITOR_SECTION_TEMPLATE = `<table class="editor-section" width=100% cellspacing="0" cellpadding="0" type="%section_type%"><tr><td><div class="editor-section-move-button"><img src="/sr/svg/icon_move.svg"></div></td><td><div class="editor-section-type-button"><img src="%section_icon%"></div></td><td width=10px></td><td class="editor-section-content"><div contenteditable="true">%section_content%</div></td></tr></table>`;

function build_markdown_editor_section(content) {
  let section_div = document.createElement('div');
  let section = EDITOR_SECTION_TEMPLATE;

  splitted_content = '';
  for (let line of content.split('\n')) {
    splitted_content += '<div>' + line + '</div>';
  }

  section = section.replace('%section_icon%', "/sr/svg/icon_markdown.svg");
  section = section.replace('%section_content%', splitted_content);
  section = section.replace('%section_type%', 'markdown');

  console.log(section);
  section_div.innerHTML = section;
  return section_div;
}

function build_editor_section(type, content) {
  if (type === 'markdown') {
    return build_markdown_editor_section(content);
  }
}

function append_editor_by_section(type, content) {
  let editor_table = document.getElementById("editor-table");
  editor_table.appendChild(build_editor_section(type, content));
}

function get_section_content_from_ui() {
  let editor_table = document.getElementById("editor-table");

  let section_contents = []
  for (let node = editor_table.firstChild; node !== null; node = node.nextSibling) {
    section_contents.push(node.innerText.trim());
  }

  return section_contents;
}

append_editor_by_section('markdown', 'asdf\nasdf\nkzjxc');
append_editor_by_section('markdown', 'asdf');
append_editor_by_section('markdown', 'asdf');
append_editor_by_section('markdown', 'asdf');

console.log(get_section_content_from_ui());
