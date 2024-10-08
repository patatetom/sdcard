#!/usr/bin/env python


# /// script
# requires-python = ">=3"
# dependencies = [
# "adb_shell>=0.4.4",
# "cffi>=1.17.1",
# "cryptography>=43.0.1",
# "fuse-python>=1.0.8",
# "libusb1>=3.1.0",
# "pyasn1>=0.6.1",
# "pycparser>=2.22",
# "rsa>=4.9"
# ]
# ///


# this python code provides read-only access to the /sdcard/ (pseudo)folder
# on an android smartphone.
# it uses fuse-python (https://github.com/libfuse/python-fuse) and
# adb_shell (https://github.com/JeffLIrion/adb_shell).


# as a reminder, android smartphone must have “developer options” enabled, as
# well as “USB debugging”, and an access validation must be performed.
# if required, you can generate a new key pair with the following commands :
# 		from adb_shell.auth.keygen import keygen
# 		keygen('/tmp/adb_shell_reader')
# the contents of the two generated files should respectively replace the two
# variables defined below.
private, public = """
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCSbBRV9bFH4Cik
KbTY6aUdLykG23gFv0Oc2RTlb3MtAcFKPIWROczi9r6Dr7M8p6SeYGqiKN79qwAX
S8XzI0E3C/ELpHIbm3vqIGUgD54CO8eKHm8q1uE8MPK5L47IJJH1Psv1PkwCPT5Q
JLctrvfRmQ+LNKR09IJbujEXkvSpszfb1xaotIOdTEKbHUJNwRtEGrT6gfFGiKsp
2GcEWrYfbs4XWwJ/fMJRGNMTNNdHmVRToL0/Boa2sBANvxomPbm7GUJV/MCE8906
kFJ1wpxR17CPdt7LSg1d2VylkjEDREEltQw2w1c5TZ96YnE4EWimy2NFSvXX8i8C
SzyrJFJbAgMBAAECggEALA7pb5QmbAI/OGZ0THDBhi6SocWYL+KFbcTETOVkOr60
cqoTZseFpyWn3egYfr/TAPTyISk7MAksVdYvEiIhlXa6aU5qJ3R5rNFinGsWmIV0
XVMbEEDoNTxlTOPKit62LJ1gscK1DFdxUJw7ojtrxl3QF4sXkTmhoAg+jWFizUzz
iVCd7SwjZpi/DJGtCCL5cw9EcYuZtXEag+ajWbGzCu9zBIFxsJqHPjTMjGKNBNVg
hHwTg6CC8yu3F3fRGZENJMKuaPZBL9KHaGeiiZSkzgPGcPPDu3XTIK5UT4r3/EOM
eyrWt4eWqNcyRcA7ekqmXBkh1tLFf/iYfrBLuq4kwQKBgQDHYLnwzmYEvGGTSBlV
0B33w+0OqgaSyhwfF8FUh9lwUIYIkHjJghyjugUpMtRQFvJHkBAiYd2aUpwYixwm
6XQ6Aq6AUcXW1/wNPtNMVaWIGGpneBxkt0+rsSND4GcKd3YJ7JxzwnDZCtq9pwtC
//dSmyczEoGE13JQimI1hJEMrwKBgQC8AVfVz2AKHHmeU7ue42n/l75ttBPI0abP
TZVeS6DIZXcT/TgiHYPzezEEu7pyh/ZtvUYkRDwNDp+e/EOAQM86RT7JV8GiP8Tv
Gfjo0qYv6zejlytEMBot3vUs13TKBa8nWZx3MLw9Xvn0qamf6A4H1W+qOjRa2G/D
/rPSxQg4FQKBgGl2JqTT6G7U3qAzYQNdRJzMTFaXZUa8Fcf0ntUBzuh0D5H0KZAd
fNy2BwjV1CxRFvL3pzEopzl8PQlWfBuxHUOaK4fAuW99a9vtwYL9QsQMdiwpAovb
0w60cjzzNE37BrsVJ2SsE1kbPr1W4MQd9UsCuudvAIeuFs+3g19fsgINAoGAIGtG
3yqsT/ILEr8zmjly3M0o3DfyNW3ZiuPA/wqhhgzhFMRUeqWGTGUQ1dUdWISTfObn
gnd1t3avFbZAWYxTb6PjKMsGK9k9N1HONy+j0p2H8aCuqEp3KTPKKVpZ3EBQrMNq
FK+Ftjt7dLIQ+u8EBFvMrpjs0EGEPFLeZVjuiuUCgYEAoCBGv3x63B7EeascnZea
5PYQQ5LNNP1WQlqKbavrW4qHcWMBeI4LbpD/V75mXyqwYVzB/kdrf+Ag1OaxKnDF
rVRI4jTYoNX9Iv3/E+F+4LW6we5RJ6Vi+ksJxWleM+xnvOIb9CWcok+ZsYIMuLYf
a20sYSh+Joe+80Tdcqkj5fs=
-----END PRIVATE KEY-----
""", """
-----BEGIN PUBLIC KEY-----
QAAAAC1yo0pbUiSrPEsCL/LX9UpFY8umaBE4cWJ6n005V8M2DLUlQUQDMZKlXNld
DUrL3naPsNdRnMJ1UpA63fOEwPxVQhm7uT0mGr8NELC2hgY/vaBTVJlH1zQT0xhR
wnx/AlsXzm4ftloEZ9gpq4hG8YH6tBpEG8FNQh2bQkydg7SoFtfbN7Op9JIXMbpb
gvR0pDSLD5nR964ttyRQPj0CTD71yz71kSTIji+58jA84dYqbx6KxzsCng8gZSDq
e5sbcqQL8Qs3QSPzxUsXAKv93iiiamCepKc8s6+DvvbizDmRhTxKwQEtc2/lFNmc
Q78FeNsGKS8dpenYtCmkKOBHsfVVFGySrq1F5NWyYYDLBlOGgpPzp1hWMvYnN64U
zcHPS4ZoUqpgEVicQpnM5n6dPuHx9YQzP7uxbg7JCysllU5NqYu/NDCEHNCCTNGe
ja27eGodW+m/iOleggth+UibFoqFBAqUegenvXKxPgvmzj+08wE0hO5TNIFkkiMN
a3JV9bn3Ojh6D5TZ710EL+aUOVFwfM6wKi2gJhYOklRaCbQCd1hVw1sx9ZP5+I0F
hwA5oJBx1FVRNfzYAIb5ImeG6ZBc42omcYNLcQ/PYP9qk+T5TfqC0uJGLiM4opWH
RT5mop8i3DpB10hlTsP1exnOo2mKAwZ3bQcuyqCeAwotARJT5rxeMAEAAQA=
-----END PUBLIC KEY-----
"""


# imports
import fuse
from io import BytesIO
from time import sleep
from os import getgid, getuid
from sys import exit, stderr
from stat import S_ISDIR as isDir
from stat import S_ISREG as isReg
from errno import ENOENT as noEntry
from errno import EACCES as accessDenied
from usb1 import USBErrorBusy as busyUSB
from adb_shell.adb_device import AdbDeviceUsb
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
from os import O_RDONLY, O_WRONLY, O_RDWR


# new API
fuse.fuse_python_api = (0, 2)
# get ids of the current user
gid, uid = getgid(), getuid()


class reader(fuse.Fuse):

	def __init__(self, *args, **kw):
		fuse.Fuse.__init__(self, *args, **kw)
		# dictionaries 'attributes', 'items' and 'buffers' will be used as caches
		self.attributes, self.items, self.buffers = {}, {}, {}
		self.root, self.nocache = False, False

	def getattr(self, path):
		if path in self.attributes:
			return self.attributes[path]
		else:
			# file attributes are obtained using device.stat
			mode, size, time = device.stat(self.root + path)
			if not mode:
				return -noEntry
			attributes = fuse.Stat()
			directory = isDir(mode)
			attributes.st_atime, attributes.st_ctime, attributes.st_mtime = time, time, time
			attributes.st_mode = (directory and 0o40550 or 0o100440)
			attributes.st_size = (not directory and size or 0)
			attributes.st_gid, attributes.st_uid = gid, uid
			attributes.st_nlink = (directory and 2 or 1)
			# caching attributes for future calls
			if not self.nocache:
				self.attributes[path] = attributes
			return attributes

	def readdir(self, path, offset):
		if path in self.items:
			for item in self.items[path]:
				yield fuse.Direntry(item)
		else:
			# list of files (eg. items) is obtained using device.list
			items = [
				item.filename.decode()
				for item in device.list(self.root + path)
				if isReg(item.mode) or isDir(item.mode)
			]
			# caching items for future calls
			if not self.nocache:
				self.items[path] = set(items)
			for item in items:
				yield fuse.Direntry(item)

	def open(self, path, flags):
		# only read-only mode supported
		if flags & (O_RDONLY | O_WRONLY | O_RDWR) != O_RDONLY:
			return -accessDenied

	def read(self, path, size, offset):
		attributes = self.attributes[path]
		if offset < attributes.st_size:
			if offset + size > attributes.st_size:
				size = attributes.st_size - offset
		else:
			return b''
		if path in self.buffers:
			return self.buffers[path].getvalue()[offset:(offset + size)]
		else:
			buffer = BytesIO()
			# file content is obtained using device.pull
			device.pull(self.root + path, buffer)
			# caching buffer for future calls
			self.buffers[path] = buffer
			return buffer.getvalue()[offset:(offset + size)]

	def release(self, path, flags):
		self.buffers.pop(path)

	def fsinit(self):
		self.root = not self.root and "/sdcard" or ""


server = reader()
server.parser.add_option(
	"-r", "--root",
	action="store_true",
	dest="root",
	help="access from / (default from /sdcard)"
)
server.parser.add_option(
	"-n", "--nocache",
	action="store_true",
	dest="nocache",
	help="do not cache data (default cache data)"
)
server.parse(values=server)


signer = PythonRSASigner(public, private)
try:
	device = AdbDeviceUsb()
except Exception as error:
	exit(error)
while not device.available:
	try:
		devnull = device.connect(rsa_keys=[signer], auth_timeout_s=0.5)
		device.close()
		devnull = device.connect(rsa_keys=[signer], auth_timeout_s=0.5)
	except busyUSB:
		# the USB port is busy: adb (android platform tools) or another instance
		# of this code may be causing the problem...
		print("USB device busy : attempt to reconnect in 3s...", file=stderr)
		sleep(3)
	except Exception as error:
		exit(error)


server.main()
device.close()

def main():
    pass
