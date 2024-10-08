import { useState } from "react";
import React from "react";

const DeleteBooking = () => {
  const [Id, setId] = useState("");

  const handleDelete = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch(`/deleBookings/${Id}`, {
        method: "DELETE",
      });

      if (response.ok) {
        alert("Booking deleted");
        setId("");
      } else {
        alert("Booking not deleted");
      }
    } catch (error) {}
  };

  return (
    <form onSubmit={handleDelete}>
      <input
        type="number"
        placeholder="Booking ID"
        value={Id}
        onChange={(e) => setId(e.target.value)}
        required
      />
      <button type="submit">Delete Booking</button>
    </form>
  );
};

export default DeleteBooking;
