# 各种数据(废弃,仅主角数据有效)
python:
    # 通用模版
    class j_data:
        def __init__(self,name="未命名",hp = 100,atk = 10,mp = 100):
            self.name = name
            self.hp = hp
            self.atk = atk
            self.mp = mp
            self.life = 1
        # 血量增减
        def change_hp(self,num):
            self.hp = max(0,self.hp + num)
            if self.hp == 0:
                self.life = 0
        # 存活判断
        def is_alive(self):
            return self.life==1
    # 角色模版
    class h_data(j_data):
        def __init__(self,name = "英雄的名字",hp = 100,atk = 20,mp = 100):
            super().__init__(name=name, hp=hp, atk=atk, mp=mp)
            z.name = name
    # 敌人模版
    class e_data(j_data):
        def __init__(self,name = "敌人",hp = 100,atk = 100,mp=0):
            super().__init__(name=name, hp=hp, atk=atk, mp=mp)
    
        