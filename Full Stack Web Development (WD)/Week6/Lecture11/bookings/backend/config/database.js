const mongoose = require("mongoose");

const MONGO_URI =
  "mongodb+srv://mongo-lesson:Angipoo123@cluster0.x1yb0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";

exports.connect = () => {
  // Connecting to the database
  mongoose
    .connect(MONGO_URI, {
      dbName: "mongo-lesson",
    })
    .then(() => {
      console.log("Successfully connected to database");
    })
    .catch((error) => {
      console.log("database connection failed. exiting now...");
      console.error(error);
      process.exit(1);
    });
};
