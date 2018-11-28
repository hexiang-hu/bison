import os.path as osp
import os, sys
import argparse
import simplejson
from jinja2 import Environment, FileSystemLoader

def get_jinja_env():
  """
  Get a jinja2 Environment object that we can use to find templates.
  """
  return Environment(loader=FileSystemLoader('.'))

if __name__ == '__main__':
  parser = argparse.ArgumentParser(add_help=False)
  parser.add_argument('--html_template', required=True)
  parser.add_argument('--rendered_html', required=True)
  args = parser.parse_args()

  env = get_jinja_env()
  template = env.get_template(args.html_template)

  with open('data.json', 'r') as in_:
    json_in = simplejson.load(in_)

  html = template.render(json_in)
  with open(args.rendered_html, 'w') as f:
    f.write(html)
