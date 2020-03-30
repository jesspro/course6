#!/usr/bin/env python3

import os
import datetime
import reports
import emails

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
                fruit["weight"]=line[1]
                fruit["name"]=line[0]
        if the_text == "":
            the_text = "<br />".join([str("name: " + fruit["name"]), str("weight: " + fruit["weight"])])
        else:
            the_text = "<br />".join([the_text, "", str("name: " + fruit["name"]), str("weight: " + fruit["weight"])])
    print(the_text)
    return the_text

def main():
    paragraph = get_data()
    today = datetime.date.today().strftime("%B %d, %Y")
    title = "Processed Update on {}".format(today)
    attachment = "/tmp/processed.pdf"
    reports.generate_report(attachment, title, paragraph)
    email = emails.generate_email("automation@example.com", "student-04-e78d857cad20@example.com", "Upload Completed - Online Fruit Store", "All fruits are uploaded to our website successfully. A detailed list is attached to this email.", attachment)
    emails.send_email(email)



if __name__ == "__main__":
    main()


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
