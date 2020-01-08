#transport error: temporary redirect @ cli.service.methods()

from suds.client import Client
import ssl
import logging
import suds
from suds.transport.http import HttpAuthenticated


'''
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)
logging.getLogger('suds.transport').setLevel(logging.DEBUG)
logging.getLogger('suds.xsdschema').setLevel(logging.DEBUG)
logging.getLogger('suds.wsdl').setLevel(logging.DEBUG)
'''

wsdl = 'https://sage-app.averda.co.za:8124/soap-wsdl/syracuse/collaboration/syracuse/CAdxWebServiceXmlCC?wsdl'
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context
cli = Client(wsdl)

print(cli)#working

#callContext from SOAP>>DIctionary>>JSON
callContext = cli.factory.create('CAdxCallContext')
print(callContext) #partially working(Extra PoolID=none; no codeUser; no password)

#create object callContext
#create input
callContext.codeLang = 'ENG'
callContext.poolAlias = 'AVERDADEV'
#only one of the two route configs show (two rout configs same name different values?)
callContext.requestConfig = 'adxwss.trace.on=on&adxwss.trace.size=16384&adonix.trace.on=on&adonix.trace.level=3&adonix.trace.size=8&adxwss.optreturn=JSON&adxwss.beautify=false'
callContext.poolId = 1000

print(callContext)#working with added values

#iets soos dit...buggy not enough input
result = cli.service.getDescription(callContext,'ZDMSAPI2')
print(result)

#result

#<?xml version="1.0" encoding="UTF-8"?>
#<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:ns0="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://schemas.xmlsoap.org/soap/encoding/" xmlns:ns2="http://www.w3.org/2001/XMLSchema" xmlns:ns3="http://www.adonix.com/WSS" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
#   <SOAP-ENV:Header/>
#   <ns0:Body>
#      <ns3:getDescription>
#         <callContext xsi:type="ns3:CAdxCallContext">
#            <codeLang xsi:type="ns2:string">ENG</codeLang>
#            <poolAlias xsi:type="ns2:string">AVERDADEV</poolAlias>
#            <poolId xsi:type="ns2:string">1000</poolId>
#            <requestConfig xsi:type="ns2:string">adxwss.trace.on=on&amp;adxwss.trace.size=16384&amp;adonix.trace.on=on&amp;adonix.trace.level=3&amp;adonix.trace.size=8&amp;adxwss.optreturn=JSON&amp;adxwss.beautify=false</requestConfig>
#         </callContext>
#         <publicName xsi:type="ns2:string">ZDMSAPI2</publicName>
#     </ns3:getDescription>
#   </ns0:Body>
# </SOAP-ENV:Envelope>

#create dictionary for callContext
callContextDict = {}

callContextDict['codeLang'] = 'ENG'
callContextDict['poolAlias'] = 'AVERDADEV'
callContextDict['requestConfig'] = 'adxwss.trace.on=on&adxwss.trace.size=16384&adonix.trace.on=on&adonix.trace.level=3&adonix.trace.size=8&adxwss.optreturn=JSON&adxwss.beautify=false'
callContextDict['poolId'] = 1000

print(callContextDict)#dictionary working

#not enough input for callContext? buggy
try:
    get_Description = cli.service.getDescription(callContextDict,'ZDMSAPI2')
except suds.WebFault as e:
    print(e)

print(get_Description)

#Dict>>JSON
import json
print(json.dumps(callContextDict))

#ArrayOfCAdxParamKeyValue
arrOfParamKeyValue = cli.factory.create('ArrayOfCAdxParamKeyValue')
print(arrOfParamKeyValue)

#create Dict
arrOfParamKeyValueDict = {}

arrOfParamKeyValueDict['_arrayType'] = ""
arrOfParamKeyValueDict['_offset'] = ""
arrOfParamKeyValueDict['_id'] = ""
arrOfParamKeyValueDict['_href'] = ""
#arrOfParamKeyValueDict['_arrayType'] = "" Duplicate?
print(arrOfParamKeyValueDict)

#Dict>>JSON
print(json.dumps(arrOfParamKeyValueDict))

#ArrayOfCAdxMessage
arrayOfCAdxMessage = cli.factory.create('ArrayOfCAdxMessage')
print(arrayOfCAdxMessage)

#create Dict
arrayOfCAdxMessageDict = {}


arrayOfCAdxMessageDict['_arrayType'] = ""
arrayOfCAdxMessageDict['_offset'] = ""
arrayOfCAdxMessageDict['_id'] = ""
arrayOfCAdxMessageDict['_href'] = ""
#arrOfParamKeyValueDict['_arrayType'] = "" Duplicate?
print(arrayOfCAdxMessageDict)

#Dict>>JSON
print(json.dumps(arrayOfCAdxMessageDict))

#ArrayOf_xsd_string
arrayOf_xsd_string = cli.factory.create('ArrayOf_xsd_string')
print(arrayOf_xsd_string)

#create Dict
arrayOf_xsd_stringDict = {}


arrayOf_xsd_stringDict['_arrayType'] = ""
arrayOf_xsd_stringDict['_offset'] = ""
arrayOf_xsd_stringDict['_id'] = ""
arrayOf_xsd_stringDict['_href'] = ""
#arrayOf_xsd_stringDict['_arrayType'] = "" Duplicate?
print(arrayOf_xsd_stringDict)

#Dict>>JSON
print(json.dumps(arrayOf_xsd_stringDict))

#CAdxMessage
cAdxMessage = cli.factory.create('CAdxMessage')
print(cAdxMessage)

#create Dict
cAdxMessageDict = {}


cAdxMessageDict['message'] = None
cAdxMessageDict['type'] = None
print(cAdxMessageDict)

#Dict>>JSON
print(json.dumps(cAdxMessageDict))

#CAdxParamKeyValue
cAdxParamKeyValue = cli.factory.create('CAdxParamKeyValue')
print(cAdxParamKeyValue)

#create Dict
cAdxParamKeyValueDict = {}


cAdxParamKeyValueDict['key'] = None
cAdxParamKeyValueDict['value'] = None
print(cAdxMessageDict)

#Dict>>JSON
print(json.dumps(cAdxParamKeyValueDict))

#CAdxTechnicalInfos
cAdxTechnicalInfos = cli.factory.create('CAdxTechnicalInfos')
print(cAdxTechnicalInfos)

#create Dict
cAdxTechnicalInfosDict = {}


cAdxTechnicalInfosDict['busy'] = None
cAdxTechnicalInfosDict['changeLanguage'] = None
cAdxTechnicalInfosDict['changeUserId'] = None
cAdxTechnicalInfosDict['flushAdx'] = None
cAdxTechnicalInfosDict['loadWebsDuration'] = None
cAdxTechnicalInfosDict['nbDistributionCycle'] = None
cAdxTechnicalInfosDict['poolDistribDuration'] = None
cAdxTechnicalInfosDict['poolEntryIdx'] = None
cAdxTechnicalInfosDict['poolExecDuration'] = None
cAdxTechnicalInfosDict['poolRequestDuration'] = None
cAdxTechnicalInfosDict['poolWaitDuration'] = None
cAdxTechnicalInfosDict['processReport'] = None
cAdxTechnicalInfosDict['processReportSize'] = None
cAdxTechnicalInfosDict['reloadWebs'] = None
cAdxTechnicalInfosDict['resumitAfterDBOpen'] = None
cAdxTechnicalInfosDict['rowInDistribStack'] = None
cAdxTechnicalInfosDict['totalDuration'] = None
cAdxTechnicalInfosDict['traceRequest'] = None
cAdxTechnicalInfosDict['traceRequestSize'] = None
print(cAdxTechnicalInfosDict)

#Dict>>JSON
print(json.dumps(cAdxTechnicalInfosDict))


#CAdxResultXml
cAdxResultXml = cli.factory.create('CAdxResultXml')
print(cAdxResultXml)

#create Dict
cAdxResultXmlDict = {}


cAdxResultXmlDict['messages'] = arrayOfCAdxMessageDict
cAdxResultXmlDict['resltXml'] = None
cAdxResultXmlDict['status'] = None
cAdxResultXmlDict['technicalInfos'] = cAdxTechnicalInfosDict
print(cAdxResultXmlDict)

#Dict>>JSON
print(json.dumps(cAdxResultXmlDict))


















