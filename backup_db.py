import shutil
import os
from datetime import datetime

DB_PATH = 'tvc.db'
BACKUP_DIR = 'backups_db'

def criar_backup():
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = os.path.join(BACKUP_DIR, f'tvc_backup_{timestamp}.db')
    shutil.copy2(DB_PATH, backup_file)
    print(f'Backup criado: {backup_file}')
    return backup_file

if __name__ == '__main__':
    criar_backup()
