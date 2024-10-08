import React, { useState } from "react";
import AddBooking from "./Components/addBooking";
import GetBookings from "./Components/getBookings";
import EditBooking from "./Components/editBooking";
import DeleteBooking from "./Components/deleteBooking";
import Login from "./components/login";
import Register from "./components/register";

const App = () => {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  const handleLogin = () => {
    setIsAuthenticated(true);
  };

  const handleRegister = () => {
    setIsAuthenticated(true);
  };

  const handleLogout = () => {
    localStorage.removeItem("token"); // Remove token from local storage
    setIsAuthenticated(false);
  };

  return (
    <div>
      <h1>Booking Management</h1>
      {!isAuthenticated ? (
        <>
          <Login onLogin={handleLogin} />
          <Register onRegister={handleRegister} />
        </>
      ) : (
        <>
          <button onClick={handleLogout}>Logout</button>
          <GetBookings />
          <AddBooking />
          <EditBooking />
          <DeleteBooking />
        </>
      )}
    </div>
  );
};

export default App;
