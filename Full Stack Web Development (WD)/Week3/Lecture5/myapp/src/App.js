import './App.css';
import Counter from './components/Counter';
import { useState } from 'react';
import DataFetcher from './components/DataFetcher';

function App() {
  const [count, setCount] = useState(100); // Initialize state with 0

  const handleIncrement = () => {
    setCount(count + 1);
  }
  
  const handleDecrement = () => {
    setCount(count - 1);
  }

  return (
    <div className="App">
      <h1>Welcome to my website</h1>
      <Counter handleIncrement={handleIncrement} handleDecrement={handleDecrement} count={count} />
      <DataFetcher />
    </div>
  );
}

export default App;