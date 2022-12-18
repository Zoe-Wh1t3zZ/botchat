import os
import re
import random
from nonebot import MessageSegment
from nonebot import on_command
from datetime import datetime
import pytz

import hoshino
from hoshino import R, Service, priv, util
from hoshino.typing import CQEvent

tz = pytz.timezone('Asia/Shanghai')

sv_help = '''
bot内置的语言库
'''.strip()

sv = Service(
    name = '语言库',  #功能名
    use_priv = priv.NORMAL, #使用权限   
    manage_priv = priv.SUPERUSER, #管理权限
    visible = False, #False隐藏
    enable_on_default = True, #是否默认启用
    bundle = '通用', #属于哪一类
    help_ = sv_help #帮助文本
    )

@sv.on_fullmatch(["帮助语言库"])
async def bangzhu_botchat(bot, ev):
    await bot.send(ev, sv_help, at_sender=True)

#=====人格=====#
@sv.on_keyword(('沙雕机器人', '笨蛋机器人', '傻逼机器人', '憨憨机器人', '憨批机器人', '沙雕派蒙', '笨蛋派蒙', '傻逼派蒙', '憨憨派蒙', '憨批派蒙'))
async def chat_sad(bot, ev):
    await bot.send(ev, '哼！你才是笨蛋呢', at_sender=True)

@sv.on_fullmatch(('老婆', 'wife', 'laopo'), only_to_me=True)
async def chat_wife(bot, ev):
    if not priv.check_priv(ev, priv.ADMIN):
        await bot.send(ev, R.img('老婆.png').cqcode)
    else:
        await bot.send(ev, 'mua❤～')
        
@sv.on_fullmatch(('群管帮助'), only_to_me=False)
async def chat_help(bot, ev):
    if not priv.check_priv(ev, priv.ADMIN):
        await bot.send(ev, '只有管理员才能执行噢~')
    else:
        await bot.send(ev, R.img('adminhelp.png').cqcode)        
        
@sv.on_fullmatch('吃派蒙', only_to_me=False)
async def chat_eatpaimon(bot, ev):
    if not priv.check_priv(ev, priv.ADMIN):
        await bot.send(ev, '派蒙不是食物，哼！', at_sender=True)
    else:
        await bot.send(ev, R.img('吃派蒙.jpg').cqcode)
        
@sv.on_fullmatch('老公', only_to_me=True)
async def chat_laogong(bot, ev):
    await bot.send(ev, '人不能，至少不应该', at_sender=True)

@sv.on_fullmatch('mua~', only_to_me=True)
async def chat_mua(bot, ev):
    if not priv.check_priv(ev, priv.ADMIN):
        await bot.send(ev, '这位先生，请控制好自己的行为', at_sender=True)
    else:
        await bot.send(ev, '欸嘿嘿~这么多人有点不好意思呢')
        

#@sv.on_fullmatch(('在吗','在不','在不在','在嘛'))
#async def hearme(bot, ev):
#    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/听得见吗.mp3'
#    await bot.send(ev, f'[CQ:record,file=file:///{path}]')

@sv.on_fullmatch(('你真棒', '你好棒', '你真厉害', '你好厉害', '真棒', '真聪明', '你真聪明'), only_to_me=True)
async def iamgood(bot, ev):
    await bot.send(ev, f'诶嘿嘿~')

##################################################
@sv.on_keyword(('诶嘿','哎嘿','欸嘿'))
async def eihe(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/DIY/诶嘿.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
    
@sv.on_keyword(('进不去'))
async def nointo(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/DIY/进不去.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
    
@sv.on_keyword(('你是谁'))
async def whoareu(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/DIY/嘿嘿你猜.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
    
@sv.on_keyword(('前面的区域'))
async def qmdqy(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/前面的区域.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
    
@sv.on_keyword(('小兄弟'))
async def small(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/小兄弟.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
    
@sv.on_keyword(('社死'))
async def social(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/社死.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')    
    
@sv.on_keyword(('耽误'))
async def dwsj(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/耽误太多时间.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
    
@sv.on_keyword(('对不起','dbq'))
async def sorry(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/难听的绰号.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
    
@sv.on_keyword(('祝福'))
async def zf(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/来个祝福.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
    
@sv.on_keyword(('泪目'))
async def leimu(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/泪目.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
    
@sv.on_keyword(('中二派蒙'))
async def zhonger(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/中二派蒙.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
    
@sv.on_keyword(('抱抱'))
async def baobao(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/真是个小可爱.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
    
@sv.on_keyword(('无语'))
async def nosay(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/无语.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
    
@sv.on_keyword(('伙伴'))
async def friend(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/伙伴.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
    
@sv.on_keyword(('好色哦','好色噢','好涩哦'))
async def sexy(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/好色哦.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
    
@sv.on_keyword(('生气'))
async def angry(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/好生气.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
    
@sv.on_keyword(('好气哦','好气噢'))
async def nervous(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/好气哦.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
    
@sv.on_keyword(('憨批'))
async def shabi(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/憨批.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
    
@sv.on_keyword(('大佬nb','大佬牛逼','卧槽大佬'))
async def dalao(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/大佬nb.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
    
@sv.on_keyword(('不是吧'))
async def asir(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/不是吧阿sir.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
    
@sv.on_keyword(('变态'))
async def biantai(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/好变态.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
    
@sv.on_keyword(('给爷爬'))
async def geiyepa(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/给爷爬.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
    
@sv.on_keyword(('信我'))
async def believeme(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/我信你个鬼.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
    
@sv.on_keyword(('这个仇','记住'))
async def thechou(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/这个仇.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
    
@sv.on_keyword(('绿茶'))
async def greentea(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/绿茶派.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')

#====海灯节限定======#
@sv.on_keyword(('冲啊','冲呀'))
async def babalago(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/芭芭拉冲呀.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')
    
@sv.on_keyword(('派毛','白毛'))
async def paimao(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/派毛.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')  

@sv.on_keyword(('让我看看'))
async def letme(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/让我看看.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')     
    
@sv.on_keyword(('爆炸','砰','嘣','嘭'))
async def boom(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/爆炸.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')    
    
@sv.on_keyword(('不见了','消失了'))
async def leave(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/不见了.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')    

@sv.on_keyword(('帝君','岩王'))
async def dijun(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/帝君.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]') 

@sv.on_keyword(('海灯节快乐'))
async def sealight(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/海灯节快乐.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')  

@sv.on_keyword(('好康','好看'))
async def nice(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/好看哦.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')  

@sv.on_keyword(('惊讶','吃惊','为什么'))
async def jingyaba(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/很惊讶.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')

@sv.on_keyword(('嘟嘟','不对不对','回答错误'))
async def indirect(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/回答错误.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')    
    
@sv.on_keyword(('敬酒不吃吃罚酒'))
async def bushitaiju(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/敬酒不吃吃罚酒.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')    
    
@sv.on_keyword(('这日子','没法','过不'))
async def nowayto(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/没法过啊.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')   

@sv.on_keyword(('吓我','吓死','吓人'))
async def xiawoyit(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/吓我一跳.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')    
    
@sv.on_keyword(('真的吗','真的嘛','确定吗','确定嘛'))
async def areusure(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/真的吗.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')    
    
@sv.on_keyword(('敢说','真勇','真强','真猛'))
async def zhenganshuo(bot, ev):
    path = 'C:/Users/Administrator/Desktop/res/img/Zoe/真敢说.mp3'
    await bot.send(ev, f'[CQ:record,file=file:///{path}]')    
#====群聊======#
@sv.on_fullmatch(('我满了', '我出了', '我成功了', '我出货了', '我没歪', '我出金了', '单抽出金'))
async def chat_congrat(bot, ev):
    await bot.send(ev, '恭喜！', at_sender=True)
    await util.silence(ev, 30)

@sv.on_fullmatch(('我歪了', '我放弃了', '我g了'))
async def chat_sympathy(bot, ev):
    if random.random()<0.50:
        await bot.send(ev, '真可惜。不过不要灰心，说不定下一次抽卡就出奇迹了呢！', at_sender=True)
    else:
        await bot.send(ev, '谢谢你非洲人，哈哈哈哈哈', at_sender=True)

@sv.on_fullmatch('我好了')
async def ddhaole(bot, ev):
    await bot.send(ev, '不许好，憋回去！')
    await util.silence(ev, 30)
    
@sv.on_keyword('不准套娃')
async def taowa(bot, ev):
    await bot.send(ev, f'不准不准套娃')

@sv.on_fullmatch('我不要你觉得')
async def wojuede(bot, ev):
    await bot.send(ev, f'我要我觉得')

@sv.on_fullmatch('与你无关')
async def yuniwugua(bot, ev):
    await bot.send(ev, f'雨女无瓜')

@sv.on_fullmatch('消除恐惧的最好办法就是面对恐惧')
async def aoligei(bot, ev):
    await bot.send(ev, f'加油，奥利给！')

@sv.on_keyword(('你这瓜', '这瓜'))
async def gua(bot, ev):
    await bot.send(ev, f'这瓜保熟吗？')

@sv.on_keyword(('这是计划的一部分', '这就是我的逃跑路线'))
async def jihua(bot, ev):
    await bot.send(ev, f'这也在你的计划之中吗，JOJO！')

@sv.on_keyword(('大威天龙', '大罗法咒', '准备捉妖', '我一眼就看出你不是人'))
async def nibushiren(bot, ev):
    await bot.send(ev, f'大威天龙\n👌世尊地藏！\n🤙大罗法咒\n🙏般若诸佛！\n✋般若巴麻哄！\n🐉飞龙在天！')

@sv.on_keyword(('兄弟们我做的对吗', '好兄弟们我做的对吗', 'xdm我做的对吗', '我做的对吗', 'hxd们我做的对吗', '兄弟萌我做的对吗', '好兄弟萌我做的对吗', '老铁们我做的对吗'))
async def zhengdaodeguang(bot, ev):
    await bot.send(ev, f'正道的光！照在了大地上~')

@sv.on_keyword(('雷霆嘎巴', '雷霆嘎巴儿'))
async def aa(bot, ev):
    await bot.send(ev, f'无情哈喇少~')

@sv.on_keyword(('你吼那么大声干什么', '你吼辣么大声干什么'))
async def wuguan(bot, ev):
    await bot.send(ev, f'那你去找物管啊')

@sv.on_keyword('这就是你分手的借口')
async def aihe(bot, ev):
    await bot.send(ev, f'🕺🕺🕺如果让你重新来过\n🕺🕺🕺你会不会爱我\n🕺🕺🕺爱情让人拥有快乐\n🕺🕺🕺也会带来折磨\n🕺🕺🕺曾经和你一起走过传说中的爱河\n🕺🕺🕺已经被我泪水淹没\n🕺🕺🕺变成痛苦的爱河')

@sv.on_keyword('我和你荡秋千')
async def qiuqian(bot, ev):
    await bot.send(ev, f'荡到那天外天🌄🌄🌄\n看到那牛郎织女相会在那银河边🌌🌌🌌\n我和你心相连💞💞💞\n幻想在那蔚蓝海边🌊🌊🌊\n坐着那小船游啊游啊游啊⛵⛵⛵\n游到爱的彼岸🏝️🏝️🏝️')

@sv.on_keyword(('大点声', '大声点', '听不见'))
async def jingshen(bot, ev):
    if random.random()<0.50:
        await bot.send(ev, '这么小声还想开军舰！？', at_sender=True)
    else:
        await bot.send(ev, '好！很有精神！', at_sender=True)

@sv.on_keyword(('三年之期', '黑羽令', '赘婿'))
async def longwangnb(bot, ev):
    if random.random()<0.50:
        await bot.send(ev, '三年之期已到，江城龙王，恭迎回府！', at_sender=True)
    else:
        await bot.send(ev, '这苏家，不待也罢！立刻下黑羽令，我要让整个江城都知道，我龙王，回来了！')    

@sv.on_keyword('一路向北')
async def yiluxiangbei(bot, ev):
        await bot.send(ev, '我一路向北，离开有你的季节~', at_sender=True)

@sv.on_keyword('敢杀我的马')
async def wodema(bot, ev):
        await bot.send(ev, 'TMD张麻子，敢杀我的🐎！')

Chabuduo_dele = '''
差不多得了，太哈人了，怎么回事呢？我先run了，可不敢乱说，谁指使你的？你有什么目的？哪来的境外势力，什么越南新闻，才不信！不信团不传团，等谣谣反转，你给我回来，我华为手机看不见！这是否有点，你麻麻地，典中典，经典咏流传，赢麻了，简中局域网，您吉祥，笑嘻了，差不多得了，都给你懂完了，赢麻了，我不好说我擦，你寄吧谁啊？苟罕见是吧，绷不住了
'''.strip()
@sv.on_keyword(('差不多得了', '绷不住了', '你寄吧谁啊'))
async def chabuduo(bot, ev):
    if random.random()<0.35:
        await bot.send(ev, Chabuduo_dele)

Ddd_d = '''
我简单说两句，至于我的身份，你明白就行，总而言之，这个事呢，现在就是这个情况，具体的呢，大家也都看得到，我因为这个身份上的问题，也得出来说那么几句，可能，你听的不是很明白，但是意思就是那么个意思，我的身份呢，不知道的你也不用去猜，这种事情见得多了，我只想说懂得都懂，不懂的我也不多解释，毕竟自己知道就好，细细品吧。你们也别来问我怎么了，利益牵扯太大，说了对你我都没好处，当不知道就行了，其余的我只能说这里面水很深，牵扯到很多东西。详细情况你们自己是很难找的，网上大部分已经删除干净了，所以我只能说懂得都懂。懂的人已经基本都获利上岸什么的了，不懂的人永远不懂，关键懂的人都是自己悟的，你也不知道谁是懂的人也没法请教，大家都藏着掖着生怕别人知道自己懂事，懂了就能收割不懂的，你甚至都不知道自己不懂。只是在有些时候，某些人对某些事情不懂装懂，还以为别人不懂。其实自己才是不懂的，别人懂的够多了，不仅懂，还懂的超越了这个范围，但是某些不懂的人让这个懂的人完全教不懂，所以不懂的人永远不懂，只能不懂装懂，别人说懂的都懂，只要点点头就行了，其实你懂的我也懂,谁让我们都懂呢,不懂的话也没必要装懂,毕竟里面牵扣扯到很多懂不了的事。这种事懂的人也没必要访出来,不懂的人看见又来问七问八,最后跟他说了他也不一定能懂,就算懂了以后也对他不好,毕竟懂的太多了不是好事。所以大家最好是不懂就不要去了解,懂太多不好。
'''.strip()
@sv.on_keyword(('懂得都懂'))
async def ddd_d(bot, ev):
    if random.random()<0.30:
        await bot.send(ev, Ddd_d)



# 图片请放于 img/keyword目录下 #

@sv.on_keyword(('确实', '有一说一', 'u1s1', 'yysy'))
async def chat_queshi(bot, ev):
    if random.random() < 0.30:
        await bot.send(ev, R.img(f"keyword/确实.jpg").cqcode)

@sv.on_keyword(('内鬼'))
async def chat_neigui(bot, ev):
    if random.random() < 0.40:
        await bot.send(ev, R.img(f"keyword/内鬼.png").cqcode)
        
@sv.on_keyword(('不要以为这样就赢了'))
async def chat_clanba(bot, ev):
    if random.random() < 0.40:
        await bot.send(ev, R.img(f"keyword/不要以为这样就赢了.jpg").cqcode)
                     
@sv.on_keyword(('上流', '上流社会', '红酒'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/上流.jpg").cqcode)
        
@sv.on_keyword(('真行', '彳亍'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/行.jpg").cqcode)
       
@sv.on_keyword(('别肝啦', '别肝了', '求求你们别肝了'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/别肝啦.jpg").cqcode)
        
@sv.on_keyword(('lsp', '老色批'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/lsp.jpg").cqcode)        
       
@sv.on_keyword(('爬', '爪巴'))
async def chat_clanba(bot, ev):
    if random.random() < 0.20:
        await bot.send(ev, R.img(f"keyword/爬.jpg").cqcode)   

@sv.on_keyword(('不会吧'))
async def chat_clanba(bot, ev):
    if random.random() < 0.30:
        await bot.send(ev, R.img(f"keyword/不会吧.jpg").cqcode)
        
@sv.on_keyword(('mana', '玛娜'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/mana.jpg").cqcode)
        
@sv.on_keyword(('整一个', '白嫖'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/整一个.png").cqcode)

@sv.on_keyword(('正道的光'))
async def chat_clanba(bot, ev):
    if random.random() < 0.40:
        await bot.send(ev, R.img(f"keyword/正道的光.jpg").cqcode)
        
@sv.on_keyword(('好臭啊', '野兽先辈'))
async def chat_clanba(bot, ev):
    if random.random() < 0.40:
        await bot.send(ev, R.img(f"keyword/臭.jpg").cqcode)
        
@sv.on_keyword(('我超勇的'))
async def chat_clanba(bot, ev):
    if random.random() < 0.40:
        await bot.send(ev, R.img(f"keyword/勇.jpg").cqcode)
        
@sv.on_keyword(('不对劲'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/不对劲.jpg").cqcode)
        
@sv.on_keyword(('respect', '尊重'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/res.jpg").cqcode)
        
@sv.on_keyword(('晒卡', '我出货啦', '我中了', '我出了'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/gacha.jpg").cqcode)
        
@sv.on_keyword(('死机', '错误', 'error'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/错误.jpg").cqcode)
        
@sv.on_keyword(('芜湖', '起飞', '飞飞飞'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/飞.jpg").cqcode)
                       
@sv.on_keyword(('你有问题'))
async def chat_clanba(bot, ev):
    if random.random() < 0.30:
        await bot.send(ev, R.img(f"keyword/123.png").cqcode)

@sv.on_keyword(('box', '角色练度'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/box.jpg").cqcode)

@sv.on_keyword(('原石', '宝石', '挖矿'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/原石.jpg").cqcode)

@sv.on_keyword(('布丁'))
async def chat_clanba(bot, ev):
    if random.random() < 0.40:
        await bot.send(ev, R.img(f"keyword/布丁.gif").cqcode)

@sv.on_fullmatch(('我能去你家吃饭嘛', '我能去你家吃饭吗'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/吃饭吃一勺.jpg").cqcode)
        
@sv.on_keyword(('武器大师', '拿来吧你'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/武器大师.jpg").cqcode)
        
@sv.on_keyword(('鬼混'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/鬼混.jpg").cqcode)
        
@sv.on_keyword(('起床了'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/起床.jpg").cqcode)
        
@sv.on_keyword(('玩原神', '原来'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/原来你也玩原神.jpg").cqcode)   

@sv.on_keyword(('屑'))
async def chat_clanba(bot, ev):
    if random.random() < 0.25:
        await bot.send(ev, R.img(f"keyword/屑.jpg").cqcode) 

@sv.on_keyword(('非常简单'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/非常简单.png").cqcode)   

@sv.on_keyword(('不简单'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/派蒙识破.png").cqcode)   

@sv.on_keyword(('怎么回事', '怎么肥四'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/怎么回事.png").cqcode)  

@sv.on_keyword(('来点色图', '来点涩图'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/来点色图.jpg").cqcode)  

@sv.on_keyword(('不知好歹', '岂有此理'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/不知好歹.jpg").cqcode) 

@sv.on_keyword(('人生啊'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/人生啊.jpg").cqcode)    

@sv.on_keyword(('落魄了'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/落魄了.png").cqcode)     

@sv.on_keyword(('原谅', '放过'))
async def chat_clanba(bot, ev):
    if random.random() < 0.45:
        await bot.send(ev, R.img(f"keyword/原谅.png").cqcode)     

@sv.on_keyword(('垃圾原神', '辣鸡原神'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/垃圾原神.png").cqcode)   

@sv.on_keyword(('来碗牛杂', '刻师傅'))
async def chat_clanba(bot, ev):
    if random.random() < 0.50:
        await bot.send(ev, R.img(f"keyword/来碗牛杂.png").cqcode)  

@sv.on_keyword(('劲爆', '刺激'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/这么刺激.png").cqcode) 

@sv.on_keyword(('你也有今天', '哈哈哈哈哈哈'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/你也有今天.png").cqcode)   

@sv.on_keyword(('上号'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/上号.png").cqcode)  

@sv.on_keyword(('就这', '九折'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/就这.png").cqcode) 

@sv.on_keyword(('小事儿', '小菜一碟'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/小事儿.png").cqcode)
        
#=================#


az_folder = R.img('keyword/az/').path
@sv.on_keyword(('啊这'))
async def chat_az(bot, ev):
    if random.random() < 0.55:
        filelist = os.listdir(az_folder)
        path = None
        while not path or not os.path.isfile(path):
            filename = random.choice(filelist)
            path = os.path.join(az_folder, filename)
            pic = R.img('keyword/az/', filename).cqcode
            await bot.send(ev, pic, at_sender=False)

jietou_folder = R.img('keyword/jt/').path
@sv.on_keyword(('接头'))
async def chat_az(bot, ev):
    if random.random() < 0.55:
        filelist = os.listdir(jietou_folder)
        path = None
        while not path or not os.path.isfile(path):
            filename = random.choice(filelist)
            path = os.path.join(jietou_folder, filename)
            pic = R.img('keyword/jt/', filename).cqcode
            await bot.send(ev, pic, at_sender=False)


niant_folder = R.img('keyword/niant/').path
@sv.on_keyword(('炼铜'))
async def chat_niant(bot, ev):
    if random.random() < 0.50:
        filelist = os.listdir(jietou_folder)
        path = None
        while not path or not os.path.isfile(path):
            filename = random.choice(filelist)
            path = os.path.join(niant_folder, filename)
            pic = R.img('keyword/niant/', filename).cqcode
            await bot.send(ev, pic, at_sender=False)
    else:
        await bot.send(ev, f'朕怎么富国强兵？')

mdjl_folder = R.img('keyword/mdjl/').path
@sv.on_keyword(('妈的绝了'))
async def chat_mdjl(bot, ev):
    if random.random() < 0.55:
        filelist = os.listdir(mdjl_folder)
        path = None
        while not path or not os.path.isfile(path):
            filename = random.choice(filelist)
            path = os.path.join(mdjl_folder, filename)
            pic = R.img('keyword/mdjl/', filename).cqcode
            await bot.send(ev, pic, at_sender=False)

@sv.on_keyword(('xcw零爆', '小仓唯零爆'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/小仓唯.jpg").cqcode)

@sv.on_keyword(('不太好吧'))
async def chat_clanba(bot, ev):
    if random.random() < 0.40:
        await bot.send(ev, R.img(f"keyword/不太好.jpg").cqcode)

@sv.on_keyword(('零花钱'))
async def chat_clanba(bot, ev):
    if random.random() < 0.40:
        await bot.send(ev, R.img(f"keyword/零花钱.jpg").cqcode)

@sv.on_keyword(('伊利亚'))
async def chat_clanba(bot, ev):
    if random.random() < 0.40:
        await bot.send(ev, R.img(f"keyword/伊利亚.jpg").cqcode)

@sv.on_keyword(('伊莉雅', 'yly'))
async def chat_clanba(bot, ev):
    if random.random() < 0.40:
        await bot.send(ev, R.img(f"keyword/伊莉雅.jpg").cqcode)

@sv.on_fullmatch(('牙白', '牙白的死呐', '厉害了啊', '牙白得死呐'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/牙白.jpg").cqcode)

@sv.on_keyword(('遇到困难', '遇到困难睡大觉'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/遇到困难.jpg").cqcode)

@sv.on_keyword(('云里雾里', '懵', '不懂'))
async def chat_clanba(bot, ev):
    if random.random() < 0.40:
        await bot.send(ev, R.img(f"keyword/云里雾里.jpg").cqcode)

@sv.on_keyword(('咕噜凌波', '咕噜灵波'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/咕噜灵波.jpg").cqcode)

@sv.on_keyword(('甜心刀'))
async def chat_clanba(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/甜心刀教程.jpg").cqcode)


#==================#

clan_folder = R.img('keyword/clan/').path
@sv.on_keyword(('会战', '公会', '会长'))
async def chat_clan(bot, ev):
    if random.random() < 0.40:
        filelist = os.listdir(clan_folder)
        path = None
        while not path or not os.path.isfile(path):
            filename = random.choice(filelist)
            path = os.path.join(clan_folder, filename)
            pic1 = R.img('keyword/clan/', filename).cqcode
            await bot.send(ev, pic1, at_sender=False)
#===================#
tree_folder = R.img('keyword/tree/').path
@sv.on_keyword(('挂树'))
async def chat_tree(bot, ev):
    if random.random() < 0.55:
        filelist = os.listdir(tree_folder)
        path = None
        while not path or not os.path.isfile(path):
            filename = random.choice(filelist)
            path = os.path.join(tree_folder, filename)
            pic2 = R.img('keyword/tree/', filename).cqcode
            await bot.send(ev, pic2, at_sender=False)
#==================#

@sv.on_fullmatch(('UE对不起', 'YUI对不起', 'yui对不起', 'ue对不起', '由衣对不起', '优衣对不起'))
async def chat_uesorry(bot, ev):
    if random.random() < 0.55:
        await bot.send(ev, R.img(f"keyword/对不起.jpg").cqcode)