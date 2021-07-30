#!/bin/bash
# run pln model using the docker gpu image (adapted from Toni's script)

#cmd_line="python3 /root/myrace/manage.py drive --model=/root/myrace/models/mymodel.h5"
cmd_line="python3 /root/myrace/manage.py drive --model /root/myrace/models/mypilot_circuit_launch_16.h5 --myconfig=myconfig-trnm.py"

echo "Executing in the docker (gpu image):"
echo $cmd_line

docker run -it --rm --network host \
  altexdim/donkeycar_race2:v1 \
  bash -c "cd /root/myrace/ && $cmd_line"

