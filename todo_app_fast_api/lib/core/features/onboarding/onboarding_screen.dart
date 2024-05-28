import 'package:flutter/material.dart';

class OnboardingScreen extends StatelessWidget {
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
                  Size(size.width * 0.9, 60),
                ),
                shape: const WidgetStatePropertyAll<OutlinedBorder>(
                  RoundedRectangleBorder(
                    borderRadius: BorderRadius.all(
                      Radius.circular(
                        14,
                      ),
                    ),
                  ),
                ),
              ),
              onPressed: () {},
              child: const Text(
                'Get Started',
                style: TextStyle(
                  fontSize: 20,
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
