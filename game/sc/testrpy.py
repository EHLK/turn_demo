class j_data:
        def __init__(self,name="未命名",hp = 100.0,atk = 10,atk_method = [{"普通攻击":{"dam":1,"damrate":1,"bloodsuck":0.0}},{"强力一击":{"dam":5,"multipler":1.1,"bloodsuck":.0}},{"吸血":{"dam":3,"multipler":1.0,"bloodsuck":.3}}]):
            self.atk_method = atk_method # 攻击方式
            self.name = name # 名字
            self.hp = hp # 当前生命值
            self.max_hp = hp # 最大生命值
            self.atk = atk # 攻击力
            self.life = True # 是否存活

            # 使用magic methods取值
        def __getitem__(self, key):
            # 允许像 a["hp"] 一样访问属性
            try:
                return getattr(self, key)
            except AttributeError:
                raise KeyError(f"对象中不存在键 {key}")
        def change_hp(self,hp:int):
            self.hp += hp
            if self.hp <= 0:
                self.hp = 0
                self.life = 0
            if self.hp>self.max_hp:
                self.hp = self.max_hp
        # 获取技能名字
        def getjnname(self,xb:int):
            temp = self.atk_method[xb].keys()
            return list(temp)[0]
        # 使用字符串返回技能效果字典
        def getstrjnxg(self,xb:int):
            strw = ""
            temp = self.atk_method[xb][self.getjnname(xb)].items()
            for i,w in enumerate(temp):
                if i == 0:
                    strw+= "伤害："+str(w[1]+self.atk)+"\n"
                elif i == 1:
                    strw+= "伤害倍率："+str(w[1])+"\n"
                elif i == 2:
                    strw+= "伤害吸血："+str(w[1])
            return strw
        # 获取技能效果字典
        def getjnxg(self,xb:int):
            temp = self.atk_method[xb].values()
            return list(temp)[0]
        # 获取攻击伤害
        def gjsh(self,xb:int):
            temp = list(self.atk_method[xb][self.getjnname(xb)].values())
            shrw = (self.atk+temp[0])*temp[1]
            return shrw
        # 改值
        def setname(self, name):
            self.name = name
            #return 1 会导致跳出界面
        def sethp(self, hp):
            self.hp = hp
            #return 1
        def setmaxhp(self, maxhp):
            self.maxhp = maxhp
            #return 1
        def setatk(self, atk):
            self.atk = atk
            #return 1
        def setlife(self, life):
            self.life = life
            #return 1
        
        def setatk_method(self,zg=None,js:str=""):
            # demo中不会根据首字母或其他规则进行排序，请自行更改
            # zg操作为增加时，列表可添加多个值，操作为删除时，列表只能删除一个值
            if zg:
                ttemp = None
                pdtemp = False
                if len(zg)==1 and type(zg)==list and type(zg[0])==dict:
                    self.atk_method.append(zg[0])
                if type(zg) == dict:
                    for i,item in enumerate(self.atk_method):
                        if item["name"] == zg["name"]: 
                            self.atk_method[i].update(zg)
                            break # 字典只会有一个，所以找到了就退出
                    self.atk_method.append(zg) # 找不到直接添加就行
                elif len(zg)>=2 and type(zg)==list: # 因为list运行重复值，所以要进行检测
                    deltemp = []
                    for i,item in enumerate(zg):
                        for j,item2 in enumerate(self.atk_method):
                            if item["name"]==item2["name"]: # 找到重复值
                                self.atk_method[j].update(zg[i]) # 更新字典
                                deltemp.append(i) # 记录重复值下标，在循环内删除会导致意料外的结果
                                break
                    zg=[item for i, item in enumerate(zg) if i not in deltemp]
            # 根据name的值删除
            if js:
                for i in range(len(self.atk_method)):
                    if self.getjnname(i)==js:
                        del self.atk_method[i]
b = 10
for i in range(b):
    
    print(b)
    print(i)