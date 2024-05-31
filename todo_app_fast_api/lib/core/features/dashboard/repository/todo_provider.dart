import 'dart:convert';

import 'package:http/http.dart' as http;
import 'package:todo_app_fast_api/core/models/todo/todo.dart';
import 'package:riverpod_annotation/riverpod_annotation.dart';

part 'todo_provider.g.dart';

@riverpod
class TodoList extends _$TodoList {
  @override
  Future<List<Todo>> build() async {
    final url = Uri.parse('http://10.0.2.2:5000/todo/');
    final Map<String, String> headers = {
      'Content-Type': 'application/json',
      //TODO Add token
    };
    http.Response response = await http.get(url, headers: headers);
    return (jsonDecode(response.body) as List)
        .cast<Map<String, Object?>>()
        .map(Todo.fromJson)
        .toList();
  }

  Future<void> addTodo(Todo todo) async {
    final url = Uri.parse('http://10.0.2.2:5000/todo/');
    final Map<String, String> headers = {
      'Content-Type': 'application/json',
      //TODO Add token
    };
    await http.post(url, headers: headers, body: todo.toJson());
    ref.invalidateSelf();
    await future;
  }
}
