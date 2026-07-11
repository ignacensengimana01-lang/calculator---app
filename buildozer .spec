[app]

# App configuration
title = Calculator
package.name = calculator
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 1.0

# Python requirements
requirements = python3,kivy

# Display settings
orientation = portrait
fullscreen = 0

# Android build settings
android.api = 34
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a,armeabi-v7a

# Optional but recommended
p4a.branch = develop
android.permissions = INTERNET,VIBRATE
