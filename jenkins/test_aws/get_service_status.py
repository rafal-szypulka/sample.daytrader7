import requests
import json
import os
import uuid
import sys
import time

service_id=sys.argv[1]
instance_id=sys.argv[2]

CAM_BEARER_TOKEN=os.environ['CAM_BEARER_TOKEN']

if CAM_BEARER_TOKEN == "":
    print("Not initialized.")
    print("Execute: source cam_api_setup.sh")
    exit(1)

CAM_TENANT_ID=os.environ['CAM_TENANT_ID']
ICP_NAMESPACE=os.environ['ICP_NAMESPACE']
CAM_TEAM_ID=os.environ['CAM_TEAM_ID']
ICP_URL=os.environ['ICP_URL']
CAM_URL=os.environ['CAM_URL']


def getIpAddress(instance):
    #get template output IP address
    #id is hardcoded in service file
    templateMappingId="daytrade4913dc32"
    instanceJson=instance["activity_deployment_details"]["instance"][templateMappingId]
    ipAddress=instanceJson["template_outputs_IP address"]
    print("template_outputs_IP address:")
    print(ipAddress)
    return ipAddress

#services
parameters={"tenantId":CAM_TENANT_ID, "ace_orgGuid":CAM_TEAM_ID, "cloudOE_spaceGuid":ICP_NAMESPACE}
head = {"Authorization": "bearer " + CAM_BEARER_TOKEN, 'Accept':'application/json'}
status="unknown"
while status!="active" and status!="error":
    ret = requests.get(CAM_URL + "/cam/composer/api/v1/ServiceInstances",
                        headers=head,
                        params=parameters,
                        verify=False)

    serviceInstances=ret.json()

    #print(json.dumps(serviceInstances, indent=2, sort_keys=True))
    print("Getting status... "),
    for instance in serviceInstances:
        if instance["ServiceID"]==service_id and instance["id"]==instance_id:
            status=instance["Status"]
            print(status)
            sys.stdout.flush()
            if status != None:
                status = status.lower()
                if status == "active":
                    #get ip address from active status
                    print("instance data:")
                    print(instance)
                    ipAddress=getIpAddress(instance)
                    f=open('IP_ADDRESS', 'w')
                    f.write(ipAddress)
                    f.close()
    time.sleep(10)
        #print(instance["Status"])
        #print("Name: %s ServiceID: %s Instance ID: %s Status: %s" % (instance["name"],instance["ServiceID"],instance["id"],instance["Status"]))

f=open('DEPLOYMENT_STATUS', 'w')
f.write(status)
f.close()

