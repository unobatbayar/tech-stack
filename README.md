# Technology Stacks — Learning Repository

Hands-on examples and a curated reference for modern full-stack development. Explore working code by folder, then use the stack guide below to see what teams commonly choose in 2026.

## Repository layout

```
tech-stack/
├── FastAPI/       # Python APIs (tutorial, Prisma integration)
├── Flask/         # Flask + SQLAlchemy + PostgreSQL examples
├── NestJS/        # Placeholder + getting-started notes
├── NextJS/        # Next.js 15 App Router (React 19, Tailwind)
├── NodeJS/        # Express server example
├── React/         # Standalone React app
├── socket.io/     # Real-time chat demo
├── sqlite3/       # SQLite examples
├── typescript/    # TypeScript basics
├── Libraries/     # Extra references (e.g. ML library list)
└── Projects/      # Larger project notes
```

## Quick start

Each folder has its own README or setup notes. Typical commands:

```bash
# Node / Next.js / React
cd NextJS/my-app   # or NextJS/nextjs-dashboard, React/my-app, NodeJS
npm install
npm run dev        # Next.js; use `npm start` for CRA-style React apps

# Python
cd FastAPI/tutorial   # or Flask/flask_sqlalchemy_postgres
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload   # FastAPI; Flask projects use `flask run` / app.py

# TypeScript compile demo
cd typescript
npx tsc
```

Prefer **Node 20+** and **Python 3.11+** for the examples in this repo.

---

## Modern stacks (2026 reference)

These are industry-common combinations—not every folder here implements all of them. Use them to plan what to learn next.

### Full-stack (TypeScript-first)

| Stack | Core pieces | Good for |
|-------|-------------|----------|
| **T3** | [Next.js](https://nextjs.org/) · [tRPC](https://trpc.io/) · [Prisma](https://www.prisma.io/) · [Tailwind](https://tailwindcss.com/) · [Auth.js](https://authjs.dev/) | End-to-end type safety, SaaS products |
| **Next.js full-stack** | App Router · Server Actions · [Drizzle](https://orm.drizzle.team/) or Prisma · Postgres · deploy on [Vercel](https://vercel.com/) | Content sites, dashboards, B2B apps |
| **PERN+** | Postgres · Express or [Hono](https://hono.dev/) · React · optional [TanStack Query](https://tanstack.com/query) | APIs you want to keep separate from the UI |

### Frontend

| Tool | Notes |
|------|--------|
| [React 19](https://react.dev/) + [Next.js 15](https://nextjs.org/docs) | Default for new web apps; App Router, RSC, Turbopack (`next dev --turbopack`) |
| [Vue 3](https://vuejs.org/) + [Nuxt](https://nuxt.com/) | Progressive apps, strong DX in Vue ecosystem |
| [SvelteKit](https://svelte.dev/) / [Astro](https://astro.build/) | Lean bundles; Astro for content-heavy sites |
| [Tailwind CSS v4](https://tailwindcss.com/) | Utility-first styling (used in `NextJS/` examples) |
| [shadcn/ui](https://ui.shadcn.com/) | Copy-paste components on Radix + Tailwind |

### Backend & APIs

| Tool | Notes |
|------|--------|
| [FastAPI](https://fastapi.tiangolo.com/) | Async Python APIs, OpenAPI docs — see `FastAPI/` |
| [NestJS](https://nestjs.com/) | Structured Node backends (see `NestJS/README.md`) |
| [Flask](https://flask.palletsprojects.com/) | Lightweight Python — see `Flask/` |
| [Hono](https://hono.dev/) / [Elysia](https://elysiajs.com/) | Fast edge-friendly APIs on Bun or Node |
| REST + [OpenAPI](https://www.openapis.org/) | Still the default for public and mobile clients |

### Data & storage

| Tool | Notes |
|------|--------|
| [PostgreSQL](https://www.postgresql.org/) | Default production relational DB |
| [SQLite](https://www.sqlite.org/) | Local/dev — see `sqlite3/` |
| [Prisma](https://www.prisma.io/) / [Drizzle](https://orm.drizzle.team/) | Type-safe ORMs for TS/JS stacks |
| [SQLAlchemy](https://www.sqlalchemy.org/) + [Alembic](https://alembic.sqlalchemy.org/) | Python ORM/migrations — see Flask & FastAPI tutorials |
| [Supabase](https://supabase.com/) / [Neon](https://neon.tech/) | Managed Postgres + auth/storage options |
| [S3](https://aws.amazon.com/s3/) / [R2](https://www.cloudflare.com/r2/) / [Cloudinary](https://cloudinary.com/) | Object and media storage |

### Auth, security & reliability

| Goal | Common approach |
|------|-----------------|
| Authentication | [Auth.js](https://authjs.dev/) (NextAuth v5), [Clerk](https://clerk.com/), [Better Auth](https://www.better-auth.com/) |
| Authorization | RBAC, route guards, tRPC `protectedProcedure` |
| Validation | [Zod](https://zod.dev/) on client and server |
| Rate limiting | Edge middleware, [Upstash Redis](https://upstash.com/) |
| Secrets | `.env` locally; platform secrets in production (never commit keys) |

### Real-time & mobile (when you need them)

| Tool | Notes |
|------|--------|
| [Socket.IO](https://socket.io/) | WebSockets with fallbacks — see `socket.io/` |
| [React Native](https://reactnative.dev/) + [Expo](https://expo.dev/) | Cross-platform mobile with shared React skills |
| [Flutter](https://flutter.dev/) | Single codebase, strong UI performance |

### DevOps & deployment

| Approach | Examples |
|----------|----------|
| Containers | [Docker](https://www.docker.com/) — used in several `Flask/` and `FastAPI/` projects |
| Frontend / full-stack hosting | Vercel, Netlify, Cloudflare Pages |
| Backend / DB hosting | Fly.io, Railway, Render, managed Postgres |
| Orchestration | Kubernetes when you outgrow PaaS |

### AI-enabled apps (2026)

| Layer | Examples |
|-------|----------|
| Models | OpenAI, Anthropic, Google Gemini, local via [Ollama](https://ollama.com/) |
| Orchestration | [Vercel AI SDK](https://sdk.vercel.ai/), [LangChain](https://www.langchain.com/) |
| Patterns | RAG over your Postgres/pgvector store, tool-calling agents, streaming UI |

---

## Examples in this repo

### Python

| Path | Description |
|------|-------------|
| `FastAPI/tutorial/` | FastAPI + SQLAlchemy + Alembic + Docker |
| `FastAPI/prisma_project/` | FastAPI with Prisma schema |
| `Flask/flask_sqlalchemy_postgres/` | Flask, SQLAlchemy, Postgres, migrations |
| `Flask/froshims/` | Multi-page Flask sample |
| `Flask/hello/` | Minimal Flask app |

### JavaScript / TypeScript

| Path | Description |
|------|-------------|
| `NextJS/my-app/` | Next.js 15, React 19, App Router, Tailwind |
| `NextJS/nextjs-dashboard/` | Dashboard-style Next.js app |
| `React/my-app/` | Create React App style example |
| `NodeJS/` | Express server |
| `socket.io/` | Real-time chat |
| `typescript/` | TS compile demo |

### Other

| Path | Description |
|------|-------------|
| `sqlite3/` | SQLite demos |
| `Libraries/machine-learning/libraries.txt` | ML library index |
| `NestJS/` | Getting started (add projects here) |
| `Projects/` | Notes for larger builds |

---

## Suggested learning path

1. **Fundamentals** — HTTP, REST, Git, one language (TypeScript or Python).
2. **One vertical slice** — e.g. `NextJS/my-app` or `FastAPI/tutorial` end to end.
3. **Data layer** — Postgres + an ORM (Prisma/Drizzle or SQLAlchemy).
4. **Production basics** — Docker, env secrets, auth, and a single deployment target.
5. **Go wider** — real-time (`socket.io/`), mobile, or AI features as your project needs them.

### External starters

- [React documentation](https://react.dev/learn)
- [Next.js Learn](https://nextjs.org/learn)
- [FastAPI tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Socket.IO chat tutorial](https://socket.io/get-started/chat/)

---

## Contributing

Add examples, fix docs, or suggest stacks you are learning. Keep each example runnable with a short README in its folder.

## License

Educational use. See individual project folders for specific licenses.
