import {AiOutlineSearch} from 'react-icons/ai'

import './SearchBar.css'

const SearchBar = () => {
  return (
    <section className='inputs-container'>
       <div className="search-container">
       <AiOutlineSearch className='search-icon'/>
        <input type="text" name="search-input" id="search-input" placeholder="Search for a country" />
       </div>
       <select name="area-input" id="area-input">
        <option selected='true' value="" disabled>Filter by Region</option>
        <option value="africa">Africa</option>
        <option value="america">America</option>
        <option value="asia">Asia</option>
        <option value="oceania  ">Oceania</option>
        <option value="europe">Europe</option>
       </select>
    </section>
  )
}

export default SearchBar