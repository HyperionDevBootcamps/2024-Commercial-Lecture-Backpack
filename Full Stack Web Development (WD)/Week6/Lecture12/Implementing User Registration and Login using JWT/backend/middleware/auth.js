// middleware/auth.js
const jwt = require("jsonwebtoken");

const JWT_SECRET = "your_jwt_secret"; // Use a secure key

const auth = (req, res, next) => {
  const token = req.headers.authorization?.split(" ")[1];
  console.log(token); // Get token from Authorization header

  if (!token) {
    return res.status(403).json({ error: "Forbidden" }); // No token, forbidden
  }

  // Verify the token
  jwt.verify(token, JWT_SECRET, (err, user) => {
    if (err) {
      return res.status(403).json({ error: "Forbidden" }); // Invalid token
    }
    req.user = user; // Attach user info to the request
    next(); // Proceed to the next middleware/route handler
  });
};

module.exports = auth;
