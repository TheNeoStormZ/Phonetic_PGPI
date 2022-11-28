"use strict"

async function hideAsync (id) {
    url = "/cesta/hide/" + String(id)
    
    base_url =  window.location.protocol + String("//")+ window.location.hostname + String(":") + window.location.port
    
    let response = await fetch(url);
    let data = await response.json();

    var container = document.getElementById("carta-" + String(id));
    var checkout_b = document.getElementById("checkout_button");
    console.log(checkout_b);
    container.remove();

    checkout_b.classList.add('disabled');


    
    return data;

  }

function reload(action,id,precio){
    var container_cantidad = document.getElementById("cantidad-"+ String(id));
    var content_cantidad = container_cantidad.innerText.slice(1);

    var container_precio = document.getElementById("precio_total");
    var content_precio = container_precio.innerText.split(": ")[1];
    console.log(container_precio)
    
    if (Boolean(action)){
        container_cantidad.innerText= "x " + String(parseInt(content_cantidad)+1);
        container_precio.innerText= "Precio total: " + String(parseFloat(content_precio)+parseFloat(precio)) + "€";
    }
    else{
        container_cantidad.innerText= "x" + String(parseInt(content_cantidad)-1);
        container_precio.innerText= "Precio total: " + String(parseFloat(content_precio)-parseFloat(precio)) + "€";
    }

    if (parseInt(container_cantidad.innerText.slice(1))<=0){
        hideAsync(id)
    }
}

async function fetchAsync (id,action,precio) {
    url = "/cesta/rm/" + String(id) + "/1"
    if (Boolean(action)){
        url = "/cesta/add/" + String(id) + "/1"
    }
    base_url =  window.location.protocol + String("//")+ window.location.hostname + String(":") + window.location.port
    
    let response = await fetch(url);
    let data = await response.json();
    
    reload(action,id,precio)
    return data;

  }




  
