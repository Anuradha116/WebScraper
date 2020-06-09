##Procedure for setup


*In visual studio open the project folder via   file->open folder and select project1.

*You should have pip installed on your machine, so you have to install scrapy with the following command “pip install scrapy”. 

*Few  more things to be install which are as follow
1. Requests : command for it “pip install requests””
2. Beautifulsoup4 : command “pip install bs4”

*Now navigate to the directory of the project  “ cd project1” in visual studio code terminal.

*For database connectivity, enter your DB host , user , password  in the  create_connection() function of pipeline.py file.

*After above step kindly create a database with name “mycontent” in mysql.

*Now on visual studio code terminal run command : ”scrapy crawl  list1”  (spider name assign as  list1).

*The websraper executes and extracts company url, whatsapp no, google lat long and insert the same in database table content_tb.