#pip3 install paramiko

import paramiko
import os

sftp_host = 'sftp_host_name'
sftp_user = ''  # username
pass_phrase = ''
pkey_file_path = ''
target_dir = r'/public/'
src_dir = ''
src_file = 'test.txt'
tgt_file = src_file


# create an ssh cleint for the session
session = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect('<hostname>', username='<username>', password='<password>', key_filename='<path/to/openssh-private-key-file>')

stdin, stdout, stderr = ssh.exec_command('ls')
print stdout.readlines()
ssh.close()
'''

session.load_system_host_keys()
# get the key from private key file
sftp_pkey = paramiko.RSAKey.from_private_key_file(
    filename=pkey_file_path, password=pass_phrase)

# connect to the ssh client
session.connect(hostname=sftp_host, port=22, pkeys=sftp_pkey,
                allow_agent=False, look_for_keys=False)
'''
# estabalish sftp connection and upload the file to required folder
with session.open_sftp() as ftp_client:
    ftp_client.put(localpath=os.path.join(src_dir, src_file),
                   remotepath=target_dir + r'/' + tgt_file, confirm=True)
