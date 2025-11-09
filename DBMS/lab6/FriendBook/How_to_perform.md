🧪 How to Perform This Experiment — FriendBook
1️⃣ Install Node.js (if not already installed)

Go to https://nodejs.org

Download and install Node.js (LTS version)

After installation, open VS Code → Terminal → New Terminal

Type the following to check if Node is installed:

node -v
npm -v

2️⃣ Open CMD inside VS Code

Open the FriendBook folder in VS Code.

Right-click → Open in Integrated Terminal (or press Ctrl + `).

3️⃣ Install Required npm Packages

Type these commands one by one in the terminal:

npm i express
npm i body-parser
npm i mysql


(If mysql gives issues, use npm i mysql2 instead.)

4️⃣ Create Database

Open MySQL / XAMPP / phpMyAdmin.

Run the schema.sql file.

SOURCE schema.sql;


This will create the database and all required tables for FriendBook.

5️⃣ Connect Node.js Server with MySQL

Open the server.js file.

In the database connection section, find the line:

password: "your password"


Replace "your password" with your actual MySQL password (for example, "root" or whatever you set).

6️⃣ Run the Node.js Server

In VS Code terminal, type:

node --watch server.js


This will start the Node server in watch mode, which means it will auto-restart if you edit the code.

7️⃣ Open the Application

Once the server starts, go to your browser and type:

http://localhost:3000


The FriendBook web app will open and connect to your MySQL database.

✅ Everything is done!
Your Node.js server, database connection, and frontend are successfully running together.