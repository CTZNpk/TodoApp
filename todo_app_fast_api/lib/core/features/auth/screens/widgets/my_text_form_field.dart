import 'package:flutter/material.dart';

class MyTextFormField extends StatelessWidget {
  const MyTextFormField({
    super.key,
    required this.controller,
    required this.label,
    required this.prefixIcon,
    required this.validator,
    this.obscureText = false,
  });

  final TextEditingController controller;
  final String label;
  final Icon prefixIcon;
  final bool obscureText;
  final Function validator;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(12.0),
      child: TextFormField(
        validator: (text) => validator(text),
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
