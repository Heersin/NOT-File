import os
import subprocess

# create extracted dir
def bin_scan(target):
    cmd = "binwalk -Me -C ftemp/ "
    type_options = [
            "-D 'png image':'png'",
            "-D 'html:html'",
            "-D 'xml:xml'"]
    full_cmd = cmd + ' '.join(type_options) + ' ' + target
    print("[*]exec bin extraction >> {}".format(full_cmd))
    os.system(full_cmd)