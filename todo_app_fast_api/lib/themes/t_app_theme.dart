import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class AppTheme {
  static Color primaryColor = const Color(0xff5a189a);
  static Color textColor = const Color(0xff10002b);
  static Color backgroundColor = const Color(0xffe0aaff);
  static Color itemColor = const Color(0xff240046);

  static ThemeData lightTheme() {
    return ThemeData(
      primaryColor: primaryColor,
      appBarTheme: AppBarTheme(
        titleTextStyle: GoogleFonts.getFont(
          'Poppins',
          fontSize: 18,
          fontWeight: FontWeight.bold,
          color: textColor,
        ),
        actionsIconTheme: IconThemeData(
          color: itemColor,
        ),
        iconTheme: IconThemeData(color: primaryColor),
        backgroundColor: backgroundColor,
      ),
    );
  }
}
