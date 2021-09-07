//埋め込めるように各ファイル名を取得
function include(filename) {
  return HtmlService.createHtmlOutputFromFile(filename).getContent();
}

//アクセスがあった際にHTML(index.html)を取得
function doGet() {
  var template = HtmlService.createTemplateFromFile('index');
  return template.evaluate().setSandboxMode(HtmlService.SandboxMode.IFRAME);
}

//指定したIDのスプレッドシートを二次配列で取得
function getData() {
  var fileid = '1bAbXtoHRG3P1hA0sol9I9NoE32Sw7NB5N7EO57PLdYI';
  return SpreadsheetApp
      .openById(fileid)
      .getActiveSheet()
      .getDataRange()
      .getValues();
}

