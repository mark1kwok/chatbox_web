# Railway.com Deployment Guide for Chatbox Web

This guide explains how to deploy the Chatbox web application to Railway.com.

## Prerequisites

- A [Railway.com](https://railway.app/) account
- Git repository of this project (GitHub, GitLab, or Bitbucket)

## Deployment Steps

### Option 1: Deploy from GitHub (Recommended)

1. **Push your code to GitHub**:
   ```bash
   git add .
   git commit -m "Ready for Railway deployment"
   git push origin main
   ```

2. **Create a new project on Railway**:
   - Go to [railway.app](https://railway.app/)
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

3. **Railway will automatically**:
   - Detect the `Dockerfile`
   - Build the multi-stage Docker image
   - Deploy the application
   - Assign a public URL

4. **Access your app**:
   - Railway will provide a URL like: `https://your-app.up.railway.app`

### Option 2: Deploy with Railway CLI

1. **Install Railway CLI**:
   ```bash
   npm install -g @railway/cli
   ```

2. **Login to Railway**:
   ```bash
   railway login
   ```

3. **Initialize and deploy**:
   ```bash
   railway init
   railway up
   ```

4. **Link to a domain** (optional):
   ```bash
   railway domain
   ```

## Configuration

### Environment Variables

Railway automatically sets the `PORT` environment variable. The server is configured to use it.

If you need to add custom environment variables:
1. Go to your project in Railway dashboard
2. Click on "Variables" tab
3. Add your variables

### Automatic Deployments

Railway can automatically deploy when you push to your main branch:
1. Go to Settings in Railway dashboard
2. Under "Deploys", enable "Auto Deploy"

## Dockerfile Explanation

The deployment uses a multi-stage build:

1. **Stage 1 (Node.js Builder)**:
   - Installs Node.js dependencies
   - Builds the web app with `npm run build:web`
   - Output: Static files in `release/app/dist/renderer/`

2. **Stage 2 (Python Runtime)**:
   - Uses Python 3.14 slim image
   - Installs FastAPI and Uvicorn
   - Copies built static files from Stage 1
   - Serves the app on Railway's `PORT`

## Build Time

- First build: ~5-10 minutes (includes npm install and build)
- Subsequent builds: ~2-5 minutes (uses cached layers)

## Costs

- Railway offers a **free tier** with:
  - $5 of usage per month
  - 500 hours of execution time
  - Unlimited deployments

- This application should easily fit within the free tier for personal use

## Monitoring

- View logs: Railway Dashboard → Your Project → Deployments
- Monitor metrics: CPU, Memory, Network usage available in dashboard

## Troubleshooting

### Build Fails

Check the build logs in Railway dashboard. Common issues:
- Missing dependencies in `package.json`
- Node.js version mismatch (requires Node 20+)

### App Not Starting

- Check that `server.py` exists in repository
- Verify `requirements.txt` has correct dependencies
- Check Railway logs for Python errors

### Static Files Not Loading

- Verify build completed successfully
- Check that `release/app/dist/renderer/` was created during build
- Ensure Dockerfile copies files correctly

## Local Testing with Docker

Test the Docker build locally before deploying:

```bash
# Build the image
docker build -t chatbox-web .

# Run the container
docker run -p 8000:8000 chatbox-web

# Access at http://localhost:8000
```

## Custom Domain

To use a custom domain:
1. Go to Railway dashboard
2. Click on "Settings"
3. Under "Domains", click "Add Domain"
4. Follow the DNS configuration instructions

## Support

- Railway Documentation: https://docs.railway.app/
- Railway Discord: https://discord.gg/railway
- Project Issues: Create an issue in your GitHub repository
