# this python file directly provides the private and public keys needed for
# adb_shell to access the android smartphone.
# as a reminder, this latter must have “developer options” enabled, as well
# as “USB debugging”, and an access validation must be performed.

# if required, you can generate a new key pair with the following commands :
#
# from adb_shell.auth.keygen import keygen
# keygen('/tmp/adb_shell_reader')
#
# the contents of the two generated files should respectively replace the two
# variables defined below.


private = """
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
"""


public = """
QAAAAC1yo0pbUiSrPEsCL/LX9UpFY8umaBE4cWJ6n005V8M2DLUlQUQDMZKlXNldDUrL3naPsNdRnMJ1UpA63fOEwPxVQhm7uT0mGr8NELC2hgY/vaBTVJlH1zQT0xhRwnx/AlsXzm4ftloEZ9gpq4hG8YH6tBpEG8FNQh2bQkydg7SoFtfbN7Op9JIXMbpbgvR0pDSLD5nR964ttyRQPj0CTD71yz71kSTIji+58jA84dYqbx6KxzsCng8gZSDqe5sbcqQL8Qs3QSPzxUsXAKv93iiiamCepKc8s6+DvvbizDmRhTxKwQEtc2/lFNmcQ78FeNsGKS8dpenYtCmkKOBHsfVVFGySrq1F5NWyYYDLBlOGgpPzp1hWMvYnN64UzcHPS4ZoUqpgEVicQpnM5n6dPuHx9YQzP7uxbg7JCysllU5NqYu/NDCEHNCCTNGeja27eGodW+m/iOleggth+UibFoqFBAqUegenvXKxPgvmzj+08wE0hO5TNIFkkiMNa3JV9bn3Ojh6D5TZ710EL+aUOVFwfM6wKi2gJhYOklRaCbQCd1hVw1sx9ZP5+I0FhwA5oJBx1FVRNfzYAIb5ImeG6ZBc42omcYNLcQ/PYP9qk+T5TfqC0uJGLiM4opWHRT5mop8i3DpB10hlTsP1exnOo2mKAwZ3bQcuyqCeAwotARJT5rxeMAEAAQA= adb_shell_reader
"""
