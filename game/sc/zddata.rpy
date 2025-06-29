#default z
#default dy1_duilie = [{"name": "队友1", "hp": 30,"max_hp":100 ,"atk": 10},{"name": "队友2", "hp": 45, "max_hp":100 ,"atk": 8}]
#default zjsx=j_data(name=z.name)
#default lkd = j_data(name="LK",hp=200,atk=23)
#default duiyou2 = j_data(name="队友2",hp=100,atk=12)
##default dy_duilie = [z.sx,lkd,duiyou2]
##e "您当前队伍中有[p_list(dy_duilie)]"
##dr_duilie = [{"name": "敌人1", "hp": 60,"max_hp":100 ,"atk": 10},{"name": "敌人2", "hp": 80,"max_hp":100, "atk": 13}]
#default dr1 = j_data(name="敌人1",hp=60,atk=18)
#default dr2 = j_data(name="敌人2",hp=80,atk=13)
#default dr3 = j_data(name="敌人3",hp=100,atk=15)
#default dr4 = j_data(name="敌人4",hp=120,atk=10)
##default dr_duilie = [dr1,dr2,dr3,j_data(name="敌人4",hp=120,atk=10)]

# 各种数据
init python:
    # 通用模版
    class j_data:
        def __init__(self,name="未命名",hp = 100.0,atk = 10,attack_method = [{"普通攻击":{"dam":1,"multipler":1,"bloodsuck":0.0}},{"强力一击":{"dam":5,"multipler":1.1,"bloodsuck":.0}},{"吸血":{"dam":3,"multipler":1.0,"bloodsuck":.3}}]):
            self.attack_method = attack_method # 攻击方式
            self.name = name # 名字
            self.hp = hp # 当前生命值
            self.max_hp = hp # 最大生命值
            self.atk = atk # 攻击力
            self.life = 1 # 是否存活

            # 使用magic methods取值
        def __getitem__(self, key):
            # 允许像 a["hp"] 一样访问属性
            if hasattr(self, key):
                return getattr(self, key)
            raise KeyError(f"对象中不存在键 {key}")
        

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
                    stemp[0] = 1
                elif len(zg)>=2 and type(zg)==list: # 因为list运行重复值，所以要进行检测
                    deltemp = []
                    for i,item in enumerate(zg):
                        for j,item2 in enumerate(self.atk_method):
                            if item["name"]==item2["name"]: # 找到重复值
                                self.atk_method[j].update(zg[i]) # 更新字典
                                deltemp.append(i) # 记录重复值下标，在循环内删除会导致意料外的结果
                                break
                    zg=[item for i, item in enumerate(zg) if i not in deltemp]
                    stemp[0] = 1
            else:
                stemp[0] = 0
            # 根据name的值删除
            if js:
                for i in range(len(self.atk_method)):
                    if js == self.atk_method[i]["name"]:
                        del self.atk_method[i]
                        stemp[1] = 1
                        break
            else:
                stemp[1] = 0
    # 数据模版函数
    
