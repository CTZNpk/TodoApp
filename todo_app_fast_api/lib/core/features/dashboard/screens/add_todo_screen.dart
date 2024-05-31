import 'package:flutter/material.dart';
import 'package:flutter_hooks/flutter_hooks.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';
import 'package:todo_app_fast_api/core/features/auth/screens/widgets/my_text_form_field.dart';

class AddTodoScreen extends HookConsumerWidget {
  const AddTodoScreen({super.key});
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final size = MediaQuery.of(context).size;
    final titleController = useTextEditingController();

    return Scaffold(
      appBar: AppBar(),
      body: ListView(
        children: [
          SizedBox(
            height: size.height * 0.5,
            child: Image.asset(
              'assets/images/tick.png',
            ),
          ),
          MyTextFormField(
            controller: titleController,
            label: 'Enter Todo Title...',
            prefixIcon: const Icon(Icons.check),
          ),
          MyTextFormField(
            controller: titleController,
            label: 'Enter Todo Description...',
            prefixIcon: const Icon(Icons.description),
          ),
          const Padding(
            padding: EdgeInsets.all(20),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Text(
                  'Repeat this todo daily',
                  style: TextStyle(
                    fontSize: 16,
                    fontWeight: FontWeight.w500,
                  ),
                ),
                Icon(Icons.check_box),
              ],
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(12.0),
            child: ElevatedButton(
              onPressed: () {},
              style: const ButtonStyle(
                fixedSize: WidgetStatePropertyAll<Size>(
                  Size(0, 50),
                ),
              ),
              child: const Text(
                'Create Todo',
              ),
            ),
          ),
        ],
      ),
    );
  }
}
