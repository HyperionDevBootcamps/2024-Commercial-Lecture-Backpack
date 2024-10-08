const express = require("express");

const port = 3000;

const addBookings = require("./routes/addBookings.js");
const deleteBooking = require("./routes/deleteBookings.js");
const getBookings = require("./routes/getBookings.js");
const editBooking = require("./routes/editBookings.js");

const app = express();

app.use(express.json());
app.use("/addBookings", addBookings);
app.use("/deleteBookings", deleteBooking);
app.use("/getBookings", getBookings);
app.use("/editBookings", editBooking);

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
