const mongoose = require("mongoose");

const MONGO_URI =
  "mongodb+srv://mongo-lesson:Angipoo123@cluster0.x1yb0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0";

exports.connect = () => {
  mongoose
    .connect(MONGO_URI, {
      dbName: "mongo-lesson",
      useNewUrlParser: true,
      useUnifiedTopology: true,
    })
    .then(() => {
      console.log("Connected to MongoDB Atlas");
    })
    .catch((error) => {
      console.error("Error connecting to MongoDB:", error);
      process.exit(1);
    });
};
