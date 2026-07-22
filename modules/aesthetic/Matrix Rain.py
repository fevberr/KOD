OPTIONS = {
    'default': {
        'columns': 80,
        'speed': 0.03,
        'charset': '0123456789ABCDEF',
        'density': 0.4,
        'fade': 0.85,
        'duration': 100,
        'color': True,
        'bold': True,
        'stream': False
    },
    'description': {
        'columns': 'Number of columns in the matrix rain display',
        'speed': 'Frame delay in seconds (lower = faster)',
        'charset': 'Character set used for falling symbols',
        'density': 'Probability of new drops appearing (0.0-1.0)',
        'fade': 'Trail fade rate (0.0-1.0, higher = longer trails)',
        'duration': 'Number of animation frames to render',
        'color': 'Enable ANSI color output',
        'bold': 'Use bold text for active drops',
        'stream': 'Stream output in real-time vs capture'
    }
}

def run(options=None):
    output = []
    try:
        opts = OPTIONS['default'].copy()
        if options:
            opts.update({k: v for k, v in options.items() if k in opts})
        
        import random
        import time
        import sys
        from io import StringIO
        
        cols = opts['columns']
        speed = opts['speed']
        charset = opts['charset']
        density = opts['density']
        fade = opts['fade']
        duration = opts['duration']
        use_color = opts['color']
        use_bold = opts['bold']
        stream_mode = opts['stream']
        
        output.append("[*] Launching Matrix Rain v2.0")
        output.append("[*] Configuration: {} cols | charset: {} | density: {}".format(cols, charset[:10], density))
        
        rows = 25
        matrix = [[' ' for _ in range(cols)] for _ in range(rows)]
        drops = [0] * cols
        trail_length = [0] * cols
        brightness = [[0.0 for _ in range(cols)] for _ in range(rows)]
        
        color_codes = {
            'reset': '\033[0m',
            'green': '\033[92m',
            'bright_green': '\033[92;1m',
            'dim_green': '\033[90;92m',
            'cyan': '\033[96m',
            'white': '\033[97m'
        }
        
        captured = StringIO()
        old_stdout = sys.stdout
        if not stream_mode:
            sys.stdout = captured
        
        try:
            output.append("[*] Rendering {} frames...".format(duration))
            
            for frame in range(duration):
                frame_lines = []
                
                for col in range(cols):
                    if random.random() < density:
                        drops[col] = rows - 1
                        trail_length[col] = random.randint(4, 12)
                    
                    if drops[col] > 0:
                        drops[col] -= 1
                        row = rows - 1 - drops[col]
                        if 0 <= row < rows:
                            char = random.choice(charset)
                            matrix[row][col] = char
                            brightness[row][col] = 1.0
                    
                    if trail_length[col] > 0:
                        trail_length[col] = max(0, trail_length[col] - fade)
                        trail_pos = rows - 1 - drops[col] - int(trail_length[col])
                        if 0 <= trail_pos < rows and trail_length[col] > 0.3:
                            if random.random() < 0.6:
                                matrix[trail_pos][col] = random.choice(charset.lower())
                                brightness[trail_pos][col] = 0.3
                            else:
                                matrix[trail_pos][col] = ' '
                                brightness[trail_pos][col] = 0.0
                    
                    for row in range(rows):
                        if matrix[row][col] != ' ' and random.random() < 0.015:
                            matrix[row][col] = random.choice(charset)
                            brightness[row][col] = min(1.0, brightness[row][col] + 0.1)
                
                for row in range(rows):
                    line = []
                    for col in range(cols):
                        char = matrix[row][col]
                        if char == ' ':
                            line.append(' ')
                        elif use_color:
                            b = brightness[row][col]
                            if b > 0.8 and use_bold:
                                line.append(color_codes['bright_green'] + char + color_codes['reset'])
                            elif b > 0.5:
                                line.append(color_codes['green'] + char + color_codes['reset'])
                            elif b > 0.2:
                                line.append(color_codes['dim_green'] + char + color_codes['reset'])
                            else:
                                line.append(color_codes['cyan'] + char + color_codes['reset'])
                        else:
                            line.append(char)
                    
                    frame_lines.append(''.join(line))
                
                if stream_mode:
                    sys.stdout.write('\033[2J\033[H')
                    sys.stdout.write('\n'.join(frame_lines))
                    sys.stdout.flush()
                    time.sleep(speed)
                else:
                    captured.write('\n'.join(frame_lines) + '\n')
                    time.sleep(speed)
                
                if frame % 10 == 0:
                    for row in range(rows):
                        for col in range(cols):
                            if random.random() < 0.03:
                                matrix[row][col] = ' '
                                brightness[row][col] = 0.0
        
        except KeyboardInterrupt:
            output.append("[!] Animation interrupted by user")
        except Exception as e:
            output.append("[!] Render error: {}".format(str(e)))
        finally:
            sys.stdout = old_stdout
            captured.close()
            if not stream_mode:
                output.append("[*] Captured {} lines of output".format(duration * rows))
        
        output.append("[+] Matrix Rain completed successfully")
        output.append("[*] Total frames: {} | Columns: {} | Speed: {}s".format(duration, cols, speed))
        output.append("[*] Shutdown complete")
        
    except Exception as e:
        output.append("[!] Fatal error: {}".format(str(e)))
        import traceback
        output.append("[!] {}".format(traceback.format_exc()))
    
    return "\n".join(output)
