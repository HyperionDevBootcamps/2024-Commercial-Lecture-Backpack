const express = require("express");
const router = express.Router();
let bookings = require("../data.js"); // Keep bookings as a reference

router.put("/:id", (req, res) => {
  let booking = bookings.find((b) => b.Id === parseInt(req.params.id)); // Use 'Id'
  if (!booking) return res.status(404).send("Booking not found");

  // Update the booking with new data from the request body
  Object.assign(booking, req.body);
  res.json(booking);
  console.log("Booking updated"); // Return the updated booking
});

module.exports = router;
