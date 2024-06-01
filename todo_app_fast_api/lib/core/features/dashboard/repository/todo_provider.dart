import 'package:todo_app_fast_api/core/api/my_api_provider.dart';
import 'package:todo_app_fast_api/core/models/todo/todo.dart';
import 'package:riverpod_annotation/riverpod_annotation.dart';

part 'todo_provider.g.dart';

@riverpod
class TodoList extends _$TodoList {
  @override
  Future<List<Todo>> build() async {
    return await ref.read(myApiProvider).getUserTodos();
  }

  Future<void> addTodo(Todo todo) async {
    await ref.read(myApiProvider).createUserTodo(todo);
    ref.invalidateSelf();
    await future;
  }
}
