let somaAdicionais = 0;
let somaPacotes = 0;
const inputNome = document.querySelector('#nome')
const containerOutput = document.querySelector('.container-output')



const calcularPacote = () => {
     const pacotes = document.querySelectorAll('input[name="pacotes"]')
    
    for (var i=0; i < pacotes.length; i++){
       pacotes[i].checked ? somaPacotes = Number(pacotes[i].value) : ''
    }
}
const calcularAdicionais = () => {
    let adicionais = [...document.querySelectorAll('.adicional')]
    for (let i = 0; i < adicionais.length; i++) {
         adicionais[i].checked === true ? somaAdicionais += Number(adicionais[i].value) : ''
    }  
}

const calcularTotal = () => {

    calcularPacote()
    calcularAdicionais()
    console.log(somaAdicionais + somaPacotes);
    if (inputNome.value != ''){
        containerOutput.innerHTML = `<h1>${inputNome.value}</h1><p>O valor que você irá pagar será: </p><p>Valor do pacote: R$ ${somaPacotes}</p><p>Valor dos adicionais: R$ ${somaAdicionais}</p>`
        inputNome.style.border = 'none'
    } else {
        inputNome.style.border = '3px solid red'
    }

}