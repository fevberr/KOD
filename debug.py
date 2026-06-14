import os
import sys
import traceback

def debug():
    print("=" * 50)
    print("23 KOD DEBUG MODE")
    print("=" * 50)
    
    print("\n[1] Checking Python version...")
    print(f"Python: {sys.version}")
    
    print("\n[2] Checking current directory...")
    print(f"Directory: {os.getcwd()}")
    print(f"Files: {os.listdir('.')}")
    
    print("\n[3] Checking required directories...")
    dirs = ["modules", "display", "utils", "data"]
    for d in dirs:
        if os.path.exists(d):
            print(f"  - {d}/ EXISTS")
            print(f"    Files: {os.listdir(d)}")
        else:
            print(f"  - {d}/ MISSING")
    
    print("\n[4] Testing imports...")
    try:
        from display.banner import show_banner
        print("  - display.banner: OK")
    except Exception as e:
        print(f"  - display.banner: FAILED - {e}")
        traceback.print_exc()
    
    try:
        from display.panels import draw_panel
        print("  - display.panels: OK")
    except Exception as e:
        print(f"  - display.panels: FAILED - {e}")
        traceback.print_exc()
    
    try:
        from config import host, port, device, system, ping
        print(f"  - config: OK (host={host}, port={port})")
    except Exception as e:
        print(f"  - config: FAILED - {e}")
        traceback.print_exc()
    
    try:
        from menu import menu
        print("  - menu: OK")
    except Exception as e:
        print(f"  - menu: FAILED - {e}")
        traceback.print_exc()
    
    try:
        from utils.loader import load_module
        print("  - utils.loader: OK")
    except Exception as e:
        print(f"  - utils.loader: FAILED - {e}")
        traceback.print_exc()
    
    try:
        from spinner import spinner
        print("  - spinner: OK")
    except Exception as e:
        print(f"  - spinner: FAILED - {e}")
        traceback.print_exc()
    
    print("\n[5] Testing banner display...")
    try:
        from display.banner import show_banner
        show_banner()
        print("  - Banner displayed")
    except Exception as e:
        print(f"  - Banner FAILED: {e}")
        traceback.print_exc()
    
    print("\n[6] Testing config values...")
    try:
        from config import get_config
        cfg = get_config()
        for k, v in cfg.items():
            print(f"  - {k}: {v}")
    except Exception as e:
        print(f"  - Config FAILED: {e}")
        traceback.print_exc()
    
    print("\n[7] Testing main.py execution...")
    try:
        exec(open("main.py").read())
    except Exception as e:
        print(f"  - main.py FAILED: {e}")
        traceback.print_exc()
    
    print("\n" + "=" * 50)
    print("DEBUG COMPLETE")
    print("=" * 50)

if __name__ == "__main__":
    debug()
