import 'package:flutter/material.dart';
import 'package:flutter/rendering.dart';
import 'package:flutter/widgets.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';
import 'package:todo_app_fast_api/themes/t_app_theme.dart';

class SignupScreen extends HookConsumerWidget {
  const SignupScreen({super.key});
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final emailController = useTextEditingController();
    final passwordController = useTextEditingController();
    final size = MediaQuery.of(context).size;

    return Scaffold(
      body: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        children: [
          SizedBox(
            height: size.height * 0.15,
          ),
          Image.asset(
            'assets/images/tick.png',
          ),
          const SizedBox(
            height: 50,
          ),
          MyTextFormField(
            controller: emailController,
          ),
          MyTextFormField(
            controller: passwordController,
          ),
          const SizedBox(
            height: 8,
          ),
          Padding(
            padding: const EdgeInsets.all(12.0),
            child: RichText(
              text: TextSpan(
                style: TextStyle(
                  color: AppTheme.primaryColor,
                  fontSize: 16,
                ),
                children: const [
                  TextSpan(text: 'Already have an account? '),
                  TextSpan(
                    text: 'Login Here',
                    style: TextStyle(
                      color: Colors.blue,
                      decoration: TextDecoration.underline,
                    ),
                  ),
                ],
              ),
            ),
          ),
          const SizedBox(
            height: 20,
          ),
          ElevatedButton(
            onPressed: () {},
            style: ButtonStyle(
              fixedSize: WidgetStatePropertyAll<Size>(
                Size(size.width * 0.9, 50),
              ),
            ),
            child: const Text(
              'Sign Up',
            ),
          )
        ],
      ),
    );
  }
}

class MyTextFormField extends StatelessWidget {
  const MyTextFormField({
    super.key,
    required this.controller,
  });

  final TextEditingController controller;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(12.0),
      child: TextFormField(
        controller: controller,
        decoration: const InputDecoration(
          filled: true,
          label: Text('Enter Email ...'),
          prefixIcon: Icon(Icons.email),
          labelStyle: TextStyle(
            color: Colors.grey,
          ),
          prefixIconColor: Colors.grey,
        ),
      ),
    );
  }
}

