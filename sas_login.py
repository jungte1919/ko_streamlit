
import saspy
import sys
import requests
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=ResourceWarning)
warnings.filterwarnings("ignore", category=ImportWarning)

version=str(sys.version_info.major)+'.'+str(sys.version_info.minor)
print(version)


def SASLogin(id, pw, sys='viya',server="Asia Pacific Home Region 1") :
  if sys == 'viya' :
    sas = saspy.SASsession(ip='147.47.206.193', user=str(id), pw=str(pw), verify=False, context='SAS Studio compute context', encoding='utf-8')
  if (sys == 'oda' and server == "US Home Region 1") :
    sas = saspy.SASsession(java='/usr/bin/java', iomhost = ['odaws01-usw2.oda.sas.com','odaws02-usw2.oda.sas.com','odaws03-usw2.oda.sas.com','odaws04-usw2.oda.sas.com'], iomport=8591, encoding='utf-8', omruser=str(id), omrpw=str(pw))
  elif (sys == 'oda' and server == "US Home Region 2") :
    sas = saspy.SASsession(java='/usr/bin/java', iomhost =['odaws01-usw2-2.oda.sas.com','odaws02-usw2-2.oda.sas.com'], iomport=8591, encoding='utf-8', omruser=str(id), omrpw=str(pw))
  elif (sys == 'oda' and server == "European Home Region 1") :
    sas = saspy.SASsession(java='/usr/bin/java', iomhost =['odaws01-euw1.oda.sas.com','odaws02-euw1.oda.sas.com'], iomport=8591, encoding='utf-8', omruser=str(id), omrpw=str(pw))
  elif (sys == 'oda' and server == "Asia Pacific Home Region 2") :
    sas = saspy.SASsession(java='/usr/bin/java', iomhost =['odaws01-apse1-2.oda.sas.com','odaws02-apse1-2.oda.sas.com'], iomport=8591, encoding='utf-8', omruser=str(id), omrpw=str(pw))
  elif (sys == 'oda' and server == "Asia Pacific Home Region 1") :
    sas = saspy.SASsession(java='/usr/bin/java', iomhost =['odaws01-apse1.oda.sas.com','odaws02-apse1.oda.sas.com'], iomport=8591, encoding='utf-8', omruser=str(id), omrpw=str(pw))
  return sas
