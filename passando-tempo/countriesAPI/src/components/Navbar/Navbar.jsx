import './Navbar.css'
import {BsMoon,BsMoonFill} from 'react-icons/bs'
import {AiOutlineSearch} from 'react-icons/ai'


const Navbar = () => {
  return (
    <nav className='navbar' >
      <h1>Logo</h1>
      <div className="darkmode-container">
          <BsMoon className='moon-icon'/>
         <h2>Dark Mode</h2>
      </div>
    </nav>
  )
}


export default Navbar