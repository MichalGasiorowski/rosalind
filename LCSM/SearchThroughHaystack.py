# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 23:29:07 2014

@author: Michal

Problem

A common substring of a collection of strings is a substring of every member 
of the collection. We say that a common substring is a longest common substring
if there does not exist a longer common substring. 
For example, "CG" is a common substring of "ACGTACGT" and "AACCGGTATA", 
but it is not as long as possible; in this case, "GTA" is a longest common 
substring of "ACGTACGT" and "AACCGTATA".

Note that the longest common substring is not necessarily unique; for a 
simple example, "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. 
(If multiple solutions exist, you may return any single solution.)

"""


from functools import wraps


def memo(func):
    cache = {}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)            
        return cache[args]
    return wrap

def lcp(i, j, s):
    ret = 0
    n = len(s)
    for k in range(n):
        if i+k >= n or j+k >=n:
            break
        if s[i+k] != s[j+k]:
            break
        ret += 1
    return ret
#print lcp(1, 3, "banana$")

def suffix_lcp(s):    
    
    n = len(s)    
    ss = [i for i in range(n)]
    suffix = sorted(ss, key = lambda x: s[x:])
    lcp_arr = [lcp(suffix[i - 1], suffix[i], s) for i in range(1, n)]
    return suffix, lcp_arr  

class Node(object):
    def __init__(self, next_node_num, p_edge, parent):
        self.is_root = False
        self.active_length = 0
        self.node_num = next_node_num
        self.p_edge = p_edge
        self.parent = parent
        self.lps_node = None
        self.first_info_node_in_subtree = None
        self.last_info_node_in_subtree = None
        first_info_node, last_info_node = None, None
        self.edges = {}

    def get_p_edge_len(self):
        if self.is_root:
            return 0
        return self.p_edge[1] - self.p_edge[0]
    def compute_active_length(self):
        if self.is_root:
            return
        self.active_length = self.parent.active_length + self.get_p_edge_len()
        
    
    def edges_to_string(self):
        ret = ""
        for edge, child_node in self.edges.items():
            ret = ret + "[" + str(edge) + ":" + str(child_node.node_num) + "],"
        return ret    
    def edges_to_string_full(self, text):
        ret = ""
        for edge, child_node in self.edges.items():
            ret = ret + "[" + text[edge[0]:edge[1]] + ":" + str(child_node.node_num) + "],"
        return ret
    def node_num_to_alphabet(self):
        A_ord = ord('A')
        return chr(self.node_num + A_ord)

class SuffixTree(object):
    maxInd = 2**30
    end_symbol = "#"
    s_separator = "$"        
   
    def __init__(self, text):
        self.text = text + SuffixTree.end_symbol
        self.info_nodes=[]
        self.n = len(self.text)
        self.next_node_num = 0
        self.root = self.build_node(None, None)
        self.root.is_root = True
        self.build_suffix_tree()
        
    def build_node(self, p_edge, parent):
        new_node = Node(self.next_node_num,  p_edge, parent)
        self.next_node_num += 1
        return new_node
    def get_edge_text(self, edge):
        #if self.n == edge[1]:
        #    return str(edge[0]) + "+"
        return self.text[edge[0]: edge[1]]
    def generate_first_last_info_nodes(self):
        def generate_first_last_info_nodes_subtree(node):
            if not node.edges:
                node.first_info_node_in_subtree = node.node_num
                node.last_info_node_in_subtree = node.node_num
            else:
                minval, maxval = 0, SuffixTree.maxInd
                for child in node.edges.values():
                    child_minval, child_maxval = generate_first_last_info_nodes_subtree(child)
                    minval, maxval = min(minval, child_minval), max(child_maxval, maxval)
                    node.first_info_node_in_subtree = minval
                    node.last_info_node_in_subtree = maxval
            return node.first_info_node_in_subtree, node.last_info_node_in_subtree
        
        generate_first_last_info_nodes_subtree(self.root)
       
    def build_suffix_tree(self):
        # lbi(i,i) >= i + active_length + min_dist       
        
        lbi, min_dist = 0, 0
        active_node, active_length = self.root, 0
        last_created_branch_node = None
        for phase_i in range(self.n):
            print "#####phase:{phase}#####".format(phase=str(phase_i))
            self.print_tree()                        
            
            if active_node.lps_node is not None: # follow suffix pointer
                active_node = active_node.lps_node
                active_length = max(active_length - 1, 0)
            else:
                active_node = self.root
                active_length = 0
            min_dist = max(0, lbi - phase_i - active_length)
            print "active_node={0}, activeL={1}, minDist={2}".format(active_node.node_num_to_alphabet(),
                                                               active_length,
                                                               min_dist)
            walk_ret = self.walk_down_tree(active_node, active_length, min_dist, (phase_i, self.n))
            active_node, active_edge , split_point, success, lbi = walk_ret
            print active_node.node_num, active_edge, split_point, success, lbi
            
            active_length = active_node.active_length
            
            if success: # completely matched pattern. Suffix is already in the tree!
                
                continue
            if active_edge is None: 
                #create new information edge from active node
                new_node = self.build_node((lbi, self.n), active_node )
                active_node.edges[(lbi, self.n)] = new_node
                self.info_nodes.append(new_node.node_num)
                if last_created_branch_node is not None:
                    last_created_branch_node.lps_node = active_node
                    last_created_branch_node = None
            else: # mismatch, we found splitting point
                #create new branch Node
                split_edge_head =(active_edge[0], active_edge[0] + split_point)
                new_branch_node = self.build_node( split_edge_head, active_node )
                #fix previous child described by active_node and active_edge 
                old_child = active_node.edges.pop(active_edge)
                split_edge_rest =(active_edge[0] + split_point, old_child.p_edge[1])
                active_node.edges[split_edge_head] = new_branch_node
                
                new_branch_node.edges[split_edge_rest] = old_child
                old_child.p_edge = split_edge_rest
                old_child.parent = new_branch_node
                # create new Information Node
                new_info_node = self.build_node((lbi, self.n), new_branch_node )
                self.info_nodes.append(new_info_node.node_num)
                new_branch_node.edges[(lbi, self.n)] = new_info_node
                new_branch_node.compute_active_length()                
                
                if last_created_branch_node is not None:
                    last_created_branch_node.lps_node = new_branch_node
                
                if active_node.is_root and new_branch_node.get_p_edge_len() == 1:
                    #this branch node suffix pointer need to be pointed to root
                    new_branch_node.lps_node = self.root
                    last_created_branch_node = None
                else:
                    last_created_branch_node = new_branch_node
                
                
        print "--------Building suffix tree finished-------"        
        return
        
    def print_tree(self):
        
        def print_node(node, level):
            #print "{indent} {node_id}:{edges}".format(indent="\t"*level, node_id= node.node_num, edges=node.edges_to_string_full(self.text))
            #if not node.edges: return
            #print "{indent} [{p_edge}]->({node_id}):".format(indent="  "*level ,
            #                                        p_edge = self.get_edge_text(node.p_edge) if node.p_edge is not None else "",
            #                                        node_id= node.node_num)
            A_ord = ord('A')
            
                
            print "{indent}{p_edge}(id={node_id}, lps={lps})".format(indent="   "*level,
                                                    p_edge = self.get_edge_text(node.p_edge) + "---" if node.p_edge is not None else "",
                                                    node_id= chr(node.node_num + A_ord),
                                                    lps= chr(node.lps_node.node_num + A_ord) if node.lps_node is not None else "None")
        
            for edge, child_node in node.edges.items():
                print_node(child_node, level + 1)
        print_node(self.root, 0)            
        
    def walk_down_tree(self, node, active_length, min_distance, pattern_ind, pattern=None):
        """
        active_node - Node from which to start walkdown
        pattern_ind - (start, end) indexes of pattern
        pattern - string with characters to compare
        Walk down tree, starting from node.
        Compare characters on edge with characters in pattern
        On mismatch return branchNode or edge and index with mismatch
        """
        if pattern is None:
            pattern = self.text
        pattern_low, pattern_high = pattern_ind
        pattern_len = pattern_high - pattern_low
        pattern_i = active_length
        
        skip_n = min_distance
        active_node = node
        active_edge = None
        
        text = self.text         
        split_point = 0
        for edge, child_node in active_node.edges.items():
            if text[edge[0]] == pattern[pattern_low + pattern_i]:
                active_edge = (edge, child_node)
                break
        if active_edge is None: # active_node is Information Node or there is no outgoing matching edge
            return active_node, active_edge , split_point, False, pattern_low + pattern_i
        
        for i in range(active_edge[0][0], active_edge[0][1]):
            if skip_n > 0:
                skip_n -= 1
                pattern_i += 1
                continue
            split_point = i - active_edge[0][0]
            if pattern_i >= pattern_len: # pattern ended, match is successfull
                return active_node, active_edge[0] , split_point, True, pattern_low + pattern_i
                
            if text[i] != pattern[pattern_low + pattern_i]: # mismatch, we found splitting point
                return active_node, active_edge[0] , split_point, False, pattern_low + pattern_i
            pattern_i += 1                
            
        # in this part we passed edge so we are in branchNode
        active_edge_length = active_edge[0][1] - active_edge[0][0]
        active_node = active_edge[1]
        return self.walk_down_tree(active_node, active_length + active_edge_length, skip_n, pattern_ind, pattern)
                
        
#ss = SuffixTree("abab")   
#ss = SuffixTree("ababbabbaabbabb")  
#ss = SuffixTree("cdddcdc")
ss = SuffixTree("abcabxabcd")        
ss.print_tree()

#print suffix_lcp("banana$")