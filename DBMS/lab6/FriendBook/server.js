const express = require("express");
const mysql = require("mysql");
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.json());

app.use(express.static(__dirname)); // To serve index.html directly

// MySQL Connection
const db = mysql.createConnection({
    host: "localhost",
    user: "root",
    password: "your password", // Add your MySQL password
    database: "frienddb"
});

db.connect(err => {
    if (err) throw err;
    console.log("✅ MySQL Connected!");
});

// Add Friend
app.post("/add", (req, res) => {
    const { name, nickname, phone, city } = req.body;
    db.query("INSERT INTO friends (name, nickname, phone, city) VALUES (?,?,?,?)",
        [name, nickname, phone, city],
        () => res.send("🎉 Friend Added Successfully!"));
});

// View All Friends
app.get("/view", (req, res) => {
    db.query("SELECT * FROM friends", (err, rows) => {
        if (err) throw err;
        res.send(rows);
    });
});

// Edit Friend
app.post("/edit/:id", (req, res) => {
    const { name, nickname, phone, city } = req.body;
    const id = req.params.id;
    db.query("UPDATE friends SET name=?, nickname=?, phone=?, city=? WHERE id=?",
        [name, nickname, phone, city, id],
        () => res.send("✅ Friend Updated!"));
});

// Delete Friend
app.get("/delete/:id", (req, res) => {
    const id = req.params.id;
    db.query("DELETE FROM friends WHERE id=?", [id],
        () => res.send("🗑️ Friend Deleted!"));
});

// Start Server
app.listen(3000, () => console.log("🚀 Server running on http://localhost:3000"));
