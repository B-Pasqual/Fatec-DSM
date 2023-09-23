import { createContext, useContext, useState } from 'react';
import dados from './data.json';

const GlobalContext = createContext();

export const useGlobalContext = () => useContext(GlobalContext);

const AppContext = ({ children }) => {
  const [name, setName] = useState('peter');

  return (
    <GlobalContext.Provider>
      {children}
    </GlobalContext.Provider>
  );
};

export default AppContext;
