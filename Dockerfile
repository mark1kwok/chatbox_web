# Multi-stage Dockerfile for Railway.com Deployment
# Builds the Chatbox Web app and serves it with Python FastAPI

# ============================================================
# Stage 1: Build the Node.js web application
# ============================================================
FROM node:22 AS builder

# Install system dependencies for sharp (image processing)
RUN apt-get update && apt-get install -y \
    python3 \
    make \
    g++ \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies (use --legacy-peer-deps to resolve dependency conflicts)
# Set npm timeout to 600 seconds for slow connections
RUN npm config set fetch-timeout 600000 && \
    npm install --legacy-peer-deps

# Copy source code
COPY . .

# Build the web app
RUN npm run build:web

# ============================================================
# Stage 2: Python runtime with FastAPI/Uvicorn
# ============================================================
FROM python:3.14-slim

WORKDIR /app

# Copy Python dependencies
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the built web app from builder stage
COPY --from=builder /app/release/app/dist/renderer /app/static

# Copy the FastAPI server
COPY server.py .

# Expose port (Railway will set PORT env variable)
EXPOSE 8000

# Railway.com will provide PORT env variable
# Update server.py to use os.getenv("PORT", "8000")
CMD ["sh", "-c", "uvicorn server:app --host 0.0.0.0 --port ${PORT:-8000}"]
