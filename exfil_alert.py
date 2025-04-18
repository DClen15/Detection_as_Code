#!/usr/bin/python3

dns_logs = [
    {"user": "alice", "domain": "login.aws.amazon.com"},
    {"user": "alice", "domain": "session.aws.amazon.com"},
    {"user": "bob", "domain": "aaaabbbbccccddddeeeeffff.exfil.com"},
    {"user": "bob", "domain": "1234567890abcdef.exfil.com"},
    {"user": "bob", "domain": "notmalicious.com"},
    {"user": "charlie", "domain": "data.leak-domain.io"},
    {"user": "charlie", "domain": "a" * 70 + ".leak-domain.io"}  
]

'''
Goal: Output users who have made at least two queries to a suspicious domain
- domain that is not allow listed
- domain with high entropy (subdomain over 50 characters)
'''

#if subdomain > 50 ALERT
#if rootdomain not in allowed_domains ALERT
def dns_exfil_alert(dns_logs):

    allowed_domains = ['amazon.com', 'notmalicious.com']
    suspicious_query = {}

    for i in dns_logs:
        root = i['domain'].split('.')
        reverse = root[::-1]
        if reverse[1] not in allowed_domains:
            if i['user'] in suspicious_query:
                suspicious_query[i['user']] += 1
            else:
                suspicious_query[i['user']] = 1
    
        for x in reverse[1:]:
            if len(x) > 50:
                if i['user'] in suspicious_query:
                    suspicious_query[i['user']] += 1
                else:
                    suspicious_query[i['user']] = 1

        if suspicious_query[i['user']] >= 2:
            print(f"Potential exfiltration detected: User {i['user']} queried suspicious domain {i['domain']}")

    #print(suspicious_query)

dns_exfil_alert(dns_logs)

