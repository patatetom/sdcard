# sdcard
**RO access to the SD card of an Android smartphone**

`sdcard` is a Python script that uses `adb_shell` and `fuse-python` (eg. BSD/Linux/OS-X only) to give fast read-only access to the `/sdcard/` (pseudo-)folder of an Android system.

the Android system accessed must have `Developer Options` enabled, as
well as `USB Debugging`. the key present in the script must be authorized on the Android side.

> _another key pair can be generated if required (see [source code](https://github.com/patatetom/sdcard/blob/main/sdcard#L12))_.


## installation

### on system side

- Debian 12 (bookworm)

```shell
# as root
apt update
apt install curl fuse3 libusb-1.0-0 python3.11 python3.11-venv unzip
curl -L https://github.com/patatetom/sdcard/archive/refs/heads/main.zip > /tmp/sdcard.zip
unzip -d /opt /tmp/sdcard.zip 
mv /opt/sdcard-main /opt/android
python3 -m venv /opt/android
/opt/android/bin/python3 -m pip install -r /opt/android/requirement.txt 
```

```shell
# as user
mkdir /tmp/mountpoint
/opt/android/bin/python3 /opt/android/sdcard /tmp/mountpoint
ls -l /tmp/mountpoint
umount /tmp/mountpoint
```


### on user side


> _Android tools (eg. `adb`) are not necessary, `adb_shell` is totally independent of them._


## usage


## links
- [adb_shell](https://github.com/JeffLIrion/adb_shell)
- [fuse-python](https://github.com/libfuse/python-fuse)
