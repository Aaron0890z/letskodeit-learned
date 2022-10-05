from selenium.webdriver.common.by import By
import traceback
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from Utilities.GenericLogger import CustomLogger
import logging
import time
import os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class SeleniumDriver():
    log = CustomLogger(logging.DEBUG)

    def __init__(self, driver):  # accepts driver
        self.driver = driver
        self.actions = ActionChains(driver)

    def getTitle(self):
        return self.driver.title

    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType + " not correct/supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with Locator:" + locator + " and Locator type: " + locatorType)
        except:
            self.log.info("Element not found with Locator:" + locator + " and Locator type: " + locatorType)
        return element

    def getElements(self, locator, locatorType="id"):
        elementList = None
        try:
            if locator:
                byType = self.getByType(locatorType)
                elementList = self.driver.find_elements(byType, locator)
            if len(elementList) > 0:
                self.log.info("Number of elements found " + str(len(elementList)))
            else:
                self.log.error("No elements found")
        except:
            self.log.error("No elements found due to locator")
        return elementList

    def elementclick(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Click on the element with Locator:" + locator + " and Locator type: " + locatorType)
        except:
            self.log.info("cannot click on the element with Locator:" + locator + " and Locator type: " + locatorType)
            print_stack()

    def getText(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            text = element.text
            if len(text) == 0:
                text = element.get_attribute('innerText')
            if len(text) != 0:
                text = text.strip()
        except:
            self.log.error("Text not found")
            text = None
        return text

    def clearField(self, locator="", locatorType="id", element=None):
        """
        Clear an element field
        """
        if locator:
            element = self.getElement(locator, locatorType)
        element.clear()
        self.log.info("Clear field with locator: " + locator +
                      " locatorType: " + locatorType)

    def sendkeys(self, data, locator="", locatorType="id", element=None):
        """
        Send keys to an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            if locator:  # This means if locator is not empty
                element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator +
                          " locatorType: " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator: " + locator +
                          " locatorType: " + locatorType)
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))

    def sendKeysWhenReady(self, data, locator="", locatorType="id"):
        """
        Send keys to an element -> MODIFIED
        Either provide element or a combination of locator and locatorType
        """
        try:
            element = self.ExplicitWait(locator, locatorType, timeout=10, pollfrequency=0.5)
            element.click()
            element.send_keys(data)

            if element.get_attribute("value") != data:
                self.log.debug("Text is not sent by xpath in field so i will try to send string char by char!")
                element.clear()
                for i in range(len(data)):
                    element.send_keys(data[i] + "")
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.info("Element not appeared on the web page")
            self.log.error("Exception Caught: {}".format(traceback.format_exc()))
            self.log.error("".join(traceback.format_stack()))

    def elementpresent(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def elementpresence(self, locator, locatorType="id"):
        try:
            bytpe = self.getByType(locatorType)
            elementlist = self.driver.find_elements(bytpe, locator)
            if len(elementlist) > 0:
                self.log.info("Element found")
                return True
            else:
                self.log.info("Element not found")
                return False
        except:
            self.log.info("Element not found")
            return False

    def isDisplayed(self, locator="", locatorType="id", element=None):
        isDisplayed = False
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                isDisplayed = element.is_displayed()
                if isDisplayed is True:
                    self.log.info("Element is displayed " + str(isDisplayed))
                else:
                    self.log.error("Element is not displayed")
                return isDisplayed
        except:
            self.log.error("No locator found")
            return False

    def ExplicitWait(self, locator="", locatorType="id", timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum ::" + str(timeout) + " :: seconds for the element")

            wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared")
            print_stack()
        return element

    def webScroll(self, no=600, direction="up"):
        """
        NEW METHOD
        """
        num = no
        if direction == "up":
            # Scroll Up
            # self.driver.execute_script("window.scrollBy(0, -1000);")
            self.driver.execute_script(f'''window.scrollBy(0, -{num});''')

        if direction == "down":
            # Scroll Down
            # self.driver.execute_script("window.scrollBy(0, 1000);")
            self.driver.execute_script(f'''window.scrollBy(0, {num});''')

    def scrollTo(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            if element is not None:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                self.log.info("scrolled to the element ")
        except:
            self.log.error("Not able to scroll to the element")

    def mouseHover(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            self.actions.move_to_element(element).perform()
            self.log.info("Mouse hovered on element")
        except:
            self.log.error("Mouse hover failed on element")

    def mouseHoversList(self, locator="", locatorType="id", element=None):
        try:
            if locator:
                element = self.getElements(locator, locatorType)
            if len(element) > 0:
                for a in range(len(element)):
                    link1 = element[a]
                    self.actions.move_to_element(link1).perform()
                    time.sleep(2)
                    self.log.info("Mouse hovered on element")
            else:
                self.log.error("Mouse not hovered")
        except:
            self.log.error("Mouse hover failed on element")

    def currentWindowHandle(self):
        element = None
        try:
            element = self.driver.current_window_handle
            if element is not None:
                self.log.info("Current window handle found" + str(element))
            else:
                self.log.error("No window handle found")
        except:
            self.log.error("Cant get window handle")
        return element

    def getWHandles(self):
        element = None
        try:
            element = self.driver.window_handles
            if element != 0:
                self.log.info("No of windows found " + str(len(element)))
            else:
                self.log.error("No window handles found")
        except:
            self.log.error("Not able to get window handles")
        return element

    def getDropDown(self, value, locator="", locatorType="id", type="value", element=None):
        try:
            if locator:
                element = self.getElement(locator, locatorType)
            sel = Select(element)
            if type == "index":
                sel.select_by_index(value)
            elif type == "visible text":
                sel.select_by_visible_text(value)
            elif type == "value":
                sel.select_by_value(value)
            else:
                self.log.error("Locator not found")
        except:
            self.log.error("Not able to get dropdown")

    def switchToIframe(self, value, type="id", element=None):
        '''
        use only if you know the iframes id, name or index other use the next below
        Switches to the iframe with id, name, index
        '''
        try:
            if type == "id":
                self.driver.switch_to.frame(value)
                self.log.info("Switched to iFrame with type: " + type)
            elif type == "name":
                self.driver.switch_to.frame(value)
                self.log.info("Switched to iFrame with type: " + type)
            elif type == "num":
                self.driver.switch_to.frame(value)
                self.log.info("Switched to iFrame with type: " + type)
        except:
            self.log.error("Could not switch to iframe with type: " + type)

    def switchToDefaultFrame(self):
        try:
            self.driver.switch_to.default_content()
            self.log.info("Switched to parent frame")
            '''
            driver.switchTo().parentFrame() - does not work, mi8 be in java()?
            driver.switchTo().default_content()'''
        except:
            self.log.error("Could not switch to parent frame")

    def SwitchFrameByIndex(self, locator, locatorType="xpath"):

        """
        Get iframe index using element locator inside iframe

        Parameters:
            1. Required:
                locator   - Locator of the element
            2. Optional:
                locatorType - Locator Type to find the element
        Returns:
            Index of iframe
        Exception:
            None
        """
        result = False
        try:
            iframe_list = self.getElementList("//iframe", locatorType="xpath")
            self.log.info("Length of iframe list: ")
            self.log.info(str(len(iframe_list)))
            for i in range(len(iframe_list)):
                self.switchToFrame(index=iframe_list[i])
                result = self.isElementPresent(locator, locatorType)
                if result:
                    self.log.info("iframe index is:")
                    self.log.info(str(i))
                    break
                self.switchToDefaultContent()
            return result
        except:
            print("iFrame index not found")
            return result

    def switchToFrame(self, id="", name="", index=None):
        """
        Switch to iframe using element locator inside iframe

        Parameters:
            1. Required:
                None
            2. Optional:
                1. id    - id of the iframe
                2. name  - name of the iframe
                3. index - index of the iframe
        Returns:
            None
        Exception:
            None
        """
        if id:
            self.driver.switch_to.frame(id)
        if name:
            self.driver.switch_to.frame(name)
        if index:
            self.log.info("Switch frame with index:")
            self.log.info(str(index))
            self.driver.switch_to.frame(index)

    def getElementAttributeValue(self, attribute, element=None, locator="", locatorType="id"):
        """
        Get value of the attribute of element

        Parameters:
            1. Required:
                1. attribute - attribute whose value to find

            2. Optional:
                1. element   - Element whose attribute need to find
                2. locator   - Locator of the element
                3. locatorType - Locator Type to find the element

        Returns:
            Value of the attribute
        Exception:
            None
        """
        if locator:
            element = self.getElement(locator=locator, locatorType=locatorType)
        value = element.get_attribute(attribute)
        return value

    def isEnabled(self, locator, locatorType="id", info=""):
        """
        Check if element is enabled

        Parameters:
            1. Required:
                1. locator - Locator of the element to check
            2. Optional:
                1. locatorType - Type of the locator(id(default), xpath, css, className, linkText)
                2. info - Information about the element, label/name of the element
        Returns:
            boolean
        Exception:
            None
        """
        element = self.getElement(locator, locatorType=locatorType)
        enabled = False
        try:
            attributeValue = self.getElementAttributeValue(element=element, attribute="disabled")
            if attributeValue is not None:
                enabled = element.is_enabled()
            else:
                value = self.getElementAttributeValue(element=element, attribute="class")
                self.log.info("Attribute value From Application Web UI --> :: " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '" + info + "' is enabled")
            else:
                self.log.info("Element :: '" + info + "' is not enabled")
        except:
            self.log.error("Element :: '" + info + "' state could not be found")
        return enabled

    def screenpShot(self, resultMessage):
        filename = resultMessage + "." + str(round(time.time() * 1000)) + ".png"
        ssdir = "../Screenshots/"
        relativeFname = ssdir + filename
        currentDir = os.path.dirname(__file__)      # Gives current dir
        destinationFile = os.path.join(currentDir, relativeFname)
        destinationDir = os.path.join(currentDir, ssdir)

        try:
            if not os.path.exists(destinationDir):
                os.makedirs(destinationDir)
            self.driver.save_screenshot(destinationFile)
            self.log.info("SS saved to dir: " + destinationFile)
        except:
            self.log.error("### Exception Occured")
            print_stack()