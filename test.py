import subprocess
print(subprocess.check_output("cat /var/log/auth.log", stderr=subprocess.STDOUT, shell=True))