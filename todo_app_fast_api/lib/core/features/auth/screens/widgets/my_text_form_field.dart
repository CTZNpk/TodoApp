import 'package:flutter/material.dart';

class MyTextFormField extends StatelessWidget {
  const MyTextFormField({
    super.key,
    required this.controller,
    required this.label,
    required this.prefixIcon,
    this.obscureText = false,
  });

  final TextEditingController controller;
  final String label;
  final Icon prefixIcon;
  final bool obscureText;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(12.0),
      child: TextFormField(
        controller: controller,
        obscureText: obscureText,
        decoration: InputDecoration(
          filled: true,
          label: Text(label),
          prefixIcon: prefixIcon,
          labelStyle: const TextStyle(
            color: Colors.grey,
          ),
          prefixIconColor: Colors.grey,
        ),
      ),
    );
  }
}
