# SMS Bridge

SMS Bridge is an open-source Android-to-desktop messaging platform currently under active development. The long-term goal of the project is to provide seamless synchronization of SMS messages, conversations, and notifications between an Android device and a desktop interface in real time.

The current version focuses on building the core communication pipeline. Notifications received on the Android device are captured using Android's Notification Listener Service, processed locally, and forwarded to a FastAPI backend. The backend analyzes incoming notifications, stores them in memory, and instantly broadcasts them to connected clients using WebSockets. This enables live updates on the browser without requiring manual page refreshes.

One of the primary features implemented in this version is automatic OTP (One-Time Password) detection. OTPs are extracted from notification text, displayed in a dedicated card layout, and can be copied instantly using a single click. Additional features include timestamp formatting, live notification synchronization, and a browser dashboard that updates in real time as new notifications arrive.

## Current Features (v0.1.0)

- Android Notification Listener Service
- FastAPI backend
- Real-time WebSocket communication
- Live browser dashboard
- Automatic OTP detection
- One-click OTP copy button
- Timestamp formatting
- Live notification synchronization
- Modular backend architecture

## Technology Stack

- Kotlin
- Jetpack Compose
- FastAPI
- Python
- HTML
- CSS
- JavaScript
- WebSockets
- Retrofit
- Pydantic

## Security Notice

This project is currently in the prototype stage. **No security mechanisms have been implemented yet.** Features such as API authentication, encryption, HTTPS, access control, secure key management, rate limiting, and production-level validation are intentionally deferred until the core functionality is complete. The current implementation is intended **only for local development and testing** and should **not** be exposed to the public internet or used in production.

## Roadmap

- Conversation-based messaging interface
- SQLite database for persistent storage
- Direct SMS database integration
- SMS sending and reply support
- Advanced search and filtering
- Contact management
- Default SMS application support
- API authentication and encryption
- Desktop application
- Cloud synchronization across multiple devices

SMS Bridge is an evolving project, and future versions will focus on transforming it into a complete cross-platform SMS management platform while improving architecture, performance, and security.