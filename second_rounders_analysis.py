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