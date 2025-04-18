#!/usr/bin/python3

login_logs = [
    {"user": "alice", "host": "host-001"},
    {"user": "alice", "host": "host-001"},
    {"user": "bob", "host": "host-002"},
    {"user": "bob", "host": "host-002"},
    {"user": "bob", "host": "host-003"},
    {"user": "bob", "host": "host-004"},
    {"user": "bob", "host": "host-005"},
    {"user": "charlie", "host": "host-006"},
    {"user": "charlie", "host": "host-006"},
]

'''
Goal: Identify users who have logged into three or more unique hosts
'''

def lateral_movement(login_logs):
    host_tracking = {}
    
    for i in login_logs:
        if i['user'] not in host_tracking:
            host_tracking[i['user']] = set([i['host']])
        else:
            if i['host'] not in host_tracking[i['user']]:
                host_tracking[i['user']].add(i['host'])
            else:
                continue
            
        if len(host_tracking[i['user']]) >= 3:
            print(f"Lateral movement suspected: User {i['user']} accessed {len(host_tracking[i['user']])} unique hosts!")

lateral_movement(login_logs)
