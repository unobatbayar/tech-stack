# 🚀 Technology Stacks Learning Repository

> A comprehensive collection of technology stacks, frameworks, and tools for building modern software projects. This repository serves as a learning resource and reference guide for developers exploring different technology combinations.

## 🆕 Latest Additions

### T3 Stack

- [T3Stack](https://create.t3.gg/) - Type-safe Next.js full-stack framework
  - [NextAuth.js](https://next-auth-example.vercel.app/) - Authentication for Next.js

### Security & Best Practices

| Goal               | Tool/Technique              |
| ------------------ | --------------------------- |
| Authentication     | NextAuth.js / Clerk         |
| Authorization      | `protectedProcedure`, RBAC  |
| Input validation   | Zod schemas                 |
| Rate limiting      | Upstash / Middleware        |
| Secrets management | `.env` + server-only access |
| Prevent spam/abuse | Rate limiting, reCAPTCHA    |
| External access    | Secure CORS setup           |

### Image Storage

- [Cloudinary](https://cloudinary.com/pricing) - Cloud-based image and video management
- [Amazon S3](https://aws.amazon.com/s3/) - Scalable object storage service

### Current Project Stack

- [Next.js](https://nextjs.org/) - React framework for production
- [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
- [ORM](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping) - Object-relational mapping for database abstraction
- [PostgreSQL](https://www.postgresql.org/) - Advanced open-source relational database
- [Docker](https://www.docker.com/) - Containerization platform

---

## 📋 Table of Contents

- [Repository Structure](#-repository-structure)
- [Quick Start](#-quick-start)
- [Technology Stacks](#-technology-stacks)
  - [Popular Full-Stack Combinations](#popular-full-stack-combinations)
  - [Frontend Technologies](#frontend-technologies)
  - [Backend Technologies](#backend-technologies)
  - [Database Technologies](#database-technologies)
  - [Mobile Development](#mobile-development)
  - [DevOps & Deployment](#devops--deployment)
  - [Specialized Technologies](#specialized-technologies)
- [Project Examples](#-project-examples)
- [Learning Resources](#-learning-resources)

---

## 📁 Repository Structure

This repository is organized by technology and includes practical examples:

```
tech-stack/
├── FastAPI/          # FastAPI Python web framework examples
├── Flask/            # Flask Python web framework examples
├── NestJS/           # NestJS TypeScript backend framework
├── NextJS/           # Next.js React framework examples
├── NodeJS/           # Node.js server-side JavaScript examples
├── React/            # React frontend library examples
├── socket.io/        # Real-time communication examples
├── sqlite3/          # SQLite database examples
├── typescript/       # TypeScript language examples
├── Libraries/        # Additional library resources
└── Projects/         # Complete project examples
```

---

## 🎯 Quick Start

### Explore by Technology

Navigate to any technology folder to find working examples and tutorials:

- **Python Backends**: `FastAPI/`, `Flask/`
- **JavaScript/TypeScript**: `NodeJS/`, `NextJS/`, `React/`, `NestJS/`, `typescript/`
- **Real-time**: `socket.io/`
- **Databases**: `sqlite3/`
- **Additional Resources**: `Libraries/`

### Running Examples

Each technology folder contains README files with setup instructions. Common commands:

```bash
# Node.js projects
npm install
npm start

# Python projects
pip install -r requirements.txt
python main.py

# TypeScript projects
npm install -g typescript
tsc index.ts
```

---

## 🛠 Technology Stacks

### Popular Full-Stack Combinations

#### The MERN Stack
| Component | Technology | Description |
|-----------|-----------|-------------|
| **M**ongoDB | [MongoDB](https://www.mongodb.com/) | NoSQL document database |
| **E**xpress.js | [Express.js](https://expressjs.com/) | Web application framework for Node.js |
| **R**eact | [React](https://reactjs.org/) | JavaScript library for building user interfaces |
| **N**ode.js | [Node.js](https://nodejs.org/en/) | JavaScript runtime environment |

#### The MEAN Stack
| Component | Technology | Description |
|-----------|-----------|-------------|
| **M**ongoDB | [MongoDB](https://www.mongodb.com/) | NoSQL document database |
| **E**xpress.js | [Express.js](https://expressjs.com/) | Web application framework for Node.js |
| **A**ngular | [AngularJS](https://angularjs.org/) | JavaScript framework for building web applications |
| **N**ode.js | [Node.js](https://nodejs.org/en/) | JavaScript runtime environment |

#### The MEVN Stack
| Component | Technology | Description |
|-----------|-----------|-------------|
| **M**ongoDB | [MongoDB](https://www.mongodb.com/) | NoSQL document database |
| **E**xpress.js | [Express.js](https://expressjs.com/) | Web application framework for Node.js |
| **V**ue.js | [Vue.js](https://vuejs.org/) | Progressive JavaScript framework |
| **N**ode.js | [Node.js](https://nodejs.org/en/) | JavaScript runtime environment |

#### The LAMP Stack
| Component | Technology | Description |
|-----------|-----------|-------------|
| **L**inux | [Linux](https://www.linux.org/) | Operating system |
| **A**pache | [Apache](https://httpd.apache.org/) | Web server |
| **M**ySQL | [MySQL](https://www.mysql.com/) | Relational database management system |
| **P**HP | [PHP](https://www.php.net/) | Server-side scripting language |

---

### Frontend Technologies

#### Modern JavaScript Frameworks

| Framework | Description | Use Cases |
|-----------|-------------|-----------|
| [React](https://reactjs.org/) | JavaScript library for building user interfaces | Single-page applications, component-based UIs |
| [Next.js](https://nextjs.org/) | React framework with SSR and static generation | Production-ready React applications, SEO-friendly sites |
| [Vue.js](https://vuejs.org/) | Progressive JavaScript framework | Interactive web interfaces, single-page applications |
| [Angular](https://angularjs.org/) | TypeScript-based web application framework | Enterprise applications, large-scale projects |

#### Styling & UI

| Technology | Description |
|------------|-------------|
| [Tailwind CSS](https://tailwindcss.com/) | Utility-first CSS framework for rapid UI development |
| [TypeScript](https://www.typescriptlang.org/) | Strongly typed superset of JavaScript |

#### State Management & Data Fetching

| Technology | Description |
|------------|-------------|
| [Apollo Client](https://www.apollographql.com/docs/react/) | GraphQL client for React with caching and state management |

---

### Backend Technologies

#### Python Frameworks

| Framework | Description | Best For |
|-----------|-------------|----------|
| [Flask](https://flask.palletsprojects.com/en/2.2.x/) | Lightweight Python web framework | Microservices, APIs, small to medium applications |
| [FastAPI](https://fastapi.tiangolo.com/) | Modern, fast Python web framework | High-performance APIs, automatic API documentation |
| [Django](https://www.djangoproject.com/) | High-level Python web framework | Full-featured web applications, rapid development |

#### JavaScript/TypeScript Frameworks

| Framework | Description | Best For |
|-----------|-------------|----------|
| [Node.js](https://nodejs.org/en/) | JavaScript runtime built on Chrome's V8 | Server-side JavaScript, real-time applications |
| [Express.js](https://expressjs.com/) | Minimal web framework for Node.js | REST APIs, web applications |
| [NestJS](https://nestjs.com/) | Progressive Node.js framework | Scalable server-side applications, TypeScript-first |

#### Java Frameworks

| Framework | Description |
|-----------|-------------|
| [Spring Boot](https://spring.io/guides/tutorials/rest/) | Java framework for building enterprise applications |

#### Ruby Frameworks

| Framework | Description |
|-----------|-------------|
| [Ruby on Rails](https://rubyonrails.org/) | Full-stack web application framework |

#### API Design

| Technology | Description |
|------------|-------------|
| [REST API](https://restfulapi.net/) | Architectural style using HTTP methods for operations |
| [GraphQL](https://graphql.org/) | Query language for APIs with flexible data retrieval |

#### ORM & Database Tools

| Technology | Description |
|------------|-------------|
| [ORM](https://en.wikipedia.org/wiki/Object%E2%80%93relational_mapping) | Object-relational mapping for database abstraction |
| [Prisma](https://www.prisma.io/) | Next-generation ORM with TypeScript support |
| [SQLAlchemy](https://www.sqlalchemy.org/) | Python SQL toolkit and ORM |

#### Architecture Patterns

| Pattern | Description |
|---------|-------------|
| [Backend For Frontend (BFF)](https://www.openlegacy.com/blog/backend-for-frontend) | Pattern where a separate backend service is created for each frontend application |

---

### Database Technologies

#### Relational Databases

| Database | Description | Use Cases |
|---------|-------------|-----------|
| [PostgreSQL](https://www.postgresql.org/) | Advanced open-source relational database | Complex queries, ACID compliance, enterprise applications |
| [MySQL](https://www.mysql.com/) | Popular open-source relational database | Web applications, content management systems |
| [SQLite](https://www.sqlite.org/index.html) | Lightweight, file-based database | Embedded applications, development, small projects |
| [SQL Server](https://www.microsoft.com/en-us/sql-server) | Microsoft's relational database | Enterprise applications, Windows ecosystem |

#### NoSQL Databases

| Database | Description | Use Cases |
|---------|-------------|-----------|
| [MongoDB](https://www.mongodb.com/) | Document-oriented NoSQL database | Flexible schemas, large-scale applications |
| [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) | Managed NoSQL database service | Serverless applications, high-performance workloads |

#### Object Storage

| Technology | Description |
|------------|-------------|
| [MinIO](https://min.io/) | AWS S3-compatible object storage solution |

#### Cloud APIs

| Service | Description |
|---------|-------------|
| [Microsoft Graph API](https://learn.microsoft.com/en-us/graph/) | API for accessing Microsoft 365 data (users, groups, calendars) |

---

### Mobile Development

#### Cross-Platform Frameworks

| Framework | Description | Best For |
|-----------|-------------|----------|
| [React Native](https://reactnative.dev/) | Framework for building native apps with React | iOS and Android apps with shared codebase |
| [Flutter](https://flutter.dev/) | Google's UI toolkit for building natively compiled apps | High-performance mobile apps, beautiful UIs |
| [Unity](https://unity.com/) | Game engine and development platform | Games, AR/VR applications |
| [Xamarin](https://dotnet.microsoft.com/en-us/apps/xamarin) | Microsoft's cross-platform mobile framework | .NET ecosystem, enterprise mobile apps |

#### Native Development

| Platform | Tools | Description |
|----------|-------|-------------|
| **iOS** | [Xcode](https://developer.apple.com/xcode/), Swift, SwiftUI | Native iOS application development |
| **Android** | [Android Studio](https://developer.android.com/studio), Kotlin, Jetpack Compose | Native Android application development |

#### Mobile Backend Services

| Service | Description |
|---------|-------------|
| [Firebase](https://firebase.google.com/) | Google's mobile and web application platform |
| [Firestore](https://firebase.google.com/docs/firestore) | NoSQL document database for mobile and web apps |

---

### DevOps & Deployment

#### Containerization

| Technology | Description |
|------------|-------------|
| [Docker](https://www.docker.com/) | Platform for containerizing applications |

#### Cloud Platforms

| Platform | Description | Resources |
|----------|-------------|-----------|
| [AWS](https://aws.amazon.com/) | Amazon Web Services cloud platform | [Getting Started Tutorials](https://aws.amazon.com/getting-started/hands-on/) |
| [Google Cloud](https://cloud.google.com/) | Google Cloud Platform | Cloud services and infrastructure |
| [Azure](https://azure.microsoft.com/) | Microsoft Azure cloud platform | Enterprise cloud solutions |

#### Deployment Strategies

- **Container Orchestration**: Kubernetes, Docker Swarm
- **Serverless**: AWS Lambda, Google Cloud Functions, Azure Functions
- **Platform as a Service**: Heroku, AWS Elastic Beanstalk

---

### Specialized Technologies

#### Real-time Communication

| Technology | Description | Use Cases |
|-----------|-------------|-----------|
| [Socket.IO](https://socket.io/) | Real-time bidirectional event-based communication | Chat applications, live updates, collaborative tools |
| [WebRTC](https://webrtc.org/) | Real-time communication for web and mobile apps | Video/audio calls, peer-to-peer connections |
| [Firebase Realtime Database](https://firebase.google.com/products/realtime-database) | Cloud-hosted NoSQL database with real-time sync | Real-time collaborative applications |
| [Agora.io](https://www.agora.io/) | Real-time engagement platform | Video, voice, and live interactive streaming |

**Socket.IO Resources:**
- [Emit Cheatsheet](https://socket.io/docs/v4/emit-cheatsheet)

#### AR/VR Development

| Technology | Description |
|------------|-------------|
| [Spatial Computing (SwiftUI / RealityKit)](https://developer.apple.com/wwdc23/topics/spatial-computing/) | Apple's framework for spatial computing applications |
| [Unity VR](https://learn.unity.com/course/create-with-vr) | Unity framework for virtual reality development |

#### Audio & Plug-ins

| Technology | Description |
|------------|-------------|
| [JUCE Framework](https://juce.com/) | Cross-platform C++ framework for audio applications |
| [C++](https://cplusplus.com/) | General-purpose programming language for system programming |

#### Hardware & IoT

| Technology | Description |
|------------|-------------|
| [Raspberry Pi](https://www.raspberrypi.com/documentation/) | Single-board computer for hardware projects |

#### Machine Learning Libraries

See `Libraries/machine-learning/libraries.txt` for a comprehensive list including:
- Scikit-learn, TensorFlow, Keras, PyTorch
- XGBoost, LightGBM, CatBoost
- And more...

---

## 📚 Project Examples

This repository contains practical examples organized by technology:

### Python Backends

- **FastAPI Projects**
  - `FastAPI/fastapi-template/` - Production-ready FastAPI template
  - `FastAPI/books-microservice/` - Books management microservice
  - `FastAPI/prisma_project/` - FastAPI with Prisma ORM
  - `FastAPI/metrics/backend/` - Metrics tracking backend

- **Flask Projects**
  - `Flask/flask_sqlalchemy_postgres/` - Flask with SQLAlchemy and PostgreSQL
  - `Flask/froshims/` - Sample Flask application
  - `Flask/hello/` - Hello World Flask example

### JavaScript/TypeScript

- **Next.js Projects**
  - `NextJS/my-app/` - Next.js application example
  - `NextJS/nextjs-dashboard/` - Dashboard application

- **React Projects**
  - `React/my-app/` - React application example

- **Node.js Projects**
  - `NodeJS/` - Express.js server example

- **Real-time**
  - `socket.io/` - Socket.IO chat application example

### Databases

- **SQLite Examples**
  - `sqlite3/` - SQLite database examples and demos

### TypeScript

- `typescript/` - TypeScript language examples and tutorials

---

## 🎓 Learning Resources

### Getting Started Guides

- [Node.js Ultimate Beginner's Guide](https://www.youtube.com/watch?v=ENrzD9HAZK4)
- [Socket.IO Getting Started](https://socket.io/get-started/chat/)

### Technology-Specific Documentation

Each technology folder contains:
- Working code examples
- Setup instructions
- README files with usage examples

### Recommended Learning Path

1. **Start with Fundamentals**
   - Choose a language (JavaScript/TypeScript or Python)
   - Learn basic web concepts (HTTP, REST APIs)

2. **Pick a Stack**
   - Frontend: React, Next.js, or Vue.js
   - Backend: Node.js/Express, FastAPI, or Flask
   - Database: PostgreSQL, MongoDB, or SQLite

3. **Build Projects**
   - Start with simple examples in this repository
   - Gradually build more complex applications
   - Explore different technology combinations

4. **Explore Advanced Topics**
   - Real-time communication (Socket.IO)
   - Containerization (Docker)
   - Cloud deployment (AWS, GCP, Azure)
   - Mobile development (React Native, Flutter)

---

## 📝 Example Project Stacks

### Modern Full-Stack Web Application

**Frontend:**
- Next.js (React framework)
- TypeScript
- Tailwind CSS
- Apollo Client (for GraphQL)

**Backend:**
- NestJS or FastAPI
- GraphQL API
- REST API
- Prisma ORM

**Database:**
- PostgreSQL
- MinIO (object storage)

**DevOps:**
- Docker
- Kubernetes (for production)

### Microservices Architecture

**API Services:**
- FastAPI (Python)
- Flask (Python)
- Node.js with Express
- Spring Boot (Java)

**Communication:**
- HTTP/REST
- GraphQL
- Message queues

**Database:**
- PostgreSQL (relational)
- MongoDB (document)
- SQLite (development)

### Mobile Application Stack

**Cross-Platform:**
- React Native
- Flutter

**Backend:**
- Node.js/Express or FastAPI
- GraphQL or REST API

**Database:**
- PostgreSQL
- SQLite (local storage)
- Firebase/Firestore

**Deployment:**
- App Store Connect (iOS)
- Google Play Console (Android)

---

## 🤝 Contributing

This is a learning repository. Feel free to:
- Add new technology examples
- Improve existing documentation
- Share your learning experiences
- Suggest new technology stacks

---

## 📄 License

This repository is for educational purposes. Check individual project folders for specific licenses.
