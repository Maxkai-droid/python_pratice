import subprocess                                                      
                                                                
def getresult(arg1):                                            
  p = subprocess.Popen(arg1, stdout=subprocess.PIPE, shell=True)
  (text, err) = p.communicate()           
  res = text.decode(errors='ignore')      
  return res      
def get_dmidecode_info(str,skip = []):
  rs = []
  cmd = "dmidecode -t memory | %s "%(str)
  ip = getresult(cmd) 
  if len(ip) >= 1 :
    ip =  ip.strip().split("\n")
    for line in ip:
      colon = line.strip().split(":")
      if 'DIMM' in colon[1]:
        floag = colon[1].strip().split("_")
        colon[1] = floag[1]
      rs.append(colon[1].strip())    
  return rs   
def get_DIMM_info():
  size = get_dmidecode_info("grep -w 'Size:' | grep -v 'Cache\|Non*\|Vol*' ")
  Vendor = get_dmidecode_info("grep -w 'Manufacturer:'")
  speed = get_dmidecode_info("grep -w 'Speed:' | grep -v 'Config*'")
  type = get_dmidecode_info("grep -w 'Type:' | grep -v 'Error' ")
  location  =get_dmidecode_info("grep -w 'Locator:' | grep -v 'Bank'")
  pn = get_dmidecode_info("grep -w 'Part Number:'")
  sn = get_dmidecode_info("grep -w 'Serial Number:'")
  empty = []
  flag = 0
  for i in reversed(range(len(type))):
    if 'Unknown' in type[i]:
      empty.append(i)
    flag= flag+1  
  if len(empty) > 0:
    for i in empty:
      del location[i]
      del type[i]
  file1 = open("DIMM_log.txt", "w")
  for k in range(len(size)):
    file1.writelines('%s \t %s \t %s \t %s \t %s \t %s \t %s \n'%(size[k],Vendor[k],speed[k],type[k],location[k],pn[k],sn[k]))
  file1.close()
  file1 = open('DIMM_log.txt', 'r')
  print(file1.read())
  file1.close()
get_DIMM_info()