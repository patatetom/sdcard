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


### system side

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
# …
# dr-xr-x--- 2 nobody nogroup 0 Jun 11 09:31  DCIM
# …
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
# …
# dr-xr-x--- 2 nobody nogroup 0 Jun 11 09:31  DCIM
# …
umount /tmp/mountpoint
```


### user side

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
# …
# dr-xr-x--- 2 nobody nogroup 0 Jun 11 09:31  DCIM
# …
umount /tmp/mountpoint
```


## usage

> _it's important to note that, by default, `sdcard` remembers the contents (metadata) of visited folders :_
> _in other words, the addition, deletion or modification on the smartphone side of a previously visited location will not be reflected by `sdcard`, unless you use the `-n` option._
>
> _the examples below are taken from the user side installation above._

```shell
~/venv/android/bin/python3 ~/venv/android/sdcard --help
Usage: sdcard [mountpoint] [options]

Options:
    -h, --help             show this help message and exit
    -o opt,[opt...]        mount options
    -r, --root             access to root (default to /sdcard)
    -n, --nocache          do not cache data (default use cached data)
FUSE options:
…
```
```shell
mkdir -p /tmp/mountpoint
~/venv/android/bin/python3 ~/venv/android/sdcard /tmp/mountpoint 
ls /tmp/mountpoint/
# Alarms   Android   Audiobooks	 DCIM   Documents   Download   Movies   Music   Notifications   Pictures   Podcasts   Recordings   Ringtones   storage
ls -l /tmp/mountpoint/
total 0
# dr-xr-x--- 2 nobody nogroup 0 Mar 22 03:00  Alarms
# dr-xr-x--- 2 nobody nogroup 0 Mar 22 03:00  Android
# dr-xr-x--- 2 nobody nogroup 0 Mar 22 03:00  Audiobooks
# dr-xr-x--- 2 nobody nogroup 0 Jun 11 09:31  DCIM
# dr-xr-x--- 2 nobody nogroup 0 Aug 28 16:18  Documents
# dr-xr-x--- 2 nobody nogroup 0 Sep 18 05:39  Download
# dr-xr-x--- 2 nobody nogroup 0 May 19 19:14  Movies
# dr-xr-x--- 2 nobody nogroup 0 May 20 06:53  Music
# dr-xr-x--- 2 nobody nogroup 0 Mar 22 03:00  Notifications
# dr-xr-x--- 2 nobody nogroup 0 Aug 10 22:38  Pictures
# dr-xr-x--- 2 nobody nogroup 0 Mar 22 03:00  Podcasts
# dr-xr-x--- 2 nobody nogroup 0 Mar 28 16:52  Recordings
# dr-xr-x--- 2 nobody nogroup 0 Mar 22 03:00  Ringtones
# dr-xr-x--- 2 nobody nogroup 0 Sep  6 23:02  storage
tar -C /tmp/mountpoint/ -cz . > /tmp/backup.tar.gz
umount /tmp/mountpoint
```


## links
- [adb_shell](https://github.com/JeffLIrion/adb_shell)
- [fuse-python](https://github.com/libfuse/python-fuse)
- [libusb](https://github.com/karpierz/libusb)
