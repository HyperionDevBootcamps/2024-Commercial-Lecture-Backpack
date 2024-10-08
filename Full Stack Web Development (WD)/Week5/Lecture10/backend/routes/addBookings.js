const express = require("express");
const Appointment = require("../model/schema.js"); // Import the Appointment model
const router = express.Router();
const auth = require("../middleware/auth.js"); // Import the authentication middleware

router.post("/", auth, async (req, res) => {
  try {
    const booking = new Appointment(req.body); // Create a new booking instance using the Appointment model
    await booking.save(); // Save the booking to the database
    res.status(201).json(booking); // Return the newly created booking
  } catch (error) {
    res.status(400).json({ error: error.message }); // Return an error message if saving fails
  }
});

module.exports = router;
