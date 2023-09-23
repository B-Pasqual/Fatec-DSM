const Menu = () => {
  return (
    <div>
      <form>
        <label for="fruta">Selecione o tipo de jogo:</label>
        <select id="tipoJogo" name="tipoJogo">
          <option value="Mega-Sena">Mega Sena</option>
          <option value="">Lotofácil</option>
        </select>
      </form>
    </div>
  );
};

export default Menu;
