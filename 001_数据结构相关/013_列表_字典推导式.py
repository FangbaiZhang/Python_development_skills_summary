# 列表推导式
l = [i for i in range(10)]
print(l)

# 字典推导式
d = {i: "b" for i in range(10)}
print(d)

# 字典推导式

# 字符串分割后得到字典
cookies = "anonymid=k06r6sdauyh36v; depovince=ZGQT; _r01_=1; JSESSIONID=abcOraT1E7z0JhHDATb0w; ick_login=8f53ebf1-b972-4572-8f77-810953dcfdfe; first_login_flag=1; ln_uact=908851835@qq.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn221/20131218/1650/original_RrRf_470e00037cf7111a.jpg; jebecookies=0f21ab0f-a7a8-4467-9bbc-13110c7a411f|||||; _de=24AF6279ED439B973399691954C56086696BF75400CE19CC; p=3ae05d78f7e97e1518aaee67caf5b2280; ap=574862780; t=495e85781ac79a4cc7e2ec9553006bb50; societyguester=495e85781ac79a4cc7e2ec9553006bb50; id=574862780; xnsid=fe384fe8; ver=7.0; loginfrom=null; wp_fold=0"
# 使用字典推导式将上述字符串转化为一个字典, 先使用;分割得到一个列表，
# 列表中每一个元素再用=进行分割，列表第一个值为键，第二个值为值
cookies ={i.split("=")[0]: i.split("=")[1] for i in cookies.split(";")}
print(cookies)