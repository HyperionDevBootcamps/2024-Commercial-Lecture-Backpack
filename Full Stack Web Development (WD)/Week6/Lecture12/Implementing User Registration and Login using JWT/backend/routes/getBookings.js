// routes/getBookings.js
const express = require("express");
const router = express.Router();
const Appointment = require("../model/schema.js");
const auth = require("../middleware/auth"); // Import JWT verification middleware

router.get("/", auth, async (req, res) => {
  try {
    const bookings = await Appointment.find();
    res.json(bookings);
  } catch (error) {
    res.status(500).send("Internal Server Error");
  }
});

module.exports = router;
