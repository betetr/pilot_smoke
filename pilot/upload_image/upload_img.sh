#!/bin/bash

source /home/lc/Desktop/owncloud_setting.sh
source /home/lc/Desktop/owncloud_operation.sh

work_dir=$(pwd)
target_dir='/report/image'
save_dir=`date +%Y-%m-%d-%H:%M`
for file in ${work_dir}${target_dir}/*;do
    temp_file=$file
    echo $temp_file
    file_upload $temp_file $save_dir 
done
 
