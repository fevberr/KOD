OPTIONS = {
    'speed': {'default': 0.03, 'description': 'Rain speed in seconds per frame'},
    'density': {'default': 80, 'description': 'Number of active drops (0-300)'},
    'seconds': {'default': 10, 'description': 'Duration to run in seconds'},
    'charset': {'default': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()', 'description': 'Characters to use'},
    'color': {'default': True, 'description': 'Enable colored output'},
    'fade': {'default': True, 'description': 'Enable fade effect on trails'}
}

def run(options=None):
    output = []
    
    try:
        opts = {}
        for key, val in OPTIONS.items():
            opts[key] = val['default']
        if options:
            for key, val in options.items():
                if key in opts:
                    opts[key] = val
        
        import os
        import sys
        import time
        import random
        
        speed = float(opts['speed'])
        density = int(opts['density'])
        seconds = int(opts['seconds'])
        charset = opts['charset']
        use_color = opts['color']
        use_fade = opts['fade']
        
        cols = os.get_terminal_size().columns
        lines = os.get_terminal_size().lines - 2
        
        output.append("[*] Matrix Rain v3.0 - Resizeable")
        output.append("[*] Terminal: {}x{} | Speed: {}s | Duration: {}s | Drops: {}".format(cols, lines, speed, seconds, density))
        
        drops = []
        for i in range(min(density, cols * 2)):
            drops.append({
                'x': random.randint(0, cols - 1),
                'y': random.randint(-lines, 0),
                'speed': random.uniform(0.5, 2.5),
                'length': random.randint(8, 30),
                'brightness': 1.0
            })
        
        start_time = time.time()
        end_time = start_time + seconds
        frame_count = 0
        
        sys.stdout.write('\033[2J\033[H')
        sys.stdout.flush()
        
        while time.time() < end_time:
            try:
                new_cols = os.get_terminal_size().columns
                new_lines = os.get_terminal_size().lines - 2
                if new_cols != cols or new_lines != lines:
                    cols = new_cols
                    lines = new_lines
                    for drop in drops:
                        if drop['x'] >= cols:
                            drop['x'] = random.randint(0, cols - 1)
                        if drop['y'] > lines:
                            drop['y'] = random.randint(-lines, 0)
            except:
                pass
            
            if len(drops) < min(density, cols * 2) and random.random() < 0.1:
                drops.append({
                    'x': random.randint(0, cols - 1),
                    'y': random.randint(-lines, 0),
                    'speed': random.uniform(0.5, 2.5),
                    'length': random.randint(8, 30),
                    'brightness': 1.0
                })
            
            if len(drops) > min(density, cols * 2):
                drops.pop(random.randint(0, len(drops) - 1))
            
            frame = []
            for y in range(lines):
                line = ""
                for x in range(cols):
                    char = " "
                    char_found = False
                    for drop in drops:
                        if drop['x'] == x:
                            if drop['y'] - drop['length'] <= y <= drop['y']:
                                char_found = True
                                dist_from_head = drop['y'] - y
                                brightness = 1.0 - (dist_from_head / drop['length'] * 0.8)
                                if dist_from_head == 0:
                                    if use_color:
                                        char = "\033[97m" + random.choice(charset) + "\033[0m"
                                    else:
                                        char = random.choice(charset).upper()
                                elif dist_from_head <= 2:
                                    if use_color:
                                        char = "\033[92m" + random.choice(charset) + "\033[0m"
                                    else:
                                        char = random.choice(charset)
                                elif use_fade and dist_from_head < drop['length'] // 2:
                                    if use_color:
                                        char = "\033[32m" + random.choice(charset) + "\033[0m"
                                    else:
                                        char = random.choice(charset).lower()
                                else:
                                    if use_color and use_fade:
                                        char = "\033[2;32m" + random.choice(charset) + "\033[0m"
                                    else:
                                        char = "."
                                break
                    if not char_found:
                        line += " "
                    else:
                        line += char
                frame.append(line)
            
            sys.stdout.write('\033[H')
            sys.stdout.write('\n'.join(frame))
            sys.stdout.flush()
            
            for drop in drops:
                drop['y'] += drop['speed']
                if drop['y'] > lines + drop['length']:
                    drop['y'] = random.randint(-lines, 0)
                    drop['x'] = random.randint(0, cols - 1)
                    drop['speed'] = random.uniform(0.5, 2.5)
                    drop['length'] = random.randint(8, 30)
            
            frame_count += 1
            time.sleep(speed)
        
        output.append("[+] Matrix Rain completed successfully")
        output.append("[*] Frames rendered: {}".format(frame_count))
        output.append("[*] Total time: {:.2f}s".format(time.time() - start_time))
        
    except KeyboardInterrupt:
        output.append("[!] Interrupted by user")
    except Exception as e:
        output.append("[!] Error: {}".format(str(e)))
        import traceback
        output.append("[!] {}".format(traceback.format_exc()))
    
    output.append("[*] Complete")
    return "\n".join(output)
