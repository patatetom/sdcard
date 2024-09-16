# sdcard
**RO access to the SD card of an Android smartphone**

`sdcard` is a Python script that uses `adb_shell` and `fuse-python` (eg. Linux) to give fast read-only access to the `/sdcard/` (pseudo-)folder of an Android system.

the Android system accessed must have `Developer Options` enabled, as
well as `USB Debugging`. the key present in the script must be authorized on the Android side.

> _another key pair can be generated if required (see [source code](https://github.com/patatetom/sdcard/blob/main/sdcard#L12))_.


## installation


## usage


## links
- [adb_shell](https://github.com/JeffLIrion/adb_shell)
- [fuse-python](https://github.com/libfuse/python-fuse)
