import base64

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

from config.setting import settings


def generate_aes_key():
    key = settings.GAME_DATA_SECRET
    if len(key) < 16:
        return key + "a" * (16 - len(key))

    if len(key) < 24:
        return key + "a" * (24 - len(key))

    if len(key) < 32:
        return key + "a" * (32 - len(key))

    return key[:32]


aes_obj = AES.new(generate_aes_key().encode("utf-8"), AES.MODE_ECB)


def pad_base64(data):
    missing_padding = len(data) % 4
    if missing_padding:
        data += "=" * (4 - missing_padding)
    return data


def aes_encrypt(data: str):
    plain_text = pad(data.encode("utf-8"), AES.block_size)
    en_bytes = aes_obj.encrypt(plain_text)
    return base64.b64encode(en_bytes).decode("utf-8")


def aes_decrypt(data: str):
    b64_str = pad_base64(data)
    base64_bytes = base64.b64decode(b64_str)
    plain_text = aes_obj.decrypt(base64_bytes)
    return unpad(plain_text, AES.block_size).decode("utf-8")
