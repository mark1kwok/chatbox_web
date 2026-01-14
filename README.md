<p align="right">
  <a href="README.md">English</a> |
  <a href="./doc/README-CN.md">简体中文</a>
</p>

# Chatbox Web (Wrapper Fork)

This is a **web-only fork** of the [Chatbox Community Edition](https://github.com/chatboxai/chatbox), open-sourced under the GPLv3 license.

> **Note**: This project is a wrapper fork that maintains only the web app version. For the original multi-platform version, visit [chatboxai/chatbox](https://github.com/chatboxai/chatbox).

---

## About

Chatbox Web is a web-based AI client for ChatGPT, Claude and other LLMs. This fork aims to:

- Provide a web-only version of Chatbox
- Add user data synchronization across devices (planned)
- Track and merge updates from the original Chatbox repository

**Web App**: [https://chatboxai.app/](https://chatboxai.app/)

---

<h1 align="center">
<img src='./doc/statics/icon.png' width='30'>
<span>Chatbox Web</span>
</h1>
<p align="center">
    <em>Your Ultimate AI Copilot on the Web.</em>
</p>

<a href="https://www.producthunt.com/posts/chatbox?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-chatbox" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=429547&theme=light" alt="Chatbox - Better&#0032;UI&#0032;&#0038;&#0032;Desktop&#0032;App&#0032;for&#0032;ChatGPT&#0044;&#0032;Claude&#0032;and&#0032;other&#0032;LLMs&#0046; | Product Hunt" style="width: 150px; height: 30px;" width="100" height="40" /></a>

<a href="./doc/statics/snapshot_light.png">
<img src="./doc/statics/snapshot_light.png" width="400"/>
</a>
<a href="./doc/statics/snapshot_dark.png">
<img src="./doc/statics/snapshot_dark.png" width="400"/>
</a>

---

## Features

-   **Local Data Storage**
    :floppy_disk: Your data remains on your device, ensuring it never gets lost and maintains your privacy.

-   **Support for Multiple LLM Providers**
    :gear: Seamlessly integrate with a variety of cutting-edge language models:

    -   OpenAI (ChatGPT)
    -   Azure OpenAI
    -   Claude
    -   Google Gemini Pro
    -   Ollama (enable access to local models)
    -   And more...

-   **Image Generation with Dall-E-3**
    :art: Create the images of your imagination with Dall-E-3.

-   **Enhanced Prompting**
    :speech_balloon: Advanced prompting features to refine and focus your queries for better responses.

-   **Markdown, Latex & Code Highlighting**
    :scroll: Generate messages with the full power of Markdown and Latex formatting, coupled with syntax highlighting for various programming languages.

-   **Prompt Library & Message Quoting**
    :books: Save and organize prompts for reuse, and quote messages for context in discussions.

-   **Streaming Reply**
    :arrow_forward: Provide rapid responses to your interactions with immediate, progressive replies.

-   **Dark Theme**
    :new_moon: A user-friendly interface with a night mode option for reduced eye strain during extended use.

-   **Multilingual Support**
    :earth_americas: Catering to a global audience by offering support in multiple languages.

---

## Architecture

**Chatbox Web is a pure Single Page Application (SPA)**:

| Aspect | Implementation |
|--------|----------------|
| Data Storage | IndexedDB (browser-based) |
| AI API Calls | Direct browser-to-API (no proxy required) |
| Server-Side Code | None - runs entirely in the browser |
| Deployment | Static files only - any web server or CDN |

**No backend server is required** for the core web app to function. It can be deployed to any static file hosting service and work out of the box.

---

## Getting Started

### Prerequisites

- Node.js (v20.x – v22.x)
- npm (required – pnpm is not supported)

### Development

```bash
# Install dependencies
npm install

# Start web app in development mode
npm run dev:web
```

### Building

```bash
# Build for web
npm run build:web

# Serve the built web app
npm run serve:web
```

Build output is placed in `release/app/dist/renderer/`.

---

## Deployment

The built web app is a static bundle (HTML, CSS, JS) that can be served by any web server:

- Nginx
- Caddy
- Apache
- Vercel
- Netlify
- GitHub Pages
- Or any static file hosting service

See [Project_Desc.md](./Project_Desc.md) for more details on this fork's goals and status.

---

## Planned Features

### Cross-Device Data Sync

A future update will add user data synchronization using a self-hosted backend:

- **Centralized storage** with SQLite database
- **Persistent volume** for data persistence across container restarts
- **FastAPI backend** with sync API endpoints
- **Cross-device access** - sync between desktop, laptop, mobile browsers

This approach eliminates the need for users to configure cloud storage credentials like Google Drive or Dropbox.

---

## FAQ

-   [Frequently Asked Questions](./doc/FAQ.md)

---

## Original Project

This is a fork of [chatboxai/chatbox](https://github.com/chatboxai/chatbox). All credit goes to the original authors.

---

## License

[GPLv3](./LICENSE)
