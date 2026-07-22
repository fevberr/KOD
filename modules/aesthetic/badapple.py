import os
import time
import re
import threading
import sys
from urllib.request import urlopen, Request
from urllib.error import URLError, HTTPError
from concurrent.futures import ThreadPoolExecutor, as_completed

OPTIONS = {
    'default': {
        'frame_count': 899,
        'fps': 6.67,
        'delay': 0.15,
        'threads': 10,
        'output_dir': 'cache'
    },
    'description': {
        'frame_count': 'Number of frames to generate',
        'fps': 'Target frames per second',
        'delay': 'Delay between frames in seconds',
        'threads': 'Number of concurrent download threads',
        'output_dir': 'Output directory for text frames'
    }
}

CLEAR = '\033[2J\033[H'
HIDE_CURSOR = '\033[?25l'
SHOW_CURSOR = '\033[?25h'

def 1(url, timeout=10):
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(req, timeout=timeout) as response:
            return response.read().decode('utf-8')
    except:
        return None

def 2(html):
    try:
        pre_match = re.search(r'<pre[^>]*>(.*?)</pre>', html, re.DOTALL)
        if pre_match:
            content = pre_match.group(1)
            content = re.sub(r'<[^>]+>', '', content)
            content = content.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
            content = content.replace('&quot;', '"').replace('&#39;', "'")
            return content
    except:
        pass
    return None

def 3(frame_num, output_dir):
    filepath = os.path.join(output_dir, f'{frame_num}.txt')
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            if content and len(content) > 10:
                return True
    
    ascii_art = 2(1(f'https://raw.githubusercontent.com/Epicpkmn11/bad-apple-html/main/frame/{frame_num}.html'))
    if ascii_art:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(ascii_art)
        return True
    return False

def 4(total_frames, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    existing_frames = []
    for i in range(1, total_frames + 1):
        filepath = os.path.join(output_dir, f'{i}.txt')
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    if len(f.read()) > 10:
                        existing_frames.append(i)
            except:
                pass
    
    if existing_frames:
        print(f'[*] Found {len(existing_frames)} existing frames in cache')
    
    missing_frames = [i for i in range(1, total_frames + 1) if i not in existing_frames]
    
    if not missing_frames:
        print('[+] All frames already downloaded!')
        return total_frames, 0, []
    
    print(f'[*] Downloading {len(missing_frames)} missing frames...')
    
    start_time = time.time()
    success_count = len(existing_frames)
    failure_count = 0
    failed_frames = []
    processed_frames = len(existing_frames)
    lock = threading.Lock()
    
    def 5(frame_num):
        nonlocal success_count, failure_count, processed_frames
        result = 3(frame_num, output_dir)
        with lock:
            processed_frames += 1
            if result:
                success_count += 1
            else:
                failure_count += 1
                failed_frames.append(frame_num)
        return result
    
    def 6():
        with ThreadPoolExecutor(max_workers=OPTIONS['default']['threads']) as executor:
            futures = {executor.submit(5, i): i for i in missing_frames}
            for future in as_completed(futures):
                yield
    
    def 7():
        elapsed = time.time() - start_time
        fps = (processed_frames - len(existing_frames)) / elapsed if elapsed > 0 else 0
        
        progress = (processed_frames - len(existing_frames)) / len(missing_frames) if missing_frames else 1
        bar_length = 40
        filled = int(bar_length * progress)
        bar = '#' * filled + '.' * (bar_length - filled)
        
        if fps > 0:
            eta_seconds = (len(missing_frames) - (processed_frames - len(existing_frames))) / fps
        else:
            eta_seconds = 0
        
        eta_minutes = int(eta_seconds // 60)
        eta_seconds = int(eta_seconds % 60)
        
        status = f'[{bar}] {processed_frames}/{total_frames} frames'
        status += f' | OK {success_count}'
        status += f' | FAIL {failure_count}'
        status += f' | {elapsed:.1f}s'
        status += f' | ETA: {eta_minutes}m{eta_seconds}s'
        status += f' | FPS: {fps:.1f}'
        
        sys.stdout.write('\r' + ' ' * 120 + '\r')
        sys.stdout.write(status)
        sys.stdout.flush()
    
    start_gen = time.time()
    for _ in 6():
        if (processed_frames - len(existing_frames)) % 5 == 0:
            7()
    
    elapsed_total = time.time() - start_gen
    
    print('\n')
    print('=' * 50)
    if failure_count == 0:
        print('[+] All frames downloaded successfully!')
    else:
        print(f'[!] {failure_count} frames failed to download')
    print(f'Total frames: {total_frames}')
    print(f'Successfully created: {success_count}')
    print(f'Failed: {failure_count}')
    print(f'Total time: {elapsed_total:.2f} seconds')
    
    if failed_frames:
        print('\nFailed frames:')
        for f in failed_frames[:10]:
            print(f'  - Frame {f}')
        if len(failed_frames) > 10:
            print(f'  ... and {len(failed_frames) - 10} more')
    
    print(f'\nOutput directory: {os.path.abspath(output_dir)}')
    print('=' * 50)
    
    return success_count, failure_count, failed_frames

def 8(output_dir):
    frames = []
    if not os.path.exists(output_dir):
        return frames
    
    for i in range(1, 900):
        filepath = os.path.join(output_dir, f'{i}.txt')
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    if len(f.read()) > 10:
                        frames.append(i)
            except:
                pass
    return frames

def 9(output_dir, frame_num):
    filepath = os.path.join(output_dir, f'{frame_num}.txt')
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except:
        return None

def 10(output_dir, total_frames, fps):
    frames = 8(output_dir)
    if not frames:
        print('[!] No frames found in cache')
        return
    
    try:
        sys.stdout.write(HIDE_CURSOR)
        sys.stdout.flush()
        
        frame_count = len(frames)
        start_time = time.time()
        frame_index = 0
        
        while True:
            frame_num = frames[frame_index % frame_count]
            ascii_art = 9(output_dir, frame_num)
            
            if ascii_art:
                sys.stdout.write(CLEAR)
                sys.stdout.write(ascii_art)
                sys.stdout.flush()
                
                elapsed = time.time() - start_time
                current_fps = frame_index / elapsed if elapsed > 0 else 0
                
                info = f'[Frame {frame_num}/{total_frames}] [FPS: {current_fps:.1f}] [Time: {elapsed:.1f}s]'
                sys.stdout.write('\n' + info)
                sys.stdout.flush()
                
                frame_index += 1
                time.sleep(1.0 / fps)
            else:
                break
                
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write(SHOW_CURSOR)
        sys.stdout.flush()
        print('\n[*] Playback stopped')

def 11(output_dir, total_frames):
    frames = 8(output_dir)
    if not frames:
        return
    
    print('[*] Splitting frames into separate files...')
    
    chunks = []
    chunk_size = 100
    for i in range(0, len(frames), chunk_size):
        chunks.append(frames[i:i + chunk_size])
    
    for idx, chunk in enumerate(chunks):
        chunk_dir = os.path.join(output_dir, f'chunk_{idx+1}')
        if not os.path.exists(chunk_dir):
            os.makedirs(chunk_dir)
        
        for frame_num in chunk:
            src = os.path.join(output_dir, f'{frame_num}.txt')
            dst = os.path.join(chunk_dir, f'{frame_num}.txt')
            if os.path.exists(src):
                try:
                    with open(src, 'r', encoding='utf-8') as f:
                        content = f.read()
                    with open(dst, 'w', encoding='utf-8') as f:
                        f.write(content)
                except:
                    pass
        
        print(f'[+] Created chunk {idx+1} with {len(chunk)} frames')
    
    print(f'[+] Split {len(frames)} frames into {len(chunks)} chunks')
    return len(chunks)

def run(options=None):
    output = []
    try:
        opts = OPTIONS['default'].copy()
        if options:
            opts.update({k: v for k, v in options.items() if k in opts})
        
        total_frames = int(opts['frame_count'])
        output_dir = str(opts['output_dir'])
        fps = float(opts['fps'])
        
        output.append('[*] Initializing Bad Apple Terminal Player...')
        time.sleep(0.1)
        
        frames_exist = 8(output_dir)
        
        if not frames_exist or len(frames_exist) < total_frames:
            output.append('[*] Checking and downloading missing frames...')
            success, failed, failed_list = 4(total_frames, output_dir)
            output.append(f'[+] Total frames available: {success}')
            if failed > 0:
                output.append(f'[!] {failed} frames failed to download')
        else:
            output.append(f'[+] All {len(frames_exist)} frames already downloaded!')
        
        output.append('[*] Splitting frames into chunks...')
        chunk_count = 11(output_dir, total_frames)
        output.append(f'[+] Created {chunk_count} chunks with 100 frames each')
        
        output.append('[*] Starting playback in terminal...')
        output.append('[+] Press Ctrl+C to exit')
        
        10(output_dir, total_frames, fps)
        
        output.append('[*] Playback ended')
        
    except Exception as e:
        output.append(f'[!] Error: {str(e)}')
        output.append('[*] Cleanup complete')
    
    return '\n'.join(output)

if __name__ == '__main__':
    print(run())
