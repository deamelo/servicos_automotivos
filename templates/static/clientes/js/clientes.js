function add_carro() {
  container = document.getElementById('form-carro')

  html =
    "<br><div class='row'><div class='col-md'> <input type='text' placeholder='marca' class='form-control' name='marca'></div><div class='col-md'> <input type='text' placeholder='modelo' class='form-control' name='modelo'></div><div class='col-md'> <input type='text' placeholder='placa' class='form-control' name='placa'></div></div>"

  container.innerHTML += html
}

function exibir_form(tipo) {
  add_cliente = document.getElementById('adicionar-cliente')
  att_cliente = document.getElementById('atualizar-cliente')

  if (tipo == '1') {
    att_cliente.style.display = 'none'
    add_cliente.style.display = 'block'
  } else if (tipo == '2') {
    add_cliente.style.display = 'none'
    att_cliente.style.display = 'block'
  }
}
