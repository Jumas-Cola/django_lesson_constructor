function appendToList(html) {
  var uls = document.getElementById('lesson_list').querySelectorAll('ul');
  var newli = document.createElement("li");
  newli.setAttribute("class", "card mb-1 bg-light");
  newli.setAttribute("draggable", "true");
  newli.setAttribute("role", "option");
  newli.setAttribute("aria-grabbed", "false");
  newli.innerHTML = html;
  var add_rem = newli.querySelector('#add_rem');
  add_rem.text = "Удалить из списка";
  add_rem.setAttribute("onclick", "this.parentNode.parentNode.remove();checkDownlBtn();");
  uls[0].appendChild(newli);
  document.querySelector('#save_btn').removeAttribute("hidden");
}


sortable('.js-sortable', {
  forcePlaceholderSize: true,
  placeholderClass: 'mb1 border',
  hoverClass: '',
  itemSerializer: function(item, container) {
    item.parent = '[parentNode]'
    item.node = '[Node]'
    item.html = item.html.replace('<', '&lt;')
    return item
  },
  containerSerializer: function(container) {
    container.node = '[Node]'
    return container
  }
})


function closeItems() {
  var items = document.querySelectorAll("[id*='multiCollapse']");
  for (i = 0; i < items.length; ++i) {
    items[i].classList.remove('show');
  }
}


function saveDoc() {
  var text = $(document.querySelectorAll('#lesson_list > ul > li > .card-body > .full_text')).text();
  var filename = "lesson_list.doc";
  var blob = new Blob([text], {
    type: "text/plain;charset=utf-8"
  });
  saveAs(blob, filename);
}

function checkDownlBtn() {
  var cards = $(document.querySelectorAll('#lesson_list > ul > li > .card-body'));
  if (!cards.length) {
    document.getElementById('save_btn').setAttribute("hidden", true);
  }
}
