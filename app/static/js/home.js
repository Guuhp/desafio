const input = document.querySelector('#myInput');
const form = document.querySelector('#myForm');

form.addEventListener('submit', function (e) {
  e.preventDefault(); // previne o envio padrão do formulário
  const valor = input.value;
  const novoAction = `/book_router/find/${valor}`;
  form.setAttribute('action', novoAction);
  form.submit(); // envia o formulário com o novo action
});






