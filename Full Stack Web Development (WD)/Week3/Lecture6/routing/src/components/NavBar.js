import { Link } from "react-router-dom"

const NavBar = ()=>{
    return (
        <nav>
            <Link to='/'>Home</Link>
            <Link to='/about'>About</Link>
            <Link to='/contact'>Contact</Link>
            <Link to='/user/1'>User 1</Link>
            <Link to='/user/2'>User 2</Link>
            <Link to='/user/3'>User 3</Link>
        </nav>
    )
}

export default NavBar