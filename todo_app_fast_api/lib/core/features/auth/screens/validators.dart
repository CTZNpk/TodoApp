bool emailValidator(String text) {
  final emailExp = RegExp(r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$');
  return emailExp.hasMatch(text);
}

bool passwordValidator(String text) {
  final passExp = RegExp(r'^(?=.*[A-Z])(?=.*\d).{6,}$');
  return passExp.hasMatch(text);
}
