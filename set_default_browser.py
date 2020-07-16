import subprocess
import os

ext_l = [   '.htm',
            '.html',
            '.mht',
            '.mhtml',
            '.partial',
            '.svg',
            '.url',
            '.website',
            '.xht',
            '.xhtml',
            
            # below should not have leading .
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

# browser_str = 'FirefoxHTML'
browser_str = 'FirefoxHTML-308046B0AF4A39CB'
FTA_abs_path = os.path.dirname(os.path.abspath(__file__)) + '//SetUserFTA//SetUserFTA'

for ext in ext_l:
    cmd = '{} {} {}'.format(FTA_abs_path, ext, browser_str)
    print(cmd)
    print(subprocess.check_output(cmd))