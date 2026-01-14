# Chatbox Web - Project Description

## Project Goal

This is a **wrapper fork** of the original [Chatbox](https://github.com/chatboxai/chatbox) open-source AI chat application. The primary goal is to:

1. **Maintain only the web app version** - stripping away all desktop (Electron) and mobile (Capacitor) specific code
2. **Add user data sync functionality** - enable cross-device synchronization via a self-hosted backend with centralized storage
3. **Track upstream updates** - eventually implement a mechanism to dynamically retrieve and merge updates from the original Chatbox repository

## Project Nature

This is a **simplified, web-only fork** that maintains the core Chatbox functionality while:

- Removing Electron main process code (desktop apps)
- Removing Capacitor code (mobile apps)
- Keeping the React frontend renderer that powers the web experience
- Adding a backend service for user data synchronization (planned)

---

## Web App Architecture: Pure Frontend SPA

**Confirmed**: The Chatbox web app is a **pure Single Page Application (SPA)** with:

| Aspect | Implementation |
|--------|----------------|
| **Data Storage** | IndexedDB (browser-based) - all data stored locally in user's browser |
| **AI API Calls** | Direct browser-to-API calls using `fetch()` - no proxy backend required |
| **Server-Side Code** | None - runs entirely in the browser |
| **Backend Dependencies** | None - can be deployed as static files |
| **Authentication** | Stored in browser's local storage via Zustand persistence |

The web app requires **no backend server** to function. It can be deployed to any static file hosting service (Nginx, Caddy, Vercel, Netlify, GitHub Pages, etc.) and work out of the box.

---

## Desktop/Mobile Code to Remove

When unbinding platform-specific code, the following can be removed:

### Electron (Desktop) Files
| Category | Path/Files |
|----------|------------|
| Main process | `src/main/` (entire directory) |
| Electron config | `electron-builder.yml` |
| Boilerplate configs | `.erb/` directory |
| Electron dependencies | `electron-updater`, `electron-store`, `electron-log`, `auto-launch` |

### Capacitor (Mobile) Files
| Category | Path/Files |
|----------|------------|
| Mobile configs | `capacitor.config.ts`, `ios/`, `android/` |
| Capacitor deps | All `@capacitor/*` packages in `package.json` |
| Mobile scripts | `npm run mobile:*` commands |

---

## Data Sync Feature (Planned)

### Architecture Overview

For cross-device data synchronization, the implementation will use a **centralized storage model**:

```
[User Device 1] ──┐
[User Device 2] ──┼───► [Sync Server] ──► [SQLite DB (Persistent Volume)]
[User Device N] ──┘               └──► Sync API Endpoints
```

### Benefits of This Approach

| Advantage | Description |
|-----------|-------------|
| **Simplified UX** | Users don't need to configure cloud storage credentials |
| **Consistent Experience** | Same sync behavior across all users |
| **Full Control** | Data stored on self-hosted infrastructure |
| **Privacy** | No 3rd party storage provider integration needed |
| **Simplified Code** | No complex OAuth flows for Google Drive/Dropbox APIs |

### Implementation Details

| Component | Technology |
|-----------|------------|
| Backend Server | FastAPI (Python) with Uvicorn |
| Database | SQLite (small scale, easy deployment) |
| Storage | Persistent volume (Docker) |
| Auth | Simple token-based or OAuth |
| API | REST endpoints for sync operations |

### Sync Flow

1. User logs in / authenticates
2. Browser app fetches data from sync server
3. Data merged with local IndexedDB
4. Changes pushed to sync server on update
5. Other devices pull updates periodically or via WebSocket

---

## Docker Multi-Stage Build

Since the web app compiles to **static files only**, the build can be cached in a Docker multi-stage setup:

```dockerfile
# Stage 1: Build React app (can be cached)
FROM node:20 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build:web

# Stage 2: Serve with web server
FROM caddy:2-alpine
COPY --from=builder /app/release/app/dist/renderer/ /srv/
# Add sync server later as another stage
```

The builder stage can be cached and reused unless `src/` files change, speeding up rebuilds.

---

## Current Status

**Phase: Initial Setup**

- [x] Repository forked from latest main branch of chatboxai/chatbox
- [x] Initial codebase analysis completed
- [x] Platform-specific code identified
- [x] Web app build process verified (`npm run build:web`)
- [x] Confirmed: Pure frontend SPA architecture (no backend required)
- [x] Build configuration stripped of desktop/mobile blocking dependencies
- [ ] User data sync feature design (pending)
- [ ] Sync backend implementation (pending)
- [ ] Upstream sync mechanism implementation (pending)

---

## Web App Deployment

### Build Prerequisites

Before running `npm run build:web`, ensure the following configuration changes are in place:

**1. Webpack DLL Config** (`.erb/configs/webpack.config.renderer.dev.dll.ts`):
```typescript
const EXCLUDE_MODULES = new Set([
    '@modelcontextprotocol/sdk',
    '@mastra/core',
    '@mastra/rag',
    '@libsql/client',
    'capacitor-stream-http',
    '@capacitor/android',  // Add this
    '@capacitor/ios',      // Add this
  ])
```

**2. Package.json Scripts**:
```json
"delete-sourcemaps": "ts-node ./.erb/scripts/delete-source-maps.js"
```
(Note: Changed from `delete-source-maps-runner.js` to `delete-source-maps.js`)

### Building the Web App

The web app code is **ready to build** and can be deployed as static files:

```bash
npm install          # Install dependencies
npm run build:web    # Output: release/app/dist/renderer/
```

### Serving Options

For serving the built web app, options include:
- **Python FastAPI**: `python server.py` (included in repo)
- **Nginx**: Traditional web server
- **Caddy**: Modern web server with automatic HTTPS
- **Apache**: Classic web server
- **Vercel/Netlify**: Serverless platforms
- **Railway.com**: Container-based deployment (see [RAILWAY_DEPLOY.md](RAILWAY_DEPLOY.md))
- Or any static file hosting service

### Railway.com Deployment

For one-click container deployment to Railway.com:

1. Push repository to GitHub
2. Connect to Railway.com
3. Railway auto-detects `Dockerfile` and deploys
4. Get a public URL instantly

See [RAILWAY_DEPLOY.md](RAILWAY_DEPLOY.md) for detailed instructions.

---

## Original Project

- **Repository**: https://github.com/chatboxai/chatbox
- **License**: GPLv3
- **Original Maintainers**: ChatboxAI team
