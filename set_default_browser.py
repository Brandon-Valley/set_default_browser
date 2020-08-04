import subprocess
import os

# helpful for finding prog_id:  https://www.techwalla.com/articles/how-to-find-progid
#     options:
#        FireFox: 'FirefoxHTML-308046B0AF4A39CB'
#        Chrome:  'ChromeHTML.GI3XCPN7GKV5EXACLTBBNILNOY'
browser_prog_id = 'ChromeHTML.GI3XCPN7GKV5EXACLTBBNILNOY'

FTA_abs_path = os.path.dirname(os.path.abspath(__file__)) + '//SetUserFTA//SetUserFTA'

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



if __name__ == '__main__': 
    for ext in ext_l:
        cmd = '{} {} {}'.format(FTA_abs_path, ext, browser_prog_id)
    #     print(cmd)
        out = subprocess.check_output(cmd)
    #     print(out)
    print('done')



