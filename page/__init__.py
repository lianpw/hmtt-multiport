from selenium.webdriver.common.by import By
from tools.read_yaml import read_yaml

# 以下数据为自媒体, 后台管理url

mp_url = 'http://ttmp.research.itcast.cn/#/login'
mis_url = 'http://ttmis.research.itcast.cn/#/'

# 以下为文章相关配置数据
title = read_yaml('mp_article.yaml')[0][0]
channel = read_yaml('mp_article.yaml')[0][4]

# 以下数据为自媒体登录模块配置数据
# 用户名
login_username = By.CSS_SELECTOR, "[placeholder='请输入手机号']"
# 密码
login_pwd = By.CSS_SELECTOR, "[placeholder='验证码']"
# 登录按钮
login_btn = By.CSS_SELECTOR, '.el-button--primary'
# 昵称
login_nickname = By.CSS_SELECTOR, '.user-name'

# 内容管理
login_content_manager = By.XPATH, "//*[text()='内容管理']/.."
# 发布文章
login_publish_article = By.XPATH, "//*[contains(text(), '发布文章')]"
# 文章标题
login_article_title = By.CSS_SELECTOR, "[placeholder='文章名称']"
# iframe 使用元素切换可以激活显示等待, 如果直接使用字符串切换,则不会激活显示等待
login_iframe = By.CSS_SELECTOR, '#publishTinymce_ifr'
# 文章内容 定位到body, 不要定位到p标签
login_content = By.CSS_SELECTOR, '#tinymce'
# 封面
login_cover = By.XPATH, "//*[text()='自动']"
# 频道 已经封装到webbase里面

# 发表 按钮
login_publish_btn = By.XPATH, "//*[text()='发表']/.."
# 结果
login_result = By.XPATH, "//*[contains(text(), '新增文章成功')]"


"""以下配置信息为后台管理元素"""
# 用户名
mis_username = By.CSS_SELECTOR, "[name='username']"
# 密码
mis_pwd = By.CSS_SELECTOR, "[name='password']"
# 登录按钮
mis_login_btn = By.CSS_SELECTOR, '#inp1'
# 昵称
mis_nickname = By.CSS_SELECTOR, '.user_info'

# 信息管理
mis_msg_manage = By.XPATH, "//*[text()='信息管理']"
# 内容审核
mis_content_audit = By.XPATH, "//*[text()='内容审核']"
# 文章标题
mis_article_title = By.CSS_SELECTOR, "[placeholder='请输入: 文章名称']"
# 频道
mis_channel = By.CSS_SELECTOR, "[placeholder='请输入: 频道']"
# 查询按钮
mis_find_btn = By.CSS_SELECTOR, '.find'
# 文章id
mis_article_id = By.CSS_SELECTOR, '.cell>span'
# 通过
mis_pass = By.XPATH, "//*[text()='通过']/.."
# 确定
mis_confirm = By.CSS_SELECTOR, '.el-message-box__btns button:nth-child(2)'

"""以下为app应用元素配置信息"""
# 包名
appPackage = 'com.itcast.toutiaoApp'
# 启动名
appActivity = '.MainActivity'

# 手机号
app_phone = By.XPATH, "//*[@class='android.widget.EditText' and @index='1']"
# app_phone = By.CLASS_NAME, 'android.widget.EditText'
# 验证码
app_verify_code = By.XPATH, "//*[@index='2' and @class='android.widget.EditText']"
# 登录按钮
app_login_btn = By.XPATH, "//*[@class='android.widget.Button']"
# 我的菜单
app_me = By.XPATH, "//*[@index='3' and contains(@text, '我的')]"