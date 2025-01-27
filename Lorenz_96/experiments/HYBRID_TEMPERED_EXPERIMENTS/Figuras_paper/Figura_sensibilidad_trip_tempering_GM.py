#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 15:50:17 2020

@author: jruiz
"""
import pickle
import sys
sys.path.append('../model/')
sys.path.append('../data_assimilation/')
import matplotlib.pyplot as plt

import numpy as np
#import sensitivity_conf_default as conf
#import assimilation_ripgm_module as ahm

#===========================================================================================================
#    LEO LOS EXPERIMENTOS DE TEMPERING 
#===========================================================================================================

file_list=['../../npz/Sesitivity_experiment_temp_multif_gm_NatureR4_Den05_Freq8_Hcuadratic.npz',
           '../../npz/Sesitivity_experiment_temp_multif_gm_NatureR4_Den05_Freq8_Hlogaritmic.npz',
           '../../npz/Sesitivity_experiment_temp_multif_gm_NatureR8_Den05_Freq8_Hlinear.npz']

analysis_rmse_temp=[]
forecast_rmse_temp=[] 
analysis_sprd_temp=[]
forecast_sprd_temp=[]
    
for my_file in file_list : 

   f=open(my_file,'rb')
   [results,mult_inf_range,nrip_range,total_analysis_rmse,total_forecast_rmse,total_analysis_sprd,total_forecast_sprd] = pickle.load(f)
   f.close()
   
   analysis_rmse_temp.append( total_analysis_rmse )
   analysis_sprd_temp.append( total_analysis_sprd ) 
   forecast_rmse_temp.append( total_forecast_rmse )
   forecast_sprd_temp.append( total_forecast_sprd )

#===========================================================================================================
#    LEO LOS EXPERIMENTOS DE RIP
#===========================================================================================================

file_list=['../../npz/Sesitivity_experiment_rip_multif_gm_NatureR4_Den05_Freq8_Hcuadratic.npz',
           '../../npz/Sesitivity_experiment_rip_multif_gm_NatureR4_Den05_Freq8_Hlogaritmic.npz',
           '../../npz/Sesitivity_experiment_rip_multif_gm_NatureR8_Den05_Freq8_Hlinear.npz']

analysis_rmse_rip=[]
forecast_rmse_rip=[] 
analysis_sprd_rip=[]
forecast_sprd_rip=[]
    
for my_file in file_list : 

   f=open(my_file,'rb')
   [results,mult_inf_range,nrip_range,total_analysis_rmse,total_forecast_rmse,total_analysis_sprd,total_forecast_sprd] = pickle.load(f)
   f.close()
   
   analysis_rmse_rip.append( total_analysis_rmse )
   analysis_sprd_rip.append( total_analysis_sprd ) 
   forecast_rmse_rip.append( total_forecast_rmse )
   forecast_sprd_rip.append( total_forecast_sprd )


plt.figure()

plt.subplot(2,2,1)

plt.plot( analysis_sprd_temp[0][:,0] , analysis_rmse_temp[0][:,0] ,'b-')
plt.plot( analysis_sprd_temp[0][:,1] , analysis_rmse_temp[0][:,1] ,'g-')
plt.plot( analysis_sprd_temp[0][:,3] , analysis_rmse_temp[0][:,3] ,'r-')

#plt.plot( analysis_sprd_adtemp[0][:,0] , analysis_rmse_adtemp[0][:,0] ,'b--')
plt.plot( analysis_sprd_rip[0][:,1] , analysis_rmse_rip[0][:,1] ,'g--')
plt.plot( analysis_sprd_rip[0][:,3] , analysis_rmse_rip[0][:,3] ,'r--')

plt.ylim(bottom=2.4,top=3.5)
plt.xlim(left=2.5,right=4.5)
plt.grid(axis='both')

plt.ylabel('RMSE')
plt.title('Cuadratic operator')

plt.subplot(2,2,2)

plt.plot( analysis_sprd_temp[1][:,0] , analysis_rmse_temp[1][:,0] ,'b-')
plt.plot( analysis_sprd_temp[1][:,1] , analysis_rmse_temp[1][:,1] ,'g-')
plt.plot( analysis_sprd_temp[1][:,3] , analysis_rmse_temp[1][:,3] ,'r-')

#plt.plot( analysis_sprd_adtemp[1][:,0] , analysis_rmse_adtemp[1][:,0] ,'b--')
plt.plot( analysis_sprd_rip[1][:,1] , analysis_rmse_rip[1][:,1] ,'g--')
plt.plot( analysis_sprd_rip[1][:,3] , analysis_rmse_rip[1][:,3] ,'r--')

plt.ylim(bottom=0.6,top=1.4)
plt.xlim(left=0.6,right=0.97)
plt.grid(axis='both')

plt.ylabel('RMSE')
plt.title('Logaritmic operator')

plt.subplot(2,2,3)

plt.plot( analysis_sprd_temp[2][:,0] , analysis_rmse_temp[2][:,0] ,'b-')
plt.plot( analysis_sprd_temp[2][:,1] , analysis_rmse_temp[2][:,1] ,'g-')
plt.plot( analysis_sprd_temp[2][:,3] , analysis_rmse_temp[2][:,3] ,'r-')

#plt.plot( analysis_sprd_adtemp[2][:,0] , analysis_rmse_adtemp[2][:,0] ,'b--')
plt.plot( analysis_sprd_rip[2][:,1] , analysis_rmse_rip[2][:,1] ,'g--')
plt.plot( analysis_sprd_rip[2][:,3] , analysis_rmse_rip[2][:,3] ,'r--')

plt.ylim(bottom=1.5,top=1.8)
plt.xlim(left=1.6,right=1.9)
plt.grid(axis='both')

plt.ylabel('RMSE')
plt.title('Linear operator')


plt.savefig('./Figura_sensibilidad_trip_tempering_GM.png')

    # import matplotlib.pyplot as plt 

    # plt.pcolormesh(nrip_range,mult_inf_range,total_analysis_rmse)
    # plt.colorbar()
    # plt.title('Analysis Rmse')
    # plt.xlabel('Rip Iterantions')
    # plt.ylabel('Multiplicative Inflation')
    # plt.show()

    # plt.plot(total_analysis_sprd[:,0],total_analysis_rmse[:,0]);plt.plot(total_analysis_sprd[:,1],total_analysis_rmse[:,1]);plt.plot(total_analysis_sprd[:,-1],total_analysis_rmse[:,-1])


    # plt.show()


