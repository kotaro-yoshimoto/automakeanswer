# coding: utf-8

# In[4]:
import numpy as np
import pandas as pd
import random


# In[5]:

#= adx^2　+ (b+e)xy　+ bey^2 +(c+f)x +(bf+ce)y+cf 
#= adx^2 + (b+e)xy+(c+f)x + bey^2+(bf+ce)y+cf 
#= adx^2 + ((b+e)y+(c+f))x + (by+c)(ey+f) 
#= {ax + (by + c)} {dx+(ey+f)}
#　　(ax+by+c)(dx+ey+f)


# In[69]:

def auto_makeanswer():

  coef = [random.randint(1, 9) for i in range(6)]

  # In[70]:

  #x^2の係数は1にしておく
  coef[0] = 1
  coef[3] = 1

  # In[71]:

  coef

  # In[74]:
  print("問題：次の式を因数分解せよ。")
  #print("{0}x^2+ {1}xy + {2}y^2 +{3}x +{4}y+{5}".format(coef[0]*coef[3], coef[1]+coef[4], coef[1]*coef[4],coef[2]+coef[5],coef[1]*coef[5]+coef[2]*coef[4], coef[2]*coef[5]))
  print("x^2+ {1}xy + {2}y^2 +{3}x +{4}y+{5}".format(coef[0]*coef[3], coef[1]+coef[4], coef[1]*coef[4],coef[2]+coef[5],coef[1]*coef[5]+coef[2]*coef[4], coef[2]*coef[5]))

  # In[75]:

  print ("答え：")
  #print("({10}x+{6}y+{7})({11}x+{8}y+{9})".format(coef[0]*coef[3], coef[1]+coef[4], coef[1]*coef[4],coef[2]+coef[5],coef[1]*coef[5]+coef[2]*coef[4], coef[2]*coef[5],coef[1],coef[2],coef[4],coef[5],coef[0],coef[3]))
  #print ("")
  #print ("ポイント：1つの文字について整理し、因数分解する")
  #print("{0}x^2+ {1}xy　+ {2}y^2 +{3}x +{4}y+{5}".format(coef[0]*coef[3], coef[1]+coef[4], coef[1]*coef[4],coef[2]+coef[5],coef[1]*coef[5]+coef[2]*coef[4], coef[2]*coef[5]))
  #print("{0}x^2+ {1}xy + {3}x　+ {2}y^2 +{4}y+{5}".format(coef[0]*coef[3], coef[1]+coef[4], coef[1]*coef[4],coef[2]+coef[5],coef[1]*coef[5]+coef[2]*coef[4], coef[2]*coef[5]))
  #print("{0}x^2+ ({1}y + {3})x　+ ({6}y+{7})({8}y+{9})".format(coef[0]*coef[3], coef[1]+coef[4], coef[1]*coef[4],coef[2]+coef[5],coef[1]*coef[5]+coef[2]*coef[4], coef[2]*coef[5],coef[1],coef[2],coef[4],coef[5]))
  #print("({10}x+({6}y+{7}))({11}x+({8}y+{9}))".format(coef[0]*coef[3], coef[1]+coef[4], coef[1]*coef[4],coef[2]+coef[5],coef[1]*coef[5]+coef[2]*coef[4], coef[2]*coef[5],coef[1],coef[2],coef[4],coef[5],coef[0],coef[3]))
  #print("({10}x+{6}y+{7})({11}x+{8}y+{9})".format(coef[0]*coef[3], coef[1]+coef[4], coef[1]*coef[4],coef[2]+coef[5],coef[1]*coef[5]+coef[2]*coef[4], coef[2]*coef[5],coef[1],coef[2],coef[4],coef[5],coef[0],coef[3]))
  print("(x+{6}y+{7})(x+{8}y+{9})".format(coef[0]*coef[3], coef[1]+coef[4], coef[1]*coef[4],coef[2]+coef[5],coef[1]*coef[5]+coef[2]*coef[4], coef[2]*coef[5],coef[1],coef[2],coef[4],coef[5],coef[0],coef[3]))
  print ("")
  print ("ポイント：1つの文字について整理し、因数分解する")
  print("x^2+ {1}xy　+ {2}y^2 +{3}x +{4}y+{5}".format(coef[0]*coef[3], coef[1]+coef[4], coef[1]*coef[4],coef[2]+coef[5],coef[1]*coef[5]+coef[2]*coef[4], coef[2]*coef[5]))
  print("x^2+ {1}xy + {3}x　+ {2}y^2 +{4}y+{5}".format(coef[0]*coef[3], coef[1]+coef[4], coef[1]*coef[4],coef[2]+coef[5],coef[1]*coef[5]+coef[2]*coef[4], coef[2]*coef[5]))
  print("x^2+ ({1}y + {3})x　+ ({6}y+{7})({8}y+{9})".format(coef[0]*coef[3], coef[1]+coef[4], coef[1]*coef[4],coef[2]+coef[5],coef[1]*coef[5]+coef[2]*coef[4], coef[2]*coef[5],coef[1],coef[2],coef[4],coef[5]))
  print("(x+({6}y+{7}))(x+({8}y+{9}))".format(coef[0]*coef[3], coef[1]+coef[4], coef[1]*coef[4],coef[2]+coef[5],coef[1]*coef[5]+coef[2]*coef[4], coef[2]*coef[5],coef[1],coef[2],coef[4],coef[5],coef[0],coef[3]))
  print("(x+{6}y+{7})(x+{8}y+{9})".format(coef[0]*coef[3], coef[1]+coef[4], coef[1]*coef[4],coef[2]+coef[5],coef[1]*coef[5]+coef[2]*coef[4], coef[2]*coef[5],coef[1],coef[2],coef[4],coef[5],coef[0],coef[3]))


  return coef

# In[ ]:



