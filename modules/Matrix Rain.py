OPTIONS = {
    'default': {
        'columns': 80,
        'speed': 0.05,
        'charset': '01',
        'density': 0.3,
        'fade': 0.9,
        'duration': 50
    },
    'description': {
        'columns': 'Number of columns in the matrix rain',
        'speed': 'Delay between frames in seconds',
        'charset': 'Character set to use for rain',
        'density': 'Probability of new drops appearing (0-1)',
        'fade': 'Fade rate for trailing characters (0-1)',
        'duration': 'Number of frames to display'
    }
}

def run(options=None):
    output = []
    try:
        opts = OPTIONS['default'].copy()
        if options:
            opts.update({k: v for k, v in options.items() if k in opts})
        
        columns = opts['columns']
        speed = opts['speed']
        charset = opts['charset']
        density = opts['density']
        fade = opts['fade']
        duration = opts['duration']
        
        import random
        import time
        import sys
        from io import StringIO
        
        output.append("[*] Initializing Matrix Rain...")
        output.append("[*] Columns: {} | Charset: {} | Density: {}".format(columns, charset, density))
        
        matrix = [[' ' for _ in range(columns)] for _ in range(20)]
        drops = [0] * columns
        trails = [0] * columns
        
        captured = StringIO()
        old_stdout = sys.stdout
        sys.stdout = captured
        
        try:
            for frame in range(duration):
                for col in range(columns):
                    if random.random() < density:
                        drops[col] = 19
                        trails[col] = random.randint(3, 8)
                    
                    if drops[col] > 0:
                        drops[col] -= 1
                        row = 19 - drops[col]
                        if row >= 0 and row < 20:
                            matrix[row][col] = random.choice(charset)
                    
                    if trails[col] > 0:
                        trails[col] = max(0, trails[col] - fade)
                        trail_row = 19 - drops[col] - int(trails[col])
                        if 0 <= trail_row < 20 and trails[col] > 0.5:
                            if random.random() < 0.7:
                                matrix[trail_row][col] = random.choice(charset).lower()
                            else:
                                matrix[trail_row][col] = ' '
                    
                    for row in range(20):
                        if matrix[row][col] != ' ' and random.random() < 0.02:
                            matrix[row][col] = random.choice(charset)
                
                sys.stdout.write('\033[H')
                for row in matrix:
                    sys.stdout.write(''.join(row) + '\n')
                sys.stdout.flush()
                time.sleep(speed)
                
                for row in range(20):
                    for col in range(columns):
                        if random.random() < 0.01:
                            matrix[row][col] = ' '
        
        except KeyboardInterrupt:
            output.append("[!] Interrupted by user")
        finally:
            sys.stdout = old_stdout
            captured.close()
        
        output.append("[+] Matrix Rain completed successfully")
        output.append("[*] Total frames rendered: {}".format(duration))
        output.append("[*] Cleanup complete")
        
    except Exception as e:
        output.append("[!] Error: {}".format(str(e)))
        import traceback
        output.append("[!] Traceback: {}".format(traceback.format_exc()))
    
    return "\n".join(output)
