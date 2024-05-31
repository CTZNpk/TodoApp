import 'package:flutter/material.dart';
import 'package:todo_app_fast_api/core/features/onboarding/onboarding_screen.dart';
import 'package:todo_app_fast_api/themes/t_app_theme.dart';

class SplashScreen extends StatelessWidget {
  const SplashScreen({super.key});

  @override
  Widget build(BuildContext context) {
    Future.delayed(const Duration(seconds: 3), () {
      Navigator.pushReplacementNamed(context, OnboardingScreen.routeName);
    });

    return Scaffold(
      backgroundColor: AppTheme.primaryColor,
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Image.asset(
              'assets/images/app_logo.png',
              scale: 2.5,
            ),
            Text(
              'Todo List App',
              style: TextStyle(
                fontSize: 26,
                color: AppTheme.backgroundColor,
              ),
            )
          ],
        ),
      ),
    );
  }
}
