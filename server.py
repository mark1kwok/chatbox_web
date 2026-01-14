"""
FastAPI server to serve the Chatbox web application.
This server serves the static files from the release/app/dist/renderer directory.
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
from pathlib import Path

app = FastAPI(title="Chatbox Web Server")

# Get the absolute path to the static files directory
BASE_DIR = Path(__file__).parent

# Support both local development and Docker deployment paths
if (BASE_DIR / "static").exists():
    # Docker deployment (copied to /app/static)
    STATIC_DIR = BASE_DIR / "static"
else:
    # Local development (built in release/app/dist/renderer)
    STATIC_DIR = BASE_DIR / "release" / "app" / "dist" / "renderer"

# Verify the static directory exists
if not STATIC_DIR.exists():
    raise RuntimeError(f"Static files directory not found: {STATIC_DIR}")

# Mount the assets directory to serve static files (JS, CSS, images, etc.)
app.mount("/assets", StaticFiles(directory=str(STATIC_DIR / "assets")), name="assets")

# Serve favicon
@app.get("/favicon.ico")
async def favicon():
    """Serve the favicon."""
    return FileResponse(str(STATIC_DIR / "favicon.ico"))

# Serve CSS files
@app.get("/{filename:path}.css")
async def serve_css(filename: str):
    """Serve CSS files."""
    css_path = STATIC_DIR / f"{filename}.css"
    if css_path.exists():
        return FileResponse(str(css_path))
    return FileResponse(str(STATIC_DIR / "index.html"))

# Serve CSS map files
@app.get("/{filename:path}.css.map")
async def serve_css_map(filename: str):
    """Serve CSS map files."""
    map_path = STATIC_DIR / f"{filename}.css.map"
    if map_path.exists():
        return FileResponse(str(map_path))
    return FileResponse(str(STATIC_DIR / "index.html"))

# Serve the index.html for all other routes (SPA fallback)
@app.get("/{full_path:path}")
async def serve_spa(full_path: str):
    """
    Serve the Single Page Application.
    All routes are handled by index.html, which will handle routing client-side.
    """
    return FileResponse(str(STATIC_DIR / "index.html"))


if __name__ == "__main__":
    import uvicorn
    
    # Support Railway.com PORT environment variable
    port = int(os.getenv("PORT", "8000"))
    
    print(f"\n{'='*60}")
    print(f"🚀 Starting Chatbox Web Server")
    print(f"{'='*60}")
    print(f"📁 Serving files from: {STATIC_DIR}")
    print(f"🌐 Access the app at: http://localhost:{port}")
    print(f"{'='*60}\n")
    
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=port,
        log_level="info"
    )
