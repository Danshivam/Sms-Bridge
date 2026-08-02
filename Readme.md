# SMSBridge

SMSBridge is a desktop companion application that allows you to:

- Read SMS from your desktop
- View OTPs instantly
- Send SMS from your PC
- Sync conversations in real time
- Manage messages from a browser

## Technologies

### Android
- Kotlin
- Jetpack Compose
- Room
- Notification Listener
- SMS APIs

### Backend
- FastAPI
- WebSockets
- SQLite

### Frontend
- HTML
- CSS
- JavaScript

## Status

🚧 Under Development

## Version 0.1.0

Implemented the first end-to-end notification pipeline.

Android:
- Added NotificationListenerService
- Extract notification title and message
- Added OTP extraction utility
- Integrated Retrofit repository for sending notifications
- Added notification inspector for debugging notification extras
- Added package filtering for Google Messages (currently optional)

Backend:
- Created FastAPI notification endpoint
- Added notification model
- Added OTP analyzer
- Added timestamp formatter
- Added WebSocket manager
- Implemented in-memory notification storage

Frontend:
- Added live dashboard
- Real-time updates using WebSockets
- OTP cards with copy button
- Formatted timestamps
- Newest notifications appear first

General:
- Verified end-to-end notification flow
- Built debugging tools for inspecting Android notification metadata