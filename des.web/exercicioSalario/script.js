const salario = document.querySelector('#inputSalario')
const botao = document.querySelector('#botao-calcular')
const porcentagem = document.querySelector('#porcentagemAumento')
const textoSaida = document.querySelector('#textoSaida')


botao.addEventListener('click', ()=>{
    if (salario.value === '' || porcentagem.value === ''){
        alert('Digite um valor em ambos os campos')
    } else 
   { const valorAjuste = (100 + Number(porcentagem.value)) / 100;
   const salarioAtualizado = (Number(salario.value) * valorAjuste).toFixed(2);
   textoSaida.innerHTML = `<p>Salario Antigo: R$ ${salario.value}</p><p>Valor do aumento: R$ ${(Number(salario.value) * Number(porcentagem.value)) / 100}</p><p>Salario atualizado: R$ ${salarioAtualizado}</p>`
}
})