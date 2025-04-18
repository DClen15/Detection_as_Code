#!/usr/bin/python3

command_logs = [
    {"user": "alice", "command": "ls"},
    {"user": "alice", "command": "cd /home"},
    {"user": "alice", "command": "ls"},
    {"user": "alice", "command": "ls"},
    {"user": "alice", "command": "ls"},
    {"user": "bob", "command": "whoami"},
    {"user": "bob", "command": "whoami"},
    {"user": "bob", "command": "cd /root"},
    {"user": "bob", "command": "whoami"},
    {"user": "bob", "command": "whoami"},
    {"user": "bob", "command": "whoami"},
]

'''
Goal: Alert is one user ran the same command three times in a row
'''
def command_alert(command_logs):
    last_command = {}

    for i in command_logs:
        if i['user'] in last_command:
            if last_command[i['user']][0] == i['command']:
                last_command[i['user']][1] += 1
                if last_command[i['user']][1] >= 3:
                    print(f"Suspicious repetition: User {i['user']} ran {i['command']} {last_command[i['user']][1]} times in a row")
            else:
                #last_command[i['user']].pop(count)
                last_command[i['user']] = [i['command'], 1]
        else:
            last_command[i['user']] = [i['command'], 1]


command_alert(command_logs)
