#!/bin/python

from time import sleep
from random import randint
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import pandas as pd
from pandas.io.html import read_html
from alpha101 import *
import pickle
import bs4

class IQCSpider():
    def __init__(self, mode):
        self.url_to_crawl = "https://websim.worldquantchallenge.com/simulate"
        self.mode = mode
        self.results = []

    # Start chromedrive
    def start_driver(self):
	print('starting driver...')
	self.display = Display(visible=0, size=(1620, 1080))
	self.display.start()
        opts = webdriver.ChromeOptions()
        opts.add_argument('--user-data-dir=/tmp')
        opts.add_argument('--disable-web-security')
        opts.add_argument('--disable-extensions')
        opts.add_argument('--incognito')
        opts.add_argument('--headless')
        opts.add_argument('--disable-gpu')
        opts.add_argument('--no-sandbox')
        opts.binary_location = '/usr/bin/google-chrome-stable'
#        opts.binary_location = '/mnt/c/Program Files (x86)/Google/Chrome/Application/chrome.exe'
#        self.driver = webdriver.Chrome()#'/usr/local/bin/chromedriver',chrome_options=opts)
        self.driver = webdriver.Firefox()

	sleep(1)

    # Close chromedriver
    def close_driver(self):
	print('closing driver...')
	self.display.stop()
	#self.driver.quit()
        try:
            self.driver.close()
	    print('closed!')
        except Exception:
            print('not able to close!')

    # Tell the browser to get a page
    def get_page(self, url):
	print('getting page...')
	self.driver.get(url)
	sleep(randint(2,3))

    # Login page
    def login(self):
	print('getting pass the gate page...')
	try:
	    form = self.driver.find_element_by_xpath('//*[@class="form-group"]')
	    form.find_element_by_xpath('//*[@id="EmailAddress"]').send_keys('qiao.xu@stonybrook.edu')
	    form.find_element_by_xpath('//*[@id="Password"]').send_keys('yourleave@')
            form.find_element_by_xpath('/html/body/main/article/div/div[2]/div/div/div[1]/div[4]/span[1]/button').click()
	    sleep(5)
	except Exception:
	    print('Cannot log in!')

    def setting(self, settings):
        #self.inspect("beforesetting")
	print('set parameters...')
        #button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/article/div/div/div[1]/div/div[1]/div/div[1]/button[1]')))
        #button = self.driver.find_element_by_xpath('/html/body/main/article/div/div/div[1]/div/div[1]/div/div[1]/button[1]')
        #form = self.driver.find_element_by_xpath('//*[@id="sim-settings-panel-wrapper"]')
        form = WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="sim-settings-panel-wrapper"]')))
        button = form.find_element_by_xpath('//button[@data-target="#sim-settings-panel-wrapper"]')
        action_chains = webdriver.ActionChains(self.driver)
        action_chains.move_to_element(button).click().perform()
#        button.click()
        sleep(randint(2,3))
        for key, item in settings.items():
            if key in ['Trunc']:
                continue
            #if key in ['decay', 'optrunc']:
            if key in ['Decay', 'Trunc']:
                select = form.find_element_by_xpath('//*[@data-fieldname="{0}"]'.format(key))
                #select = self.driver.find_element_by_xpath('//*[@name="{0}"]'.format(key))
                #select.click()
                #select.send_keys(Keys.CONTROL+"a")
                #select.send_keys(Keys.DELETE)
                #select.send_keys(item)
                action_chains = webdriver.ActionChains(self.driver)
                #action_chains.click(codeMirror).perform()
                action_chains.move_to_element(select).click()
                action_chains.send_keys(item).perform()
            #elif key in ['backdays']:
                #select = self.driver.find_element_by_xpath('//*[@name="{0}"]'.format(key))
                #action_chains = webdriver.ActionChains(self.driver)
                #action_chains.click(select)
                #if key != 'backdays':
                #    action_chains.send_keys(Keys.CLEAR)
                #action_chains.send_keys(item)
                #action_chains.perform()

                #print select.get_property('attributes')[0]
                #print select.get_property('attributes')[0][u'value']
                #self.driver.execute_script("document.querySelectorAll('label.boxed')[1].click()")
            else:
                #select = form.find_element_by_xpath('//*[@data-fieldname="{0}"]/option[@value="{1}"]'.format(key,item))
                #select = form.find_element_by_xpath('//*[@name="{0}"]/option[@value="{1}"]'.format(key,item))
                select = Select(form.find_element_by_xpath('//*[@data-fieldname="{0}"]'.format(key)))
                #action_chains = webdriver.ActionChains(self.driver)
                #action_chains.click(select).perform()
                select.select_by_visible_text(item)
                #action_chains.send_keys(Keys.CLEAR).perform()
                #action_chains.send_keys(item).perform()
                #select.click()
                #print select.get_property('attributes')[0]
                #select.send_keys(item)
                #sleep(randint(1,2))
                #print select.get_property('attributes')[0][u'value']
            sleep(randint(2,3))

        #for key, item in settings.items():
        #    select = form.find_element_by_xpath('//*[@data-fieldnname="{0}"]'.format(key))
        #    print select, select.text, select.get_property('attributes')[0]

        #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,'//button[@name="save-sim-settings'))).click() #Simulate
        #save = form.find_element_by_xpath('//*[@id="save-sim-settings"]')
        #save.click()
        #sleep(randint(5,6))
        form = self.driver.find_element_by_xpath('//*[@id="sim-settings-panel-wrapper"]')
        button = form.find_element_by_xpath('//button[@data-target="#sim-settings-panel-wrapper"]')
        button.click()
        sleep(randint(1,2))
        #self.inspect("aftersetting")

    def send_exp(self, exp):
        form = self.driver.find_element_by_xpath('//*[@id="codeForm"]')
        if self.mode == 'Example':
            #form.find_element_by_xpath('//*[@id="codeForm"]/div[2]/div/div/div[1]/button').click() #Example
            WebDriverWait(form, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="codeForm"]/div[2]/div/div/div[1]/button'))).click() #Example
        else:
            codeMirror = self.driver.find_element_by_xpath('//*[@id="code-editor-container"]/div/div[6]/div[1]/div/div/div/div[5]/pre')
            action_chains = webdriver.ActionChains(self.driver)
            #action_chains.click(codeMirror).perform()
            action_chains.move_to_element(codeMirror).click()
            action_chains.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.DELETE)
            action_chains.send_keys(exp).perform()
        sleep(2)
        inputexp = self.driver.find_element_by_xpath('//*[@id="code-editor-container"]').text
        #WebDriverWait(form, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="codeForm"]/div[2]/div/div/div[2]/button'))).is_displayed() #Simulate
        form = self.driver.find_element_by_xpath('//*[@id="codeForm"]')
        #WebDriverWait(form, 100).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#codeForm > div:nth-child(2) > div > div > div:nth-child(2) > button'))).click() #Simulate
        #button = form.find_element_by_xpath('//*[@id="codeForm"]/div[2]/div/div/div[2]/button')
        button = form.find_element_by_css_selector('#codeForm > div:nth-child(2) > div > div > div:nth-child(2) > button') #Simulate
 #       button.click() #Simulate
        action_chains = webdriver.ActionChains(self.driver)
        action_chains.move_to_element(button).click().perform()
#        self.driver.execute_script("argument[0].click()",button)
        print('now running...')
        print 'config:', mode, settings, inputexp
        sleep(60)
        return inputexp

    def grab_result(self):
	print('grabbing results...')
        #self.inspect("results_aftersleep")
        #form = self.driver.find_element_by_xpath('//*[@id="simOutput"]')
        #stattab = WebDriverWait(form, 1000).until(EC.presence_of_element_located((By.ID, "test-statsBtn")))
        #stattab = form.find_element_by_xpath('//*[@id="test-statsBtn"]')
        stattab = None
        time0 = 0
        while not stattab and time0 < 1000:
            try:
                stattab = self.driver.find_element_by_xpath('//*[@id="test-statsBtn"]')
            except:
                sleep(1)
                time0 += 1
        stattab.click()
        sleep(1)
        form = self.driver.find_element_by_xpath('//*[@id="statsTab"]')
        table = form.find_element_by_xpath('//*[@id="pnlStats"]/div/div/div/div/div/table').get_attribute('outerHTML')
        self.data = read_html(table)[0]
        col= self.data.columns[:-1]
        self.data.drop(self.data.columns[0],axis=1,inplace=True)
        self.data.columns = col
        print (self.data)

    def parse(self, dict, exp):
	self.start_driver()
        self.get_page(self.url_to_crawl)
        self.login()
        self.setting(dict)
        for expression in exp:
            expression = self.send_exp(expression)
            self.grab_result()
            sharpe = self.data.iloc[6]['Sharpe']
            fitness = self.data.iloc[6]['Fitness']
            self.results.append((settings, expression, self.data, sharpe, fitness))
            sleep(randint(3,5))
        self.close_driver()
        return self.results
        #return settings, exp, self.data, sharpe, fitness

    def inspect(self, name):
        f = open('html_source_code_{0}.html'.format(name), 'w')
        source_codes = self.driver.find_elements_by_xpath('//*[id="save-sim-settings"]')
        for source_code in source_codes:
            source_code = source_code.get_attribute("outerHTML")
            f.write(source_code.encode('utf-8'))
        f.close()
        #ids = self.driver.find_elements_by_xpath('//*[@id]')
        #print "--------------------------------------"
        #for ii in ids:
        #    try:
        #        print ii.text, ii.get_attribute('id'), ii.get_attribute('text')
        #    except Exception:
        #        print None
        #print "--------------------------------------"

# Run spider
#IQC = IQCSpider()
#print(IQC.parse(['close']))
#IQC.parse(alphas)

results = []

settings = {'Region': 'USA',
        'Universe':'TOP3000',
        'Delay': '1',
        'Decay': '4',
        'Trunc': '0.1',
        'Neut': 'Subindustry'
        #'backdays': '256'
        }
'''
settings = {'region': 'USA',
        'univid':'TOP3000',
        'delay': '1',
        'decay': 4,
        'optrunc': '0.1',
        'opneut': 'Subindustry'
        #'backdays': '256'
        }
'''
Regions = ['USA']
Universes = ['TOP3000','TOP500']
Delays = ['1', '0']
Decays = ['4']
MaxStockWeights = ['0.1']
Neutralizations = ['None','Market','Industry','Subindustry']
Lookbackdayss = ['256', '512']
mode = 'Simulate'

for Region in Regions:
    settings['Region'] = Region
    for Universe in Universes:
        settings['Universe'] = Universe
        for Delay in Delays:
            settings['Delay'] = Delay
            for Decay in Decays:
                settings['Decay'] = Decay
                for MaxStockWeight in MaxStockWeights:
                    settings['Trunc'] = MaxStockWeight
                    for Neutralization in Neutralizations:
                        settings['Neut'] = Neutralization
                        #for Lookbackdays in Lookbackdayss:
                        #    settings['backdays'] = Lookbackdays
                            #for alpha in alphas[1:3]:
                        IQC = IQCSpider(mode)
                        results = results + IQC.parse(settings, alphas[:2])
                            #sleep(10)

sort_results = sorted(results, key=lambda tup: tup[3], reverse = True)
print(sort_results)
with open('test_{0}.txt'.format(mode), 'w') as thefile:
    for item in sort_results:
        thefile.write("%s\n" % str(item))

with open('outfile_{0}'.format(mode), 'wb') as fp:
    pickle.dump(sort_results, fp)
