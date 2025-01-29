import re

url_details = "facebook <https://www.facebook.com/>, instagram <https://www.instagram.com/>, flipkart <https://www.flipkart.com/>"
result = re.findall(r"(\w+)\s*<https?://.*?>", url_details)
print(result)

result = re.search(r"(\w+)\s*<https?://.*?>", url_details)
print(result)

