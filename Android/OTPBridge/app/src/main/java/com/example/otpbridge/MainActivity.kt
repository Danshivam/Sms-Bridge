package com.example.otpbridge

import android.os.Bundle
import android.widget.Toast
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.lifecycle.lifecycleScope
import com.example.otpbridge.repository.SmsRepository
import com.example.otpbridge.ui.theme.OTPBridgeTheme
import kotlinx.coroutines.launch
import com.example.otpbridge.model.NotificationMessage

class MainActivity : ComponentActivity() {

    private val repository = SmsRepository()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        enableEdgeToEdge()

        setContent {
            OTPBridgeTheme {
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    HomeScreen {
                        lifecycleScope.launch {

                            try {
                                repository.sendNotification(
                                    NotificationMessage(
                                        app = "SMS Bridge",
                                        title = "Test",
                                        message = "Hello Android! your otp is 723864",
                                        timestamp = System.currentTimeMillis()
                                    )
                                )

                                Toast.makeText(
                                    this@MainActivity,
                                    "Message Sent",
                                    Toast.LENGTH_SHORT
                                ).show()

                            } catch (e: Exception) {

                                Toast.makeText(
                                    this@MainActivity,
                                    "Error: ${e.message}",
                                    Toast.LENGTH_LONG
                                ).show()
                            }
                        }
                    }
                }
            }
        }
    }
}

@Composable
fun HomeScreen(
    onSendClick: () -> Unit
) {

    Column(
        modifier = Modifier.fillMaxSize(),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {

        Button(
            onClick = onSendClick
        ) {

            Text("Send Test Message")

        }
    }
}