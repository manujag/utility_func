# pip3 install paramiko
import os
import paramiko
import random

for i in range(10):
    print(random.randint(0, 10))

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

session.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# get the key from private key file
sftp_pkey = paramiko.RSAKey.from_private_key_file(
    filename=pkey_file_path, password=pass_phrase)

# connect to the ssh client
session.connect(hostname=sftp_host, port=22, pkey=sftp_pkey, disabled_algorithms={'pubkeys': ['rsa-sha2-256', 'rsa-sha2-512']},
                allow_agent=False, look_for_keys=False)

# estabalish sftp connection and upload the file to required folder
with session.open_sftp() as ftp_client:
    ftp_client.put(localpath=os.path.join(src_dir, src_file),
                   remotepath=target_dir + r'/' + tgt_file, confirm=True)
