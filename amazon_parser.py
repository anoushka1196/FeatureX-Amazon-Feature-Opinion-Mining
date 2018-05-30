#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import codecs
import csv
import sys
import os
import fnmatch
import re

if sys.version_info[0] >= 3:
    import html


def get_review_filesnames(input_dir):
    for root, dirnames, filenames in os.walk(input_dir):
        for filename in fnmatch.filter(filenames, '*.html'):
            yield os.path.join(root, filename)


idre = re.compile('product\-reviews/([A-Z0-9]+)/ref\=cm_cr_arp_d_hist', re.MULTILINE | re.S)
contentre = re.compile(
    'cm_cr-review_list.*?>(.*?)(?:askReviewsPageAskWidget|a-form-actions a-spacing-top-extra-large|/html)',
    re.MULTILINE | re.S)
blockre = re.compile('a-section review\">(.*?)report-abuse-link', re.MULTILINE | re.S)
ratingre = re.compile('star-(.) review-rating', re.MULTILINE | re.S)
titlere = re.compile('review-title.*?>(.*?)</a>', re.MULTILINE | re.S)
datere = re.compile('review-date">(.*?)</span>', re.MULTILINE | re.S)
reviewre = re.compile('base review-text">(.*?)</span', re.MULTILINE | re.S)
userre = re.compile('profile\/(.*?)["/].*?\<\/div\>.*?\<\/div\>.', re.MULTILINE | re.S)
helpfulre = re.compile('review-votes.*?([0-9]+).*?([0-9]+)', re.MULTILINE | re.S)


def main():
    # sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
    parser = argparse.ArgumentParser(
        description='Amazon review parser')
    parser.add_argument('-d', '--dir', help='Directory with the data for parsing', required=True)
    parser.add_argument('-o', '--outfile', help='Output file path for saving the reviews in csv format', required=True)

    args = parser.parse_args()

    reviews = dict()

    with codecs.open(args.outfile, 'w', encoding='ascii', errors='ignore') as out:
        writer = csv.writer(out, lineterminator='\n')
        for filepath in get_review_filesnames(args.dir):
            with codecs.open(filepath, mode='r', encoding='ascii', errors='ignore') as file:
                htmlpage = file.read()
            if not idre.search(htmlpage):
                continue
            id_ = idre.findall(htmlpage)[0]
            print(id_, filepath)
            htmlpage = contentre.findall(htmlpage)[0]
            for block in blockre.findall(htmlpage):
                title = titlere.findall(block)[0]
                reviewtext = reviewre.findall(block)[0]
                if sys.version_info[0] >= 3:
                    try:
                        title = html.unescape(title)
                    except Exception:
                        pass
                    try:
                        reviewtext = html.unescape(reviewtext)
                    except Exception:
                        pass
                rating = int(ratingre.findall(block)[0])
                date = datere.findall(block)[0]
                user = 'ANONYMOUS'
                usermatch = userre.findall(block)
                if usermatch:
                    user = usermatch[0]
                if rating >= 4:
                    binaryrating = 'positive'
                else:
                    binaryrating = 'negative'
                if sys.version_info[0] >= 3:
                    review_row = [id_, date, user, title, reviewtext, rating, binaryrating]
                else:
                    review_row = [id_, unicode.encode(date, encoding='ascii', errors='ignore'),
                                  unicode.encode(user, encoding='ascii', errors='ignore'),
                                  unicode.encode(title, encoding='ascii', errors='ignore'),
                                  unicode.encode(reviewtext, encoding='ascii', errors='ignore'), rating,binaryrating]
                writer.writerow(review_row)


if __name__ == '__main__':
    main()
