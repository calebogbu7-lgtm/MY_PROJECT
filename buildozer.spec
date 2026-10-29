[app]

title = CalebMath
package.name = calebmath
package.domain = org.caleb

source.dir = src
source.include_exts = py,kv,png,jpg,atlas

version = 0.1.0

requirements = python3,kivy==2.3.1

orientation = portrait
fullscreen = 0

android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

android.debug_artifact = apk
android.release_artifact = aab

osx.kivy_version = 2.3.1

ios.kivy_ios_url = https://github.com/kivy/kivy-ios
ios.kivy_ios_branch = master

ios.ios_deploy_url = https://github.com/phonegap/ios-deploy
ios.ios_deploy_branch = 1.12.2

ios.codesign.allowed = false


[buildozer]

log_level = 2
warn_on_root = 1

