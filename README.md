# tencent_mini

### 腾讯迷你项目后台

    django版本：1.8.2
    python版本：2.7

    第三方库：
        pillow

### 调用借口说明

    ##移动端接口格式说明

    1. 移动端统一采用post方法调用
    2. post方法中只传一对参数

    参数名："method"

    参数值：参数值为json格式，具体内容如下：
    {"name":"xxx", "args":{"arg1":"value1", "arg2":"value2","arg3:":"value3",...}}


    注释：
    "name":"xxx", 其中xxx表示具体函数名
    "args":"xxx", 后面xxx表示函数的参数列表
    
    ################################################################
    
    ##服务器端借口格式说明:
    
    1.服务器端返回一个httpResponse，具体数据也是用json进行返回
    
    格式如下：
    {"retCode": 0, "retMsg":"返回码描述","retValue":[{"arg1":"value1", "arg2":"value2",...}, {"arg1":"value1", "arg2":"value2",...},...]}

    注释：
    retCode表示返回码，0表示成功，-1表示失败
    retMsg表示返回码的描述，当retCode=-1时，retMsg包含更详细的错误信息，当retCOde为0时，retMsg为空字符串
    retValue是具体的返回值，先查看retCode的值是否为0，若为0，retValue才有意义，此时可查看具体的返回值。由于返回值有多组，因此用数组表示
    
    
    
    
    ###########################################################
    具体接口说明：
    
    1.注册功能：by perryhuang, 2016_06_25 
    
    post参数名：method
    post参数内容：{"name":"register", "args":{"user_id":"15666666666", "user_password":"123"}}
    
    服务器返回值(json格式):
        注册成功：
        {"retValue": "", "retCode": 0, "retMsg": ""}
        注册失败：
        {"retValue": "", "retCode": -1, "retMsg": "xxxxx"}
        
        
    2.登陆功能：by stanwu, 2016/06/25
    
    post参数名：method
    post参数内容：{"name":"login", "args":{"user_id":"15666666666", "user_password":"123"}}
    
    服务器返回值(json格式):
        注册成功：
        {"retValue": "", "retCode": 0, "retMsg": ""}
        注册失败：
        {"retValue": "", "retCode": -1, "retMsg": "xxxxx"}
        
        
    3.完善个人信息功能：by chayfan, 2016/06/25
    
    post参数名：method
    post参数内容：{"name":"completeUserInfo","args":{"user_id":"xxx","user_nickname":"xxx","user_gender":1,"user_age":2,"user_address":"xxx", "user_interest":1}}
    
    modify by perryhuang：
        删除json格式中的user_avatar字段
        user_avatar信息包含在request.FILES中,参数名为"user_avatar"
    
    服务器返回值(json格式):
        注册成功：
        {"retValue": "", "retCode": 0, "retMsg": ""}
        注册失败：
        {"retValue": "", "retCode": -1, "retMsg": "xxxxx"}
        
        
    4.发布收养信息：by stanwu, 2016/06/25
    
    post参数名：method
    post参数内容：{"name":"issueAdoptPetInfo","args":{"user_id":"xxx", "activity_introduction":"xxx", "activity_address":"xxx","activity_longitude":"xxx","activity_latitude":"xxx","activity_pet_type":xxx,"activity_price":xxx, "activity_start_time":"xxx", "activity_end_time":"xxx"}}
    
    modify by perryhuang:
        删除json格式中的activity_picture字段
        activity_picture信息包含在request.FILES中，参数名为"activity_picture"
        
    服务器返回值(json格式):
        注册成功：
        {"retValue": "", "retCode": 0, "retMsg": ""}
        注册失败：
        {"retValue": "", "retCode": -1, "retMsg": "xxxxx"}
        
        
    5.预约寄养
    post参数名：method
    post参数内容：{"name":"issueFosterPetInfo","args":{"user_id":"xxx", "activity_id":xxx}}
    
    服务器返回值(json格式):
        注册成功：
        {"retValue": "", "retCode": 0, "retMsg": ""}
        注册失败：
        {"retValue": "", "retCode": -1, "retMsg": "xxxxx"}
        
        
    6.获取信息列表
    post参数名：method
    post参数内容：{"name":"getInfoList","args":{"user_id":"xxx","activity_type":xxx,"number":xxx, "sort_type":0}}
    
    服务器返回值(json格式)：
        请求失败：
        {"retValue": "", "retCode": -1, "retMsg": "xxxxx"}
        请求成功：
        {"retValue":[{"activity_id":xxx, "activity_picture":xxx, "activity_price":xxx, "user_nickname":"xxx", "user_avatar":xxx, "user_address":"xxx"},{...},...], "retCode": 0, "retMsg": ""}
    
    
    7.获取详细收养信息
    post参数名：method
    post参数内容：{"name":"getAdoptDetailList","args":{"activity_id":xxx}}
    
    服务器返回值(json格式)：
        请求失败：
        {"retValue": "", "retCode": -1, "retMsg": "xxxxx"}
        请求成功：
        {"retValue":[{"user_id","xxx", "activity_picture":xxx, "user_avatar":xxx, "user_nickname":"xxx", "user_age":xxx, "user_interest":xxx, "activity_pet_type":xxx, "activity_price":xxx, "activity_address":"xxx", "activity_introduction":"xxx","activity_start_time":"xxx", "activity_end_time":"xxx"}], "retCode": 0, "retMsg": ""}
    
    
    
    
