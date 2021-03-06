#!/bin/bash

set -o errexit

#Deploy Daytrader app to ICP
#Step 1 push image
source build.env

__image_name=${APP_NAME}:${VERSION}

echo "Deploying ${__image_name} to ICP..."

source jenkins/prod_icp/variables.sh

#login to icp
docker login ${__docker_registry} -u $ICP_ADMIN_CREDS_USR -p $ICP_ADMIN_CREDS_PSW

#remember to add docker registry certificate 
#https://www.ibm.com/support/knowledgecenter/en/SSBS6K_2.1.0.3/manage_images/configuring_docker_cli.html
#tag and push image
docker tag ${__image_name} ${__icp_image_name}
echo "Pushing ${__image_name} to ICP..."
docker push ${__icp_image_name}
