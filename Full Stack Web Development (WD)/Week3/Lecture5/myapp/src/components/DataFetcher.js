import React, { useState, useEffect } from 'react';

function DataFetcher() {
  const [data, setData] = useState([]);

  useEffect(() => {
    // Fetch data from an API
    fetch('https://jsonplaceholder.typicode.com/users')
      .then((response) => response.json())
      .then((data) => setData(data));
  }, []); // The empty array means this effect runs only once after the component mounts.

  return (
    <div>
      <h1>Data from API:</h1>
      {/* Using .map to iterate and display user data */}
      <ul>
        {data.map((user) => (
          <li key={user.id}>
            <h3>{user.name}</h3>
            <p>Email: {user.email}</p>
            <p>Company: {user.company.name}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default DataFetcher;
