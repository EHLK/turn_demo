# debug临时定义使用
# default turns = 0
# 使用define的值不能回滚及存档
# 使用default赋值在游戏启动或新游戏加载是定义（前提是未被定义过）
#default def_y_team = [{"name": "队友1", "hp": 30, "atk": 10},{"name": "队友2", "hp": 45, "atk": 8}]
#default def_d_team = [{"name": "敌人1", "hp": 60, "atk": 10},{"name": "敌人2", "hp": 45, "atk": 13}]
default turns = 1
default dmsg = ""
default 待执行操作列表 = [[],[],[]]
image atk_button_idle:
    "images/atk_menu.png"
    zoom 0.5
image no_atk_button:
    "images/no_atk_menu.png"
    zoom 0.5
image atk_button_hover:
    "images/atk_menu.png"
    blur 1.5
    zoom 0.5
image dqxzjt:
    "images/jt_dqxz.png"
    zoom 0.1
    align(0.5, 0.5)
image jt_reday:
    "images/jt_zbjx.png"
    zoom 0.2
    align(0.5, 0.5)
label mycc(team_cy,team_cd):
    # 初始值
    python:
        store.battle_jg = ""
        # 简单初始化，因为没有类似速度啥的属性
        quick_menu = False
        # 回合数初始化为1
        store.turns = 1
        # 当前选择的敌人，默认第一个
        sd= 0
        # 当前选择的角色，默认第一个
        sy= 0
        # 重新写了逻辑，突然发现要的可能不是你打一下我打一下的，而是我们打完敌人再打的
        # 0 角色下标 1 操作下标 2 操作目标
        待执行操作列表=[[],[],[]]
    call screen mycc_screen(team_cy,team_cd)
    return
# 使用python防止场景预加载


screen mycc_screen(team_y=[],team_d=[]):
    # 下标列表
    $ 可操友队 = 可操作下标列表(dw=team_cy,已操角色=待执行操作列表[0])
    # 背景
    frame:
        background "#dadada"
        # 左边距
        xfill True
        yfill True
        vbox:
            xfill True
            yfill True
            #xycenter (0.5,0.5)
            # 顶部信息框
            frame:
                background RoundRect("#3f3f3f")
                xycenter (0.5,0.58)
                xysize(0.98,0.15)  # 减小了信息框因为不想写蓝条了
                frame:
                    xycenter(0.5,0.5)
                    #background Solid("#00ff0d")
                    background None
                    hbox:
                        xfill True
                        yfill True
                        # 顶左 选中的队友数据
                        frame:
                            xsize 0.4
                            background None
                            xfill True
                            # 头像
                            frame:
                                xfill True
                                yfill True
                                xysize(100,100)
                                # 头像占位
                                text str(team_y[sy]['name'][0] or "王")  size 100 align(0.5, 0.5)
                                # add Placeholder(base="bg")
                            frame:
                                offset(110,58)
                                bar:
                                    value AnimatedValue(value=team_y[sy]["hp"],range=team_y[sy]["max_hp"],delay=0.5)
                                    xysize(400,30)
                                    at bar_shake
                            hbox:
                                offset(110,0)
                                text "[team_y[sy]['name']]" size 50
                                text "等级1" yalign 1.0 offset(3,-3) # 界面写麻了，不想加等级属性了
                                # 用来看效果的，勿点
                            textbutton "[team_y[sy]['hp']]":
                                offset(110,60)
                                text_size 20
                                text_outlines [(absolute(2), "#effdff", absolute(0), absolute(0))]
                                text_color "#000000"
                                text_selected_color "#7573f5"
                                hovered SetVariable("team_y[sy]['hp']",50)
                                unhovered SetVariable("temp",50)
                                #action SetVariable("team_y[0]['hp']",30)
                                #action Function(ChangeValue,team=team_y,amount = -10) 错误用法
                                action Function(team_y[sy].sethp,30)
                        frame:
                            background None
                            xsize 0.33
                            xfill True
                            align(0.5, -0.2)
                        # 顶中 回合数
                            frame:
                                align(0.5, 0.5)
                                background RoundRect("#ff0000")
                                text "{color=#BF3512}{size=50}{b}回合 [store.turns]"
                        # 顶右 敌人数据
                        frame:
                            # 右边比左边多部分像素
                            xsize 1.0
                            #xfill True
                            background None
                            align(0.5, 0.0)
                            xfill True
                            # 头像
                            hbox:
                                xfill True
                                frame:
                                    background None
                                    align(2.0,0.0)
                                    hbox:
                                        align(.0, 0.5)
                                        #offset(-195,0)
                                        text "等级1" offset(0,11)
                                        text "[team_d[sd]['name']]" size 50 offset(0,-6) xalign(1.0)
                                frame:
                                    align(1.0,0.0)
                                    xfill True
                                    yfill True
                                    xysize(100,100)
                                    # 头像占位
                                    text str((team_d[sd]["name"][0] or "1"))  size 100 align(0.5, 0.5)
                            
                            frame:
                                offset(210,58)
                                # 此bar中left为少，right为多 敌人的
                                bar:
                                    bar_invert True
                                    left_bar "gui/bar/right_hong.png"
                                    right_bar "gui/bar/left_hong.png"
                                    value AnimatedValue(value=team_d[sd]["hp"],range=team_d[sd]["max_hp"],delay=0.5)
                                    xysize(400,30)
                                    at bar_shake
                            text "[team_d[sd]['hp']:.1f]/[team_d[sd]['max_hp']]" align((0.82, 0.7))
            # 左半队友及右半敌人队列框
            frame:
                background None
                ycenter(0.5)
                xcenter(0.5)
                ysize(0.95)
                xsize(0.98)
                yfill True
                xfill True
                hbox:
                    yfill True
                    xfill True
                    frame:
                        xycenter(0.163,0.5)
                        xsize(305)
                        background RoundRect("#3f3f3f")
                        ysize(0.99)
                        yfill True
                        # 友方队列
                        vpgrid:
                            spacing 10
                            xsize(440)
                            cols 1 # 列数
                            rows len(team_y) # 行数
                            for a,t_c in enumerate(team_y):
                                $ name = t_c['name'] # 不定义该局部变量会导致所有角色名一样
                                $ hp = t_c['hp']
                                $ max_hp = t_c['max_hp']
                                hbox:
                                    frame:
                                        #background None
                                        button:
                                            vbox:
                                                text "[name]" size 30 align(0.5, 0.5)
                                                bar value AnimatedValue(hp,max_hp,1.0) xsize(270)
                                            action If(t_c["life"],SetVariable("sy",a),Function(定义消息,turns=store.turns,t="已阵亡无法操作",c=1))
                                    if a in 待执行操作列表[0]:
                                        add "jt_reday"
                                    if sy == a:
                                        add "dqxzjt"

                        #text "[config.transientwwwwwwwwwwww
                    # 右半敌人队列
                    frame:
                        xsize(300)
                        xycenter(0.84,0.5)
                        background RoundRect("#3f3f3f")
                        ysize(0.99)
                        vpgrid:
                            spacing 10
                            xsize(300)
                            cols 1 # 列数
                            rows len(team_d) # 行数
                            for a,t_c in enumerate(team_d):
                                $ name = t_c['name'] # 不定义该局部变量会导致所有角色名一样
                                $ hp = t_c['hp']
                                $ max_hp = t_c['max_hp']
                                frame:
                                    # background None
                                    button:
                                        vbox:
                                            text "[name]" size 30 align(0.5, 0.5)
                                            bar value AnimatedValue(hp,max_hp,1.0) xsize(270):
                                                left_bar "gui/bar/right_hong.png"
                                                right_bar "gui/bar/left_hong.png"
                                                bar_invert True
                                        action SetVariable("sd",a)
                # 操作框
                frame:
                    ysize(0.2)
                    xsize(0.65)
                    align(0.5, 1.0)
                    background None
                    grid 3 1:
                        spacing 24
                        frame:
                            background RoundRect("#3f3f3f")
                            mousearea:
                                area(0, 0, 1.0, 1.0)
                                # 不使用transition的原因是前一个动画没放完，后一个就不会播放，快速滑过后视觉效果很差
                                #hovered ShowTransient("cd",transition=moveinbottom,cd_name="gj",x=1)
                                if sy in 可操友队 and sy not in 待执行操作列表[0]:
                                    hovered  ShowTransient("cd_gj",dqxz=team_y[sy],team_d=team_d,team_y=team_y,sy=sy)
                                #unhovered Hide("cd_gj", transition=moveoutbottom)
                            yfill True
                            xsize(0.32)
                            imagebutton:
                                if sy in 可操友队 and sy not in 待执行操作列表[0]:
                                    idle "atk_button_idle"
                                    action ShowTransient("cd_gj",dqxz=team_y[sy],team_d=team_d,team_y=team_y,sy=sy)
                                else:
                                    idle "no_atk_button"
                                    action Function(定义消息,turns=store.turns,t="本回合已操作",c=1)
                                align(0.5,0.5) 
                                
                        frame:
                            background RoundRect("#3f3f3f")
                            mousearea:
                                area(0, 0, 1.0, 1.0)
                                #hovered ShowTransient("cd",transition=moveinbottom,cd_name="jn",x=1)
                                hovered ShowTransient("cd_jn")
                                #unhovered Hide("cd_jn", transition=moveoutbottom)
                            yfill True
                            xsize(0.32)
                            textbutton "技能":
                                text_size 50
                                align(0.5,0.5)
                                action ShowTransient("cd_jn")
                        frame:
                            background RoundRect("#3f3f3f")
                            mousearea:
                                area(0, 0, 1.0, 1.0)
                                #hovered ShowTransient("cd",transition=moveinbottom,cd_name="tp",x=1)
                                hovered ShowTransient("cd_tp",transform=moveinbottom,team_d=team_d,team_y=team_y,sy=sy)
                                #unhovered Hide("cd_tp", transition=moveoutbottom)
                            yfill True
                            xsize(0.32)
                            textbutton "逃跑":
                                
                                text_size 50
                                align(0.5,0.5)
                                action ShowTransient("cd_tp")
screen cd_gj(dqxz,team_d,team_y,sy,turns=turns):
    modal 0
    frame:
        background None
        ysize(.17)
        xsize(.64)
        align(0.5, 0.977)
        frame:
            background RoundRect("#3f3f3f")
            xsize(.34)
            yfill 1
            mousearea:
                area(0, 0, 1.0, 1.0)
                unhovered Hide("cd_gj")
            vpgrid:
                cols 3
                rows 3
                for i in range(len(dqxz["atk_method"])):
                    add make_skill_button(dqxz,index=i,team_d=team_d, team_y=team_y, sy=sy)
                textbutton "取消":
                    action Hide("cd_gj")
    $ tooltip = GetTooltip()
    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True
            frame:
                xalign 0.5
                text tooltip
init python:
    def make_skill_button(dq, index,team_d, team_y, sy):
        name = dq.getjnname(index)
        desc = dq.getstrjnxg(index)
        return TextButton(
            name,
            tooltip=desc,
            clicked=ShowTransient("cd_gj2", team_d=team_d, jn=index, team_y=team_y, sy=sy)
        )
    def make_sr_button(mb,team_d,jn,team_y,sy,turns):
        name = team_d[mb]['name']
        desc = "" if team_d[mb]['life'] else "已死亡"
        return TextButton(
            name,
            tooltip=desc,
            hovered=SetVariable("sd",mb),
            clicked=[Hide("cd_gj2"),Hide("cd_gj"),Function(前置判断,待执行操作列表=待执行操作列表,友队=team_y,角色下标=sy,目标下标=mb,操作下标=jn,敌队=team_d,回合数=turns)])
screen cd_gj2(team_d,jn,team_y,sy,turns=turns):
    frame:
        background None
        ysize(.17)
        xsize(.64)
        align(0.5, 0.977)
        frame:
            background RoundRect("#3f3f3f")
            xsize(.34)
            yfill 1
            mousearea:
                area(0, 0, 1.0, 1.0)
                unhovered Hide("cd_gj2")
            vpgrid:
                cols 3
                rows 3
                for i in range(len(team_d)):
                    add make_sr_button(mb=i,team_d=team_d,jn=jn,team_y=team_y,sy=sy,turns=turns)
                textbutton "取消":
                    action Hide("cd_gj2")
    $ tooltip = GetTooltip()
    if tooltip:
        nearrect:
            focus "tooltip"
            prefer_top True
            frame:
                xalign 0.5
                text tooltip
screen cd_jn:
    modal 0
    frame:
        background None
        ysize(.17)
        xsize(.64)
        align(0.5, 0.977)
        frame:
            background RoundRect("#3f3f3f")
            xalign(0.5)
            xsize(.34)
            yfill 1
            mousearea:
                area(0, 0, 1.0, 1.0)
                #hovered ShowTransient("cd",transition=moveinbottom,cd_name="gj",x=1)
                unhovered Hide("cd_jn")
            textbutton "治疗":
                action [Hide("cd_jn"),Function(定义消息,turns=store.turns,t="功能没写doge",c=1)]
screen cd_tp:
    modal 0
    frame:
        background None
        ysize(.17)
        xsize(.64)
        align(0.5, 0.977)
        frame:
            xalign(1.0)
            xsize(.34)
            yfill 1
            mousearea:
                area(0, 0, 1.0, 1.0)
                #hovered ShowTransient("cd",transition=moveinbottom,cd_name="gj",x=1)
                unhovered Hide("cd_tp")
            textbutton "逃跑":
                action [SetVariable("battle_jg","tp"),Jump("zdjs")]
screen popup_screen(texts):
    modal True  # 阻止与背景交互
    
    frame:
        background Solid("#000000", alpha=0.7)
        xysize (850, 600)
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 5
            xalign 0.5
            yfill True
            xfill True
            frame:
                xfill True
                yfill True
                background None
                vbox:
                    xfill True
                    xalign 0.5
                    text "[texts[0]]" size 40 color "#ffffff" xalign 0.5 yalign 0.0
                    grid 1 2:
                        xalign 0.5
                        yfill True
                        if(texts[1]):
                            vbox:
                                xfill True
                                text "友方行动" size 30 color "#0f0" xalign 0.5
                                for value in texts[1]:
                                    text "[value]" size 25 color "#fff" xalign 0.5
                        if(texts[2]):
                            vbox:
                                xfill True
                                text "敌方行动" size 30 color "#f00" xalign 0.5
                                for value in texts[2]:
                                    text "[value]" size 25 color "#fff" xalign 0.5
                        if(texts[3]):
                            vbox:
                                xfill True
                                text "注意" size 35 color "#ff0000" xalign 0.5
                                for value in texts[3]:
                                    text "[value]" size 30 color "#fff" xalign 0.5

                textbutton "——————点击关闭——————":
                    align(0.5,1.0)
                    action If(store.battle_jg!="",[Hide("mycc_screen"),Hide("popup_screen"),Jump("zdjs")],Hide("popup_screen"))