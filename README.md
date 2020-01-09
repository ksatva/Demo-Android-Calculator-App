# A demo calculator application for android using Kivy and buildozer
   
--------------
### Main script
    main.py

-------
### Apk file
    bin/kvcalc__armeabi-v7a-0.1-armeabi-v7a-debug.apk

-----
## Summary of Steps
    Create virtual environment
        $ python3 -m venv my_kivy_project
        $ source bin/activate
    
    Install Kivy in the virtual environment 'my_kivy_project'
        $ python -m pip install kivy
    
    Write python script 
        calculator.py 
    
    Install buildozer and dependencies
        $ pip install buildozer
        Install dependencies depending on the OS distribution
    
    Deploy 
        $ mkdir calculatorApp & cd calculatorApp
        $ buildozer init
        Edit the buildozer.spec file for creating necessary labels
        
        Copy and Rename the calculator.py as main.py in the calculatorApp directory
    
        $ buildozer -v android debug
        
    The apk file will be created in ./bin directory    

------
#### Reference and further reading
    https://realpython.com/mobile-app-kivy-python/
    https://kivy.org/doc/stable/guide/lang.html
    https://buildozer.io/
