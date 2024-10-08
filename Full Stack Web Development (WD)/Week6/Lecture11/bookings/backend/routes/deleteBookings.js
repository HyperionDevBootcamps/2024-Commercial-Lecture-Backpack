const express = require("express");
const Appointment = require("../model/schema.js"); // Import the Appointment model
const router = express.Router();
router.delete("/:id", async (req, res) => {
  try {
    const booking = await Appointment.findOneAndDelete({
      Id: parseInt(req.params.id),
    }); // Find and delete the booking
    if (!booking) return res.status(404).send("Booking not found"); // If no booking found, return 404
    res.status(204).send(); // Send a response with no content (204)
    console.log("Booking deleted");
  } catch (error) {
    res.status(500).json({ error: error.message }); // Return an error message if something goes wrong
  }
});

module.exports = router;
