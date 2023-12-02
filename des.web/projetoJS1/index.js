const valorEntrada = document.getElementById('n1')

valorEntrada.addEventListener('input', ()=>{
    const valorN1 = Number(valorEntrada.value)
    console.log(valorN1);
})

somar = ()=>{
    alert(Number(valorEntrada.value) + 10)
}

dobro = () => {
    alert((Number(valorEntrada.value) * 2).toFixed(2))
}

const botao = document.getElementById('btn');
