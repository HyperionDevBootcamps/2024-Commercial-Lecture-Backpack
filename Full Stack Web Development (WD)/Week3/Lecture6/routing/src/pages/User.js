import { useParams } from "react-router-dom"
import NavBar from "../components/NavBar"

const User = ()=>{
    const { userId } = useParams()
    return (
        <div>
            <NavBar/>
            <h1>User { userId }</h1>
        </div>
    )
}

export default User