# Deployment Files Summary

This document summarizes the deployment setup for the Chatbox Web application.

## Files Created/Modified

### 1. **Dockerfile**
Multi-stage Docker build that:
- Stage 1: Builds the Node.js web app
- Stage 2: Serves with Python FastAPI/Uvicorn
- Optimized for Railway.com (uses PORT environment variable)

### 2. **.dockerignore**
Excludes unnecessary files from Docker build:
- `node_modules/`, `.venv/`
- Development files (`.vscode/`, tests)
- Documentation (except README.md)
- Platform-specific code (electron, capacitor)

### 3. **server.py** (Updated)
FastAPI server with:
- Support for PORT environment variable (Railway.com)
- Dual path support (local dev + Docker deployment)
- Serves static files from `release/app/dist/renderer/` or `static/`

### 4. **requirements.txt** (Updated)
Python dependencies:
```
fastapi==0.115.6
uvicorn[standard]==0.34.0
```

### 5. **RAILWAY_DEPLOY.md**
Complete deployment guide for Railway.com with:
- Step-by-step deployment instructions
- Configuration options
- Troubleshooting tips
- Local Docker testing commands

### 6. **Project_Desc.md** (Updated)
- Current Status: Marked build configuration as complete
- Added "Build Prerequisites" section with webpack config fixes
- Added Railway.com deployment section

### 7. **package.json** (Fixed)
- Fixed script: `delete-source-maps.js` (was `delete-source-maps-runner.js`)

### 8. **.erb/configs/webpack.config.renderer.dev.dll.ts** (Fixed)
- Added `@capacitor/android` and `@capacitor/ios` to EXCLUDE_MODULES

## Quick Commands

### Local Development
```bash
# Install dependencies
npm install

# Build the web app
npm run build:web

# Start local server
python server.py
# Or with venv:
.venv/Scripts/python.exe server.py

# Access at: http://localhost:8000
```

### Docker Build & Test
```bash
# Build Docker image
docker build -t chatbox-web .

# Run container
docker run -p 8000:8000 chatbox-web

# Access at: http://localhost:8000
```

### Railway.com Deployment
```bash
# Option 1: GitHub Integration (Recommended)
git push origin main
# Then connect repo in Railway dashboard

# Option 2: Railway CLI
railway login
railway init
railway up
```

## Deployment Flow

```
┌─────────────────┐
│  Source Code    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  npm install    │  ← Installs Node.js dependencies
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ npm run build:  │  ← Compiles React app to static files
│      web        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Static Files   │  ← Output: release/app/dist/renderer/
└────────┬────────┘
         │
         ├─────────────────────┐
         │                     │
         ▼                     ▼
┌────────────────┐    ┌────────────────┐
│ Local Server   │    │ Docker Build   │
│  (server.py)   │    │  (Dockerfile)  │
└────────────────┘    └────────┬───────┘
                              │
                              ▼
                      ┌────────────────┐
                      │  Railway.com   │
                      │  Deployment    │
                      └────────────────┘
```

## Environment Variables

### Local Development
- No environment variables required
- Default port: 8000

### Railway.com
- `PORT`: Automatically set by Railway (typically 8000-9000)
- Server automatically uses this variable

## Build Requirements

### Node.js Stage
- Node.js 22.x
- npm 11.x
- ~5-10 minutes build time

### Python Stage
- Python 3.14
- FastAPI + Uvicorn
- ~1-2 minutes install time

## Next Steps

1. ✅ Web app build working locally
2. ✅ FastAPI server working locally
3. ✅ Docker configuration created
4. ⏳ Test Docker build locally (optional)
5. ⏳ Deploy to Railway.com
6. ⏳ Add custom domain (optional)
7. ⏳ Implement user data sync (future feature)
