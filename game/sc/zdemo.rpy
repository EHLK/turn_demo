# debug临时定义使用
# default turns = 0
# 使用define的值不能回滚及存档
# 使用default赋值在游戏启动或新游戏加载是定义（前提是未被定义过）
#default def_y_team = [{"name": "队友1", "hp": 30, "atk": 10},{"name": "队友2", "hp": 45, "atk": 8}]
#default def_d_team = [{"name": "敌人1", "hp": 60, "atk": 10},{"name": "敌人2", "hp": 45, "atk": 13}]

label mycc(team_cy=[],team_cd=[]):
    # 初始值
    python:
        quick_menu = False
        # 回合数
        turns = 1
        # 复制传入的参数，预想是team的形式为全局，直接读就行然后，再读取相应角色的属性，但demo懒得做，直接传入参数了
        # 初始化battle_flag作为值传出或传入，用于判断战斗是否胜利
        battle_flag = True
        # 队友当前选择的角色序号，用做头像占位
        dyc_tx = 0
        # 临时变量用于检查效果
        temp = 100
        max_temp = 100
        # 当前选择的敌人，默认第一个
        sd= 0
        # 当前选择的角色，默认第一个
        sy= 0

    call screen mycc_screen(team_cy,team_cd)
    return
# 使用python防止场景预加载


screen mycc_screen(team_y=[],team_d=[]):
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
                                # add text_demo()可以用来显示血量
                            textbutton "[team_y[0]['hp']]":
                                offset(110,60)
                                text_size 20
                                text_outlines [(absolute(2), "#effdff", absolute(0), absolute(0))]
                                text_color "#000000"
                                text_selected_color "#7573f5"
                                hovered SetVariable("team_y[0]['hp']",50)
                                unhovered SetVariable("temp",50)
                                #action SetVariable("team_y[0]['hp']",30)
                                #action Function(ChangeValue,team=team_y,amount = -10) 错误用法
                                action Function(team_y[0].sethp,30)
                        frame:
                            background None
                            xsize 0.33
                            xfill True
                            align(0.5, -0.2)
                        # 顶中 回合数
                            frame:
                                align(0.5, 0.5)
                                background RoundRect("#ff0000")
                                text "{color=#BF3512}{size=50}{b}回合 [turns]"
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
                        $ test_team = [{"name":"1","hp":100},{"name":"2","hp":100}]
                        vpgrid:
                            spacing 10
                            xsize(300)
                            cols 1 # 列数
                            rows len(team_y) # 行数
                            for a,t_c in enumerate(team_y):
                                $ name = t_c['name'] # 不定义该局部变量会导致所有角色名一样
                                $ hp = t_c['hp']
                                $ max_hp = t_c['max_hp']
                                frame:
                                    # background None
                                    button:
                                        vbox:
                                            text "[name]" size 30 align(0.5, 0.5)
                                            bar value AnimatedValue(hp,max_hp,1.0) xsize(270)
                                        action SetVariable("sy",a)
                                    #vbox:
                                    #    text "[name]"
                                    #    bar value AnimatedValue(hp,100,1.0) xsize(280)
                            #add build_bpgrid_list(team_y)
                            #AnimatedValue(value=team_d[sd]["hp"],range=team_d[sd]["max_hp"]
                            
                            #add ["text '1'","text '2'"]

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
                            mousearea:
                                area(0, 0, 1.0, 1.0)
                                # 不使用transition的原因是前一个动画没放完，后一个就不会播放，快速滑过后视觉效果很差
                                #hovered ShowTransient("cd",transition=moveinbottom,cd_name="gj",x=1)
                                hovered  ShowTransient("cd_gj",)
                                #hovered function()
                                #unhovered Hide("cd_gj", transition=moveoutbottom)
                            yfill True
                            xsize(0.32)
                            textbutton "攻击": # 防止手机玩家弄不出来
                                text_size 50
                                align(0.5,0.5)
                                action ShowTransient("cd_gj",dqxz = team_y[sy])
                        frame:
                            mousearea:
                                area(0, 0, 1.0, 1.0)
                                #hovered ShowTransient("cd",transition=moveinbottom,cd_name="jn",x=1)
                                hovered ShowTransient("cd_jn")
                                #unhovered Hide("cd_jn", transition=moveoutbottom)
                            yfill True
                            xsize(0.32)
                            textbutton "技能": # 防止手机玩家弄不出来
                                text_size 50
                                align(0.5,0.5)
                                action ShowTransient("cd_jn")
                        frame:
                            mousearea:
                                area(0, 0, 1.0, 1.0)
                                #hovered ShowTransient("cd",transition=moveinbottom,cd_name="tp",x=1)
                                hovered ShowTransient("cd_tp",transform=moveinbottom)
                                #unhovered Hide("cd_tp", transition=moveoutbottom)
                            yfill True
                            xsize(0.32)
                            textbutton "逃跑": # 防止手机玩家弄不出来
                                text_size 50
                                align(0.5,0.5)
                                action ShowTransient("cd_tp")
                            
init python:
    def build_bpgrid_list(team):
        items = []
        for char in team:
            name = char['name']
            hp = char['hp']
            # 创建一个 vbox
            max_hp = char['max_hp']
            bar_temp = bar(value=AnimatedValue(value=hp,range=max_hp,delay=1.0))
    def test_text(team):
        #grid_temp = vpgrid()
        #addtest = Frame(Solid("#fff"))
        for char in team:
            name = char['name']
            hp = char['hp']
            max_hp = char['max_hp']
            bar_temp = Bar(value=AnimatedValue(value=hp,range=max_hp,delay=1.0))
            #fr.add_all(bar_temp)
            return bar_temp
    pass

screen cd(cd_name,x):
    modal 0
    frame:
        background None
        ysize(.17)
        xsize(.64)
        align(0.5, 0.977)
        if cd_name == "gj":
            frame:
                xsize(.34)
                yfill 1
                mousearea:
                    area(0, 0, 1.0, 1.0)
                    #hovered ShowTransient("cd",transition=moveinbottom,cd_name="gj",x=1)
                    unhovered Hide("cd", transition=moveoutbottom)
                textbutton "普通攻击":
                    action [Hide("cd")]
                    tooltip "没有伤害"
        elif cd_name == "jn":
            frame:
                xalign(0.5)
                xsize(.34)
                yfill 1
                mousearea:
                    area(0, 0, 1.0, 1.0)
                    #hovered ShowTransient("cd",transition=moveinbottom,cd_name="gj",x=1)
                    unhovered Hide("cd", transition=moveoutbottom)
                textbutton "占位字2":
                    action [Hide("cd")]
        elif cd_name == "tp":
            frame:
                xalign(1.0)
                xsize(.34)
                yfill 1
                mousearea:
                    area(0, 0, 1.0, 1.0)
                    #hovered ShowTransient("cd",transition=moveinbottom,cd_name="gj",x=1)
                    unhovered Hide("cd", transition=moveoutbottom)
                textbutton "占位字3":
                    action [Hide("cd")]
        else:
            frame:
                mousearea:
                    area(0, 0, 1.0, 1.0)
                    #hovered ShowTransient("cd",transition=moveinbottom,cd_name="gj",x=1)
                    unhovered Hide("cd", transition=moveoutbottom)
                xsize(1.0)
                textbutton "非法字符":
                    action [Hide("cd")]
# 将上面的screen分割
screen cd_gj(dqxz):
    modal 0
    frame:
        background None
        ysize(.17)
        xsize(.64)
        align(0.5, 0.977)
        frame:
            xsize(.34)
            yfill 1
            mousearea:
                area(0, 0, 1.0, 1.0)
                unhovered Hide("cd_gj")
            hbox:
                for i in enumerate(dqxz):
                textbutton "普通攻击":
                    action [Hide("cd_gj")]
                textbutton "特殊攻击":
                    action [Hide("cd_gj")]
screen cd_jn:
    modal 0
    frame:
        background None
        ysize(.17)
        xsize(.64)
        align(0.5, 0.977)
        frame:
            xalign(0.5)
            xsize(.34)
            yfill 1
            mousearea:
                area(0, 0, 1.0, 1.0)
                #hovered ShowTransient("cd",transition=moveinbottom,cd_name="gj",x=1)
                unhovered Hide("cd_jn")
            textbutton "占位字2":
                action [Hide("cd_jn")]

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
            textbutton "占位字3":
                action [Hide("cd_tp")]
    $ tooltip = GetTooltip()

    if tooltip:

        nearrect:
            focus "tooltip"
            prefer_top True

            frame:
                xalign 0.5
                text tooltip

screen tooltip_example():
    vbox:
        textbutton "北":
            action Return("n")
            tooltip "去约见北极熊。"

        textbutton "南":
            action Return("s")
            tooltip "前往热带。"

        textbutton "东":
            action Return("e")
            tooltip "我们可以拥抱黎明。"

        textbutton "西":
            action Return("w")
            tooltip "去欣赏最美的日落。"

    $ tooltip = GetTooltip()

    if tooltip:

        nearrect:
            focus "tooltip"
            prefer_top True

            frame:
                xalign 0.5
                text tooltip