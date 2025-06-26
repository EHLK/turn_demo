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
    turn_count = 0  # 回合数
    is_player_turn = True  # 是否玩家回合

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    scene bg room

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    show eileen happy

    # 此处显示各行对话。

    e "你叫什么？"
    $ p_data = hero_data(renpy.input("请输入昵称") or "zed")
    # 弹出一个输入框，等待用户输入。
    z "我好像叫[z.name]"
    hide eileen
    $ dy_duilie = [{"name": "队友1", "hp": 30, "atk": 10},{"name": "队友2", "hp": 45, "atk": 8}]
    #e "您当前队伍中有[p_list(dy_duilie)]"
    $ dr_duilie = [{"name": "敌人1", "hp": 60, "atk": 10},{"name": "敌人2", "hp": 45, "atk": 13}]
    #e "您将遇到的敌人为[p_list(dr_duilie)]"
    $ quick_menu = False # 将快捷菜单栏隐藏
    call screen mycc
    return
