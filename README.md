# sdcard

**USB read-only access to SD card on Android system**

`sdcard` is a Python script that uses `adb_shell`, `fuse-python` (eg. BSD/Linux/OS-X only) and `libusb` to give fast read-only access to the `/sdcard/` (pseudo-)folder (eg. downloads, photos, etc...) of an Android system.

> _**the Android system accessed must have `Developer Options` enabled, as well as `USB Debugging`.**_
> _**the key present in the script must be authorized on the Android side.**_
>
> _another key pair can be generated if required (see [source code](https://github.com/patatetom/sdcard/blob/main/sdcard#L12))_.


## installation

> _these are installation examples, other ways of doing things are possible._
>
> _Android tools (eg. `adb`) are not necessary, `adb_shell` is totally independent of them._


### on system side

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
python3 -m venv ~/venv/android
~/venv/android/bin/python3 -m pip install -r ~/venv/android/requirement.txt
mkdir /tmp/mountpoint
~/venv/android/bin/python3 ~/venv/android/sdcard /tmp/mountpoint
ls -l /tmp/mountpoint
umount /tmp/mountpoint
```


## usage

> _it's important to note that, by default, `sdcard` remembers the contents (metadata) of visited folders :_
> _in other words, the addition, deletion or modification on the smartphone side of a previously visited location will not be reflected by `sdcard`, unless you use the `-n` option._

## links
- [adb_shell](https://github.com/JeffLIrion/adb_shell)
- [fuse-python](https://github.com/libfuse/python-fuse)
- [libusb](https://github.com/karpierz/libusb)
