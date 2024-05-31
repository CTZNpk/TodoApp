import 'package:flutter/material.dart';
import 'package:todo_app_fast_api/core/features/auth/screens/login_screen.dart';
import 'package:todo_app_fast_api/core/features/auth/screens/signup_screen.dart';
import 'package:todo_app_fast_api/core/features/dashboard/screens/add_todo_screen.dart';
import 'package:todo_app_fast_api/core/features/dashboard/screens/main_screen.dart';
import 'package:todo_app_fast_api/core/features/onboarding/onboarding_screen.dart';

Route<dynamic> generateRoute(RouteSettings settings) {
  switch (settings.name) {
    case OnboardingScreen.routeName:
      return MaterialPageRoute(
        builder: (context) => const OnboardingScreen(),
      );
    case LoginScreen.routeName:
      return MaterialPageRoute(
        builder: (context) => const LoginScreen(),
      );
    case SignupScreen.routeName:
      return MaterialPageRoute(
        builder: (context) => const SignupScreen(),
      );
    case MainPage.routeName:
      return MaterialPageRoute(
        builder: (context) => const MainPage(),
      );
    case AddTodoScreen.routeName:
      return MaterialPageRoute(
      builder: (context) => const AddTodoScreen(),
      );
    default:
      return MaterialPageRoute(
        builder: (context) => const Scaffold(
          body: Center(
            child: Text('This Page Does not Exist'),
          ),
        ),
      );
  }
}
