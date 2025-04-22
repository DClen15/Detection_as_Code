#!/usr/bin/python3
import json
import math

download_logs = [
    {"user": "alice", "file": "Q1_Report.pdf", "date": "2025-04-10"},
    {"user": "alice", "file": "Q2_Report.pdf", "date": "2025-04-10"},
    {"user": "alice", "file": "VacationPolicy.docx", "date": "2025-04-09"},
    {"user": "bob", "file": "SalesData.csv", "date": "2025-04-10"},
    {"user": "bob", "file": "Q1_Report.pdf", "date": "2025-04-09"},
    {"user": "bob", "file": "Q2_Report.pdf", "date": "2025-04-09"},
    {"user": "bob", "file": "Q3_Report.pdf", "date": "2025-04-09"},
    {"user": "bob", "file": "Q4_Report.pdf", "date": "2025-04-10"},
    {"user": "charlie", "file": "LegalAgreement.docx", "date": "2025-04-10"},
    {"user": "charlie", "file": "CustomerList.csv", "date": "2025-04-10"},
    {"user": "charlie", "file": "AuditData.xlsx", "date": "2025-04-10"},
    {"user": "charlie", "file": "TaxDocs.pdf", "date": "2025-04-10"},
    {"user": "charlie", "file": "MergersPlan.pptx", "date": "2025-04-10"},
]


'''
Goal: Track a users downloads per day. If there downloads doubles the next day flag it.
Day 1: Downloaded 2 Files
Day 2: Downloaded 4 Files (ALERT)
Day 1: Downloaded 2 Files
Day 2: Downloaded 3 Files (no alert)
'''

def baseline(download_logs):
    #Make a JSON like structure to accumualate the averages
    avg_download = {}
    for i in download_logs:
    
        if i['user'] not in avg_download:
            avg_download[i['user']] = {i['date'] : [i['file']]}
        elif i['date'] not in avg_download[i['user']]:
            avg_download[i['user']][i['date']] = [i['file']]
        else:
            avg_download[i['user']][i['date']] += [i['file']]

    return avg_download

def track_average(avg_download):
    #Calculate the average download per day for each user
    #Total files/total days (round down)

    days = 0
    files = 0
    user_avg = {}
    for key,value in avg_download.items():
        for key2, value2, in value.items():
            files += len(value2)
            days += 1
        average = math.floor(files/days)
        user_avg[key] = average


    #Calculate if the current days download is above the baselined average
    #If yes, alert!

    #key = alice
    #value = {date: [files], date2: [files]}
    for key,value in avg_download.items():
        #key2 = date
        #value2 = [files]
        for key2, value2 in value.items():
            if len(value2) > user_avg[key]:
                print(f"Anomaly detected: User {key} downloaded {len(value2)} files on {key2} (average: {user_avg[key]} per day)")


result = baseline(download_logs)

track_average(result)
