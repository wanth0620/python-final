#!/usr/bin/python
#coding:utf-8

from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()

#start = input("input the start date:")
#end = input("input the end date:")

driver.get("https://www.google.com/search?client=firefox-b-ab&q=kktix")
driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='附有網站連結的網頁搜尋結果'])[1]/following::h3[1]").click()
driver.find_element_by_link_text("Explore").click()

driver.find_element_by_id("search_form_start_at").click()
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Sa'])[1]/following::td[3]").click()
driver.find_element_by_id("search_form_end_at").click()
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Sa'])[1]/following::td[33]").click()
driver.find_element_by_id("search_form_category_id").click()
Select(driver.find_element_by_id("search_form_category_id")).select_by_visible_text("Food")
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='By Date'])[1]/following::option[8]").click()
driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='By Date'])[1]/following::input[3]").click()
