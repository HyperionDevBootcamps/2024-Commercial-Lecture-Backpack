import React, { useState } from "react";

const EditBooking = () => {
  const [Id, setId] = useState("");
  const [userName, setUserName] = useState("");
  const [service, setService] = useState("");
  const [date, setDate] = useState("");
  const [time, setTime] = useState("");

  const handleEdit = async (e) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem("token"); // Get token from local storage
      const response = await fetch(`/editBookings/${Id}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`, // Include token in header
        },
        body: JSON.stringify({ userName, service, date, time }),
      });

      if (response.ok) {
        alert("Booking updated!");
        // Reset the fields
        setId("");
        setUserName("");
        setService("");
        setDate("");
        setTime("");
      } else {
        alert("Error updating booking");
      }
    } catch (error) {
      console.error("Error updating booking:", error);
    }
  };

  return (
    <form onSubmit={handleEdit}>
      <input
        type="number"
        placeholder="Booking ID"
        value={Id}
        onChange={(e) => setId(e.target.value)}
        required
      />
      <input
        type="text"
        placeholder="New User Name"
        value={userName}
        onChange={(e) => setUserName(e.target.value)}
        required
      />
      <input
        type="text"
        placeholder="New Service"
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
      <button type="submit">Edit Booking</button>
    </form>
  );
};

export default EditBooking;
