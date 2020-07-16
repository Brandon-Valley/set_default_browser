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

# helpful for finding prog_id:  https://www.techwalla.com/articles/how-to-find-progi
browser_prog_id = 'FirefoxHTML-308046B0AF4A39CB'
FTA_abs_path = os.path.dirname(os.path.abspath(__file__)) + '//SetUserFTA//SetUserFTA'

for ext in ext_l:
    cmd = '{} {} {}'.format(FTA_abs_path, ext, browser_prog_id)
    print(cmd)
    print(subprocess.check_output(cmd))