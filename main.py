import sys, mechanize, random, json

# Import Config
with open('config.json') as json_data_file:
    config = json.load(json_data_file)

# Setup Browser
br = mechanize.Browser()
br.set_handle_robots(False)

# Login
br.open(config["router"]["login_uri"])
print br.title()
br.select_form(nr=0)
br.form['loginUsername'] = config["router"]["user"]
br.form['loginPassword'] = config["router"]["password"]
br.submit()

# Go to the right page
br.open(config["router"]["wireless_uri"])
print br.title()
br.select_form(name='wlanRadio')
print br
channels = [x for x in br.form.possible_items('ChannelNumber') if x not in br.form['ChannelNumber']]
br.form['ChannelNumber'] = [random.choice(channels)]
br.find_control('commitwlanRadio').readonly = False
br.form['commitwlanRadio'] = '1'
br.form['Band'] = ['1']
resp=br.submit()
resp=resp.get_data()
#print resp
