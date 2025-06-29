# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。
define a = Character("阿卡丽", color = (255, 0, 0))
define e = Character("艾琳")
define z = Character("zed",color = (0, 255, 0))
# 游戏在此开始。 
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
    python:
        dy1_duilie = [{"name": "队友1", "hp": 30,"max_hp":100 ,"atk": 10},{"name": "队友2", "hp": 45, "max_hp":100 ,"atk": 8}]
        z.sx=j_data(name=z.name)
        lkd = j_data(name="LK",hp=200,atk=23)
        duiyou2 = j_data(name="队友2",hp=100,atk=12)
        dy_duilie = [z.sx,lkd,duiyou2]
        #e "您当前队伍中有[p_list(dy_duilie)]"
        #dr_duilie = [{"name": "敌人1", "hp": 60,"max_hp":100 ,"atk": 10},{"name": "敌人2", "hp": 80,"max_hp":100, "atk": 13}]
        dr1 = j_data(name="敌人1",hp=60,atk=18)
        dr2 = j_data(name="敌人2",hp=80,atk=13)
        dr3 = j_data(name="敌人3",hp=100,atk=15)
        dr4 = j_data(name="敌人4",hp=120,atk=10)
        dr_duilie = [dr1,dr2,dr3,j_data(name="敌人4",hp=120,atk=10)]
    #e "您将遇到的敌人为[p_list(dr_duilie)]"
    #$ quick_menu = False # 将快捷菜单栏隐藏
    z "暂停并保存查看一下变量是否被保存"
    #z "[jssj.zjdata.name]"
    call mycc(dy_duilie,dr_duilie)
    z "充满疑问"
    return

