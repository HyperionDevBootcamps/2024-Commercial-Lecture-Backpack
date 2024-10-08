const express = require("express");
const router = express.Router();
const bookings = require("../data.js");

router.get("/", (req, res) => {
  res.json(bookings);
});
module.exports = router;
