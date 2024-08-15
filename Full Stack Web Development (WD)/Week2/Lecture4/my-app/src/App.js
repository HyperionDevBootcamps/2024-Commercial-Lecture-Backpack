//functional component
//JSX - javascrip xml
import NavBar from "./components/NavBar";
import Footer from "./components/Footer";
import "./App.css"
function App() {
  return (
    <div className="container">
      <NavBar />
      <Footer />
    </div>
  );
}

export default App; //the only export of the file
