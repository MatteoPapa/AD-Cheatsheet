import yaml
from jinja2 import Template
from collections import defaultdict

# Load config
with open("config.yaml") as f:
    config = yaml.safe_load(f)

# Load commands
with open("commands.yaml") as f:
    command_data = yaml.safe_load(f)

# Render placeholders
for cmd in command_data['commands']:
    cmd['cmd'] = Template(cmd['cmd']).render(config)

# Group by section
grouped = defaultdict(list)
for cmd in command_data['commands']:
    grouped[cmd['section']].append(cmd)

# Load and render template
with open("cheatsheet.j2") as f:
    template = Template(f.read())

html = template.render(sections=grouped)

with open("cheatsheet.html", "w") as f:
    f.write(html)

print("✅ Cheatsheet HTML generato!")
