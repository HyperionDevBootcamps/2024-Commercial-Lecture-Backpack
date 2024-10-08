const mongoose = require("mongoose"); // Import the Mongoose library to interact with MongoDB

// Create a new schema for appointments
const appointmentSchema = new mongoose.Schema({
  Id: {
    type: Number, // The ID of the appointment, stored as a number
    required: true, // This field is mandatory
    unique: true, // No two appointments can have the same ID
  },
  userName: {
    type: String, // The name of the user, stored as a string
    required: true, // This field is mandatory
  },
  service: {
    type: String, // The type of service requested (e.g., "Manicure"), stored as a string
    required: true, // This field is mandatory
  },
  date: {
    type: Date, // The date of the appointment, stored as a Date object
    required: true, // This field is mandatory
  },
  time: {
    type: String, // The time of the appointment (e.g., "11:30"), stored as a string
    required: true, // This field is mandatory
  },
});

// Create a Mongoose model based on the appointment schema
const Appointment = mongoose.model("Appointment", appointmentSchema);

// Export the Appointment model for use in other parts of the application
module.exports = Appointment;
