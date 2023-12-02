async function rodaRotina() {
  //Seleção dos elementos
  const inputCEP = document.querySelector('#input-cep');
  const outputCidade = document.querySelector('#cidade-output');
  const inputIdade = document.querySelector('#input-idade');
  const opcoesTermos = document.querySelectorAll('.opcao-termo');

  //Nome da cidade
  const response = await fetch(
    `https://viacep.com.br/ws/${inputCEP.value}/json/`
  );
  const data = await response.json();
  outputCidade.textContent += `${data.localidade}`;

  //Idade
  const idade = Number(inputIdade.value);
  alert(`soma ${idade} + 30 = ${idade + 30}`);

  //Checando se foi aceito
  opcoesTermos.forEach((opcao) => {
    if (opcao.checked) {
      if (opcao.value === 'sim') {
        alert('Cadastrado com sucesso');
      } else {
        alert('Você precisa aceitar os termos');
      }
    }
  });
}
