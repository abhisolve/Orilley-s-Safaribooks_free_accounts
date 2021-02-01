# -*- coding: utf-8 -*-
"""
    This spider creates accounts for Orilley Safari Books
"""
import scrapy
from splinter import Browser
from scraper.utils.generate_random_emails import generatemail
import names
from password_generator import PasswordGenerator
from accounts.models import SafariAccount
import time


class CreateaccountsSpider(scrapy.Spider):
    """
        class variables here, with browser instance,
        and urls to visit/scrape
    """
    name = 'createaccounts'
    allowed_domains = ['https://www.oreilly.com/member/register']
    start_urls = ['https://www.oreilly.com/member/register/']
    browser = Browser('firefox', headless=True, incognito=True)

    def parse(self, response):
        """
            this method is called as a callback to start scraping
        """
        email = generatemail()
        first_name = names.get_first_name()
        last_name = names.get_last_name()
        password_generator_instance  = PasswordGenerator()
        password_generator_instance.minlen = 10
        password = password_generator_instance.generate()

        self.browser.visit(self.start_urls[0])

        self.browser.fill('first_name', first_name)
        self.browser.fill('last_name', last_name)
        self.browser.fill('email', email)
        self.browser.fill('password', password)

        self.browser.find_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div/div/div[2]/div[1]/div/div[1]/form/button').click()
        SafariAccount.objects.create(name=first_name+' '+last_name, email=email, password=password)

        self.browser.quit()