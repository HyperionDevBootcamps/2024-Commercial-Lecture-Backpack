import React, { useEffect, useState } from "react";

const GetBookings = () => {
  const [bookings, setBookings] = useState([]);
  const [error, setError] = useState(null); // State for error handling

  const fetchBookings = async () => {
    try {
      const token = localStorage.getItem("token"); // Get token from local storage
      const response = await fetch("/getBookings", {
        headers: {
          Authorization: `Bearer ${token}`, // Include token in header
        },
      });

      if (!response.ok) {
        const errorText = await response.text(); // Get the response text for errors
        throw new Error(errorText); // Throw an error with the response text
      }

      const data = await response.json();
      setBookings(data); // Set bookings data
    } catch (error) {
      console.error("Error fetching bookings:", error);
      setError(error.message); // Set error message to state
    }
  };

  useEffect(() => {
    fetchBookings(); // Fetch bookings when component mounts
    const interval = setInterval(fetchBookings, 5000); // Fetch bookings every 5 seconds

    return () => clearInterval(interval); // Clear interval on unmount
  }, []);

  return (
    <div>
      <h2>Bookings</h2>
      {error && <p style={{ color: "red" }}>Error: {error}</p>}{" "}
      {/* Display error message */}
      <ul>
        {bookings.map((booking) => (
          <li key={booking._id}>
            {booking.Id} - {booking.userName} - {booking.service} -{" "}
            {booking.date} at {booking.time}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default GetBookings;
