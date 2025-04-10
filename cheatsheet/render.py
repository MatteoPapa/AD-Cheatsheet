import yaml
from jinja2 import Template
from collections import defaultdict

# Load config values (IP addresses, ports, etc.)
with open("config.yaml") as f:
    config = yaml.safe_load(f)

# Load command data and useful links
with open("commands.yaml") as f:
    command_data = yaml.safe_load(f)

# Render useful_links
for link in command_data['useful_links']:
    link['url'] = Template(link['url']).render(config)

# Render command strings
for cmd in command_data['commands']:
    cmd['cmd'] = Template(cmd['cmd']).render(config)

# Group commands by section
grouped = defaultdict(list)
for cmd in command_data['commands']:
    grouped[cmd['section']].append(cmd)

# Load Jinja2 template
with open("cheatsheet.j2") as f:
    template = Template(f.read())

# Render the template with context
html = template.render(
    sections=grouped,
    useful_links=command_data['useful_links']
)

# Output HTML to file
with open("cheatsheet.html", "w") as f:
    f.write(html)

print("✅ Cheatsheet HTML generato!")
