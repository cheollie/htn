package com.example.htn2023syde

import io.flutter.embedding.android.FlutterActivity
import io.flutter.embedding.android.FlutterActivity
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugins.firebase.messaging.FlutterFirebaseMessagingService
import io.flutter.plugins.GeneratedPluginRegistrant
import com.google.firebase.messaging.FirebaseMessaging

class MainActivity : FlutterActivity() {
    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        GeneratedPluginRegistrant.registerWith(flutterEngine)

        // Initialize Firebase Cloud Messaging
        FirebaseMessaging.getInstance().isAutoInitEnabled = true
        FlutterFirebaseMessagingService.setPluginRegistrant(this)
    }
}

import 'package:firebase_messaging/firebase_messaging.dart';

final FirebaseMessaging _firebaseMessaging = FirebaseMessaging();

void configureFirebaseMessaging() {
  _firebaseMessaging.configure(
    onMessage: (Map<String, dynamic> message) async {
      // Handle the received message when the app is in the foreground.
    },
    onLaunch: (Map<String, dynamic> message) async {
      // Handle the tapped notification when the app is closed.
    },
    onResume: (Map<String, dynamic> message) async {
      // Handle the tapped notification when the app is in the background.
    },
  );
}
