// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'todo.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

_$TodoImpl _$$TodoImplFromJson(Map<String, dynamic> json) => _$TodoImpl(
      title: json['title'] as String,
      description: json['description'] as String,
      isDaily: json['isDaily'] as bool,
      isCompleted: json['isCompleted'] as bool,
    );

Map<String, dynamic> _$$TodoImplToJson(_$TodoImpl instance) =>
    <String, dynamic>{
      'title': instance.title,
      'description': instance.description,
      'isDaily': instance.isDaily,
      'isCompleted': instance.isCompleted,
    };
