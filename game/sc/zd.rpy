default xuanz = 0  # 控制界面按钮的使用
default zhandou_time = 0   # 战斗回合数
 
# 敌方和我方的各项数值均采用浮点数，使用round保留一位小数（直接去掉尾部）
default gamer_xue = 500.00 # 玩家血量
default gamer_gong = 100.00 # 玩家攻击力
default gamer_fang = 50.00 # 玩家防御力
default gamer_fang_max = 100.00 # 玩家防御力上限
default gamer_xue_max = 500.00 # 玩家血量上限
 
default npc_name = ""  # 敌方名字
default npc_xue = 0.00 # 敌方血量
default npc_gong = 0.00 # 敌方攻击力
default npc_fang = 0.00 # 敌方防御力
 
screen zhandou():
    # 轮到玩家的战斗回合时，玩家会来到这个界面选择行为
    # 显示战斗回合数
    text "{color=#BF3512}{size=50}{b}战斗回合数   [zhandou_time]":
        xycenter(0.1,0.59)
        
    frame:
        xycenter(0.5,0.8)
        xysize(1920,400)
        hbox:
            ycenter 0.12
            xpos 0.05
            # 显示玩家和敌方的各项数值
            vbox:
                text "[persistent.gamer_name]的角色信息{space=30}"
                text "[npc_name]的角色信息{space=30}"
            vbox:
                text "血量[gamer_xue]{space=30}"
                text "血量[npc_xue]{space=30}"
            vbox:
                text "攻击力[gamer_gong]{space=30}"
                text "攻击力[npc_gong]{space=30}"
            vbox:
                text "防御力[gamer_fang]{space=30}"
                text "防御力[npc_fang]{space=30}"
        vbox:
            xycenter(0.07,0.5)
            # 点击按钮，显示各种行为的具体行为
            textbutton "{size=40}攻击":
                # 控制按钮的选择，如果不使用会导致玩家可以打开多个界面
                if xuanz == 0 or xuanz == 1:
                    # 将其他按钮锁定，并临时打开一个界面
                    action [SetVariable("xuanz",1),ShowTransient("gongji")]
            textbutton "{size=40}防御":
                if xuanz == 0 or xuanz == 2:
                    action [SetVariable("xuanz",2),ShowTransient("fangyu")]
            textbutton "{size=40}治疗":
                if xuanz == 0 or xuanz == 3:
                    action [SetVariable("xuanz",3),ShowTransient("zhiliao")]
 
screen gongji():
    # 攻击行为的界面
    frame:
        xycenter(0.5,0.83)
        xysize(1080,300)
 
        textbutton "{size=50}削韧型攻击":
            xycenter(0.15,0.2)
            action [SetVariable("xuanz",0),    # 让所有按钮都可以选择
                    SetVariable("zhandou_time",zhandou_time+1), # 使战斗回合数+1
                    Jump("jisuan_削韧型攻击"), # 跳到该行为的计算过程
                    Hide("gongji")]            # 关闭当前界面
 
        # 让所有按钮都可以选择，并关闭当前界面
        textbutton "返回":
            xycenter(0.95,0.9)
            action [SetVariable("xuanz",0),Hide("gongji")]
 
# 之后的内容就都是类似的了
 
screen fangyu():
    # 防御行为的界面
    frame:
        xycenter(0.5,0.83)
        xysize(1080,300)
        # 如果防御大于等于上限时就无法使用
        if gamer_fang < gamer_fang_max:
            textbutton "{size=50}常规型防御":
                xycenter(0.15,0.2)
                action [SetVariable("xuanz",0),
                        SetVariable("zhandou_time",zhandou_time+1),
                        Jump("jisuan_常规型防御"),
                        Hide("fangyu")]
        elif gamer_fang >= gamer_fang_max:
            text "{size=50}{i}防御已达到最大值":
                xycenter(0.5,0.5)
         
        textbutton "返回":
            xycenter(0.95,0.9)
            action [SetVariable("xuanz",0),Hide("fangyu")]
 
screen zhiliao():
    # 治疗行为的界面
    frame:
        xycenter(0.5,0.83)
        xysize(1080,300)
        # 如果血量大于等于上限时就无法使用
        if gamer_xue < gamer_xue_max:
            textbutton "{size=50}防御型治疗":
                xycenter(0.15,0.2)
                action [SetVariable("xuanz",0),
                        SetVariable("zhandou_time",zhandou_time+1),
                        Jump("jisuan_防御型治疗"),
                        Hide("zhiliao")]
        elif gamer_xue >= gamer_xue_max:
            text "{size=50}{i}血量已达到最大值":
                xycenter(0.5,0.5)
 
        textbutton "返回":
            xycenter(0.95,0.9)
            action [SetVariable("xuanz",0),Hide("zhiliao")]
 
# 各类行为的计算过程我写的都有些复杂，如果是第一次尝试可以试着用更简单的计算方法
label jisuan_削韧型攻击:
    # “削韧型攻击”的计算过程
    if gamer_gong > npc_fang:
        # 当玩家攻击力大于敌方防御力时
        centered "{size=80}{color=#BF3512}{b}对[npc_name]造成了[round((gamer_gong-npc_fang),1)]点的伤害，并造成[round((npc_fang * 0.05),1)]点削韧！{nw=10}"
        $ npc_xue = round(npc_xue + (npc_fang - gamer_gong),1)
        $ npc_fang = round(npc_fang - (npc_fang * 0.05),1)
    elif gamer_gong <= npc_fang:
        # 当玩家攻击力小于等于敌方防御力时
        centered "{size=80}{color=#BF3512}{b}对[npc_name]造成了[round((npc_fang*0.2),1)]点的削韧！{nw=10}"
        $ npc_fang = round(npc_fang - (npc_fang * 0.2),1)
        if gamer_gong > npc_fang:
            # 当此次攻击使敌方防御力低于玩家攻击力时
            centered "{size=80}{color=#BF3512}{b}成功将[npc_name]破韧！{nw=10}"
 
    if npc_xue <= 0:
        # 当此次攻击使敌方血量小于等于0时
        centered "{size=80}{color=#BF3512}{b}[npc_name]已经被你击败！{nw=10}"
        return
     
    # 玩家行动回合结束，跳转到敌方的行动回合
    jump npc_jisuan
 
label jisuan_常规型防御:
    centered "{size=80}{color=#BF3512}{b}回复了[round((gamer_fang*0.2 + gamer_fang_max*0.1),1)]点防御值！{nw=10}"
    $ gamer_fang = round(gamer_fang + (gamer_fang*0.2 + gamer_fang_max*0.1),1)
    if gamer_fang > gamer_fang_max:
        # 当此次回复后的防御力高于上限时，将防御力等于上限
        $ gamer_fang = gamer_fang_max
    jump npc_jisuan
 
label jisuan_防御型治疗:
    centered "{size=80}{color=#BF3512}{b}回复了[round(gamer_xue_max * 0.05 + gamer_xue * 0.05)]点的血量和[round(gamer_xue * 0.01 + gamer_xue_max * 0.01)]点防御！{nw=10}"
    $ gamer_xue = round(gamer_xue + gamer_xue_max * 0.05 + gamer_xue * 0.05)
    $ gamer_fang =  round(gamer_fang + gamer_xue * 0.01 + gamer_xue_max * 0.01)
    if gamer_fang > gamer_fang_max:
        # 当此次回复后的血量高于上限时，将血量等于上限
        $ gamer_fang = gamer_fang_max
    jump npc_jisuan
 
label npc_jisuan:
    # 敌方行为的计算过程
    "接下来是[npc_name]的行动回合！"
    if npc_gong > gamer_fang:
        # 敌方攻击力高于玩家防御力时
        centered "{size=80}{color=#BF3512}{b}[npc_name]对你造成了[round((npc_gong - gamer_fang),1)]点的伤害，并造成[round((gamer_fang * 0.05),1)]点削韧！{nw=10}"
        $ gamer_xue = round(gamer_xue + (gamer_fang - npc_gong),1)
        $ gamer_fang = round(gamer_fang - (gamer_fang * 0.05),1)
    elif npc_gong <= gamer_fang:
        # 敌方攻击力小于等于玩家防御力时
        centered "{size=80}{color=#BF3512}{b}[npc_name]对你造成了[round((npc_fang * 0.2),1)]点的削韧！{nw=10}"
        $ gamer_fang = round(gamer_fang - (gamer_fang * 0.2),1)
        if npc_gong > gamer_fang:
            centered "{size=80}{color=#BF3512}{b}你被绿成功破韧！{nw=10}"
    if gamer_xue <= 0:
        # 玩家血量归零时
        centered "{size=80}{color=#BF3512}{b}菜！{nw=10}"
        return
    else:
        # 敌方行动回合结束，回到玩家的行动回合
        call screen zhandou