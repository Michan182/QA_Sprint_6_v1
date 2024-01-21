from selenium.webdriver.common.by import By

class StartPageScooterLocators:
    #локатор в хедере
    ORDER_BUTTON_HEADER = (By.XPATH,  "//button[@class='Button_Button__ra12g']")
    #локатор ниже на странице
    ORDER_BUTTON_FOOTER = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")

