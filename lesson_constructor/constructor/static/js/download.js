function saveDoc() {
  var text = document.body.textContent;
  var filename = "lesson_list.doc";
  var blob = new Blob([text], {
    type: "text/plain;charset=utf-8"
  });
  saveAs(blob, filename);
}

saveDoc();
