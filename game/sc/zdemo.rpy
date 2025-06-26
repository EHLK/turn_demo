# debug临时定义使用
# default turns = 0
default def_y_team = [{"name": "队友1", "hp": 30, "atk": 10},{"name": "队友2", "hp": 45, "atk": 8}]
default battle_flag = True
default def_d_team{"name": "敌人1", "hp": 60, "atk": 10},{"name": "敌人2", "hp": 45, "atk": 13}
screen mycc(team_cy=[],team_cd=[]):
    # 初始值
    python:
        # 回合数
        turns = 0
        # 传入的参数预定义，预想是team的形式为全局，直接读就行然后，再读取相应角色的属性，但demo懒得做，直接传入参数了
        team = team_cy
        team_cd = team_cd
        # 初始化battle_flag
        battle_flag = True
    # 背景
    frame:
        background "#dadada"
        # 左边距
        xfill True
        yfill True
        # 顶部信息框
        frame:
            background RoundRect("#3f3f3f")
            xycenter (0.5,0.12)
            xysize(0.98,0.2)
            # 排版用hbox
            hbox:
                # 队友数据
                vbox:
                    xsize 0.4
                    xfill True
                    # 头像
                    frame:
                        xfill True
                        yfill True
                        xysize(100,100)
                        add Placeholder(base="bg")
                        offset(10,10)
                vbox:
                    xsize 0.2
                    xfill True
                # 顶中 回合数
                    frame:
                        align(0.5, 0.5)
                        background RoundRect("#3f3f3f")

                        text "{color=#BF3512}{size=50}{b}回合 [turns]"
                            
                # 敌人数据


                    
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