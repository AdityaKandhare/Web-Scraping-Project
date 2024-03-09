import requests
from bs4 import BeautifulSoup

book_titles = [] # Create an empty list
page=int(input("There are 51 pages in total, So it will check from start to the page number you selected; Choose a number from 1 to 51 for page "))
if(page>51 or page<1):
    print("Invalid Page Number")
else:
    for n in range(1,page):
        url = f"http://books.toscrape.com/catalogue/page-{n}.html"  # URL for the page
        response = requests.get(url) #Send GET request to the URL

        if response.status_code == 200: #Check if the request was successful
            soup = BeautifulSoup(response.text, "html.parser") #parse HTML content of the page using BeautifulSoup


            products = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3") #taking all the products from the page

            for product in products: #extract all products
                title = product.h3.a["title"]
                rating_class = product.select_one("p.star-rating")["class"][1]
                cost = product.select_one("p.price_color").get_text(strip=True)

                book_titles.append({  #store to the list
                    "Title": title,
                    "Rating": rating_class,
                    "Cost": cost
                })
        else: #handle error if it fails
            print(f"Failed to retrieve the webpage for page {n}.")

    for book in book_titles:  #print all details
        print(f"Title: {book['Title']}, Rating: {book['Rating']}, Cost: {book['Cost']}")

    email=str(input("Do you want me to send this book titles to your mail (yes/no) :")) #asking user if they need mail
    if(email=="yes"):
            import smtplib
            from email.mime.multipart import MIMEMultipart
            from email.mime.text import MIMEText

            #declaring the username and password
            gmail_username = "your_email@example.com"
            gmail_password = "  " #please do not share this creds with anyone
            recipient_email = str(input("Enter the recipient email address :")) #taking input from user for recipient mail

            server = smtplib.SMTP("smtp.gmail.com", 587) # Create an SMTP session
            server.starttls()  # start TLS encryption

            server.login(gmail_username, gmail_password) # Login to Gmail account

            #email content
            email_subject = "List of Book Titles with Ratings"
            email_body = "\n".join(f"Title: {book['Title']}, Rating: {book['Rating']}" for book in book_titles)

            # Create the MIME object
            msg = MIMEMultipart()
            msg['From'] = gmail_username
            msg['To'] = recipient_email
            msg['Subject'] = email_subject

            # Attach the email body as plain text
            msg.attach(MIMEText(email_body, 'plain'))

            server.sendmail(gmail_username, recipient_email, msg.as_string())  # Send the email

            server.quit() # Close the SMTP server
            print(f"We have mailed you the list on {recipient_email}.")
            print("Thanks for your time, have a good day ahead!!")
    else:
        print("Thanks for your time, have a good day ahead!!")