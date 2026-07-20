import os
import sys
import time
import random

OPTIONS = {
    'text': {'default': '', 'description': 'Text to glitch'},
    'duration': {'default': '10', 'description': 'Seconds to glitch'}
}

def run(options=None):
    if options and options.get('text'):
        text = options.get('text')
    else:
        text = 'text'
    
    if options and options.get('duration'):
        try:
            duration = int(options.get('duration'))
        except:
            duration = 10
    else:
        duration = 10
    
    try:
        chars = "!@#$%^&*()_+{}|:<>?~"
        end_time = time.time() + duration
        
        while time.time() < end_time:
            glitched = ""
            for char in text:
                roll = random.random()
                if roll < 0.3:
                    glitched += random.choice(chars)
                elif roll < 0.15:
                    glitched += char.upper() if char.islower() else char.lower()
                elif roll < 0.05:
                    glitched += ""
                else:
                    glitched += char
            
            colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m', '\033[97m']
            color = random.choice(colors)
            
            if random.random() < 0.03:
                sys.stdout.write("\033[2m" + " " * 80 + "\033[0m\r")
            
            if random.random() < 0.02:
                sys.stdout.write("\033[2m" + " " * 80 + "\033[0m\r")
                time.sleep(0.02)
            
            sys.stdout.write(f"\r{color}{glitched}\033[0m")
            sys.stdout.flush()
            time.sleep(random.uniform(0.015, 0.05))
            
    except KeyboardInterrupt:
        pass
    
    return ""
