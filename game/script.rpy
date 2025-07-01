# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
define a = Character("阿卡丽", color = (255, 0, 0))
define e = Character("艾琳")
define z = Character("zed",color = (0, 255, 0))
# 游戏在此开始。 
default battle_jg = ""
init python:
    # 循环取出列表中的元素，结合为字符串输出
    def p_list(list):
        ol = ""
        for i in list:
            ol += str(i["name"]) + "、"
        return ol.rstrip("、")
    # 定义一些初始变量
    player_team = [{"name": "队友1", "hp": 30, "atk": 10}, {"name": "队友2", "hp": 45, "atk": 8}]
    enemies = [{"name": "敌人1", "hp": 60, "atk": 10},{"name": "敌人2", "hp": 45, "atk": 13}]  # 由战斗函数传入
    current_actor = None  # 当前操作角色
    target = None  # 当前选定目标

label start:
    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    scene bg room

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    show eileen happy

    # 此处显示各行对话。

    e "你叫什么？"
    $ z.name = renpy.input("请输入昵称") or "zed"
    # 弹出一个输入框，等待用户输入。
    z "我好像叫[z.name]"
    hide eileen
    z "战斗不支持回滚操作，但也没禁用回滚，回滚会导致需要重新打"
    call zlyc
    z "demo结束"
    return
label zlyc:
    python:
        duiyou1=j_data("小黄")
        z.sx=j_data(name=z.name)
        lkd = j_data(name="LK",hp=200,atk=33,atk_method=[{"普通攻击1":{"dam":1,"multipler":1,"bloodsuck":0.0}},{"强力一击1":{"dam":5,"multipler":1.1,"bloodsuck":.0}},{"吸血":{"dam":3,"multipler":1.0,"bloodsuck":.3}}])
        duiyou2 = j_data(name="队友2",hp=10,atk=12,atk_method=[{"普通攻击2":{"dam":1,"multipler":1,"bloodsuck":0.0}},{"强力一击2":{"dam":5,"multipler":1.1,"bloodsuck":.0}},{"吸血":{"dam":3,"multipler":1.0,"bloodsuck":.3}}])
        duiyou2.setatk_method(js="吸血")
        dr1 = j_data(name="敌人1",hp=60,atk=18)
        dr2 = j_data(name="敌人2",hp=80,atk=13)
        dr3 = j_data(name="敌人3",hp=100,atk=15)
        dr5 = j_data(name="敌人5",hp=120,atk=10)
    menu:
        "想要几个队友？几个敌人？\n我就写了四套"
        "3队友,4敌人":
            python:
                dy_duilie = [z.sx,lkd,duiyou2]
                dr_duilie = [dr1,dr2,dr3,j_data(name="敌人4",hp=100,atk=10)]
        "4队友,3敌人":
            python:
                dy_duilie = [z.sx,lkd,duiyou2,duiyou1]
                dr_duilie = [dr1,dr2,dr3,j_data(name="敌人4",hp=100,atk=10)]
        "2队友,2敌人":
            python:
                dy_duilie = [z.sx,lkd]
                dr_duilie = [dr1,dr2]
        "1队友,2敌人":
            python:
                dy_duilie = [z.sx]
                dr_duilie = [dr1,dr2]
    
    #e "您将遇到的敌人为[p_list(dr_duilie)]"
    #$ quick_menu = False # 将快捷菜单栏隐藏
    #z "[jssj.zjdata.name]"
    $ renpy.call("mycc",team_cy=dy_duilie,team_cd=dr_duilie)
    return

label zdjs:
    if battle_jg == "tp":
        z "逃掉了"
    elif battle_jg == "win":
        z "战斗胜利"
    elif battle_jg == "lose":
        z "战斗失败"
    menu:
        "再来一次吗？"
        "来":
            jump zlyc
        "不":
            "战斗结束"
    z "[battle_jg]"
    return
