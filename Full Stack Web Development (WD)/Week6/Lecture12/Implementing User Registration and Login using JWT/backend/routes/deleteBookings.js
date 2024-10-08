// routes/deleteBookings.js
const express = require("express");
const router = express.Router();
const Appointment = require("../model/schema.js");
const auth = require("../middleware/auth"); // Import JWT verification middleware

router.delete("/:id", auth, async (req, res) => {
  try {
    const booking = await Appointment.findOneAndDelete({
      Id: parseInt(req.params.id),
    });

    if (!booking) return res.status(404).send("Booking not found");

    res.status(204).send();
  } catch (error) {
    console.error("Error deleting booking:", error);
    res.status(500).send("Internal Server Error");
  }
});

module.exports = router;
