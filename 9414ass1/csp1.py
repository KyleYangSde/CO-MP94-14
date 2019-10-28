# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 18:45:31 2019

@author: kyle
"""
from searchGeneric import Searcher,AStarSearcher
from cspProblem import CSP,Constraint
from cspConsistency import Search_with_AC_from_CSP
import sys

with open(sys.argv[1], 'r') as f:
    constraint = []
    meeting = []
    domains = []
    hard = []
    soft = []
    hard_list = []
    for i in f:
        i = i.replace('\n',' ')
        i = i.replace(',',' ')
        i = i.replace('  ',' ')
        i = i.split(' ')
        if i[0] == '#':
            continue
        if i[0] == 'meeting':
            meeting.append(i[1])
        if i[0] == 'constraint':
            for j in range(len(i)):
                if i[j] != '' and i[j] != 'constraint':
                    constraint.append(i[1:-1])
        if i[0] == 'domain':
            for j in range(len(i)):
                if i[j] != '' and i[j] != 'domain':
                    domains.append(i[1:-1])
    b_constraint = list(set([tuple(t) for t in constraint ]))
    b_constraint = [list(v) for v in b_constraint]
    domains = list(set([tuple(t) for t in domains]))
    domains = [list(v) for v in domains]
    for i in domains:
        if i[-1] == 'soft':
            soft.append(i)
        if i[-1] == 'hard':
            hard.append(i)     
    variables = []
    variables = meeting

        
####### constraint((m1,m2),before)
####### m1 m2 m3 dictionary m1:(day,time)
####### binary constrain
def before(m1,m2):
    if m1<m2:
        return True
    else:
        return False
    
def same_day(m1,m2):
    if m1//8 == m2//8:
        return True
    else:
        return False

def one_day_between(m1,m2):
    a = abs(m1//8 - m2//8)
    if a == 2:
        return True
    else:
        return False
    
def one_hour_between(m1,m2):
    b = abs(m1%8 - m2%8)
    if b == 2:
        return True
    else:
        return False


####hard constrain
def hard_cons(each_hard,a):
    after_hard = []
    day = ['mon','tue','wed','thu','fri']
    meet_time = ['9am','10am','11am','12pm','13pm','14pm','15pm','16pm']
    #print(a)
    #print(each_hard[0])
    if len(each_hard) == 3:
         if each_hard[1] == 'mon':
             for i in a[each_hard[0]]:##i//8 = 0
                if i // 8 == 0:
                    after_hard.append(i)
         if each_hard[1] == 'tue':
             for i in a[each_hard[0]]:##i//8 = 0
                if i // 8 == 1:
                    after_hard.append(i)
         if each_hard[1] == 'wed':
             for i in a[each_hard[0]]:##i//8 = 0
                if i // 8 == 2:
                    after_hard.append(i)
         if each_hard[1] == 'thu':
             for i in a[each_hard[0]]:##i//8 = 0
                if i // 8 == 3:
                    after_hard.append(i)
         if each_hard[1] == 'fri':
             for i in a[each_hard[0]]:##i//8 = 0
                if i // 8 == 4:
                    after_hard.append(i)
         if each_hard[1] == '9am':
             for i in a[each_hard[0]]:##i//8 = 0
                if i % 8 == 0:
                    after_hard.append(i)
         if each_hard[1] == '10am':
             for i in a[each_hard[0]]:##i//8 = 0
                if i % 8 == 1:
                    after_hard.append(i)
         if each_hard[1] == '11am':
             for i in a[each_hard[0]]:##i//8 = 0
                if i % 8 == 2:
                    after_hard.append(i)
         if each_hard[1] == '12pm':
             for i in a[each_hard[0]]:##i//8 = 0
                if i % 8 == 3:
                    after_hard.append(i)
         if each_hard[1] == '13pm':
             for i in a[each_hard[0]]:##i//8 = 0
                if i % 8 == 4:
                    after_hard.append(i)
         if each_hard[1] == '14pm':
             for i in a[each_hard[0]]:##i//8 = 0
                if i % 8 == 5:
                    after_hard.append(i)
         if each_hard[1] == '15pm':
             for i in a[each_hard[0]]:##i//8 = 0
                if i % 8 == 6:
                    after_hard.append(i)
         if each_hard[1] == '16pm':
             for i in a[each_hard[0]]:##i//8 = 0
                if i % 8 == 7:
                    after_hard.append(i)
         if each_hard[1] == 'morning':
             for i in a[each_hard[0]]:##i//8 = 0
                if i % 8 < 3:
                    after_hard.append(i)
         if each_hard[1] == 'afternoon':
             for i in a[each_hard[0]]:##i//8 = 0
                if i % 8 >= 3:
                    after_hard.append(i)
                    
    if len(each_hard) == 5:
        if 'before' not in each_hard and 'after' not in each_hard:
            a = []
            a = each_hard[2].split('-')
            a.insert(0,each_hard[1])
            a.insert(3,each_hard[3])
            b = day.index(a[0]) *8 + meet_time.index(a[1])
            c = day.index(a[2]) *8 + meet_time.index(a[3])
            for i in range(0,40):
                if i>b and i<c:
                    after_hard.append(i)
        if 'before' in each_hard:
            if each_hard[2] in day and each_hard[3] in meet_time:
                for i in range(0,40):
                    if i < day.index(each_hard[2]) + meet_time.index(each_hard[3]) :
                            after_hard.append(i)
        
        if 'after' in each_hard:
            #print(each_hard[2])
            #print(each_hard[3])
            if each_hard[2] in day and each_hard[3] in meet_time:
                for i in range(0,40):
                    if i > day.index(each_hard[2]) + meet_time.index(each_hard[3]) :
                            after_hard.append(i)

    if len(each_hard) == 4:
        if 'before' in each_hard:
            if each_hard[2] in day:
                for i in range(0,40):
                    if i//8 < day.index(each_hard[2]):
                            after_hard.append(i)
                            
            if each_hard[2] in meet_time:
                for i in range(0,40):
                    if i%8 < meet_time.index(each_hard[2]):
                            after_hard.append(i)
                            
        if 'after' in each_hard:
            if each_hard[2] in day:
                for i in range(0,40):
                    if i//8 > day.index(each_hard[2]):
                            after_hard.append(i)
                            
            if each_hard[2] in meet_time:
                for i in range(0,40):
                    if i%8 > meet_time.index(each_hard[2]):
                            after_hard.append(i)
            
    after_hard.insert(0,each_hard[0])
    return after_hard       
        
##### creat_board
def create_board(meeting):
    a = []
    all_board = {}
    for i in range(0,40):
        a.append(i)
    
    for j in meeting:
        all_board[j] = a
    return all_board

###get the hard list to get the unique list
###c is the hard constrain output
def after_hard_cons(meeting):
    a = create_board(meeting) 
    b = []
    c = []
    e = {}
    #######e is the dict that contains the variable after hard
    for i in hard:
        b.append(hard_cons(i,a))
    
    for i in b:
        for j in b[b.index(i)+1:]:
            if i[0] in j:
                c.append(list(set(i).intersection(set(j))))
    ########c is the 2 dimension list that needs    
    for i in variables:
        count = 0
        for j in b:
            if j[0] == i:
                count+=1
        if count == 1:
            for j in b:
                if i in j:
                    c.append(j)
    
    ########format make m is in the front
    for i in c:
        for j in range(len(i)):
            if str(i[j])[0] == 'm':
                if j == 0:
                    e[str(i[j])] = set(i[1:])
                else:
                    e[str(i[j])] = set(i[:j] + i[j+1:])
                    
    ########give domain to empty set
    d = [i for i in range(40)]     
    f = []
    for j in meeting:
        if j not in e.keys():
            f.append(j)
            
    for i in f:
        e[i] = set(d)
    
    ###print('e',e)
    return e

after_hard_cons(meeting)
def construct_cons(constraint):
    cons_list = []
    for i in constraint:
        if i[1] == 'before':
            cons_list.append(Constraint((i[0],i[2]),before))
        if i[1] == 'same-day':
            cons_list.append(Constraint((i[0],i[2]),same_day))
        if i[1] == 'one-day-between':
            cons_list.append(Constraint((i[0],i[2]),one_day_between))
        if i[1] == 'one-hour-between':
            cons_list.append(Constraint((i[0],i[2]),one_hour_between))
    #####    print(cons_list)
    return cons_list        

##### cost{'m1':[],'m2':[],'m3':[]}   ['early-morning,early-morning',early-afternoon']
##### cost{'m1':'early-morning','m2':'early-morning','m3':'early-afternoon'}
def cost_a(soft,variables):
    cost = {}
    for i in variables:
        cost[i] = []
    for j in soft:
        cost[j[0]].append(j[1])

    return cost

class extend_AStarSearcher(AStarSearcher):
    max_display_level = 0
    def add_to_frontier(self,path):
        value = self.problem.heuristic(path.end())
        self.frontier.add(path, value)
    

class Search_with_AC_from_Cost_CSP(Search_with_AC_from_CSP):
    def heuristic(self,node):
        result = 0
        for key in node:   # m1,m2
            herist = float('inf')
            for i in node[key]:  #{0,1,2}   {0,1,2,32,33...} 
                temp = 0
                for j in cost[key]:  #{early_morning}
                    if j == 'early-morning':
                        temp += i%8
                    if j == 'late-afternoon':
                        temp += abs (7 - i%8)
                    if j == 'early-week':
                        temp += i//8
                    if j  == 'late-week':
                        temp += abs(4-i//8) 
                    if j  == 'midday':
                        temp += abs(3 - i%8)
                if temp < herist:
                    herist = temp      
            result += herist
       # print("gigogogogo",result)
       # print("nnnnnnnnnn",node)
        return result  


def printf():
    get_day = {}
    get_time = {}
    output = {}
    output = b.solution.end()
    for key in output:##key m1 m2
        for number in output[key]:
            if number // 8 == 0:
                get_day[key] = 'mon'
            if number // 8 == 1:
                get_day[key] = 'tue'
            if number // 8 == 2:
                get_day[key] = 'wed'
            if number // 8 == 3:
                get_day[key] = 'thu'
            if number // 8 == 4:
                get_day[key] = 'fri'
            if number % 8 == 0:
                get_time[key] = '9am'
            if number % 8 == 1:
                get_time[key] = '10am'
            if number % 8 == 2:
                get_time[key] = '11am'
            if number % 8 == 3:
                get_time[key] = '12pm'
            if number % 8 == 4:
                get_time[key] = '13pm'
            if number % 8 == 5:
                get_time[key] = '14pm'
            if number % 8 == 6:
                get_time[key] = '15pm'
            if number % 8 == 7:
                get_time[key] = '16pm'
    for key in cost:
        print(f'{key}:{get_day[key]} {get_time[key]}')
    print(f'cost:{a.heuristic(b.solution.end())}')
#    print(get_day)
#    print(get_time)





#print(after_hard_cons(meeting))
#print('domains:',domains)
#print('variables:',variables)
#print('constraint:',constraint)
#print('soft:',soft)
#print('hard:',hard)
####cons is the constraint between varieable
####cos is the soft cost of ideal format
####cos = cost(soft,variables)
####domain is the all the possible cost after hard constrain
####create the csp            
#add the cost in _init_    
###### get the minimal cost of soft constraint
#print("EEEE",cost)
#print(b.solution.end())
#print(a.heuristic(b.solution.end()))


cost = cost_a(soft,variables)        
cons = construct_cons(constraint)
domains = after_hard_cons(meeting)
csp0 = CSP(domains, cons)
a = Search_with_AC_from_Cost_CSP(csp0)
b = extend_AStarSearcher(a)
b.search()
printf()
    