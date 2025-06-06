from jinja2 import Environment, FileSystemLoader
import os

# Set up the environment
current_dir = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(current_dir))

# Load the template
template = env.get_template('hello_template.j2')

# Render with context
output = template.render(name='Joaquin')
print(output)

template2 = env.get_template('template_2.j2')
output2 = template2.render(name='Bob', age=16)
print(output2)