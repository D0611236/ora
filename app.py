from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import random



app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('yivMuXMVVCYp4akbbyWixSoZpjCquczpnjw1PMsd63aGDPAoGVAmtBNpiKX1RvTu9NLh6g1OAGwJ/ploFtg4hPKNbBCtJS+Q52jD6KdbZBWM1uerozP0J2PPGdGzcI0d92kaHHYT1hHLmSjgGkCnfQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('b1874a7a204e95099e021932f7da6f0f')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    get = event.message.text
#event.gessage.text接收使用者文字訊息

#############################################
#回傳文字訊息
    if(get == '？' or get =='?'):
        message = TextSendMessage(text = '?')
    if('如何' in get):
        get = 'replySituation'
    if('要嘛' in get):
        get = 'replySituation'
    if('要嗎' in get):
        get = 'replySituation'
    if(get == 'replySituation'):
        result = random.randint(0, 1)
        if(result == 0):
            message = TextSendMessage(text = '我想想😶')
        if(result > 0):
            message = TextSendMessage(text = '有人要吃橘子嗎(=ﾟωﾟ)つ🍊')
    if(get == '幹'):
        message = TextSendMessage(text = '怕.jpg')
    if(get == '啾'):
        message = TextSendMessage(text = '啾~❤')
    if(get == '誌誌帥嗎'):
        message = TextSendMessage(text = '好帥帥~ 幽默又可愛 喜歡❤')
    if(get == '祥育!' or get == '祥育！'):
        message = TextSendMessage(text = '帥帥帥帥')
    if(get == '不知道'):
        message = TextSendMessage(text = '我也不知道')
    if(get == '飲料骰子'):
        result = random.randint(0, 5)
        if(result == 0):
            message = TextSendMessage(text = '超商飲料')
        if(result == 1):
            message = TextSendMessage(text = '你他媽不會喝水嘛?')
        if(result == 2):
            message = TextSendMessage(text = '迷迷迷客夏')
        if(result == 3):
            message = TextSendMessage(text = '喝清心好開心')
        if(result == 4):
            message = TextSendMessage(text = '來個五十杯五十嵐')
        if(result > 4):
            message = TextSendMessage(text = '圓石來電')
    if(get == '逢甲肚子餓'):
        result = random.randint(0, 22)
        if(result == 0):
            message = TextSendMessage(text = '超商食品')
        if(result == 1):
            message = TextSendMessage(text = '甲賽')
        if(result == 2):
            message = TextSendMessage(text = '好而大居酒屋')
        if(result == 3):
            message = TextSendMessage(text = '隨義煮')
        if(result == 4):
            message = TextSendMessage(text = '來來魯肉飯')
        if(result == 5):
            message = TextSendMessage(text = '職人牛排')
        if(result == 6):
            message = TextSendMessage(text = '六扇門')
        if(result == 7):
            message = TextSendMessage(text = '九湯屋')
        if(result == 8):
            message = TextSendMessage(text = '七味廚坊')
        if(result == 9):
            message = TextSendMessage(text = '豐成麵館')
        if(result == 10):
            message = TextSendMessage(text = '吉蜂蒸餃')
        if(result == 11):
            message = TextSendMessage(text = '八方雲集')
        if(result == 12):
            message = TextSendMessage(text = '大丁拉麵')
        if(result == 13):
            message = TextSendMessage(text = '九州拉麵')
        if(result == 14):
            message = TextSendMessage(text = '黑盒子')
        if(result == 15):
            message = TextSendMessage(text = '擄胃專家')
        if(result == 16):
            message = TextSendMessage(text = '吉野烤肉飯')
        if(result == 17):
            message = TextSendMessage(text = '紅辣椒')
        if(result == 18):
            message = TextSendMessage(text = '小辣椒')
        if(result == 19):
            message = TextSendMessage(text = '麥當勞')
        if(result == 20):
            message = TextSendMessage(text = '鴨樓鴨肉飯')
        if(result == 21):
            message = TextSendMessage(text = '泡麵')
        if(result > 21):
            message = TextSendMessage(text = '粥遊天下')

#############################################
#回傳圖片訊息
    if(get == '庭庭抽'):
        message = ImageSendMessage(
            original_content_url = 'https://i.imgur.com/fTlDhKn.jpg',
            preview_image_url = 'https://i.imgur.com/fTlDhKn.jpg'
        )
    if(get == '庭婆抽'):
        message = ImageSendMessage(
            original_content_url = 'https://i.imgur.com/RyhdOXR.jpg',
            preview_image_url = 'https://i.imgur.com/RyhdOXR.jpg'
        )
    if(get == '剛剛在Dcard看到一個可愛der女森'):
        message = ImageSendMessage(
            original_content_url = 'https://i.imgur.com/bc7Oig5.jpg',
            preview_image_url = 'https://i.imgur.com/bc7Oig5.jpg'
        )
    if('黑人問號' in get):
        message = ImageSendMessage(
            original_content_url = 'https://i.imgur.com/zTOnfAi.jpg',
            preview_image_url = 'https://i.imgur.com/zTOnfAi.jpg'
        )
    if(get == '科學社社長抽' or get == '晴天抽'):
        message = ImageSendMessage(
            original_content_url = 'https://i.imgur.com/Cd2eUnx.jpg',
            preview_image_url = 'https://i.imgur.com/Cd2eUnx.jpg'
        )
    if(get == '劉德滑抽'):
        message = ImageSendMessage(
            original_content_url = 'https://i.imgur.com/sXXJq48.jpg',
            preview_image_url = 'https://i.imgur.com/sXXJq48.jpg'
        )
    if(get == '程程抽'):
        message = ImageSendMessage(
            original_content_url = 'https://i.imgur.com/dcO8RVL.jpg',
            preview_image_url = 'https://i.imgur.com/dcO8RVL.jpg'
        )
    if(get == '無疑王玉抽'):
        message = ImageSendMessage(
            original_content_url = 'https://i.imgur.com/KiodYrk.jpg',
            preview_image_url = 'https://i.imgur.com/KiodYrk.jpg'
        )
    if(get == '+淳抽'):
        message = ImageSendMessage(
            original_content_url = 'https://i.imgur.com/IksKVP1.jpg',
            preview_image_url = 'https://i.imgur.com/IksKVP1.jpg'
        )
    if(get == '阿祥抽'):
        message = ImageSendMessage(
            original_content_url = 'https://i.imgur.com/ZIjyjuI.jpg',
            preview_image_url = 'https://i.imgur.com/ZIjyjuI.jpg'
        )
    if(get == '癡漢二人組'):
        message = ImageSendMessage(
            original_content_url = 'https://i.imgur.com/FabmRZg.jpg',
            preview_image_url = 'https://i.imgur.com/FabmRZg.jpg'
        )
    if(get == '阿倩仔抽'):
        result = random.randint(0, 1)
        if(result == 0):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/vi3VuEx.jpg',
                preview_image_url = 'https://i.imgur.com/vi3VuEx.jpg'
            )
        if(result > 0):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/PTMT6fO.jpg',
                preview_image_url = 'https://i.imgur.com/PTMT6fO.jpg'
            )
    if(get == '雨林抽'):
        result = random.randint(0, 1)
        if(result == 0):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/dsmxnc8.jpg',
                preview_image_url = 'https://i.imgur.com/dsmxnc8.jpg'
            )
        if(result > 0):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/UN5J92A.jpg',
                preview_image_url = 'https://i.imgur.com/UN5J92A.jpg'
            )
    if(get == '誌誌抽'):
        message = ImageSendMessage(
            original_content_url = 'https://i.imgur.com/tslkGF3.jpg',
            preview_image_url = 'https://i.imgur.com/tslkGF3.jpg'
        )
    if(get == '唇語抽' or get == '脣語抽'):
        result = random.randint(0, 5)
        if(result == 0):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/mDAHeVc.jpg',
                preview_image_url = 'https://i.imgur.com/mDAHeVc.jpg'
            )
        if(result == 1):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/sEM6T0o.jpg',
                preview_image_url = 'https://i.imgur.com/sEM6T0o.jpg'
            )
        if(result == 2):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/ntyCKwx.jpg',
                preview_image_url = 'https://i.imgur.com/ntyCKwx.jpg'
            )
        if(result == 3):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/JIiCoNv.jpg',
                preview_image_url = 'https://i.imgur.com/JIiCoNv.jpg'
            )
        if(result == 4):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/kTpBKD1.jpg',
                preview_image_url = 'https://i.imgur.com/kTpBKD1.jpg'
            )
        if(result > 4):
            message = ImageSendMessage(
            original_content_url = 'https://i.imgur.com/KjfihNR.jpg',
            preview_image_url = 'https://i.imgur.com/KjfihNR.jpg'
        )
    if('肥胖熊' in get or '放屁熊' in get):
        result  = random.randint(0, 47)
        if(result == 0):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/LNLwOVY.jpg',
                preview_image_url = 'https://i.imgur.com/LNLwOVY.jpg'
            )
        if(result == 1):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/sTWlG2b.jpg',
                preview_image_url = 'https://i.imgur.com/sTWlG2b.jpg'
            )
        if(result == 2):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/wDAMnCX.jpg',
                preview_image_url = 'https://i.imgur.com/wDAMnCX.jpg'
            )
        if(result == 3):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/G6lDc9U.jpg',
                preview_image_url = 'https://i.imgur.com/G6lDc9U.jpg'
            )
        if(result == 4):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/phZJGVL.jpg',
                preview_image_url = 'https://i.imgur.com/phZJGVL.jpg'
            )
        if(result == 5):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/eJcwUGe.jpg',
                preview_image_url = 'https://i.imgur.com/eJcwUGe.jpg'
            )
        if(result == 6):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/yPDo6VK.jpg',
                preview_image_url = 'https://i.imgur.com/yPDo6VK.jpg'
            )
        if(result == 7):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/BBO6tQu.jpg',
                preview_image_url = 'https://i.imgur.com/BBO6tQu.jpg'
            )
        if(result == 8):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/jBi8Sa9.jpg',
                preview_image_url = 'https://i.imgur.com/jBi8Sa9.jpg'
            )
        if(result == 9):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/98hr5ig.jpg',
                preview_image_url = 'https://i.imgur.com/98hr5ig.jpg'
            )
        if(result == 10):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/VPK8tuM.jpg',
                preview_image_url = 'https://i.imgur.com/VPK8tuM.jpg'
            )
        if(result == 11):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/MuG3owb.jpg',
                preview_image_url = 'https://i.imgur.com/MuG3owb.jpg'
            )
        if(result == 12):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/z5RxVYl.jpg',
                preview_image_url = 'https://i.imgur.com/z5RxVYl.jpg'
            )
        if(result == 13):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/4A8dlmW.jpg',
                preview_image_url = 'https://i.imgur.com/4A8dlmW.jpg'
            )
        if(result == 14):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/7alh4ix.jpg',
                preview_image_url = 'https://i.imgur.com/7alh4ix.jpg'
            )
        if(result == 15):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/HDiELMy.jpg',
                preview_image_url = 'https://i.imgur.com/HDiELMy.jpg'
            )
        if(result == 16):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/t4EDBCz.jpg',
                preview_image_url = 'https://i.imgur.com/t4EDBCz.jpg'
            )
        if(result == 17):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/XU1Z6tM.jpg',
                preview_image_url = 'https://i.imgur.com/XU1Z6tM.jpg'
            )
        if(result == 18):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/XY8pQ6Q.jpg',
                preview_image_url = 'https://i.imgur.com/XY8pQ6Q.jpg'
            )
        if(result == 19):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/jiVI0J3.jpg',
                preview_image_url = 'https://i.imgur.com/jiVI0J3.jpg'
            )
        if(result == 20):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/sSTXmq6.jpg',
                preview_image_url = 'https://i.imgur.com/sSTXmq6.jpg'
            )
        if(result == 21):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/SBvTEjw.jpg',
                preview_image_url = 'https://i.imgur.com/SBvTEjw.jpg'
            )
        if(result == 22):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/lCwVkvS.jpg',
                preview_image_url = 'https://i.imgur.com/lCwVkvS.jpg'
            )
        if(result == 23):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/uAXnv9W.jpg',
                preview_image_url = 'https://i.imgur.com/uAXnv9W.jpg'
            )
        if(result == 24):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/YyYv9hM.jpg',
                preview_image_url = 'https://i.imgur.com/YyYv9hM.jpg'
            )
        if(result == 25):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/RFENycJ.jpg',
                preview_image_url = 'https://i.imgur.com/RFENycJ.jpg'
            )
        if(result == 26):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/OfKQOKk.jpg',
                preview_image_url = 'https://i.imgur.com/OfKQOKk.jpg'
            )
        if(result == 27):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/JXuEoYW.jpg',
                preview_image_url = 'https://i.imgur.com/JXuEoYW.jpg'
            )
        if(result == 28):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/2MR4pod.jpg',
                preview_image_url = 'https://i.imgur.com/2MR4pod.jpg'
            )
        if(result == 29):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/BwBlOmh.jpg',
                preview_image_url = 'https://i.imgur.com/BwBlOmh.jpg'
            )
        if(result == 30):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/okHH47T.jpg',
                preview_image_url = 'https://i.imgur.com/okHH47T.jpg'
            )
        if(result == 31):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/udEoS30.jpg',
                preview_image_url = 'https://i.imgur.com/udEoS30.jpg'
            )
        if(result == 32):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/njqbkwU.jpg',
                preview_image_url = 'https://i.imgur.com/njqbkwU.jpg'
            )
        if(result == 33):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/pdWBGLi.jpg',
                preview_image_url = 'https://i.imgur.com/pdWBGLi.jpg'
            )
        if(result == 34):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/msLQCud.jpg',
                preview_image_url = 'https://i.imgur.com/msLQCud.jpg'
            )
        if(result == 35):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/domV0Jw.jpg',
                preview_image_url = 'https://i.imgur.com/domV0Jw.jpg'
            )
        if(result == 36):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/MQrm4q3.jpg',
                preview_image_url = 'https://i.imgur.com/MQrm4q3.jpg'
            )
        if(result == 37):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/JNirvQx.jpg',
                preview_image_url = 'https://i.imgur.com/JNirvQx.jpg'
            )
        if(result == 38):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/Kw8bwgH.jpg',
                preview_image_url = 'https://i.imgur.com/Kw8bwgH.jpg'
            )
        if(result == 39):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/F4iUPI1.jpg',
                preview_image_url = 'https://i.imgur.com/F4iUPI1.jpg'
            )
        if(result == 40):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/rCPtvXd.jpg',
                preview_image_url = 'https://i.imgur.com/rCPtvXd.jpg'
            )
        if(result == 41):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/GscGrLH.jpg',
                preview_image_url = 'https://i.imgur.com/GscGrLH.jpg'
            )
        if(result == 42):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/rZX4v8K.jpg',
                preview_image_url = 'https://i.imgur.com/rZX4v8K.jpg'
            )
        if(result == 43):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/qTi3T42.jpg',
                preview_image_url = 'https://i.imgur.com/qTi3T42.jpg'
            )
        if(result == 44):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/rmEL3j0.jpg',
                preview_image_url = 'https://i.imgur.com/rmEL3j0.jpg'
            )
        if(result == 45):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/Kk4eE3p.jpg',
                preview_image_url = 'https://i.imgur.com/Kk4eE3p.jpg'
            )
        if(result == 46):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/5GPsvyi.jpg',
                preview_image_url = 'https://i.imgur.com/5GPsvyi.jpg'
            )
        if(result > 46):
            message = ImageSendMessage(
                original_content_url = 'https://i.imgur.com/OlgCSqb.jpg',
                preview_image_url = 'https://i.imgur.com/OlgCSqb.jpg'
            )
    
#############################################
#回傳ButtonsTemplate訊息
    if(get == '汪'):
        message = TemplateSendMessage(
            alt_text = '用手機看好不好?',
            template = ButtonsTemplate(
                title = '測試用',
                text = '預祝各位期末ALL PASS',
                thumbnail_image_url = 'https://i.imgur.com/74HtSJK.jpg',
                actions = [
                    MessageTemplateAction(
                        label = '伯朗咖啡',
                        text = '好喝'
                    )
                ]
            )
        )
    if('哈' in get):
        message = TemplateSendMessage(
            alt_text = '打開手機，許願池在你的手機裡?',
            template = ButtonsTemplate(
                title = '哈哈哈精靈許願池',
                text = '夢幻歌單，實現巨星之夢',
                thumbnail_image_url = 'https://i.imgur.com/jD1JAoH.jpg',
                actions = [
                    MessageTemplateAction(
                        label = 'ʕ•ᴥ•ʔ',
                        text = '肥胖熊'
                    ),
                    MessageTemplateAction(
                        label = '晶球',
                        text = '想出現在圖庫裡? 請將你的照片郵寄至ricky870921@gmail.com'
                    ),
                    URITemplateAction(
                        label = '呱風螫天 feat.韶洋',
                        uri = 'https://youtu.be/jyyq8UmJBh0'
                    )
                ]
            )
        )
    if(get == 'drama'):
        message = TemplateSendMessage(
            alt_text = 'drama for mobile.',
            template = ButtonsTemplate(
                title = '注意!↓',
                text = '感謝你的注意.',
                thumbnail_image_url = 'https://i.imgur.com/YjNKSS5.jpg',
                actions = [
                    URITemplateAction(
                        label = '不完美的正義',
                        uri = 'http://www.777drama.com/vod/14/18320play.html?18320-1-3'
                    ),
                    URITemplateAction(
                        label = '惡鄰布局',
                        uri = 'http://www.5goup.com/user/getmovie/show/5c078cc7d55812466c8887c7'
                    ),
                    URITemplateAction(
                        label = '噤界',
                        uri = 'https://pttplay.com/vod-play-id-RjlB-src-1-num-6x.html'
                    ),
                    URITemplateAction(
                        label = '夕霧花園',
                        uri = 'http://www.777drama.com/vod/14/19322play.html?19322-1-4'
                    )
                ]
            )
        )

#############################################
#回傳CarouselColumnTemplate訊息
#多個ButtonsTemplate
    if(get == '蝦米' or get == '當然'):
        get = '橘子'
    if(get == '橘子'):
        message = TemplateSendMessage(
            alt_text = '噹噹 小丁噹小丙噹小乙噹小甲噹',
            template = CarouselTemplate(
                columns = [
                    CarouselColumn(
                        thumbnail_image_url = 'https://i.imgur.com/VQpvhMX.jpg',
                        title = '在此提供香豔照',
                        text = '請別攝取過量',
                        actions = [
                            MessageTemplateAction(
                                label = '內克·脖子',
                                text = '誌誌抽'
                            ),
                            MessageTemplateAction(
                                label = '甩奶',
                                text = '庭庭抽'
                            ),
                            MessageTemplateAction(
                                label = '吉他社社長',
                                text = '阿祥抽'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url = 'https://i.imgur.com/f6aeyv4.jpg',
                        title = '奉上真實寫真',
                        text = '衝一點別太龜',
                        actions = [
                            MessageTemplateAction(
                                label = '女神雙下巴',
                                text = '唇語抽'
                            ),
                            MessageTemplateAction(
                                label = '風保大姐頭',
                                text = '程程抽'
                            ),
                            MessageTemplateAction(
                                label = '橘子本人',
                                text = '雨林抽'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url = 'https://i.imgur.com/4gzv4mJ.png',
                        title = '那些年，我們一起追的男孩',
                        text = '結果還是被發卡',
                        actions = [
                            MessageTemplateAction(
                                label = '2-021',
                                text = '剛剛在Dcard看到一個可愛der女森'
                            ),
                            MessageTemplateAction(
                                label = '劉·精益補習班',
                                text = '劉德滑抽'
                            ),
                            MessageTemplateAction(
                                label = '金正恩',
                                text = '晴天抽'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url = 'https://i.imgur.com/IbbQ1xo.jpg',
                        title = '解剖結果出來了',
                        text = '死因 - 解剖',
                        actions = [
                            MessageTemplateAction(
                                label = '國軍弟兄',
                                text = '無疑王玉抽'
                            ),
                            MessageTemplateAction(
                                label = '智障',
                                text = '+淳抽'
                            ),
                            MessageTemplateAction(
                                label = 'O777777',
                                text = '阿倩仔抽'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url = 'https://i.imgur.com/QD3Yikd.jpg',
                        title = 'I\'m still the same.',
                        text = '小考分數還是沒有變',
                        actions = [
                            MessageTemplateAction(
                                label = '我好興奮阿',
                                text = '癡漢二人組'
                            ),
                            MessageTemplateAction(
                                label = 'Wi-Fi',
                                text = 'WiFi'
                            ),
                            MessageTemplateAction(
                                label = '點歌許願池',
                                text = '哈'
                            )
                        ]
                    )
                ]
            )
        )    
    if(get == 'wifi' or get == 'WiFi'):
        message = TemplateSendMessage(
            alt_text = 'Please check your phone for password.',
            template = CarouselTemplate(
                columns = [
                    CarouselColumn(
                        thumbnail_image_url = 'https://i.imgur.com/UydhwfG.png',
                        title = 'Select Wi-Fi Name.',
                        text = 'tap which wi-fi you connected.',
                        actions = [
                            MessageTemplateAction(
                                label = 'N317',
                                text = 'N317_WiFi'
                            ),
                            MessageTemplateAction(
                                label = 'ASUS-RT51U',
                                text = 'D0645758'
                            ),
                            MessageTemplateAction(
                                label = 'NOV6-13',
                                text = '0911128943'
                            )
                        ]
                    )
                ]
            )
        )
    
#############################################
#回傳ImageCarouselTemplate訊息
    if(get == 'd'):
        #print("Image Carousel")
        message = TemplateSendMessage(
        alt_text='ImageCarousel template',
        template=ImageCarouselTemplate(
            columns=[
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/IbbQ1xo.jpg',
                    action=MessageTemplateAction(
                        label='postback1',
                        text='postback text1'
                    )
                ),
                ImageCarouselColumn(
                    image_url='https://i.imgur.com/VQpvhMX.jpg',
                    action=MessageTemplateAction(
                        label='postback2',
                        text='postback text2'
                    )
                )
            ]
        )
        )

    
#############################################
    if(get == '紹洋晴天破音'):
        message = AudioSendMessage(
            original_content_url='https://drive.google.com/file/d/1qsYbtwVQzrHVuiy3JPIFdwcF-vTr3l7j/view?usp=sharing',
            duration=240000
        )
    line_bot_api.reply_message(event.reply_token, message)

if __name__ == "__main__":
    app.run()
