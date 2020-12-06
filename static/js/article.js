  function addFootnote(id) {
    var footnote_link = document.getElementById(id);
    var footnote_title = footnote_link.getAttribute('footnote-title');
    var footnote_text = footnote_link.getAttribute('footnote-text');

    var footnote = document.createElement('div');
    footnote.id = id + '-footnote';
    footnote.className = 'footnote';

    var footnote_title_div = document.createElement('div');
    footnote_title_div.innerHTML = footnote_title ;
    footnote_title_div.className = "footnote_title"
    footnote.appendChild(footnote_title_div);

    var footnote_text_div = document.createElement('div');
    footnote_text_div.innerHTML = footnote_text;
    footnote.appendChild(footnote_text_div);

    document.getElementById("footnote_container").appendChild(footnote);
  }

  for (footnote_link of document.getElementsByClassName('footnote_link')) {
    addFootnote(footnote_link['id']);
  }

  let opened_footnotes = []

  function showFootnote(id) {
    console.log("showFootnote id:", id);
    var footnote = document.getElementById(id + '-footnote');
    let new_height = 0;
    for (child of footnote.children) {
      new_height += child.getBoundingClientRect().height;
    }
    console.log(new_height);
    footnote.style.height = new_height + 10 + "px";
    footnote.style.top = document.getElementById("" + id).getBoundingClientRect().top - new_height - 50 + 'px';
    footnote.style.left = document.getElementById("" + id).getBoundingClientRect().left + 'px';
    if (!footnote.classList.contains("show")) {
      footnote.classList.toggle("show");
      opened_footnotes.push(id);
    }
  }

  function closeFootnote(id) {
    var footnote = document.getElementById(id + '-footnote');
    if (footnote.classList.contains("show")) {
      footnote.classList.toggle("show");
    }
  }

  window.addEventListener('scroll', function(e) {
    for (footnote_id of opened_footnotes) {
      closeFootnote(footnote_id);
    }
    opened_footnotes = [];
  });

