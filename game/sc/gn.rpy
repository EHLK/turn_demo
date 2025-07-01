init python:
    # texts = [回合数,[友方战斗信息],[敌方战斗信息],[其他提示信息]]
    # c定义后不发送，c定义后发送 str原信息
    def 定义消息(turns=None,olds:list=[],y="",d="",t="",c=0):
        texts=[0,[],[],[]]
        if olds:
            texts=olds
            if turns:
                olds[0]="第"+str(turns)+"回合"
            else:
                olds[0]="第"+str(store.turns)+"回合"
        else:
            texts[0]="第"+str(store.turns)+"回合"
        if y != "":
            texts[1].append(y)
        if d != "":
            texts[2].append(d)
        if t != "":
            texts[3].append(t)
        if c==1:
            store.dmsg=texts
            show_popup(texts)
        else:
            store.dmsg=texts
            return texts
    # 战斗信息弹窗
    def show_popup(message):
        renpy.show_screen("popup_screen",texts=message)
    # 回合机制判断
    def 回合计算(待执行操作列表,回合数,友队,敌队):
        # 初始化处理
        tempmessage = 定义消息(turns=回合数)
        # 伤害计算及信息计算
        #  友方行动
        tempmessage = 伤害结算(待执行操作列表,友队,敌队,回合数,tempmessage,yd=1)
        #   重置友方意图队列
        store.待执行操作列表 = [[],[],[]]
        #  敌方行动
        tempmessage = 敌方行动(敌队,友队,回合数,tempmessage)
        定义消息(turns=回合数,olds=tempmessage,c=1)
        if 全死判断(友队):
            store.battle_jg = "lose"
            renpy.hide_screen("mycc")
        if  全死判断(敌队):
            store.battle_jg = "win"
        store.turns = 回合数 +1
    # 0 角色下标 1 操作下标 2 操作目标
    # 待执行操作列表=[[],[],[]]
    def 伤害结算(待执行操作列表,友队,敌队,回合数,消息队列,yd=1):
        xxtemp = {
            'turns':回合数,
            'c':0,
        }
        texts = 消息队列
        for i in range(len(待执行操作列表[0])):
            if yd==1:
                y=伤害计算(友队,待执行操作列表[0][i],待执行操作列表[1][i],敌队,待执行操作列表[2][i])
                texts=定义消息(y=y,olds=texts,**xxtemp)
            else:
                d=伤害计算(友队,待执行操作列表[0][i],待执行操作列表[1][i],敌队,待执行操作列表[2][i])
                texts=定义消息(d=d,olds=texts,**xxtemp)
        return texts

    def 前置判断(待执行操作列表,友队,角色下标,目标下标,操作下标,敌队,回合数):
        添加操作(待执行操作列表,角色下标,操作下标,目标下标)
        if len(待执行操作列表[0]) == len(存活下标(友队)):
            battlejg = 回合计算(待执行操作列表,回合数,友队,敌队)
            if battlejg == 0:
                store.battle_jg = "lose"
                renpy.jump("zdjs")
            elif battlejg == 1:
                store.battle_jg = "win"
                renpy.jump("zdjs")
    def 添加操作(待执行操作列表,角色下标,操作下标,目标下标):
        待执行操作列表[0].append(角色下标)
        待执行操作列表[1].append(操作下标)
        待执行操作列表[2].append(目标下标)
    def 可操作下标列表(dw,已操角色):
        # 没有操作过并且存活   ↑列表
        dl = []
        for i in 存活下标(dw):
            if i not in 已操角色:
                dl.append(i)
        return dl
    def 存活下标(队伍):
        dl = []
        for i in range(len(队伍)):
            if 队伍[i]["life"]:
                dl.append(i)
        return dl
    def 伤害计算(友队,友下标,技能,敌队,目标):
        sh,hp = 友队[友下标].gjsh(技能)
        敌队[目标].change_hp(-sh)
        友队[友下标].change_hp(hp)
        if hp >0:
            return f"{友队[友下标]['name']} 使用 {友队[友下标].getjnname(技能)} 对 {敌队[目标]['name']} 造成了 {sh:.2f} 点伤害，恢复了 {hp:.2f} 点生命值。"
        return f"{友队[友下标]['name']} 使用 {友队[友下标].getjnname(技能)} 对 {敌队[目标]['name']} 造成了 {sh:.2f} 点伤害"
    # 如果都死了，就结束
    def 全死判断(友队):
        if 存活下标(友队):
            return False
        return True
    def 敌方行动(敌队,友队,回合数,消息队列):
        操作列表 = [[],[],[]]
        for i in range(len(存活下标(敌队))):
            a,b,c = 敌方意图(敌队,友队,操作列表)
            添加操作(操作列表,a,c,b)
        return 伤害结算(操作列表,敌队,友队,回合数,消息队列,yd=0)

    def 敌方意图(敌队,友队,操作队列):
        # 敌方存活单位随机选择一个没死的友方单位
        ch=可操作下标列表(敌队,操作队列[0])
        mb=存活下标(友队)
        i = renpy.random.choice(存活下标(敌队))
        a=renpy.random.choice(ch) # 角色下标
        b=renpy.random.choice(mb) # 角色下标
        c=renpy.random.randint(0,(len(敌队[i]["atk_method"])-1)) # 攻击方式下标
        return a,b,c
    def 添加队列(队伍,添加的角色):
        队伍.append(添加的角色)
