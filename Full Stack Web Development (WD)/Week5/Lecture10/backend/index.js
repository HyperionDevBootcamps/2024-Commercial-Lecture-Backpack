require("dotenv").config();
require("./config/database.js").connect(); // Connect to MongoDB
const express = require("express");
const Appointment = require("./model/schema.js");
const bcrypt = require("bcrypt"); // Import the Appointment model

const port = 3005;

const authRoutes = require("./routes/auth.js");
const addBookings = require("./routes/addBookings.js");
const deleteBooking = require("./routes/deleteBookings.js");
const getBookings = require("./routes/getBookings.js");
const editBooking = require("./routes/editBookings.js");

const app = express();

app.use(express.json());
app.use("/auth", authRoutes);
app.use("/addBookings", addBookings); // Mount the addBookings route
app.use("/deleteBookings", deleteBooking); // Mount the deleteBookings route
app.use("/getBookings", getBookings); // Mount the getBookings route
app.use("/editBookings", editBooking); // Mount the editBookings route

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`); // Start the server
});
