// app.js 
const fs = require("fs");
const express = require("express");
const bodyParser = require("body-parser");
const app = express();
app.use(bodyParser.json());

const dataFilePath = "data.json";

app.get("/user/list", (req, res) => {
  fs.readFile(dataFilePath, "utf8", (err, data) => {
    if (err) {
      res.status(500).json({ error: "Internal server error" });
      return;
    }
    res.json(JSON.parse(data));
  });
});

app.get("/user/list/:username", (req, res) => {
  const username = req.params.username;
  fs.readFile(dataFilePath, "utf8", (err, data) => {
    if (err) {
      res.status(500).json({ error: "Internal server error" });
      return;
    }
    const users = JSON.parse(data);
    const user = users.find((user) => user.username === username);
    if (user) {
      res.json(user);
    } else {
      res.status(404).json({ error: "User not found" });
    }
  });
});

app.post("/user/add", (req, res) => {
  const newUser = req.body;
  console.log(newUser);
  if (
    !newUser.username ||
    !newUser.name ||
    !newUser.password ||
    !newUser.occupation
  ) {
    return res.status(400).json({ error: "Missing required fields" });
  }
  fs.readFile(dataFilePath, "utf8", (err, data) => {
    if (err) {
      res.status(500).json({ error: "Internal server error" });
      return;
    }
    const users = JSON.parse(data);
    if (users.some(user => user.username === newUser.username)) {
        return res.status(409).json({ error: "Username already exists" });
      }
    users.push(newUser);
    fs.writeFile(dataFilePath, JSON.stringify(users, null, 2), (err) => {
      if (err) {
        res.status(500).json({ error: "Internal server error" });
        return;
      }
      res.json({ message: "User added successfully" });
    });
  });
});

app.patch("/user/update/:username", (req, res) => {
  const username = req.params.username;
  const updatedFields = req.body;

  fs.readFile(dataFilePath, "utf8", (err, data) => {
    if (err) {
      res.status(500).json({ error: "Internal server error" });
      return;
    }
    const users = JSON.parse(data);
    const index = users.findIndex((user) => user.username === username);
    if (index !== -1) {
      users[index] = { ...users[index], ...updatedFields };
      fs.writeFile(dataFilePath, JSON.stringify(users, null, 2), (err) => {
        if (err) {
          res.status(500).json({ error: "Internal server error" });
          return;
        }
        res.json({ message: "User updated successfully" });
      });
    } else {
      res.status(404).json({ error: "User not found" });
    }
  });
});

app.delete("/user/delete/:username", (req, res) => {
  const username = req.params.username;
  fs.readFile(dataFilePath, "utf8", (err, data) => {
    if (err) {
      res.status(500).json({ error: "Internal server error" });
      return;
    }
    const users = JSON.parse(data);
    const index = users.findIndex((user) => user.username === username);
    if (index !== -1) {
      users.splice(index, 1);
      fs.writeFile(dataFilePath, JSON.stringify(users, null, 2), (err) => {
        if (err) {
          res.status(500).json({ error: "Internal server error" });
          return;
        }
        res.json({ message: "User deleted successfully" });
      });
    } else {
      res.status(404).json({ error: "User not found" });
    }
  });
});

const PORT = 8080;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
