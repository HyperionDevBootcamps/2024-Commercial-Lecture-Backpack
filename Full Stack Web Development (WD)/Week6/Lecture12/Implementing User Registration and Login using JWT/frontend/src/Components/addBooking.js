import React, { useState } from "react";

const AddBooking = () => {
  const [Id, setId] = useState("");
  const [userName, setUserName] = useState("");
  const [service, setService] = useState("");
  const [date, setDate] = useState("");
  const [time, setTime] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem("token"); // Get token from local storage
      const response = await fetch("/addBookings", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`, // Include token in header
        },
        body: JSON.stringify({ Id, userName, service, date, time }),
      });

      if (response.ok) {
        alert("Booking added!");
        // Reset the fields
        setId("");
        setUserName("");
        setService("");
        setDate("");
        setTime("");
      } else {
        alert("Error adding booking");
      }
    } catch (error) {
      console.error("Error adding booking:", error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="number"
        placeholder="ID"
        value={Id}
        onChange={(e) => setId(e.target.value)}
        required
      />
      <input
        type="text"
        placeholder="User Name"
        value={userName}
        onChange={(e) => setUserName(e.target.value)}
        required
      />
      <input
        type="text"
        placeholder="Service"
        value={service}
        onChange={(e) => setService(e.target.value)}
        required
      />
      <input
        type="date"
        value={date}
        onChange={(e) => setDate(e.target.value)}
        required
      />
      <input
        type="time"
        value={time}
        onChange={(e) => setTime(e.target.value)}
        required
      />
      <button type="submit">Add Booking</button>
    </form>
  );
};

export default AddBooking;
