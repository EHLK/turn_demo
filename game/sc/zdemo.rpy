# debug临时定义使用
# default turns = 0
default def_y_team = [{"name": "队友1", "hp": 30, "atk": 10},{"name": "队友2", "hp": 45, "atk": 8}]
default battle_flag = True
default def_d_team = {"name": "敌人1", "hp": 60, "atk": 10},{"name": "敌人2", "hp": 45, "atk": 13}
default temp = 1
default count = 1

screen mycc(team_cy=[],team_cd=[]):
    # 初始值
    python:
        # 回合数
        turns = 1
        # 复制传入的参数，预想是team的形式为全局，直接读就行然后，再读取相应角色的属性，但demo懒得做，直接传入参数了
        y_team = team_cy
        d_team = team_cd
        # 初始化battle_flag作为值传出或传入，用于判断战斗是否胜利
        battle_flag = True
        # 队友当前选择的角色序号，用做头像占位
        dyc_tx = 0
        # 临时变量用于检查效果
        
        max_temp = 100
    # 背景
    frame:
        background "#dadada"
        # 左边距
        xfill True
        yfill True
        # 顶部信息框
        frame:
            background RoundRect("#3f3f3f")
            xycenter (0.5,0.095)
            xysize(0.98,0.15)  # 减小了信息框因为不想写蓝条了
            # 排版用hbox
            frame:
                #background Solid("#00ff0d")
                background None
                hbox:
                    xfill True
                    yfill True
                    # 顶左 队友数据
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
                            text str((dyc_tx or "1"))  size 100 align(0.5, 0.5)
                            # add Placeholder(base="bg")
                            #offset(10,10)
                        frame:
                            offset(110,58)
                            bar value AnimatedValue(value=temp,range=max_temp,delay=1.0) xysize(400,30):
                                id "my_bar1"
                        hbox:
                            offset(110,0)
                            text "姓名" size 50
                            text "等级1" yalign 1.0 offset(0,-2)
                        textbutton "1111111111":
                            offset(110,60)
                            text_size 20
                            text_outlines [(absolute(2), "#effdff", absolute(0), absolute(0))]
                            text_color "#000000"
                            text_selected_color "#7573f5"
                            hovered SetVariable("temp",80)
                            unhovered SetVariable("temp",50)
                            action SetVariable("temp",30)
                    frame:
                        background None
                        xsize 0.33
                        xfill True
                        align(0.5, 0.0)
                    # 顶中 回合数
                        frame:
                            align(0.5, 0.5)
                            background RoundRect("#ff0000")
                            text "{color=#BF3512}{size=50}{b}回合 [turns] [count]"
                    # 顶右 敌人数据
                    frame:
                        # 用该方法右边会比左边多部分像素
                        xsize 1.0
                        #xfill True
                        background None
                        align(0.5, 0.0)
                        xfill True
                        # 头像
                        frame:
                            align(1.0,0.0)
                            xfill True
                            yfill True
                            xysize(100,100)
                            # 头像占位
                            text str((dyc_tx or "1"))  size 100 align(0.5, 0.5)


# 抖动动画
transform shake:
    on show:
        repeat True
        linear 0.05 xoffset -2
        linear 0.05 xoffset +4
        linear 0.05 xoffset -4
        linear 0.05 xoffset +2
        set xoffset 0
        jump_out
# demo 函数
python:
    def shake_demo():
        
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