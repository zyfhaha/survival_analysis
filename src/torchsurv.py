# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 04:26:56 2020

@author: Administrator
"""

import torch
'''
example of Rlist:
    assume patients have been ordered according to time,
    the first element of each element of Rlist,is the index of 
    an uncersored patient
Rlist=[[1,2,3,4,5],[3,4,5],[4,5]]
'''
class coxloss(torch.nn.Module):  #resnet
    def __init__(self,Rlist):
        #c=1 uncensored,dead
        #c=0 censored,alive
        super(coxloss, self).__init__()
        self.Rlist=Rlist
    def forward(self,pred): 
#pred.size()==batch,if pred.size()==batch,1,then it should be converted by pred=pred.squueze(1)
        z=torch.zeros(1)
        for subset in self.Rlist:
            z=z+pred[subset[0]]-torch.log(\
   torch.sum(torch.exp(pred[subset]),dim=0))
        return -z 
 
 
def torch_cindex(y_pred,Rlist):
    cor=torch.zeros(1)
    total=torch.zeros(1)
    for subset in Rlist:
        cor+=sum( y_pred[subset[0]]>y_pred[subset[1:]] )
        total+=len(subset)
    print(total)
    return cor/total
#hhhhhhh