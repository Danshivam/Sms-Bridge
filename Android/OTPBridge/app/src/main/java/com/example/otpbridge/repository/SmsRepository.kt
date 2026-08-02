package com.example.otpbridge.repository

import com.example.otpbridge.model.NotificationMessage
import com.example.otpbridge.network.ApiClient

class SmsRepository {

    suspend fun sendNotification(notification: NotificationMessage) {
        ApiClient.api.sendNotification(notification)
    }

}