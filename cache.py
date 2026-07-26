import os
import json
import hashlib
import time
from datetime import datetime
from typing import Optional, Dict

class CacheManager:
    def __init__(self, cache_dir: str, max_age: int = 3600):
        self.cache_dir = cache_dir
        self.max_age = max_age
    
    def generate_key(self, config: Dict) -> str:
        data = f"{config['target']}_{config['ports']}_{config['timeout']}_{config['threads']}_{config['scan_type']}"
        if config.get('banner_grab'):
            data += "_banner"
        return hashlib.md5(data.encode()).hexdigest()
    
    def get(self, key: str) -> Optional[Dict]:
        cache_file = os.path.join(self.cache_dir, f"{key}.json")
        
        if not os.path.exists(cache_file):
            return None
        
        try:
            with open(cache_file, 'r') as f:
                data = json.load(f)
            
            if 'timestamp' in data:
                ts = datetime.fromisoformat(data['timestamp']).timestamp()
                if time.time() - ts > self.max_age:
                    return None
            
            return data
        except:
            return None
    
    def save(self, key: str, data: Dict):
        cache_file = os.path.join(self.cache_dir, f"{key}.json")
        try:
            with open(cache_file, 'w') as f:
                json.dump(data, f, indent=2)
        except:
            pass
    
    def clear(self, age: Optional[int] = None):
        if age is None:
            age = self.max_age
        
        try:
            for filename in os.listdir(self.cache_dir):
                if filename.endswith('.json'):
                    filepath = os.path.join(self.cache_dir, filename)
                    try:
                        with open(filepath, 'r') as f:
                            data = json.load(f)
                        if 'timestamp' in data:
                            ts = datetime.fromisoformat(data['timestamp']).timestamp()
                            if time.time() - ts > age:
                                os.remove(filepath)
                    except:
                        continue
        except:
            pass
    
    def stats(self) -> Dict:
        stats = {'files': 0, 'size': 0, 'oldest': None, 'newest': None}
        
        try:
            for filename in os.listdir(self.cache_dir):
                if filename.endswith('.json'):
                    filepath = os.path.join(self.cache_dir, filename)
                    stats['files'] += 1
                    stats['size'] += os.path.getsize(filepath)
                    
                    try:
                        with open(filepath, 'r') as f:
                            data = json.load(f)
                        if 'timestamp' in data:
                            ts = datetime.fromisoformat(data['timestamp'])
                            if stats['oldest'] is None or ts < stats['oldest']:
                                stats['oldest'] = ts
                            if stats['newest'] is None or ts > stats['newest']:
                                stats['newest'] = ts
                    except:
                        pass
        except:
            pass
        
        return stats
