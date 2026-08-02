package com.example.otpbridge.network

import com.example.otpbridge.model.NotificationMessage
import retrofit2.Response
import retrofit2.http.Body
import retrofit2.http.POST

interface ApiService {

    @POST("/notification")
    suspend fun sendNotification(
        @Body notification: NotificationMessage
    ): Response<Unit>
}
