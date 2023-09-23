
const BlocoJogo = () => {
    let meuArray = Array.from({length: 25}, (_, i) => i + 1);


  return <div className="bloco_jogo">
    {meuArray.map((numero, index) => {
        console.log(numero);

        return <div className="circulo_valores">
            <h3 className="valoresJogo" >{numero}</h3>
        </div>
    })}
  </div>
}

export default BlocoJogo