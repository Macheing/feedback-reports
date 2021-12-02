#!/usr/bin/env python3
import socket
import shutil
import psutil
import emails
import os

def cpu_checks():
    '''checks CPU: return True if cpu utilizations is bellow or equals 80%. 
        Otherwise False and alert message is send to an email.
    '''
    cpu_usage = psutil.cpu_percent(interval=1)
    return cpu_usage <= 80

def disk_checks():
    ''' checks disk space: return True if disk space is greater than 20% of its total size.
        otherwise False and alert message is send to an email.
    '''
    disk_space = shutil.disk_usage('/')
    # convert disk free space into percent.
    available_space = (disk_space.used/disk_space.total) * 100
    # check if free space is greater or equals 20%.
    return available_space >= 20

def memory_checks():
    '''checks if available is greater than 500MB. Otherwise False, and alert message is send to an email.'''
    # check virtual memory
    virtual_memory = psutil.virtual_memory()
    # available memory in virtual memory
    available = virtual_memory.available
    # convert available memory to MB
    memory_in_MB = available/1024 **2 
    return memory_in_MB >= 500

def hostname_checks():
    '''return True if localhost is 127.0.0.1. Otherwise False, and alert message is send to an email.'''
    local_host = socket.gethostbyname('localhost')
    return local_host == '127.0.0.1'

def send_warning():
    ''' send warning message (s) to provide email addresses if any of the above functions return False.'''
    # Email contents.
    sender = 'automation@example.com'
    reciever = "{}@example.com".format(os.environ["USER"])
    body = 'Please check your system and resolve the issue as soon as possible.'
    count_emails = 0

    if not cpu_checks():
        # run only when cpu usage is greater than 80%.
        subject = 'Error - CPU usage is over 80%'
        message = emails.generate_email(sender,reciever,subject,body,attachment_path=None)
        emails.send_email(message)
        count_emails += 1
        print('Done sending an email with subject of: {}!'.format(subject))

    if not disk_checks():
        # run only when available disk space is less than 20%.
        subject = 'Error - Available disk space is less than 20%'
        message = emails.generate_email(sender,reciever,subject,body,attachment_path=None)
        emails.send_email(message)
        count_emails += 1
        print('Done sending an email with subject of: {}!'.format(subject))

    if not memory_checks():
        # run only when available memory is less than 500MB.
        subject = 'Error - Available memory is less than 500MB'
        message = emails.generate_email(sender,reciever,subject,body,attachment_path=None)
        emails.send_email(message)
        count_emails += 1
        print('Done sending an email with subject of: {}!'.format(subject))
    
    if not hostname_checks():
        # run on when hostname "localhost" cannot be resolved to "127.0.0.1".
        subject = 'Error - localhost cannot be resolved to 127.0.0.1'
        message = emails.generate_email(sender,reciever,subject,body,attachment_path=None)
        emails.send_email(message)
        count_emails += 1
        print('Done sending an email with subject of: {}!'.format(subject))

    else:
        # run only when system is running ok.
        print('Your system is running smoothly!')
    
    # display number of alert messages sent to the provided email address(es)
    return 'You have ({}) alert message(s) in your email inbox.'.format(count_emails)

# calling the function.
print(send_warning())

 # To test this script, install the stress tool.
 # run sudo apt install stress
 # run stress --cpu 8 
 # run ./health_check.py in another terminal
