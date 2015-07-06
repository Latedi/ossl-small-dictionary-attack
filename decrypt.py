#!/usr/bin/env python
import subprocess
import os
fn = open(os.devnull, "w")
passwords = ["password1", "password2", "password3", "etc..."]
commands = ["openssl", "", "-d", "-in", "encrypted_file_name", "-pass", ""]
algorithms = os.popen("openssl list-cipher-commands").read()
algorithms = algorithms.split("\n")
for a in algorithms:
        commands[1] = a
        for p in passwords:
                commands[6] = "pass:" + p
                ret = subprocess.call(commands, stdout=fn, stderr=fn)
                if(ret == 0):
                        ret = os.system("openssl " + a + " -d -in encfile -out ./out/" + a + "-" + p + " -pass pass:" + p)
