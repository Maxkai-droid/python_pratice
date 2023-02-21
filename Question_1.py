import subprocess                                                                                           
import re                                                       
import math                                                     
                                                                
def getresult(arg1):                                            
  p = subprocess.Popen(arg1, stdout=subprocess.PIPE, shell=True)
  (text, err) = p.communicate()           
  res = text.decode(errors='ignore')      
  return res                              
                                          
def is_float(string):                     
  pattern= r"^[-+]?[0-9]*\.?[0-9]+$"      
  match = re.match(pattern,string)        
  return bool(match) 

def get_ave_sum_inputPower():
  cmd = "rackmoninfo  |grep 'Input Power'"                      
  ip = getresult(cmd)          
  if len(ip) >= 1 :                             
    ip =  ip.strip().split("\n")
    total = 0
    total_ave = 0                            
    for line in ip:       
      value = line.strip().split(" ")  
      sum_input = math.fsum(float(x) for x in value if is_float(x))
      av_input = sum_input/sum(1 for x in value if is_float(x))                                      
      print('%s | %.3f | %.3f'%(line,sum_input,av_input))
      total = total + sum_input 
      total_ave += av_input
    print ('Total: %.3f | avg total: %.3f '%(total,total_ave/len(ip)))

get_ave_sum_inputPower()       

