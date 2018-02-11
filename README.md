##Automatic TSS Checker
[I saw the recent post about 1Conan adding support for paid users to auto save their blobs](https://www.reddit.com/r/jailbreak/comments/7wt5ft/news_you_can_now_support_1conans_tss_saver_on/?ref=share&ref_source=link). I like his tools very much but don't use his website and would much prefer to store my own blobs, so I wrote a quick python script which grabs all the blobs which IPSW.me says are available for the given devices. It's python2 and uses only libraries available in the default OSX build. 

###Instructions
1. Clone this repo, unzip it somewhere
2. Edit AutoTSS/main.py, add your devices to the `devices_to_monitor` variable as well as editing the `program_path` variable to point to the absolute location of the AutoTSS folder (WITH A TRAILING SLASH!)
3. For good measure, `chmod +x main.py tsschecker`
4. Test it by running `python <absolute path to main.py>`. In AutoTSS/Blobs you should now see folders with each devices ecid and inside that you should have all available blobs saved.
4. Run `crontab -e`, add the line `*/10 * * * * /Library/Frameworks/Python.framework/Versions/2.7/bin/python <ABSOLUTE PATH TO main.py>`
5. Enjoy!