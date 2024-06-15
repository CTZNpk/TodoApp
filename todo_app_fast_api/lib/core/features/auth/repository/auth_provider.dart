import 'package:flutter/widgets.dart';
import 'package:riverpod_annotation/riverpod_annotation.dart';
import 'package:todo_app_fast_api/core/api/my_api_provider.dart';
import 'package:todo_app_fast_api/core/utils/utils.dart';

part 'auth_provider.g.dart';

@riverpod
Future signUp(
    SignUpRef ref, BuildContext context, String email, String password) async {
  try {
    await ref.read(myApiProvider).signup(email, password);
  } catch (e) {
    if (context.mounted) {
      showSnackBar(context: context, content: e.toString());
    }
  }
}

@riverpod
Future login(
    LoginRef ref, BuildContext context, String email, String password) async {
  try {
    await ref.read(myApiProvider).login(email, password);
  } catch (e) {
    if (context.mounted) {
      showSnackBar(context: context, content: e.toString());
    }
  }
}
