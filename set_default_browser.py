import subprocess
import os

ext_l = [   'htm',
            'html',
            'mht',
            'mhtml',
            'partial',
            'svg',
            'url',
            'website',
            'xht',
            'xhtml',
            'FTP',
            'HTTP',
            'https',
            'http',
            'MK',
            'RES'
        ]

# SetuserFTA  http FirefoxHTML
# SetuserFTA  https FirefoxHTML
# SetuserFTA  .htm FirefoxHTML
# SetuserFTA  .html FirefoxHTML
# SetuserFTA  .url FirefoxHTML

browser_str = 'FirefoxHTML'
FTA_abs_path = 'SetUserFTA/SetUserFTA'

for ext in ext_l:
    cmd = FTA 
