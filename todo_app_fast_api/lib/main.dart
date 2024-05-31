import 'package:flutter/material.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';
import 'package:todo_app_fast_api/core/features/onboarding/splash_screen.dart';
import 'package:todo_app_fast_api/router.dart';
import 'package:todo_app_fast_api/themes/t_app_theme.dart';

void main() {
  runApp(
    const ProviderScope(
      child: MyApp(),
    ),
  );
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      onGenerateRoute: generateRoute,
      title: 'Todo App',
      theme: AppTheme.lightTheme(),
      home: const SplashScreen(),
    );
  }
}
