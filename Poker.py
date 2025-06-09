'''当玩家弃权时，无需再输入“-1”，只需直接按“Enter”键。'''
from random import randint
#判断能否找到：
def found(cards,player,A,B,C,D):
    if player==0:
        tmpA=A
        for card in cards:
            if not card in tmpA:
                return False
            else:
                pos=tmpA.find(card)
                tmpA=tmpA[:pos]+tmpA[pos+1:]
    elif player==1:
        tmpB=B
        for card in cards:
            if not card in tmpB:
                return False
            else:
                pos=tmpB.find(card)
                tmpB=tmpB[:pos]+tmpB[pos+1:]
    elif player==2:
        tmpC=C
        for card in cards:
            if not card in tmpC:
                return False
            else:
                pos=tmpC.find(card)
                tmpC=tmpC[:pos]+tmpC[pos+1:]
    elif player==3:
        tmpD=D
        for card in cards:
            if not card in tmpD:
                return False
            else:
                pos=tmpD.find(card)
                tmpD=tmpD[:pos]+tmpD[pos+1:]
    return True
#判断所出牌各位数字相同：
def same(cards):
    num=len(cards)
    for i in range(1,num):
        if cards[i]!=cards[i-1]:
            return False
    return True
#判断顺子：
def single_shunzi(cards):
    order='3456789TJQKA'
    num=len(cards)
    if num<3:
        return False
    for card in cards:
        if not card in order:
            return False
    for i in range(1,num):
        if order.find(cards[i])!=order.find(cards[i-1])+1:
            return False
    return True
def double_shunzi(cards):
    order='3456789TJQKA'
    num=len(cards)
    if num<6:
        return False
    for card in cards:
        if not card in order:
            return False
    for i in range(0,num-1,2):
        if cards[i]!=cards[i+1]:
            return False
    if cards[-2]!=cards[-1]:
        return False
    for i in range(2,num,2):
        if order.find(cards[i])!=order.find(cards[i-2])+1:
            return False
        return True
#判断炸弹：
def bomb(pre,cur):
    order='3456789TJQKA2SB'
    if len(pre)<len(cur) or single_shunzi(pre) or double_shunzi(pre):
        return True
    elif len(pre)==len(cur) and order.find(pre)<order.find(cur):
        return True
    return False
#判断最初是否可以出牌：
def judge_start(cards):
    if len(cards)==1:
        return True
    elif (len(cards)==2 or len(cards)==3) and same(cards):
        return True
    elif single_shunzi(cards) or double_shunzi(cards):
        return True
    elif len(cards)>=4 and same(cards):
        return True
    return False
#判断是否可以出牌：
def judge(pre,cur):
    order='O3456789TJQKA2SB'
    global num
    if len(cur)>=4 and same(cur):
        return bomb(pre,cur)
    elif len(pre)==1:
        if len(cur)==1 and order.find(cur)>order.find(pre):
            num=1
            return True
    elif len(pre)==2 and same(pre):
        if len(cur)==2 and same(cur) and order.find(cur[0])>order.find(pre[0]):
            num=2
            return True
    elif len(pre)==3 and same(pre):
        if len(cur)==3 and same(cur) and order.find(cur[0])>order.find(pre[0]):
            num=3
            return True
    elif len(pre)>=4 and not (single_shunzi(pre) or double_shunzi(pre)):
        if len(cur)<4:
            return False
    if single_shunzi(pre):
        if len(pre)==len(cur) and single_shunzi(cur) and order.find(cur[0])>order.find(pre[0]):
            return True
    elif double_shunzi(pre):
        if len(pre)==len(cur) and double_shunzi(cur) and order.find(cur[0])>order.find(pre[0]):
            return True
    return False
#双扣的结束条件：
def shuangkou_end(A,B,C,D):
    if len(A)==0:
        if len(C)==0 or len(B)==len(D)==0:
            return True
    elif len(B)==0:
        if len(D)==0 or len(A)==len(C)==0:
            return True
    if len(C)==0:
        if len(A)==0 or len(B)==len(D)==0:
            return True
    elif len(D)==0:
        if len(B)==0 or len(A)==len(C)==0:
            return True
    return False
cards=[];end='not end'
while end!='':
    game_type=int(input('选择类型（输入半角数字）：1、双人；2、斗地主（三人）；3、双扣（四人）：'))
    if game_type==1:
#定义所有的牌：
        for i in range(3,10):
            cards+=[str(i)]*4
        cards+=['T' for i in range(4)]+['J' for i in range(4)]+['Q' for i in range(4)]+['K' for i in range(4)]
        cards+=['A' for i in range(4)]+['2' for i in range(4)]+['S','B']
        print('所有的牌：',cards,'共'+str(len(cards))+'张。')
#分发牌：
        indexA=[]
        for a in range(int(len(cards)/2)):
            temp=randint(0,len(cards)-1)
            while temp in indexA:
                temp=randint(0,len(cards)-1)
            indexA+=[temp]
        indexB=[]
        for b in range(len(cards)):
            if not b in indexA:
                indexB+=[b]
#将牌的索引按从小到大的顺序排序：
        for i in range(len(indexA)-1,0,-1):
            in_order=True
            for j in range(i):
                if indexA[j]>indexA[j+1]:
                    indexA[j],indexA[j+1]=indexA[j+1],indexA[j]
                    in_order=False
            if in_order:
                break
        for i in range(len(indexB)-1,0,-1):
            in_order=True
            for j in range(i):
                if indexB[j]>indexB[j+1]:
                    indexB[j],indexB[j+1]=indexB[j+1],indexB[j]
                    in_order=False
            if in_order:
                break
        print('“10”用“T”代替，“小王”用“S”代替，“大王”用“B”代替。')
        print('请使用半角数字或半角大写英文字母输入所出的牌。')
#将索引与牌对应：
        A=B=''
        print('甲方牌：')
        for a in indexA:
            A+=cards[a]
            print(cards[a],end=',')
        print('共'+str(len(indexA))+'张。')
        print('乙方牌：')
        for b in indexB:
            B+=cards[b]
            print(cards[b],end=',')
        print('共'+str(len(indexB))+'张。')
#分发牌完成，开始：
        pre=input('甲方出牌：')
        while not found(pre,0,A,'','',''):
            print('所出牌中含有不存在的。')
            pre=input('甲方出牌：')
        while not judge_start(pre):
            print('无效。')
            pre=input('甲方出牌：')
        for card in pre:
            pos=A.find(card)
            A=A[:pos]+A[pos+1:]
        print('甲方牌：',A)
        print('乙方牌：',B)
        players='甲乙'
        player=1
        start=False
        while len(A)>0 and len(B)>0:
            cur=input(players[player]+'方出牌（弃权直接按“Enter”键）：')
            if cur=='':
                player=1-player
                start=True
                continue
            while (cur!='' and not found(cur,player,A,B,'','')) or (start and not judge_start(cur)) or (cur!='' and not judge(pre,cur) and not start):
                while cur!='' and not found(cur,player,A,B,'',''):
                    print('所出牌中含有不存在的。')
                    cur=input(players[player]+'方出牌（弃权直接按“Enter”键）：')
                while start and not judge_start(cur):
                    print('无效。')
                    cur=input(players[player]+'方出牌（弃权直接按“Enter”键）：')
                while cur!='' and not judge(pre,cur) and not start:
                    print('无效。')
                    cur=input(players[player]+'方出牌（弃权直接按“Enter”键）：')
            if cur=='':
                player=1-player
                start=True
                continue
#更新甲、乙的牌：
            if player==0:
                for card in cur:
                    pos=A.find(card)
                    A=A[:pos]+A[pos+1:]
            else:
                for card in cur:
                    pos=B.find(card)
                    B=B[:pos]+B[pos+1:]
            print('甲方牌：',A)
            print('乙方牌：',B)
            player=1-player
            pre=cur
            start=False
        if len(A)==0:
            print('甲胜。')
        else:
            print('乙胜。')
    elif game_type==2:
#定义所有的牌：
        for i in range(3,10):
            cards+=[str(i)]*4
        cards+=['T' for i in range(4)]+['J' for i in range(4)]+['Q' for i in range(4)]+['K' for i in range(4)]
        cards+=['A' for i in range(4)]+['2' for i in range(4)]+['S','B']
        print('所有的牌：',cards,'共'+str(len(cards))+'张。')
#分发牌：
        reserved=[]
        for i in range(3):
            temp=randint(0,len(cards)-1)
            while temp in reserved:
                temp=randint(0,len(cards)-1)
            reserved+=[temp]
        num=len(cards)-3
        indexA=[]
        for a in range(int(num/3)):
            temp=randint(0,len(cards)-1)
            while temp in indexA or temp in reserved:
                temp=randint(0,len(cards)-1)
            indexA+=[temp]
        indexB=[]
        for b in range(int(num/3)):
            temp=randint(0,len(cards)-1)
            while temp in indexA or temp in indexB or temp in reserved:
                temp=randint(0,len(cards)-1)
            indexB+=[temp]
        indexC=[]
        for c in range(len(cards)):
            if not c in indexA and not c in indexB and not c in reserved:
                indexC+=[c]
#将牌的索引按从小到大的顺序排序：
        indexA.sort()
        indexB.sort()
        indexC.sort()
        print('“10”用“T”代替，“小王”用“S”代替，“大王”用“B”代替。')
        print('请使用半角数字或半角大写英文字母输入所出的牌。')
#将索引与牌对应：
        A=B=C=''
        print('甲方牌：')
        for a in indexA:
            A+=cards[a]
            print(cards[a],end=',')
        print('共'+str(len(indexA))+'张。')
        print('乙方牌：')
        for b in indexB:
            B+=cards[b]
            print(cards[b],end=',')
        print('共'+str(len(indexB))+'张。')
        print('丙方牌：')
        for c in indexC:
            C+=cards[c]
            print(cards[c],end=',')
        print('共'+str(len(indexC))+'张。')
        print('预留牌：',end='')
        for card in reserved:
            print(cards[card],end=' ')
        lord=int(input('地主（输入半角数字，1代表甲，2代表乙，3代表丙）：'))-1
        while not (lord==0 or lord==1 or lord==2):
            lord=int(input('输入错误。地主（输入半角数字，1代表甲，2代表乙，3代表丙）：'))-1
#由于添加预留牌的一方需将索引重新排序，原来的牌需清空（但索引无需清空）；
#否则将索引排序后对应添加牌时会导致其原有的牌被重复添加：
        if lord==0:
            A=''
            for card in reserved:
                indexA.append(card)
            indexA.sort()
            print('甲方牌：',end='')
            for a in indexA:
                A+=cards[a]
                print(cards[a],end=',')
            print('共'+str(len(indexA))+'张。')
        elif lord==1:
            B=''
            for card in reserved:
                indexB.append(card)
            indexB.sort()
            print('乙方牌：',end='')
            for b in indexB:
                B+=cards[b]
                print(cards[b],end=',')
            print('共'+str(len(indexB))+'张。')
        elif lord==2:
            C=''
            for card in reserved:
                indexC.append(card)
            indexC.sort()
            print('丙方牌：',end='')
            for c in indexC:
                C+=cards[c]
                print(cards[c],end=',')
            print('共'+str(len(indexC))+'张。')
#分发牌完成，开始：
        pre=input('甲方出牌：')
        while not found(pre,0,A,'','',''):
            print('所出牌中含有不存在的。')
            pre=input('甲方出牌：')
        while not judge_start(pre):
            print('无效。')
            pre=input('甲方出牌：')
        for card in pre:
            pos=A.find(card)
            A=A[:pos]+A[pos+1:]
        print('甲方牌：',A)
        print('乙方牌：',B)
        print('丙方牌：',C)
        players='甲乙丙'
        player=1
        empty=0
        start=False
        while len(A)>0 and len(B)>0 and len(C)>0:
            cur=input(players[player]+'方出牌（弃权直接按“Enter”键）：')
            if empty==2:
                start=True
            while (cur!='' and not found(cur,player,A,B,C,'')) or (cur!='' and start and not judge_start(cur)) or (cur!='' and not start and not judge(pre,cur)):
                while cur!='' and not found(cur,player,A,B,C,''):
                    print('所出牌中含有不存在的。')
                    cur=input(players[player]+'方出牌（弃权直接按“Enter”键）：')
                while cur!='' and start and not judge_start(cur):
                    print('无效。')
                    cur=input(players[player]+'方出牌（弃权直接按“Enter”键）：')
                while cur!='' and not start and not judge(pre,cur):
                    print('无效。')
                    cur=input(players[player]+'方出牌（弃权直接按“Enter”键）：')
            if cur=='':
                empty+=1
                player=(player+1)%3
                continue
#更新甲、乙的牌：
            if player==0:
                for card in cur:
                    pos=A.find(card)
                    A=A[:pos]+A[pos+1:]
            elif player==1:
                for card in cur:
                    pos=B.find(card)
                    B=B[:pos]+B[pos+1:]
            elif player==2:
                for card in cur:
                    pos=C.find(card)
                    C=C[:pos]+C[pos+1:]
            print('甲方牌：',A)
            print('乙方牌：',B)
            print('丙方牌：',C)
            player=(player+1)%3
            pre=cur
            empty=0
            start=False
        if lord==0:
            if len(A)==0:
                print('甲胜。')
            else:
                print('乙、丙胜。')
        elif lord==1:
            if len(B)==0:
                print('乙胜。')
            else:
                print('甲、丙胜。')
        elif lord==2:
            if len(C)==0:
                print('丙胜。')
            else:
                print('甲、乙胜。')
    elif game_type==3:
#定义所有的牌：
        for i in range(3,10):
            cards+=[str(i)]*8
        cards+=['T' for i in range(8)]+['J' for i in range(8)]+['Q' for i in range(8)]+['K' for i in range(8)]
        cards+=['A' for i in range(8)]+['2' for i in range(8)]+['S','S','B','B']
        print('所有的牌：',cards,'共'+str(len(cards))+'张。')
#分发牌：
        indexA=[]
        for a in range(int(len(cards)/4)):
            temp=randint(0,len(cards)-1)
            while temp in indexA:
                temp=randint(0,len(cards)-1)
            indexA+=[temp]
        indexB=[]
        for b in range(int(len(cards)/4)):
            temp=randint(0,len(cards)-1)
            while temp in indexA or temp in indexB:
                temp=randint(0,len(cards)-1)
            indexB+=[temp]
        indexC=[]
        for c in range(int(len(cards)/4)):
            temp=randint(0,len(cards)-1)
            while temp in indexA or temp in indexB or temp in indexC:
                temp=randint(0,len(cards)-1)
            indexC+=[temp]
        indexD=[]
        for d in range(len(cards)):
            if not d in indexA and not d in indexB and not d in indexC:
                indexD+=[d]
#将牌的索引按从小到大的顺序排序：
        for i in range(len(indexA)-1,0,-1):
            in_order=True
            for j in range(i):
                if indexA[j]>indexA[j+1]:
                    indexA[j],indexA[j+1]=indexA[j+1],indexA[j]
                    in_order=False
            if in_order:
                break
        for i in range(len(indexB)-1,0,-1):
            in_order=True
            for j in range(i):
                if indexB[j]>indexB[j+1]:
                    indexB[j],indexB[j+1]=indexB[j+1],indexB[j]
                    in_order=False
            if in_order:
                break
        for i in range(len(indexC)-1,0,-1):
            in_order=True
            for j in range(i):
                if indexC[j]>indexC[j+1]:
                    indexC[j],indexC[j+1]=indexC[j+1],indexC[j]
                    in_order=False
            if in_order:
                break
        for i in range(len(indexD)-1,0,-1):
            in_order=True
            for j in range(i):
                if indexD[j]>indexD[j+1]:
                    indexD[j],indexD[j+1]=indexD[j+1],indexD[j]
                    in_order=False
            if in_order:
                break
        print('“10”用“T”代替，“小王”用“S”代替，“大王”用“B”代替。')
        print('请使用半角数字或半角大写英文字母输入所出的牌。')
#将索引与牌对应：
        A=B=C=D=''
        print('甲方牌：')
        for a in indexA:
            A+=cards[a]
            print(cards[a],end=',')
        print('共'+str(len(indexA))+'张。')
        print('乙方牌：')
        for b in indexB:
            B+=cards[b]
            print(cards[b],end=',')
        print('共'+str(len(indexB))+'张。')
        print('丙方牌：')
        for c in indexC:
            C+=cards[c]
            print(cards[c],end=',')
        print('共'+str(len(indexC))+'张。')
        print('丁方牌：')
        for d in indexD:
            D+=cards[d]
            print(cards[d],end=',')
        print('共'+str(len(indexD))+'张。')
#分发牌完成，开始：
        pre=input('甲方出牌：')
        while not found(pre,0,A,'','',''):
            print('所出牌中含有不存在的。')
            pre=input('甲方出牌：')
        while not judge_start(pre):
            print('无效。')
            pre=input('甲方出牌：')
        for card in pre:
            pos=A.find(card)
            A=A[:pos]+A[pos+1:]
        print('甲方牌：',A)
        print('乙方牌：',B)
        print('丙方牌：',C)
        print('丁方牌：',D)
        players='甲乙丙丁'
        player=1
        empty=0
        need=0
        start=False
        while not shuangkou_end(A,B,C,D):
            cur=input(players[player]+'方出牌（弃权直接按“Enter”键）：')
            remaining=[len(A),len(B),len(C),len(D)]
#如果当前玩家已出完牌：
            while remaining[player]==0:
                player=(player+1)%4
#统计没出完牌的玩家：
            for i in remaining:
                if i>0:
                    need+=1
            if empty==need-1:
                start=True
            while (cur!='' and not found(cur,player,A,B,C,D)) or (cur!='' and start and not judge_start(cur)) or (cur!='' and not start and not judge(pre,cur)):
                while cur!='' and not found(cur,player,A,B,C,D):
                    print('所出牌中含有不存在的。')
                    cur=input(players[player]+'方出牌（弃权直接按“Enter”键）：')
                while cur!='' and start and not judge_start(cur):
                    print('无效。')
                    cur=input(players[player]+'方出牌（弃权直接按“Enter”键）：')
                while cur!='' and not start and not judge(pre,cur):
                    print('无效。')
                    cur=input(players[player]+'方出牌（弃权直接按“Enter”键）：')
            if cur=='':
                empty+=1
                player=(player+1)%4
                need=0
                continue
#更新甲、乙的牌：
            if player==0:
                for card in cur:
                    pos=A.find(card)
                    A=A[:pos]+A[pos+1:]
            elif player==1:
                for card in cur:
                    pos=B.find(card)
                    B=B[:pos]+B[pos+1:]
            elif player==2:
                for card in cur:
                    pos=C.find(card)
                    C=C[:pos]+C[pos+1:]
            else:
                for card in cur:
                    pos=D.find(card)
                    D=D[:pos]+D[pos+1:]
            print('甲方牌：',A)
            print('乙方牌：',B)
            print('丙方牌：',C)
            print('丁方牌：',D)
            player=(player+1)%4
            pre=cur
            empty=0
            need=0
            start=False
        if len(A)==len(C)==0:
            print('甲、丙胜。')
        else:
            print('乙、丁胜。')
    end=input('直接按“Enter”键以结束，输入任意其它字符以重新开始：')
