名字_path='D:\\不会编程\\python\\实验文件夹\\信息2.txt'
姓_path='D:\\不会编程\\python\\实验文件夹\\自己的第一个py库的有关信息文档.txt'
姓=[]
单字名=[]
双字名=[]
with open(姓_path,"r",encoding='utf-8') as x:
    for line in x.readlines():
        姓.extend(line.strip().split('、'))

with open(名字_path,"r",encoding='utf-8') as mz:
    for line in mz.readlines():
        if len(line.split('\n')[0])==1:
            单字名.append(line.split('\n')[0])
        else :
            双字名.append(line.split('\n')[0])

tuple(姓)
tuple(单字名)
tuple(双字名)

import random
class FakeUser:
    def fakename(self,account=1,oneword=False,twoword=False):
        n=0
        while n<=account:
          if oneword:
             full_name=random.choice(姓)+random.choice(单字名)
          elif twoword:
             full_name=random.choice(姓)+random.choice(双字名)
          else :
             full_name=random.choice(姓)+random.choice(双字名+单字名)
          yield full_name
          n+=1
    def fake_gender(self,account=1):
        n=0
        while n<=account:
            gender=random.choice(['男','女','未知'])
            yield gender
            n += 1


class SnsUser(FakeUser):
    def get_followers(self,few=True,a_lot=False,account=1):
        n=0
        while n<=account:
            if few:
               followers=random.randrange(1,50)
            else :
               followers=random.randrange(200,10000)
            yield followers
            n+=1
user_a=FakeUser()
user_b=SnsUser()
for name in user_a.fakename(30):
    print(name)
for gender in user_a.fake_gender(30):
    print(gender)
for follower in user_b.get_followers(few=True,account=30):
    print(follower)


