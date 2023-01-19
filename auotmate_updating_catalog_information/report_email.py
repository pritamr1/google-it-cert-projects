#!/usr/bin/env python3
import os
import datetime
import reports
import emails

def gen_pdf_content():
    json_data = []
    path = r"/home/student-02-26b21f26a289/supplier-data/descriptions/"
    files = os.listdir(path)

    for file in files:
        if file[-3:] == "txt":
            with open(path + file, 'r') as f:
                info = f.readlines()
                info = [x.replace("\n","") for x in info]
                json_format = {}
                json_format["name"] = info[0]
                json_format["weight"] = info[1]
                json_data.append(json_format)

    pdf_string = ""

    for i in json_data:
        pdf_string += "name:" + i["name"] + "<br/>" + "weight:" +i["weight"] + "<br/><br/>"

    day = datetime.date.today()
    title = "Processed Update on "+day.strftime("%B")+" " +day.strftime("%d")+", " + day.strftime("%Y")

    return pdf_string, title


if __name__ == "__main__":
    pdf_string, title = gen_pdf_content()
    reports.generate_report("/tmp/processed.pdf" , title, pdf_string)
    msg = emails.generate_email("automation@example.com", "username@example.com", "Upload Completed-Online Fruit Store", 
                               "All fruits are uploaded to our website successfully. A detailed list is attached to this email", "/tmp/processed.pdf")
    emails.send(msg)
