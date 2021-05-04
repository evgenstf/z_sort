const EDITOR_SECTION_TEMPLATE = `
<td>
  <table class="editor-section" width=100% cellspacing="0" cellpadding="0">
    <tr>
      <td>
        <div class="editor-section-type-button">
          <img src="%section_icon%">
        </div>
      </td>
      <td>
        <div class="editor-section-move-button">
          <img src="/sr/svg/icon_move.svg">
        </div>
      </td>
      <td width=10px>
      </td>
      <td class="editor-section-content">
        <div contenteditable="true">
          %section_content%
        </div>
      </td>
    </tr>
  </table>
</td>
`;

function build_markdown_editor_section(content) {
  let section_div = document.createElement('tr');
  let section = EDITOR_SECTION_TEMPLATE;
  section = EDITOR_SECTION_TEMPLATE.replace('%section_icon%', "/sr/svg/icon_markdown.svg");
  section = section.replace('%section_content%', content);
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

}

append_editor_by_section('markdown', 'asdf');
append_editor_by_section('markdown', 'asdf');
append_editor_by_section('markdown', 'asdf');
append_editor_by_section('markdown', 'asdf');

append_editor_by_section('markdown', 'asdf');
append_editor_by_section('markdown', 'asdf');
append_editor_by_section('markdown', 'asdf');
append_editor_by_section('markdown', 'asdf');

append_editor_by_section('markdown', 'asdf');
append_editor_by_section('markdown', 'asdf');
append_editor_by_section('markdown', 'asdf');
append_editor_by_section('markdown', 'asdf');
