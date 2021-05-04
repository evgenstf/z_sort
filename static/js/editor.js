const EDITOR_SECTION_TEMPLATE = `<table  width=100% cellspacing="0" cellpadding="0" type="%section_type%"><tr><td><img class="editor-section-move-button" src="/sr/svg/icon_move.svg"></td><td><img class="editor-section-type-button" src="%section_icon%"></td><td width=10px></td><td class="editor-section-content"><div contenteditable="true">%section_content%</div></td></tr></table>`;

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
  section_div.className = 'editor-section';
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

append_editor_by_section('markdown', '01');
append_editor_by_section('markdown', '02');
append_editor_by_section('markdown', '03');
append_editor_by_section('markdown', '04');

append_editor_by_section('markdown', '01');
append_editor_by_section('markdown', 'lkkk');
append_editor_by_section('markdown', '03');
append_editor_by_section('markdown', '04');

append_editor_by_section('markdown', '01');
append_editor_by_section('markdown', '02');
append_editor_by_section('markdown', '03');
append_editor_by_section('markdown', '04');

append_editor_by_section('markdown', '01');
append_editor_by_section('markdown', '02');
append_editor_by_section('markdown', '03');
append_editor_by_section('markdown', '04');

console.log(get_section_content_from_ui());



let draggingEle;
let placeholder;
let isDraggingStarted = false;

let x = 0;
let y = 0;

// Swap two nodes
const swap = function(nodeA, nodeB) {
  const parentA = nodeA.parentNode;
  const siblingA = nodeA.nextSibling === nodeB ? nodeA : nodeA.nextSibling;

  // Move `nodeA` to before the `nodeB`
  nodeB.parentNode.insertBefore(nodeA, nodeB);

  // Move `nodeB` to before the sibling of `nodeA`
  parentA.insertBefore(nodeB, siblingA);
};

// Check if `nodeA` is above `nodeB`
const isAbove = function(mouseY, nodeB) {
  // Get the bounding rectangle of nodes
  const rectB = nodeB.getBoundingClientRect();

  return rectB.top < mouseY && mouseY < rectB.top + rectB.height;
};

const mouseMoveHandler = function(mouse) {
  // Set position for dragging element
  draggingEle.style.position = 'absolute';
  draggingEle.style.y = `${mouse.y - y}px`;


  const draggingRect = draggingEle.getBoundingClientRect();
  const prevEle = draggingEle.previousElementSibling;
  const nextEle = placeholder.nextElementSibling;


  if (prevEle) {
    const prevEleRect = prevEle.getBoundingClientRect();
    if (mouse.y < prevEleRect.top + Math.min(draggingRect.height, prevEleRect.height)) {
      swap(prevEle, draggingEle);
      swap(prevEle, placeholder);
      return;
    }
  }

  if (nextEle) {
    const nextEleRect = nextEle.getBoundingClientRect();
    if (mouse.y > nextEleRect.top + nextEleRect.height - Math.min(draggingRect.height, nextEleRect.height)) {
      swap(nextEle, placeholder);
      swap(nextEle, draggingEle);
    }
  }
};

const finishDraggingHandler = function() {
  console.log('finishDraggingHandler called');
  isDraggingStarted = false;

  try {
    const list = document.getElementById('editor-table');
    list.removeChild(placeholder);
  } catch { }

  draggingEle.style.removeProperty('y');
  draggingEle.style.removeProperty('x');
  draggingEle.style.removeProperty('position');

  x = null;
  y = null;
  draggingEle = null;

  document.removeEventListener('mousemove', mouseMoveHandler);
  document.removeEventListener('mousedown', finishDraggingHandler);
  document.removeEventListener('mouseup', mouseUpHandler);

  const list = document.getElementById('editor-table');
  // Query all items
  [].slice.call(list.querySelectorAll('.editor-section')).forEach(function(item) {
    item.classList.remove('no-hover');
  });
};

const mouseUpHandler = function() {
  document.addEventListener('mousedown', finishDraggingHandler);
}

const startDraggingHandler = function(mouse) {
  console.log('mouse:', mouse);
  if (!isDraggingStarted) {
    isDraggingStarted = true;

    draggingEle = mouse.path.find(item => item.className == 'editor-section');

    const draggingRect = draggingEle.getBoundingClientRect();
    placeholder = document.createElement('div');
    placeholder.classList.add('placeholder');
    draggingEle.parentNode.insertBefore(placeholder, draggingEle.nextSibling);
    placeholder.style.height = `${draggingRect.height}px`;

    // Calculate the mouse position
    const rect = draggingEle.getBoundingClientRect();
    console.log("rect:", rect);
    x = mouse.x - rect.left;
    y = mouse.y - rect.top;

    mouseMoveHandler(mouse);
    // Attach the listeners to `document`
    document.addEventListener('mousemove', mouseMoveHandler);
    document.addEventListener('mouseup', mouseUpHandler);

    const list = document.getElementById('editor-table');
    // Query all items
    [].slice.call(list.querySelectorAll('.editor-section')).forEach(function(item) {
      item.classList.add('no-hover');
    });
  }
}

const list = document.getElementById('editor-table');
// Query all items
[].slice.call(list.querySelectorAll('.editor-section-move-button')).forEach(function(item) {
  item.addEventListener('mousedown', startDraggingHandler);
});

