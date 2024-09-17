# sdcard
**RO access to the SD card of an Android smartphone**

`sdcard` is a Python script that uses `adb_shell` and `fuse-python` (eg. BSD/Linux/OS-X only) to give fast read-only access to the `/sdcard/` (pseudo-)folder of an Android system.

**the Android system accessed must have `Developer Options` enabled, as well as `USB Debugging`.**
**the key present in the script must be authorized on the Android side.**

> _another key pair can be generated if required (see [source code](https://github.com/patatetom/sdcard/blob/main/sdcard#L12))_.


## installation

### on system side

> _these are installation examples, other ways of doing things are possible._
>
> _Android tools (eg. `adb`) are not necessary, `adb_shell` is totally independent of them._

- Archlinux (2024.09.01)

```shell
# as root, install system dependencies if not already installed
pacman -Sy
pacman -S fuse3 python3
ln -s fusermount3 /usr/bin/fusermount
```
```shell
# as root, install Python virtual environment
curl -L https://github.com/patatetom/sdcard/archive/refs/heads/main.zip > /tmp/sdcard.zip
python3 -m zipfile -e /tmp/sdcard.zip /opt
mv /opt/sdcard-main /opt/android
python3 -m venv /opt/android
/opt/android/bin/python3 -m pip install -r /opt/android/requirement.txt
```

```shell
# as user, run/test Python script
mkdir /tmp/mountpoint
/opt/android/bin/python3 /opt/android/sdcard /tmp/mountpoint
ls -l /tmp/mountpoint
umount /tmp/mountpoint
```

- Debian (12/bookworm)

```shell
# as root, install system dependencies if not already installed
apt update
apt install curl fuse3 libusb-1.0-0 python3.11 python3.11-venv
```
```shell
# as root, install Python virtual environment
curl -L https://github.com/patatetom/sdcard/archive/refs/heads/main.zip > /tmp/sdcard.zip
python3 -m zipfile -e /tmp/sdcard.zip /opt
mv /opt/sdcard-main /opt/android
python3 -m venv /opt/android
/opt/android/bin/python3 -m pip install -r /opt/android/requirement.txt 
```

```shell
# as user, run/test Python script
mkdir /tmp/mountpoint
/opt/android/bin/python3 /opt/android/sdcard /tmp/mountpoint
ls -l /tmp/mountpoint
umount /tmp/mountpoint
```


### on user side

> _system dependencies (`fuse`, `libusb` and `python`) are still required_

```shell
curl -L https://github.com/patatetom/sdcard/archive/refs/heads/main.zip > /tmp/sdcard.zip
python3 -m zipfile -e /tmp/sdcard.zip ~/venv/
mv ~/venv/sdcard-main ~/venv/android
~/venv/android/bin/python3 -m pip install -r ~/venv/android/requirement.txt
mkdir /tmp/mountpoint
~/venv/android/bin/python3 ~/venv/android/sdcard /tmp/mountpoint
ls -l /tmp/mountpoint
umount /tmp/mountpoint
```


## usage


## links
- [adb_shell](https://github.com/JeffLIrion/adb_shell)
- [fuse-python](https://github.com/libfuse/python-fuse)
