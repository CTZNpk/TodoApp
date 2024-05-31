import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:hooks_riverpod/hooks_riverpod.dart';
import 'package:intl/intl.dart';
import 'package:todo_app_fast_api/themes/t_app_theme.dart';

class MainPage extends HookConsumerWidget {
  static const routeName = '/main_page';
  const MainPage({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final now = DateTime.now();
    final size = MediaQuery.of(context).size;

    return Scaffold(
      appBar: AppBar(
        title: Text(
          DateFormat('MMMM dd').format(now).toString(),
        ),
        centerTitle: true,
      ),
      drawer: Drawer(
        backgroundColor: AppTheme.backgroundColor,
        child: ListView(
          children: [
            Card(
              elevation: 6,
              color: AppTheme.cardBackgroundColor,
              margin: EdgeInsets.all(20),
              child: Padding(
                padding: const EdgeInsets.all(12.0),
                child: Text(
                  'haidersultan7675@gmail.com',
                  style: TextStyle(fontSize: 16),
                ),
              ),
            ),
            Card(
              elevation: 6,
              color: AppTheme.cardBackgroundColor,
              margin: EdgeInsets.only(
                left: 20,
                right: 20,
                top: 15,
                bottom: 20,
              ),
              child: Padding(
                padding: const EdgeInsets.all(12.0),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(
                      'Disable Account',
                      style: TextStyle(fontSize: 16),
                    ),
                    Icon(Icons.disabled_visible),
                  ],
                ),
              ),
            ),
            Card(
              elevation: 6,
              color: AppTheme.cardBackgroundColor,
              margin: EdgeInsets.only(
                left: 20,
                right: 20,
                top: 15,
              ),
              child: Padding(
                padding: const EdgeInsets.all(12.0),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    Text(
                      'Logout',
                      style: TextStyle(fontSize: 16),
                    ),
                    Icon(Icons.logout_outlined)
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
      body: Column(
        children: [
          Expanded(
            child: ListView(
              children: [
                SizedBox(
                  height: 121,
                  child: ListView(
                    reverse: true,
                    scrollDirection: Axis.horizontal,
                    children: [
                      DateCircle(
                        dateTime: DateTime(now.year, now.month, now.day + 3),
                      ),
                      DateCircle(
                        dateTime: DateTime(now.year, now.month, now.day + 2),
                      ),
                      DateCircle(
                        dateTime: DateTime(now.year, now.month, now.day + 1),
                      ),
                      DateCircle(
                        dateTime: DateTime(now.year, now.month, now.day),
                      ),
                      DateCircle(
                        dateTime: DateTime(now.year, now.month, now.day - 1),
                      ),
                      DateCircle(
                        dateTime: DateTime(now.year, now.month, now.day - 2),
                      ),
                    ],
                  ),
                ),
                Container(
                  height: 250,
                  decoration: BoxDecoration(
                    color: AppTheme.secondaryColor,
                    borderRadius: const BorderRadius.only(
                      bottomLeft: Radius.elliptical(300, 40),
                      bottomRight: Radius.elliptical(300, 40),
                    ),
                  ),
                  child: Center(
                    child: Text(
                      "Streak : 40000", //TODO
                      style: GoogleFonts.poppins().copyWith(
                        fontWeight: FontWeight.w600,
                        fontSize: 40,
                      ),
                    ),
                  ),
                ),
                TodoCard(size: size),
              ],
            ),
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {},
        backgroundColor: AppTheme.cardBackgroundColor,
        elevation: 10,
        child: const Icon(Icons.add),
      ),
    );
  }
}

class TodoCard extends StatelessWidget {
  const TodoCard({
    super.key,
    required this.size,
  });

  final Size size;

  @override
  Widget build(BuildContext context) {
    return Card(
      shadowColor: AppTheme.primaryColor,
      color: AppTheme.cardBackgroundColor,
      elevation: 5,
      margin: const EdgeInsets.all(20),
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                SizedBox(
                  width: size.width * 0.6,
                  child: Text(
                    'THIS IS A TODO TITLE',
                    style: TextStyle(
                      fontWeight: FontWeight.w600,
                      fontSize: 16,
                    ),
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.only(top: 8.0),
                  child: SizedBox(
                    width: size.width * 0.6,
                    child: Text(
                      'THIS A TODOD HAHAHAHHAHAHA, fas dasdas das das d a dwqeqweqw this is a long one and i will do it every day hhahahahahaha',
                    ),
                  ),
                ),
              ],
            ),
            Icon(Icons.check_box)
          ],
        ),
      ),
    );
  }
}

class DateCircle extends StatelessWidget {
  const DateCircle({super.key, required this.dateTime});

  final DateTime dateTime;

  String getStringAboveCircle() {
    if (dateTime.weekday == DateTime.now().weekday) {
      return 'Today';
    }
    if (dateTime.weekday == 1) {
      return 'M';
    }
    if (dateTime.weekday == 2) {
      return 'T';
    }
    if (dateTime.weekday == 3) {
      return 'W';
    }
    if (dateTime.weekday == 4) {
      return 'T';
    }
    if (dateTime.weekday == 5) {
      return 'F';
    }
    return 'S';
  }

  @override
  Widget build(BuildContext context) {
    final bool isToday = dateTime.weekday == DateTime.now().weekday;
    return Column(
      children: [
        Padding(
          padding: const EdgeInsets.only(top: 8, bottom: 8),
          child: Center(
            child: Text(
              getStringAboveCircle(),
              style: const TextStyle(
                fontWeight: FontWeight.w600,
              ),
            ),
          ),
        ),
        Padding(
          padding: const EdgeInsets.all(9.0),
          child: Container(
            width: 50,
            height: 50,
            decoration: BoxDecoration(
              color: isToday ? AppTheme.primaryColor : AppTheme.backgroundColor,
              borderRadius: const BorderRadius.all(
                Radius.circular(100),
              ),
              border: Border.all(width: 2, color: AppTheme.primaryColor),
            ),
            child: Center(
              child: Text(
                DateFormat('dd')
                    .format(
                      dateTime,
                    )
                    .toString(),
                style: TextStyle(
                  fontWeight: FontWeight.w600,
                  color:
                      isToday ? AppTheme.backgroundColor : AppTheme.textColor,
                ),
              ),
            ),
          ),
        ),
      ],
    );
  }
}
