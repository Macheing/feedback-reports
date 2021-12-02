#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(filename, title, info):
    '''generate a simple pdf report inform of 1-dimensional list. '''
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"], encoding='utf8')
    report_info = Paragraph(info, styles["BodyText"], encoding='utf8')
    empty_line = Spacer(1,20)
    report.build([report_title, empty_line, report_info, empty_line])