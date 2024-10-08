import React, { useState, useEffect } from "react";

const GetBooking = () => {
  const [bookings, setBookings] = useState([]);

  const fetchBookings = async () => {
    try {
      const response = await fetch("/getBookings");
      const data = await response.json();
      setBookings(data);
    } catch (error) {
      console.log("Error fetching the bookings");
    }
  };

  useEffect(() => {
    fetchBookings();
  }, []);

  return (
    <div>
      <h2>Bookings</h2>
      <ul>
        {bookings.map((booking) => (
          <li key={booking._id}>
            {booking.Id} -{booking.userName} - {booking.service} -{" "}
            {booking.date} at {booking.time}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default GetBooking;
