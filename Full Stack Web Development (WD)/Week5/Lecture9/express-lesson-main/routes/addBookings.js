const express = require("express");
const bookings = require("../data.js");
const router = express.Router();

router.post("/", (req, res) => {
  console.log(req.body); // Debugging line
  let booking = { Id: bookings.length + 1, ...req.body }; // Ensure 'Id' is used
  bookings.push(booking); // Push the new booking
  res.status(201).json(booking); // Return the newly created booking
});

module.exports = router;
