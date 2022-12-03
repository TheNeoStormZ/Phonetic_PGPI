
async function comprarAsync(productoId) {
  var lote;

  var element = document.getElementById('lote');

  if (element != null) {
    lote = element.value;
  }

  base_url = window.location.protocol + String("//") + window.location.hostname + String(":") + window.location.port

  url = "/producto/" + String(productoId) + "?lote=" + String(lote) + "&&comprar"

  let response = await fetch(url);

  window.location.href = "/checkout"

  return 0;

}
