# Common variables

export PATH=~/.local/bin/:$PATH

#set work dir because jenkins executes this from parent dir
export __work_dir=jenkins/dev_aws

#hardcoded template name
export CAM_SERVICE_NAME="DaytraderAtFrankfurt"

export __ver=$(cat VERSION) 
export __tar_name=${APP_NAME}.tar

export __gz_name=${__tar_name}.gz

#Docker image was build in previous Jenkins stage
export __docker_image_name=${APP_NAME}:latest
