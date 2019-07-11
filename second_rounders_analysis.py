#!/usr/bin/env python
# coding: utf-8

from datascience import *
import numpy as np

# access the csv file
picks_data = Table.read_table("second_rounders_2005-14.csv")

# General analysis
avg_yrs = round(np.mean(picks_data.column('Yrs')))
avg_games = round(np.mean(picks_data.column('G')))
avg_pts = round(np.mean(picks_data.column('PTS_per_G')), 1)
avg_vorp = round(np.mean(picks_data.column('VORP')), 1)
print("The average second rounder will have a " + str(avg_yrs) + " year career.")
print("The average second rounder will play " + str(avg_games) + " games in their career.")
print("The average second rounder score " + str(avg_pts) + " points per game in their career.")
print("The average second rounder brings " + str(avg_vorp) + " value over replacement player (VORP) throughout their career.")

# average games per draft year
for i in range(2005, 2015):
    year_data = picks_data.where("Draft Year", are.equal_to(i))
    draftyr_yrs = round(np.mean(year_data.column('G')))
    print(str(i) + " draftees played an average of " + str(draftyr_yrs) + " games in their career.")

# Output
'''
The average second rounder will have a 3.0 year career.
The average second rounder will play 152.0 games in their career.
The average second rounder score 3.6 points per game in their career.
The average second rounder brings 1.3 value over replacement player (VORP) throughout their career.
2005 draftees played an average of 285.0 games in their career.
2006 draftees played an average of 150.0 games in their career.
2007 draftees played an average of 135.0 games in their career.
2008 draftees played an average of 163.0 games in their career.
2009 draftees played an average of 211.0 games in their career.
2010 draftees played an average of 70.0 games in their career.
2011 draftees played an average of 150.0 games in their career.
2012 draftees played an average of 162.0 games in their career.
2013 draftees played an average of 89.0 games in their career.
2014 draftees played an average of 102.0 games in their career.
'''