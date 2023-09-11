from jinja2 import Template
import toml


data = toml.load("make_inv/config.toml")

test_partner = {}
for key, value in data['sites']['testpartner'].items():
	test_partner.update({ key : value })

test_partner_db = {}
for key, value in data['sites']['testpartner']['db'].items():
	test_partner_db.update({ key : value })

template = Template("""[{{group}}]
{{partner}} ansible_host={{ip}}\n
[{{group}}:vars]
base={{base}}
user={{user}}
password={{password}}""")

render = template.render(group = test_partner['server_group'],partner = test_partner['partner_name'] ,
ip = test_partner['server_ip']['main'], base = test_partner_db['base'],
user = test_partner_db['user'], password = test_partner_db['password'])

with open('inventory', 'w') as file:
	file.write(render)

	
