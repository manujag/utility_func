# pip3 install paramiko
# pip3 install pysftp
import os
import pysftp
import paramiko
from io import StringIO

sftp_host = 'sftp_host_name'
sftp_user = ''  # username
pass_phrase = ''
pkey_text = ''
target_dir = r'/public/'
src_dir = ''
src_file = 'test.txt'
tgt_file = src_file

key_file_obj = StringIO(pkey_text)

# get the key from private key file
sftp_pkey = paramiko.RSAKey.from_private_key(
    file_obj=key_file_obj, password=pass_phrase)

# connect to the ssh client
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
with pysftp.Connection(sftp_host, username=sftp_user, private_key=sftp_pkey) as sftp:
    sftp.put(localpath=os.path.join(src_dir, src_file),
             remotepath=target_dir + r'/' + tgt_file, confirm=True)
