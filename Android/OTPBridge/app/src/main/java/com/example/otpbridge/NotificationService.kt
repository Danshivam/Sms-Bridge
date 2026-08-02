package com.example.otpbridge

import android.service.notification.NotificationListenerService
import android.service.notification.StatusBarNotification
import android.util.Log
import com.example.otpbridge.util.OtpExtractor
import android.app.Notification
import com.example.otpbridge.model.NotificationMessage
import com.example.otpbridge.repository.SmsRepository
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch

class NotificationService : NotificationListenerService() {
    companion object {
        private const val TAG = "OTP_SERVICE"

        private const val SMS_PACKAGE =
            "com.google.android.apps.messaging"
    }

    private val repository = SmsRepository()

    override fun onListenerConnected() {
        super.onListenerConnected()
        Log.i(TAG, "Notification Listener Connected")
    }


    override fun onNotificationPosted(sbn: StatusBarNotification?) {
        super.onNotificationPosted(sbn)

        if (sbn == null) return

        val extras = sbn.notification.extras

        // Log every notification
        Log.i(TAG, "========== Notification Extras ==========")

        for (key in extras.keySet()) {
            val value = extras.get(key)
            Log.i(TAG, "$key = $value")
        }

        Log.i(TAG, "=========================================")

        val title = extras.getString(Notification.EXTRA_TITLE) ?: ""

        val message = extras
            .getCharSequence(Notification.EXTRA_TEXT)
            ?.toString()
            ?: ""

        if (message.contains("doing work in the background", ignoreCase = true)) {
            return
        }

        val otp = OtpExtractor.extract(message)

        if (otp != null) {
            Log.i(TAG, "OTP Found: $otp")
        } else {
            Log.i(TAG, "No OTP Found")
        }

        Log.i(TAG, "========== Notification ==========")
        Log.i(TAG, "App     : ${sbn.packageName}")
        Log.i(TAG, "Sender  : $title")
        Log.i(TAG, "Message : $message")
        Log.i(TAG, "===============================")

        // Only Google Messages notifications are sent to the server
        if (sbn.packageName != SMS_PACKAGE) {
            Log.i(TAG, "Not an SMS notification. Skipping server upload.")
            return
        }

        CoroutineScope(Dispatchers.IO).launch {
            try {
                repository.sendNotification(
                    NotificationMessage(
                        app = sbn.packageName,
                        title = title,
                        message = message,
                        timestamp = System.currentTimeMillis()
                    )
                )

                Log.i(TAG, "Notification sent to server")

            } catch (e: Exception) {
                Log.e(TAG, "Failed to send notification", e)
            }
        }
    }
}