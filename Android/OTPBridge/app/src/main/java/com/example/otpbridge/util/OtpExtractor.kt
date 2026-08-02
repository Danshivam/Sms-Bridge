package com.example.otpbridge.util

object OtpExtractor {

    private val otpRegex = Regex("\\b\\d{4,8}\\b")

    fun extract(message: String): String? {
        return otpRegex.find(message)?.value
    }
}