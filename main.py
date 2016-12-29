import vkapi

v = vkapi.api()
st, res = v.getUserInfo('210700286')
print(st, res)
