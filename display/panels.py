def draw_panel(title, content, status=""):
    print(f"\n+--- {title}")
    lines = content.split('\n')
    for line in lines:
        print(f"| {line}")
    if status:
        print(f"|- Status: {status}")
    print("------------------------------")
