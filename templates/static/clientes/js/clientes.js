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

  fetch('/clientes/atualiza_cliente/', {
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
      document.getElementById('form-att-cliente').style.display = 'block'

      nome = document.getElementById('nome')
      nome.value = data['nome']

      sobrenome = document.getElementById('sobrenome')
      sobrenome.value = data['sobrenome']

      email = document.getElementById('email')
      email.value = data['email']

      cpf = document.getElementById('cpf')
      cpf.value = data['cpf']
    })
}
