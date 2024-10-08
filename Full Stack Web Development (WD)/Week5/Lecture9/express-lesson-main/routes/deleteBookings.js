const express = require("express");
const router = express.Router();
let bookings = require("../data.js"); // Keep bookings as a reference

router.delete("/:id", (req, res) => {
  let index = bookings.findIndex((b) => b.Id === parseInt(req.params.id));
  if (index === -1) return res.status(404).send("Booking not found");
  bookings.splice(index, 1);
  res.status(204).send();
  console.log("Booking deleted");
});

module.exports = router;
