import React from 'react';

export default function Counter({ handleIncrement, handleDecrement, count }) {

  return (
    <div>
        <h1>{count}</h1>
        <button onClick={handleIncrement}>Increment</button>
        <button onClick={handleDecrement}>Decrement</button>
    </div>
  );
};