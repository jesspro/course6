#!/usr/bin/env python3

import os
from datetime import date
import reports

path = os.path.normpath(os.path.join(os.getcwd(), "supplier-data", "descriptions"))



def get_data(directory)
    the_text = ""
    for item os.listdir(directory):
        fruit.clear()
        filename=os.path.join(directory,item)
        with open(filename) as f:
            line=f.readlines()
            for i in range(2,len(line)):
                fruit["weight"]=int(line[1].strip('\n'))
                fruit["name"]=line[0].strip('\n')
        the_text = "</ br>".join(("name: " + fruit["name"]), ("weight: " + fruit["weight"], "", the_text))
    print(the_text)
    return the_text

def main(argv):
  data = get_data(path)
  today = date.today()
  title = "Processed Update on {}".format(today)
  reports.generate_report("/tmp/processed.pdf", title, data)


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
