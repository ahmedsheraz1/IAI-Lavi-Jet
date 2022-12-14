Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import hmac, hashlib
m = hmac.new(b'secret key', digestmod=hashlib.blake2s)
m.update(b'IAI Lavi')
m.hexdigest()
'cb2303df9e27237b7d5ebe79812eeb332f79da7690e2338f43b581759a54e39e'
