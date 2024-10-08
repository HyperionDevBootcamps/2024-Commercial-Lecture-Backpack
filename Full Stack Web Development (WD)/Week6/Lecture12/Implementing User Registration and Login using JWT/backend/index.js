require("./config/database.js").connect(); // Ensure your database connection is correct
const express = require("express");
const port = 3001;

const addBookings = require("./routes/addBookings.js");
const deleteBooking = require("./routes/deleteBookings.js");
const getBookings = require("./routes/getBookings.js");
const editBooking = require("./routes/editBookings.js");
const authRoutes = require("./routes/auth.js");
const cors = require("cors");
const app = express();

app.use(express.json());
app.use(
  cors({
    origin: "http://localhost:3000", // Ensure this matches your frontend URL
    methods: ["GET", "POST", "PUT", "DELETE"],
    allowedHeaders: ["Content-Type", "Authorization"],
  })
);

// Use routes
app.use("/auth", authRoutes);
app.use("/addBookings", addBookings);
app.use("/deleteBookings", deleteBooking);
app.use("/getBookings", getBookings);
app.use("/editBookings", editBooking);

// Error handling middleware
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send("Something broke!");
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
