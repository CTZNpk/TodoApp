import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';
import 'package:todo_app_fast_api/core/features/auth/repository/auth_provider.dart';
import 'package:todo_app_fast_api/core/features/auth/screens/signup_screen.dart';
import 'package:todo_app_fast_api/core/features/auth/screens/validators.dart';
import 'package:todo_app_fast_api/core/features/auth/screens/widgets/my_text_form_field.dart';
import 'package:todo_app_fast_api/themes/t_app_theme.dart';

class LoginScreen extends HookConsumerWidget {
  static const routeName = '/login_screen';
  const LoginScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final emailController = useTextEditingController();
    final passwordController = useTextEditingController();
    final size = MediaQuery.of(context).size;
    final formKey = GlobalKey<FormState>();

    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Login Screen',
          style: TextStyle(
            fontSize: 20,
          ),
        ),
        centerTitle: true,
      ),
      body: Form(
        key: formKey,
        child: ListView(
          children: [
            SizedBox(
              height: size.height * 0.4,
              child: Image.asset(
                'assets/images/tick.png',
              ),
            ),
            MyTextFormField(
              controller: emailController,
              label: "Enter Email ...",
              prefixIcon: const Icon(Icons.email),
              validator: emailValidator,
            ),
            MyTextFormField(
              controller: passwordController,
              label: "Enter Password ...",
              prefixIcon: const Icon(Icons.password),
              obscureText: true,
              validator: passwordValidator,
            ),
            const SizedBox(
              height: 8,
            ),
            Center(
              child: Padding(
                padding: const EdgeInsets.all(12.0),
                child: RichText(
                  text: TextSpan(
                    style: TextStyle(
                      color: AppTheme.primaryColor,
                      fontSize: 16,
                    ),
                    children: [
                      const TextSpan(text: 'New to todo list app? '),
                      TextSpan(
                        text: 'Signup Here',
                        recognizer: TapGestureRecognizer()
                          ..onTap = () {
                            Navigator.pushReplacementNamed(
                                context, SignupScreen.routeName);
                          },
                        style: const TextStyle(
                          color: Colors.blue,
                          decoration: TextDecoration.underline,
                        ),
                      ),
                    ],
                  ),
                ),
              ),
            ),
            Padding(
              padding: const EdgeInsets.only(
                left: 12.0,
                right: 12.0,
                bottom: 12.0,
              ),
              child: ElevatedButton(
                onPressed: () => ref.read(
                  loginProvider(
                    context,
                    emailController.text.trim(),
                    passwordController.text.trim(),
                  ),
                ),
                style: ButtonStyle(
                  fixedSize: WidgetStatePropertyAll<Size>(
                    Size(size.width * 0.9, 50),
                  ),
                ),
                child: const Text(
                  'Login',
                ),
              ),
            )
          ],
        ),
      ),
    );
  }
}
