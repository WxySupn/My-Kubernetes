import os
import argparse
import yaml
import re

def GetImageID(user):
    cmd = "docker ps -a | grep code-pod-"+user+"_code-pod-"+user+"-v2"
    sign = os.popen(cmd).read()

    if sign == "":
        return 0

    pattern = re.compile(r'([0-9a-z]*)([ ]* )')
    image_id = re.match(pattern, sign)
    return image_id.group(1)

if __name__=="__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-u", "--user", default="root")
    parser.add_argument("-n", "--name", default="test")
    parser.add_argument("-t", "--tag", default="v1")

    args = parser.parse_args()
    user = args.user
    name = args.name
    tag  = args.tag

    image_id = GetImageID(user)
    if (image_id == 0):
        print "Not here!"
    else:
        print "Get image_id: "+image_id
        cmd = "docker commit "+image_id+" 219.245.186.40:5000/"+name+":"+tag
        os.system(cmd)
        cmd = "docker push 219.245.186.40:5000/" + name + ":" + tag
        os.system(cmd)