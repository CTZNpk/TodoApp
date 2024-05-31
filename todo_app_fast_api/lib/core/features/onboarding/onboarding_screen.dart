import 'package:flutter/material.dart';
import 'package:todo_app_fast_api/core/features/auth/screens/login_screen.dart';

class OnboardingScreen extends StatelessWidget {
  static const routeName = '/onboarding_screen';
  const OnboardingScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final size = MediaQuery.of(context).size;
    return Scaffold(
      body: Column(
        mainAxisAlignment: MainAxisAlignment.end,
        children: [
          Expanded(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Image.asset('assets/images/onboarding_todo.png'),
                const Padding(
                  padding: EdgeInsets.all(8.0),
                  child: Text(
                    'Welcome to Todo List App where you can manage your daily and weekly tasks and get your weekly reviews',
                    textAlign: TextAlign.center,
                    style: TextStyle(fontSize: 22),
                  ),
                ),
              ],
            ),
          ),
          Padding(
            padding: const EdgeInsets.only(bottom: 20.0),
            child: ElevatedButton(
              style: ButtonStyle(
                fixedSize: WidgetStatePropertyAll<Size>(
                  Size(size.width * 0.9, 50),
                ),
              ),
              onPressed: () => Navigator.pushReplacementNamed(
                context,
                LoginScreen.routeName,
              ),
              child: const Text(
                'Get Started',
              ),
            ),
          ),
        ],
      ),
    );
  }
}
