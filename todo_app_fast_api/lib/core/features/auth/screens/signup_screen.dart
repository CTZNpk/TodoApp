import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';
import 'package:todo_app_fast_api/core/features/auth/repository/auth_provider.dart';
import 'package:todo_app_fast_api/core/features/auth/screens/login_screen.dart';
import 'package:todo_app_fast_api/core/features/auth/screens/validators.dart';
import 'package:todo_app_fast_api/core/features/auth/screens/widgets/my_text_form_field.dart';
import 'package:todo_app_fast_api/themes/t_app_theme.dart';

class SignupScreen extends HookConsumerWidget {
  static const routeName = '/signup_screen';
  const SignupScreen({super.key});


  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final emailController = useTextEditingController();
    final passwordController = useTextEditingController();
    final confirmPasswordController = useTextEditingController();
    final size = MediaQuery.of(context).size;
    final formKey = GlobalKey<FormState>();

    void signUp(){
       ref.read(
        signUpProvider(
          context,
          emailController.text.trim(),
          passwordController.text.trim(),
        ),);
    }

    return Scaffold(
      appBar: AppBar(
        title: const Text(
          'Signup Screen',
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
            MyTextFormField(
              controller: confirmPasswordController,
              label: "Enter Confirm Password ...",
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
                      const TextSpan(text: 'Already have an account? '),
                      TextSpan(
                        text: 'Login Here',
                        recognizer: TapGestureRecognizer()
                          ..onTap = () {
                            Navigator.pushReplacementNamed(
                                context, LoginScreen.routeName);
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
                onPressed: ,
                style: ButtonStyle(
                  fixedSize: WidgetStatePropertyAll<Size>(
                    Size(size.width * 0.9, 50),
                  ),
                ),
                child: const Text(
                  'Signup',
                ),
              ),
            )
          ],
        ),
      ),
    );
  }
}
