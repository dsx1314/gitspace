import hashlib
def haxi(message):
    sha = hashlib.sha1()
    sha.update(message.encode('utf-8'))
    return sha.hexdigest()

if __name__ == '__main__':
    print(haxi('S3bdVQKIzQ39ic9eAYnnMqh3rzoKcy18083101650676881'))


import hashlib
def haxi01(message):
    sha = hashlib.md5()
    sha.update(message.encode('utf-8'))
    return sha.hexdigest()

if __name__ == '__main__':
    print(haxi01('1650528055'))