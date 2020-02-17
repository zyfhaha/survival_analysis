# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 13:06:12 2020

@author: Administrator
"""

def simulatedata(n,p,true_beta,noise):
    '''
    n:samples
    p:dimensions
    true_beta:true effective features' coefficients
    noise,gaussian noise added
    
    return x,t,delta(x.shape=(n,p),y.shape=(p,1),delta.shape=(p,1))
    '''
    pass

def splitdata(training_percent,val_percent):
    '''
    split data into training,val,test
    '''
    pass





    
    
def buildmodel(encoder_hidden_size,decoder_hidden_size,lambda1,dropout_p):
    '''
    return a model,fully connected
    encoder, hidden units = encoder_hidden_size
    ex,encoder_hidden_size=[200,100,50]
    '''
 
def training(x, t,delta,model):
    '''
    given x,t,delta,train a model
    '''
    
def adjusthyper(x, t,delta,model):
    '''
    given x,t,delta,train a model
    '''
    
    
def evaluate(x, t,delta,model):
    '''
    given x,t,delta,train a model
    '''