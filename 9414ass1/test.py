# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 13:37:50 2019

@author: kyrie
"""

a = {1:2,2:4}
print(a.get(key))

def search(self):
        while not self.empty_frontier():
            path = self.frontier.pop()#
            print(path)
          #  self.display(2, "Expanding:",path,"(cost:",path.cost,")")
            self.num_expanded += 1
            if self.problem.is_goal(path.domains):    # solution found
                self.display(1, self.num_expanded, "paths have been expanded and",
                            len(self.frontier), "paths remain in the frontier")
                self.solution = path   # store the solution found
                return path
            else:
                neighs = self.problem.neighbors(path.domains)
                
                self.display(3,"Neighbors are", neighs)
                for arc in reversed(neighs):
                    self.add_to_frontier(Path(path,arc))
                self.display(3,"Frontier:",self.frontier)
        self.display(1,"No (more) solutions. Total of",
                     self.num_expanded,"paths expanded.")
        
        
        
class extend_Search_with_AC_from_Cost_CSP(Search_with_AC_from_CSP):
    def __init__(self, csp):
        self.cons = Con_solver(csp)  #copy of the CSP
        self.domains = self.cons.make_arc_consistent()
        self.csp = csp

    def is_goal(self, node):
        return all(len(node[var])==1 for var in node)
    
    def start_node(self):
        return self.domains
    
    def neighbors(self,node):
        neighs = []
        nlist = []
        var = select(node)#改 选域最大的 m1m2
        if var:
            dom1, dom2 = partition_domain(node[var])
            self.display(2,"Splitting", var, "into", dom1, "and", dom2)
            to_do = self.cons.new_to_do(var,None)
            for dom in [dom1,dom2]:
                newdoms = copy_with_assign(node,var,dom)
                cons_doms = self.cons.make_arc_consistent(newdoms,to_do)
                if all(len(cons_doms[v])>0 for v in cons_doms):
                    neighs.append(cons_doms)
                else:
                    self.display(2,"...",var,"in",dom,"has no solution")
        return neighs
