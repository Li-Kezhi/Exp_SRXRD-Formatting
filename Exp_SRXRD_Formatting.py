#!/usr/bin/python
#coding=utf-8

'''
To convert data obtained from Beijing Synchrome Radiation SR-XRD to two columns

Original data contains three colomns: 2theta angles, output signal and input signal
'''

__author__ = "LI Kezhi" 
__date__ = "$2016-10-13$"
__version__ = "1.0"

folder = r'E:\SkyDrive\Sharing data\SRXRD\20161010_MnFe\Raw Data' + '\\'
name = r'Fe25.txt'
route = folder + name

lineNum = 0
output = open(folder + 'Formatted\\' + name + '.dat', 'w')
for line in open(route, 'r'):
    if lineNum >= 2:
        splitting = line.split('\t')
        angle = float(splitting[0])
        signal = float(splitting[1]) / float(splitting[2])    # divided by initial intensity
        output.writelines('%9.5f\t%12.8f\n' % (angle, signal))
    lineNum += 1
output.close()