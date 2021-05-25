import os
import shutil
 
current_dir = os.getcwd()
 
for f in os.listdir(current_dir):
    filename, file_ext = os.path.splitext(f)
 
    try:
        if not file_ext:
            pass

        elif file_ext in ('.mp4'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Python_movies', f'{filename}{file_ext}'))

        elif file_ext in ('.mp3'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Python_songs', f'{filename}{file_ext}'))
 
        elif file_ext in ('.py'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Python_files', f'{filename}{file_ext}'))
        elif file_ext in ('.jpg', '.png', '.gif'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Image_files', f'{filename}{file_ext}'))
        elif file_ext in ('.xls', '.xlsx', '.xltx', '.xlsm'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Excel_files', f'{filename}{file_ext}'))
            
        else:
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Other_files', f'{filename}{file_ext}'))                        
 
    except (FileNotFoundError, PermissionError)        :
        pass
