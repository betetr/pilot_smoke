#!/bin/bash

function folder_create
{
   local workspace folder
   workspace=${1}
   folder=${2}

   echo "[OWNCLOUD_INFO]: mkdir ${folder} in ${workspace}"
   result=`curl -X MKCOL -u ${OWNCLOUD_USERNAME}:${OWNCLOUD_PASSWORD} "${OWNCLOUD_FILE_API}/${workspace}/${folder}"`
   if [[ ${result} == "" ]]; then
     echo "[OWNCLOUD_INFO]: create folder successfully !!"
     return
   fi
   echo "$result" | grep "already exists</s:message>"
   if [[ $? -eq 0 ]]; then
      echo "[OWNCLOUD_INFO]: create folder successfully !!"
   else
      echo "[OWNCLOUD_ERROR]: create folder failed !!"
      exit 1
   fi

}

function directory_create
{
   local directorys parent
   directorys=${1}
   directorys=${directorys//"/"/" "}
   echo "[OWNCLOUD_INFO]: mkdir -p " ${directorys}

   parent="pilot_prtscn"
   for dir in ${directorys}
   do
     folder_create ${parent} ${dir}
     if [[ $? -eq 1 ]]; then
       exit 1
     fi
     parent="${parent}/${dir}"
   done
   echo "[OWNCLOUD_INFO]: create directory successfully !!"
}

# for example:
# currentTime=`date "+%Y-%m-%d_%H-%M-%S"`
# file_upload TDH-5.0-28859f9e-zh.3.10.0-229.el7.x86_64.tar.gz "transwarp-5.0/IMAGE/centos-7/${currentTime}"
function file_upload
{
   local localFile targetDirectory
   localFile=${1}
   targetDirectory=${2}

   if [[ ! -f $localFile ]]; then
     echo "[OWNCLOUD_ERROR]: No such file or directory: " $localFile
     exit 1
   fi

   directory_create ${targetDirectory}
   result=`curl -u ${OWNCLOUD_USERNAME}:${OWNCLOUD_PASSWORD} --upload-file "${localFile}" "${OWNCLOUD_FILE_API}/pilot_prtscn/${targetDirectory}/"`
   if [[ $? -eq 0 && ${result} == "" ]]; then
     echo "[OWNCLOUD_INFO]: upload file successfully !!"
   else
     echo "[OWNCLOUD_ERROR]: upload file failed !!"
   fi
}

#delete folder or file
function folder_file_delete
{
   local directory
   directory=${1}

   echo "[OWNCLOUD_INFO]: delete ${directory} in ${OWNCLOUD_SERVICE_ADDRESS}"
   result=`curl -X DELETE -u ${OWNCLOUD_USERNAME}:${OWNCLOUD_PASSWORD} "${OWNCLOUD_SERVICE_ADDRESS}/${directory}"`
   if [[ ${result} == "" ]]; then
     echo "[OWNCLOUD_INFO]: delete directory successfully !!"
     return
   fi
   echo "$result" | grep "could not be located</s:message>"
   if [[ $? -eq 0 ]]; then
      echo "[OWNCLOUD_WARN]: no such file or directory, cannot delete !!"
   else
      echo "[OWNCLOUD_ERROR]: delete folder failed !!"
      exit 1
   fi

}

function file_shareToUser
{
   local ownCloudPath shareName username
   ownCloudPath=${1}
   shareName=${2}
   username=${3}

   result=`curl -X POST  --user ${OWNCLOUD_USERNAME}:${OWNCLOUD_PASSWORD} "${OWNCLOUD_SHARE_API}" --data "path=/TRANSWARP_RELEASES/${ownCloudPath}&shareType=0&permissions=1&name=${shareName}&shareWith=${username}"`

   if [[ $? -eq 0 ]]; then
     if [[ ${result} =~ "<status>ok</status>" ]]; then
        echo "[OWNCLOUD_INFO]: share file successfully !!"
        return
     else
        if [[ ${result} =~ "Path already shared with this user</message>" ]]; then
            echo "[OWNCLOUD_INFO]: share file already existed !!"
            return
        else
            echo "[OWNCLOUD_ERROR]: share file failed !!"
            exit 1
        fi
     fi
   else
     echo "[OWNCLOUD_ERROR]: share file failed !!"
     exit 1
   fi
}

#batch_file_delete  INTERNAL/transwarp-5.1/IMAGE/centos-7 /tmp/tmp.2Zm6QAgTdi 10
function batch_file_delete
{
  directory=${1}
  tmpfile=${2}
  surivorNumber=${3}

  curl -X PROPFIND  -u xuekai:xuekai "${OWNCLOUD_FILE_API}/TRANSWARP_RELEASES/${directory}" > ${tmpfile}
  if [[ `cat ${tmpfile} | grep "could not be located</s:message>"` ]]; then
     echo "[OWNCLOUD_ERROR]: no such directory  !!"
     exit 1
  fi
  cat ${tmpfile} | grep "<d:href>" | sed "s/<[^>]*>//g" | sort -r | sed '1d' | sed '$d' | sed "1, ${surivorNumber}d" | while read line
  do
    echo ${line}
    folder_file_delete ${line}
  done
}

#batch_file_delete
#folder_file_delete
#file_shareToUser
#file_upload


