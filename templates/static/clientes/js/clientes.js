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

function dados_cliente() {
  id_cliente = document.getElementById('cliente-select').value
  csrf_token = document.querySelector('[name=csrfmiddlewaretoken]').value

  data = new FormData()
  data.append('id_cliente', id_cliente)

  fetch('/clientes/atualizar_cliente/', {
    method: 'POST',
    headers: {
      'X-CSRFToken': csrf_token
    },
    body: data
  })
    .then(function (result) {
      return result.json()
    })
    .then(function (data) {
      info_clientes = document.getElementById('form-att-cliente')
      info_clientes.style.display = 'block'

      id = document.getElementById('id')
      id.value = data['cliente_id']
      console.log(id)
      nome = document.getElementById('nome')
      nome.value = data['cliente']['nome']

      sobrenome = document.getElementById('sobrenome')
      sobrenome.value = data['cliente']['sobrenome']

      email = document.getElementById('email')
      email.value = data['cliente']['email']

      cpf = document.getElementById('cpf')
      cpf.value = data['cliente']['cpf']

      div_carros = document.getElementById('carros')
      div_carros.innerHTML = ''

      for (i = 0; i < data['carros'].length; i++) {
        div_carros.innerHTML +=
          "<form action='/clientes/atualizar_carro/" +
          data['carros'][i]['id'] +
          "' method='POST'>\
          <div class='row'>\
                  <div class='col-md'>\
                      <input class='form-control' name='marca' type='text' value='" +
          data['carros'][i]['fields']['marca'] +
          "'>\
                  </div>\
                  <div class='col-md'>\
                      <input class='form-control' name='modelo' type='text' value='" +
          data['carros'][i]['fields']['modelo'] +
          "'>\
                  </div>\
                  <div class='col-md'>\
                      <input class='form-control' type='text' name='placa' value='" +
          data['carros'][i]['fields']['placa'] +
          "' >\
                  </div>\
                  <div class='col-md'>\
                      <input class='btn btn-lg btn-success' type='submit'>\
                  </div>\
              </form>\
              <div class='col-md'>\
                  <a href='/clientes/excluir_carro/" +
          data['carros'][i]['id'] +
          "' class='btn btn-lg btn-danger'>EXCLUIR</a>\
              </div>\
          </div><br>"
      }
    })
}
