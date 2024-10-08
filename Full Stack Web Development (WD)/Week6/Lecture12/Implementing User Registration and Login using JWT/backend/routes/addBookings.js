// routes/addBookings.js
const express = require("express");
const router = express.Router();
const Appointment = require("../model/schema.js");
const auth = require("../middleware/auth"); // Import the auth middleware

router.post("/", auth, async (req, res) => {
  try {
    const booking = new Appointment(req.body);
    await booking.save();
    res.status(201).json(booking);
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});

module.exports = router;
