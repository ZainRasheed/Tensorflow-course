# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 00:40:58 2020

Introduction to tensor flow
- Installing Tensor flow
- Basic tensorflow programming
- Linear regression with tensor flow

@author: MohammedS2
"""

"""ÏNSTALLING TENSORFLOW 2.0"""
"""
Create a different environment
$ conda create --name tensorflow2 python=3.7 anaconda
$ conda activate tensorflow2

Go to the cmd from navigator
$ python --version
$ python -m pip install --upgrade pip
$ pip install tensorflow
$ pip install --upgrade tensorflow==2.0.0-rc1 --user  or the latest version tensorflow==2.1.0-rc1 --user 

To verify the installation
$conda list
Check the tensorflow module's version
"""
import tensorflow as tf

print(tf.version)


"""TENSOR AND SESSION"""
"""
Tensor is a partially defined computation vector, it can have one no dimenstion, one dimension, and more.

Session is to execute created sessions.
"""

#Create a Tensor  SCALAR TENSOR/ NO DIMENSION
string_variable = tf.Variable("Dummy string", tf.string)
int_variable = tf.Variable(123, tf.int64)
float_ariable = tf.Variable(1.234, tf.float64)
print(string_variable, int_variable, float_ariable)
#OUTPUT
# <tf.Variable 'Variable:0' shape=() dtype=string, numpy=b'Dummy string'>
# <tf.Variable 'Variable:0' shape=() dtype=int32, numpy=123>
# <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=1.234>

#RANK/DEGREE TENSOR
rank1_tensor = tf.Variable(["Dummy1"], tf.string)  #Rank 1, on 1d array 
rank2_tensor = tf.Variable(["First row", "Second column"], ["second row", "second column"], ["third row", "second column"]) #A matrix of 3x2
print(rank1_tensor, rank2_tensor) 
#OUTPUT
# <tf.Variable 'Variable:0' shape=() dtype=string, numpy=b'Dummy string'> <tf.Variable 'Variable:0' shape=() dtype=int32, numpy=123> <tf.Variable 'Variable:0' shape=() dtype=float32, numpy=1.234>
# <tf.Variable 'Variable:0' shape=(2,) dtype=string, numpy=array([b'Dummy1', b'Dummy2'], dtype=object)> <tf.Variable 'Variable:0' shape=(2,) dtype=string, numpy=array([b'First row', b'Second column'], dtype=object)>

tf.rank(rank1_tensor)


