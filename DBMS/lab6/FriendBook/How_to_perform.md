#  How to Perform This Experiment — FriendBook

---

##  Install Node.js (if not already installed)

- Go to [https://nodejs.org](https://nodejs.org)  
- Download and install **Node.js (LTS version)**  
- After installation, open **VS Code → Terminal → New Terminal**  
- Type the following commands to verify Node installation:
  ```bash
  node -v
  npm -v
  ```

---

##  Open CMD inside VS Code

- Open the **FriendBook** folder in **VS Code**  
- Right-click → **Open in Integrated Terminal**  
  *(or press `Ctrl + `)*  

---

##  Install Required npm Packages

Type these commands one by one in the terminal:
```bash
npm i express
npm i body-parser
npm i mysql
```
💡 *If `mysql` gives issues, use this instead:*
```bash
npm i mysql2
```

---

##  Create Database

- Open **MySQL / XAMPP / phpMyAdmin**  
- Run the **schema.sql** file:
  ```sql
  SOURCE schema.sql;
  ```
- This will create the database and all required tables for **FriendBook**.

---

## Connect Node.js Server with MySQL

- Open the **server.js** file.  
- In the database connection section, find the line:
  ```js
  password: "your password"
  ```
- Replace `"your password"` with your actual **MySQL password** (for example, `"root"` or the one you set manually).

---

## Run the Node.js Server

Type the following command in VS Code terminal:
```bash
node --watch server.js
```
*This will start the Node server in watch mode, so it auto-restarts when you modify your code.*

---

## 7️⃣ Open the Application

Once the server starts successfully, open your browser and visit:
```
http://localhost:3000
```

The **FriendBook** web app will load and connect to your MySQL database.

---

## Everything is Done!

Your **Node.js server**, **MySQL database**, and **frontend (index.html)** are all connected and running successfully.  
Now your **FriendBook** experiment is fully working!

---

