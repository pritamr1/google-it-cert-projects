import psutil
import emails
import socket

def health_check():
    path = "/"
    errors = []
    cpu_threshold = 80
    memory_threshold = 500 *1024*1024
    disk_threshold = 80
    local_host_ip = "127.0.0.1"

    if psutil.cpu_percent(1) > 80:
        errors.append("Error-CPU usage is over 80%")
    
    if psutil.disk_usage(path).percent > 80:
        errors.append("Error-Available disk space is less than 20%")

    if psutil.virtual_memory().available < memory_threshold:
        errors.append("Error-Available memory is less than 500MB")
    
    if socket.gethostbyname("localhost") != local_host_ip:
        errors.append("Error-localhost cannot be resolved to 127.0.0.1")

    return errors

issues = health_check()
if issues != []:
    for i in issues:
        msg = emails.generate_email("auotmation@example.com", "username@example.com", i,"Please check your system and resolve the issue as soon as possible.")
        emails.send(msg) 