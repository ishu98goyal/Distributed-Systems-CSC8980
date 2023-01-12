#!/usr/bin/env python
# coding: utf-8

# # PROJECT 1

# In[ ]:


from itertools import combinations
import pprint
import itertools

N=0
MaekawaSets = []


# In[78]:


def print_sets(sets):
    for i in range(len(sets)):
        if i<9:
            print("Set "+ str(i+1)+ "  :", sets[i] )
        else:
            print("Set "+ str(i+1)+ " :", sets[i] )


# In[79]:


def print_sets(sets):
    for i in range(len(sets)):
        if i<9:
            print("Set "+ str(i+1)+ "  :", sets[i] )
        else:
            print("Set "+ str(i+1)+ " :", sets[i] )


# In[80]:


# check if N - number of nodes can be expressed in the form - (k^2-k+1)
def findK(N):
    for i in range(round(N/2)+1):
        if (pow(i,2) - i + 1) == N:
            return i
    return N


# In[81]:


#Set creation for all possible combinations
def createSets(N, K): 
    print()
    print('************ Creating Sets ************')
    print()
    print('Received N and K as: {} and {}'.format(N, K))
    print('Starting to create sets...')
    print()
    L=list(range(1,N+1))
    A=[",".join(map(str, comb)) for comb in combinations(L, K)]

    # Converting each element in the A list to list and storing in myList
    myList=[]
    finalList=[]
    for i in range(len(A)):
        myList.append(A[i].split(','))

    # filter for repetative couplings
    couplingsTemp = []
    couplings = []
    for List in myList:
        couplingsTemp.append([",".join(map(str, comb)) for comb in combinations(List, 2)])
    for couple in couplingsTemp:
        for i in range(len(couple)):
            if str(couple[i]) not in str(couplings):
                couplings.append(couple[i])
            else:
                continue

    # Preparing Final Set
    finalList = []
    for j in myList:
        counter=0
        p=[",".join(map(str, comb)) for comb in combinations(j, 2)]
        for i in p:
            if i in couplings:
                counter=counter+1
        if counter==len(p):
            couplings=list(set(couplings)^set(p))
            finalList.append(j)
    return finalList


# In[82]:


# If N = K^2-K+1 then execute this function
def optimalSets(N, K):
    print('{} can be expressed as k*k - k + 1'.format(N))
    print()
    MaekawaSets = createSets(N,K)
    print_sets(MaekawaSets)
    print("\n")
    print('*******Set Creation Completed*******')
    return MaekawaSets


# In[83]:


# create the degenerate sets
# once the sets are created with a new N greater than the original entered by the user
# we need to perform filtering on it
'''
Algorithm to do it:-
1. for element in subset:
       for el in element:
            if el == newN:
                el=N
            if el > N:
                # perform relevant replacements
                #  eg. N=5, newN=7, el=6 then el should be replaced by 4 i.e. N-1
                el = N - (newN-el)
2. After the replacements have been done, we need to delete the redundant lists.
3. Make the lists free of the duplicates if any
4. Finally, len(subsets) = N
'''

def degenerateSetCreation(N, newN, setsGenerated):
    print('******* Degenerate Sets Creation *******')
    print()
    print('Starting Degenerate Sets Creation...')
    print()
    # Step 1
    for i in range(len(setsGenerated)):
        subset = setsGenerated[i]
        for j in range(len(subset)):
            element = subset[j]
            if element == newN:
                subset[j] = str(N)
            if int(element) > N:
                subset[j] = str(N - (newN - int(element)))
    # Step 2 and 3
    for subset in setsGenerated:
        subset.sort()
    deleteDuplicateSets = list(setsGenerated for setsGenerated,_ in itertools.groupby(setsGenerated))
    for i in range(len(deleteDuplicateSets)):
        subset = deleteDuplicateSets[i]
        deleteDuplicateSets[i] = list(subset for subset,_ in itertools.groupby(subset))
    return deleteDuplicateSets


# In[84]:


# If N != K^2-K+1 then execute this function
# find the nearest possible number such that M > N and can be expressed as M=L^2-L+1 
# here L=K

def nonOptimalSets(K):
    print('{} cannot be expressed as k*k - k + 1'.format(K))
    
    print()

    print('Finding new temporary N...')
    newN = K
    foundTempN = False
    newK=0
    while foundTempN == False:
        newN+=1
        newK = findK(newN)
        if newK != newN:
            foundTempN = True
    print('Temporary N found is: {}'.format(newN))
    print('Therefore we will create sets of size {} from {} different nodes.'.format(newK, newN))
    
    # create sets for the new N found
    tempSets = createSets(newN, newK)
    print()
    print('Set Creation with new value of \'N\' complete...')
    
    # degenerate sets creation
    MaekawaSets = degenerateSetCreation(N=K, newN=newN, setsGenerated=tempSets)
    print_sets(MaekawaSets)
    print()
    print('*******Final Degenerate Set Creation Completed*******')
    print('*******Set Creation Completed*******')
    return MaekawaSets


# In[85]:


# entry point
def setGenerationAlgorithm(Nodes):
    subsetSize = findK(Nodes)
    if(subsetSize==Nodes):  
        return nonOptimalSets(K=subsetSize)
    else:
        return optimalSets(N=Nodes, K=subsetSize)


# In[86]:


numberOfNodes = int(input('Enter number of nodes: '))
print()

sets=setGenerationAlgorithm(numberOfNodes)
print("\n")
while(True):
    print()
    print("*******Set Menu*******")
    print("1. To Add Node/Nodes")
    print("2. To Remove Node/Nodes")
    print("3. Exit")
    
    option=int(input('Enter option: '))
    
    if option == 1:
        nodes=int(input('Enter number of nodes to be added: '))
        numberOfNodes=numberOfNodes+nodes
        sets=setGenerationAlgorithm(numberOfNodes)

    elif option == 2:
        nodes=int(input('Enter number of nodes to be removed: '))
        numberOfNodes=numberOfNodes-nodes
        sets=setGenerationAlgorithm(numberOfNodes)
    else:
        break


# # Connection between P1 and P2
# 

# In[87]:


# Preparation for Config.py
request=[]
request_set=[]
for i in sets:
    res = dict.fromkeys(i)
    request.append(res)
for i in request:
    a={int(k): v for k, v in i.items()}
    request_set.append(a)


# In[88]:


r=list(request_set)


# In[89]:


file=[["NUM_NODE = " + str(numberOfNodes)],["INIT_PORT = 3000"],["NODE_PORT = [(INIT_PORT + i) for i in xrange(NUM_NODE)]"],['RECV_BUFFER = 4096'],["REQUEST_SETS = "+str(request_set)]]


# In[94]:


with open(r'config.py', 'w') as fp:
    fp.flush()
    for item in file:
        fp.write("%s\n" % item[0])
print('Config.Py File Created')

