import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_messaging/firebase_messaging.dart';
import 'package:logger/logger.dart'; // Import the logger package

import 'src/app.dart';
import 'src/settings/settings_controller.dart';
import 'src/settings/settings_service.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();

  final FirebaseMessaging firebaseMessaging = FirebaseMessaging.instance;

  // Request notification permissions
  await firebaseMessaging.requestPermission();


  // Set up a logger instance
  var logger = Logger();

  // Get the FCM token
String? fcmToken = await firebaseMessaging.getToken();
logger.d("FCM Token: $fcmToken"); // Log the FCM token

  // Handle incoming FCM messages
  FirebaseMessaging.onMessage.listen((RemoteMessage message) {
    // Handle the received message when the app is in the foreground.
    logger.d("onMessage: $message"); // Use logger for debugging
  });

  FirebaseMessaging.onMessageOpenedApp.listen((RemoteMessage message) {
    // Handle the tapped notification when the app is in the background or terminated.
    logger.d("onMessageOpenedApp: $message"); // Use logger for debugging
  });

  final settingsController = SettingsController(SettingsService());
  await settingsController.loadSettings();

  runApp(MyApp(settingsController: settingsController));
}


