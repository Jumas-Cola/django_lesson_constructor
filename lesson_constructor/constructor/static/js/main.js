function appendToList(html) {
  var uls = document.getElementById('lesson_list').querySelectorAll('ul');
  var newli = document.createElement("li");
  newli.setAttribute("class", "card mb-1 bg-light");
  newli.setAttribute("draggable", "true");
  newli.setAttribute("role", "option");
  newli.setAttribute("aria-grabbed", "false");
  newli.innerHTML = html;
  manage_methods = newli.querySelector("#manage_methods");
  if (manage_methods) {
    manage_methods.remove();
  }
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

function download() {
  let ids_list = JSON.stringify($("#lesson_list .method_id").map(function() {
    return $.trim($(this).text());
  }).get());
  $("#ids").attr("value", ids_list);
  $("#ids_list").submit();
  $("#ids").attr("value", "");
}

function checkDownlBtn() {
  var cards = $(document.querySelectorAll('#lesson_list > ul > li > .card-body'));
  if (!cards.length) {
    document.getElementById('save_btn').setAttribute("hidden", true);
  }
}
