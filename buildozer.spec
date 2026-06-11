[app]
title = CopyAI
package.name = copyai
package.domain = org.twizz
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

# Ye 2 line sabse important hain:
android.accept_sdk_license = True
android.sdk_build_tools_version = 33.0.0

[buildozer]
log_level = 2
warn_on_root = 1
