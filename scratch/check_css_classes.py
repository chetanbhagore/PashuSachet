with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

classes = [
    'role-subnav-bar',
    'role-subnav-btn',
    'role-workspace-view',
    'notebook-tab-view',
    'stepper-progress-bar',
    'stepper-node',
    'symptom-select-card',
    'passport-card',
    'herd-carousel-track',
    'notebook-modal-overlay'
]

for c in classes:
    if f'.{c}' in css:
        print(f"Found .{c} in style.css")
    else:
        print(f"MISSING .{c} in style.css")
