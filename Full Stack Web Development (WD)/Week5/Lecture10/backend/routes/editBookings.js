const express = require("express");
const Appointment = require("../model/schema.js"); // Import the Appointment model
const router = express.Router();

router.put("/:id", async (req, res) => {
  try {
    const booking = await Appointment.findOneAndUpdate(
      { Id: parseInt(req.params.id) },
      req.body,
      { new: true }
    ); // Update and return the new booking
    if (!booking) return res.status(404).send("Booking not found"); // If no booking found, return 404
    res.json(booking); // Return the updated booking
    console.log("Booking updated");
  } catch (error) {
    res.status(500).json({ error: error.message }); // Return an error message if something goes wrong
  }
});

module.exports = router;
