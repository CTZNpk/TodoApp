import 'dart:convert';

import 'package:dio/dio.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';
import 'package:todo_app_fast_api/core/api/custom_interceptor.dart';
import 'package:todo_app_fast_api/core/models/todo/todo.dart';

final myApiProvider = Provider((ref) => MyApi());

class MyApi {
  final Dio _dio = Dio(
    BaseOptions(
      baseUrl: 'http://10.0.2.2:8000/',
      responseType: ResponseType.json,
      contentType: 'application/json',
    ),
  );

  MyApi() {
    _dio.interceptors.add(CustomInterceptors());
  }

  Future login(String email, String password) async {
    try {
      FormData formData =
          FormData.fromMap({'username': email, 'password': password});
      await _dio.post('login', data: formData);
    } on DioException catch (e) {
      throw e.response!.data['detail'];
    }
  }

  Future signup(String email, String password) async {
    try {
      FormData formData =
          FormData.fromMap({'username': email, 'password': password});
      await _dio.post('signup', data: formData);
    } on DioException catch (e) {
      throw e.response!.data['detail'];
    }
  }

  Future<List<Todo>> getUserTodos() async {
    Response response = await _dio.get('todo');
    return (jsonDecode(response.data) as List)
        .cast<Map<String, Object?>>()
        .map(Todo.fromJson)
        .toList();
  }

  Future createUserTodo(Todo todo) async {
    await _dio.post('todo', data: todo.toJson());
  }

  Future checkTodo(String todoId) async {
    await _dio.post('/$todoId/done');
  }

  Future deleteTodo(String todoId) async {
    await _dio.delete('/$todoId');
  }

  Future updateTodo(Todo todo) async {
    await _dio.patch('/${todo.id}', data: todo.toJson());
  }
}
