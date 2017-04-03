# A script to control a series of routers. which can read output of a given command
# in a seperated text file for further processing.
# Author: Adam Mujtaba
import paramiko
from hosts import host

config_file = 'config.txt'
username = 'admin'
password = 'cisco'

SSH = paramiko.SSHClient()
SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy())


for connect in host:
    try:
        print('connecting to ' + host)
        SSH.connect(host, port=22, username=username, password=password)
    except paramiko.ssh_exception.NoValidConnectionsError:
        print('multiple connections were made, please set time delay to the script.')
    except paramiko.ssh_exception.AuthenticationException:
        print('authentication failed')
    except paramiko.ssh_exception.SSHException:
        print('failed to accomodate a connection to the server, please check connection or inputs')
    except Exception:
        print('something went wrong')

    with open(config_file, 'r') as output:
        output_config = output.readlines()
        for line in output_config:
            shell_input, shell_output, shell_error = SSH.exec_command(output_config[line].replace('\n', ''))
            with open('Output.txt', 'w') as writer:
                writer.write(shell_output.read())
                writer.close()
