# sdcard
read-only access to the SD card of an Android smartphone

`sdcard` is a python script that uses `adb_shell` and `fuse-python` (eg. Linux) to give read-only access to the `/sdcard/` (pseudo-)folder of an android system.

the android system accessed must have `developer options` enabled, as
well as `USB debugging`. the key present in the script must be authorized on the android side.

> _another key pair can be generated if required (see [source code](https://github.com/patatetom/sdcard/blob/main/sdcard#L12))_.


## installation


## usage


## links
- [adb_shell](https://github.com/JeffLIrion/adb_shell)
- [fuse-python](https://github.com/libfuse/python-fuse)
