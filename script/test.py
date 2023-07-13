from tbselenium.tbdriver import TorBrowserDriver
with TorBrowserDriver("/home/linuxmint/Schreibtisch/") as driver:
    driver.get('https://check.torproject.org')
