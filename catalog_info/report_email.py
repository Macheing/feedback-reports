#!/usr/bin/env python3
import os, datetime
import reports
import emails

# current date
today_date = datetime.datetime.now().strftime("%b %d, %Y")

def pdf_generate(path):
    pdf_content = ''
    files = os.listdir(path)
    for file in files:
        if file.endswith('.txt'):
            with open(path + file, 'r') as open_file:
                data = open_file.readlines()
                # show data would appear in pdf file
                pdf_format = 'name: '+data[0] + '<br/>' + 'weight: ' + data[1] + '<br/><br/>'
                pdf_content += pdf_format
        else:
            # file doesn't have .txt extension
            continue
    print('Done generating pdf content!')
    return pdf_content

if __name__=='__main__':
    # data path
    path = 'supplier-data/descriptions/'
    # generate report by passing pdf contents, tile of report, report file name.
    content = pdf_generate(path=path)
    title = 'process Updated on ' + today_date
    reports.generate_report('/tmp/processed.pdf', title, content)
    # email contents
    sender = 'automation@example.com'
    reciever = "{}@example.com".format(os.environ["USER"])
    subject = "Upload Completed - Online Fruit Store"
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    attachement = "/tmp/processed.pdf"
    # compose an email by passing sender and reciever emails, subject line, body or main message and attachment.
    message = emails.generate_email(sender,reciever,subject,body,attachement)
    # send an email to a concerned email address
    emails.send_email(message)
    print('Done sending an email!')
