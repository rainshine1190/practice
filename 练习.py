# import rsa
# #生成一对公钥和私钥
# pub,pri = rsa.newkeys(1024)
# message = 'hello world'
# message = message.encode()
# print('使用公钥加密后字符串为',message)
# cryptedMessage = rsa.encrypt(message,pub)
# print('使用公钥加密后字符串为',cryptedMessage)
#
# message = rsa.decrypt(cryptedMessage,pri)
# print('使用私钥解密后',message)

def func4(n):
    if n<=2 :
        return 1
    return func4(n-1)+func4(n-2)
result=func4(4)
print(result)


