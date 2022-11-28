"use strict"

async function comprarAsync (productoId) {
    lote = document.getElementById('lote').value

    base_url =  window.location.protocol + String("//")+ window.location.hostname + String(":") + window.location.port

    url = "/producto/" + String(productoId) + "?lote=" + String(lote) + "&&comprar"
    
    let response = await fetch(url);

    window.location.href = "/checkout"
    
    return 0;

  }
