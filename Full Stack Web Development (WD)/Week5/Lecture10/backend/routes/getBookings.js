const express = require("express");
const Appointment = require("../model/schema.js"); // Import the Appointment model
const router = express.Router();

router.get("/", async (req, res) => {
  try {
    const bookings = await Appointment.find(); // Retrieve all bookings from the database
    res.json(bookings); // Return the bookings
  } catch (error) {
    res.status(500).json({ error: error.message }); // Return an error message if something goes wrong
  }
});

module.exports = router;
