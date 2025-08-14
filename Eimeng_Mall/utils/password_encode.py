import hashlib

#字符串转MD5
def get_md5(param):
    md5 = hashlib.md5()
    md5.update(param.encode())
    return md5.hexdigest()