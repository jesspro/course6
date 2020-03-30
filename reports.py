#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(attachment, title, paragraph):

    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(attachment)
    report_title = Paragraph(title, styles["H1"])
    #report_info = Paragraph(paragraph, styles["BodyText"])
    empty_line = Spacer(1,20)

    report_structure = [report_title, empty_line]
    fruits = paragraph.split("<br /><br />")
    for fruit in fruits:
        report_info = Paragraph(fruit, styles["BodyText"])
        report_structure.append(report_info)
        report_structure.append(empty_line)    
    report.build([report_structure])
