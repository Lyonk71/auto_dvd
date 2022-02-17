import subprocess
import os
import time

USERDIR = os.getenv('HOME')

while True:
    try:
        DISC_TITLE = subprocess.run(
            ["blkid", "-o", "value", "-s", "LABEL", "/dev/sr0"],
            capture_output=True,
            text=True).stdout.strip('\n')
        if len(DISC_TITLE) > 1:
            os.makedirs(f'{USERDIR}/movies/new/{DISC_TITLE}')
            subprocess.run([
                'makemkvcon', 'mkv', 'disc:0', 'all', '--minlength=1800', '-r',
                '--messages=auto_dvd_logs.txt',
                f'{USERDIR}/movies/new/{DISC_TITLE}'
            ])
            subprocess.run('eject')
    except:
        pass
    finally:
        time.sleep(5)
