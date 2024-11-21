from selenium import webdriver
from time import  sleep
d = webdriver.Chrome()
def my_test(values_to_check, excpected):
    d.get("file:///C:/Users/Eden/Downloads/tip_calc/index.html")
    d.find_element(by="id",value="billamt").send_keys("100")
    d.find_element(by="xpath", value='//*[@id="serviceQual"]/option[3]').click()
    d.find_element(by="id", value="peopleamt").send_keys("5")
    d.find_element(by="id", value="calculate").click()
    excpected = "4.00"
    actual = d.find_element(by="id", value="tip").text
    is_visable = d.find_element(by="id", value="tip").is_displayed()
    assert actual == excpected
    assert is_visable == True
first_values = ["100","5","2"]
my_test(first_values,"6,00")