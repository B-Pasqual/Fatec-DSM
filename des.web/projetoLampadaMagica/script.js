//Seleção dos elementos

const lampada = document.getElementById('lampada')
const b_ligar = document.querySelector('.ligar')
const b_desligar = document.querySelector('.desligar')
const b_aparecer = document.querySelector('.aparecer')
const b_sumir = document.querySelector('.sumir')
const b_alternar = document.querySelector('.alternar')
const b_balada = document.querySelector('.balada')


//! Funções
function ligar(){
     lampada.src = './luzLigada.gif'
     document.getElementById('titulo').style.color = 'red'

}
function desligar(){
    lampada.setAttribute('src', './luzDesligada.gif')
}
function sumir(){
    lampada.hidden = true;
}
function aparecer (){
    lampada.hidden = false;
}
function alternar (){
    console.log(lampada.getAttribute('src'))
    if (lampada.getAttribute('src') == './luzLigada.gif') {
        desligar()
    } else if (lampada.getAttribute('src') == './luzDesligada.gif'){
        ligar()
    }
}
let tempo = 1000;

function balada (){
     tempo = tempo - 100;
    setInterval(()=>{
        if (lampada.getAttribute('src') == './luzLigada.gif') {
            desligar()
            document.body.style.background = '#ffff'
    
        } else if (lampada.getAttribute('src') == './luzDesligada.gif'){
            ligar()
            document.body.style.background = '#000'
        }
    }, tempo)
}








//Intervalo na piscada
/*  setInterval(()=>{
     if (lampada.getAttribute('src') == './luzLigada.gif') {
        desligar()
        document.body.style.background = '#ffff'

    } else if (lampada.getAttribute('src') == './luzDesligada.gif'){
        ligar()
        document.body.style.background = '#000'
    }
}, 500) 

 */


b_ligar.addEventListener('click', ligar)
b_desligar.addEventListener('click', desligar)
b_sumir.addEventListener('click', sumir)
b_aparecer.addEventListener('click', aparecer)
b_alternar.addEventListener('click', alternar)
b_balada.addEventListener('click', balada)
lampada.addEventListener('mouseover', ligar )
lampada.addEventListener('mouseout', desligar)

