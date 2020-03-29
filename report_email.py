#!/usr/bin/env python3

import os
from datetime import date
import reports
import emails
import sys

path = os.path.normpath(os.path.join(os.getcwd(), "supplier-data", "descriptions"))
fruit = {}


def get_data():
    the_text = ""
    for item in os.listdir(path):
        fruit.clear()
        filename=os.path.join(path,item)
        with open(filename) as f:
            line=f.readlines()
            for i in range(2,len(line)):
                fruit["weight"]=line[1].strip('\n')
                fruit["name"]=line[0].strip('\n')
        if the_text == "":
            the_text = "<br/>".join([str("name: " + fruit["name"]), str("weight: " + fruit["weight"])])
        else:
            the_text = "<br/>".join([the_text, "", str("name: " + fruit["name"]), str("weight: " + fruit["weight"])])
    print(the_text)
    return the_text

def main(argv):
    data = get_data()
    today = date.today().strftime("%B %d, %Y")
    title = "Processed Update on {}".format(today)
    reports.generate_report("/tmp/processed.pdf", title, data)
    email = emails.generate_email("automation@example.com", "student-01-aba8cdda2c75@example.com", "Upload Completed - Online Fruit Store", "All fruits are uploaded to our website successfully. A detailed list is attached to this email.", "/tmp/processed.pdf")
    emails.send_email(email)

  # TODO: send the PDF report as an email attachment


if __name__ == "__main__":
    main(sys.argv)


# import all the necessary libraries(os, datetime and reports)
# that will be used to process the text data from the
# supplier-data/descriptions directory into the format below:

# name: Apple
#
# weight: 500 lbs
#
# [blank line]
#
# name: Avocado
#
# weight: 200 lbs
#
# [blank line]
#
# Once you have completed this, call the main method which will
# process the data and call the generate_report method from the
# reports module:

# if __name__ == "__main__":

# You will need to pass the following arguments to the
# reports.generate_report method: the text description processed
# from the text files as the paragraph argument, the report title
# as the title argument, and the file path of the PDF to be
# generated as the attchment argument (use "/tmp/processed.pdf")

# reports.generate_report(attachment, title, paragraph)
