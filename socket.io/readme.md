# Socket.IO Examples

This directory contains Socket.IO real-time communication examples and projects.

## 📖 About Socket.IO

Socket.IO enables real-time, bidirectional and event-based communication between the browser and the server. It works on every platform, browser or device, focusing equally on reliability and speed.

## 📁 Contents

- `index.js` - Socket.IO server implementation
- `index.html` - Client-side HTML example
- `start.html` - Alternative client example
- `package.json` - Project dependencies
- `readme.md` - Quick reference notes

## 🚀 Quick Start

### Installation

```bash
npm install
```

### Running the Server

```bash
node index.js
```

### Opening the Client

Open `index.html` or `start.html` in your browser, or serve it through a web server.

## 📚 Resources

- [Socket.IO Official Website](https://socket.io/)
- [Socket.IO Getting Started Guide](https://socket.io/get-started/chat/)
- [Socket.IO Documentation](https://socket.io/docs/v4/)
- [Socket.IO Emit Cheatsheet](https://socket.io/docs/v4/emit-cheatsheet)

## 💡 Key Concepts

### Server-Side (Node.js)

```javascript
const io = require('socket.io')(server);

io.on('connection', (socket) => {
  console.log('User connected');
  
  socket.on('message', (data) => {
    io.emit('message', data);
  });
});
```

### Client-Side (Browser)

```javascript
const socket = io();

socket.on('connect', () => {
  console.log('Connected to server');
});

socket.emit('message', 'Hello Server');
socket.on('message', (data) => {
  console.log('Received:', data);
});
```

## 🔧 Common Use Cases

- Real-time chat applications
- Live notifications
- Collaborative editing
- Live data dashboards
- Gaming applications
- Live updates and feeds
