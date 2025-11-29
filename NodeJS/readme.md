# Node.js Examples

This directory contains Node.js server-side JavaScript examples and projects.

## 📖 About Node.js

Node.js is an open-source server environment that allows you to run JavaScript on the server. It's built on Chrome's V8 JavaScript engine and enables building scalable network applications.

## 📁 Contents

- `server.js` - Express.js server example with REST API endpoints
- `package.json` - Project dependencies
- `readme.md` - Quick reference notes

## 🚀 Quick Start

### Installation

```bash
npm install
```

### Running the Server

```bash
node server.js
```

The server will start on `http://localhost:3000` (or the port specified in your `.env` file).

### Example Endpoints

- `GET /` - Hello World
- `GET /api/items` - Get all items
- `POST /api/items` - Create a new item

## 📚 Resources

- [Node.js Official Website](https://nodejs.org/)
- [Node.js Documentation](https://nodejs.org/docs/)
- [Express.js Documentation](https://expressjs.com/)
- [Getting Started with Node.js Backend](https://medium.com/@holasoymalva/how-to-create-my-first-backend-project-with-node-js-0f8463cc24be)
- [W3Schools Node.js Tutorial](https://www.w3schools.com/nodejs/default.asp)

## 💡 Common Commands

```bash
# Install dependencies
npm install

# Start server
node server.js

# Run with nodemon (auto-restart on changes)
npx nodemon server.js
```
