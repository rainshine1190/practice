#1-get请求

import requests,json

# payload = {
#     'k':'java'
# }
# #get传参
# re = requests.get(url='https://wanandroid.com/wxarticle/list/405/1/json',params=payload)
#
# dict1 = re.json()
#
# print(dict1['data']['curPage'])

#-------------------------------------------------------------------------------------
# post方法，参数为表单
# payload = {
#     'username':'liangchao',
#     'password':'123456'
# }
# url = 'https://www.wanandroid.com/user/login'
#
# re = requests.post(url=url,data=payload)
#
# print('---',re.cookies)
#
# cookie = re.cookies
#
#
# #post方法，参数为json
# payload = {
#     'name':'liangchao',
#     'link':'123456'
# }
# url = 'https://www.wanandroid.com/lg/collect/addtool/json'
#
#
# re = requests.post(url=url,data=payload,cookies = cookie)
#
# print(re.text,re.status_code)



#post方法，参数为json

# payload1 = {
#     'username':'liangchao',
#     'password':'123456'
# }
# payload2 = {
#     'name':'liangchao',
#     'link':'http://www.baidu.com'
# }
# url1 = 'https://www.wanandroid.com/user/login'
# url2 = 'https://www.wanandroid.com/lg/collect/addtool/json'
# s = requests.session()
#
# re = s.post(url=url1,data=payload1)
#
# re2 = s.post(url=url2,data=payload2)
#
# print(re2.text,re2.status_code)


#--------------------------------------------


payload1 = {
    'username':'liangchao',
    'password':'123456'
}


re = requests.post(url='http://httpbin.org/post',data=payload1)

print(re.text)