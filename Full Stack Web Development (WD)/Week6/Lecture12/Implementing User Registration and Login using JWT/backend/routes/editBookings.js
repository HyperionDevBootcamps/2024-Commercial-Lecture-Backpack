// routes/editBookings.js
const express = require("express");
const router = express.Router();
const Appointment = require("../model/schema.js");
const auth = require("../middleware/auth"); // Import JWT verification middleware

router.put("/:id", auth, async (req, res) => {
  try {
    const booking = await Appointment.findOneAndUpdate(
      { Id: parseInt(req.params.id) },
      req.body,
      { new: true, runValidators: true }
    );

    if (!booking) {
      return res.status(404).send("Booking not found");
    }

    res.json(booking);
  } catch (error) {
    console.error("Error updating booking:", error);
    res.status(500).send("Internal Server Error");
  }
});

module.exports = router;
