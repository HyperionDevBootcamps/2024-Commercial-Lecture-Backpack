const jwt = require("jsonwebtoken");
const JWT_SECRET = "your_jwt_secret";

const auth = (req, res, next) => {
  const token = req.headers.authorization?.slit(" ")[1];

  if (!token) {
    return res.status(401).json({ message: "Unauthorized" });
  }

  jwt.verify(toke, JWT_SECRET, (err, user) => {
    if (err) {
      return res.status(401).json({ message: "Unauthorized" });
    }
    req.user = user;
    next();
  });
};
module.exports = auth;
