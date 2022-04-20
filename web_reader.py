from bs4 import BeautifulSoup
import requests


class Web_Reader(object):


    def read_product(self, url):

        output = ""

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

        page = requests.get(url, headers=headers)

        soup1 = BeautifulSoup(page.content, "html.parser")
        soup2 = BeautifulSoup(soup1.prettify(), "html.parser")


        feature_div = soup2.find(id='detailBullets_feature_div')
        detail_list = feature_div.find_all('ul')

        count = 0

        # bsr is best sellers rank
        found_bsr = False
        bsr = ""

        for item in detail_list:

            item_str = str(item)
            if item_str.__contains__("Best Sellers Rank:"):

                spans = item.find('span')

                for span in spans:

                    if found_bsr == True and span.get_text().__contains__("in Kindle"):

                        text = span.get_text()
                        count += 1

                        # Collect all the digits from the text
                        for char in text:
                            if char.isdigit():
                                bsr += str(char)

                        # We've found the bsr, so return
                        return bsr

                    # Once we find the text "Best Sellers Rank:", we'll want the next span, that contains the bsr
                    if str(span).__contains__("Best Sellers Rank:"):
                        found_bsr = True

        return output



    def read_category(self, category_url):

        output = ""

        amazon_root = "https://www.amazon.com/"
        search_url = amazon_root + category_url

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
        page = requests.get(search_url, headers=headers)

        soup1 = BeautifulSoup(page.content, "html.parser")
        soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

        output += "<h3>Results:</h3>" + search_url

        # Search Results
        output += "<br>" + soup2.find('div', 'a-section a-spacing-small a-spacing-top-small').get_text()

        output += "<br><h3>Links:</h3>"

        # Get list of product links
        # links = soup2.find_all('a', 'a-link-normal s-link-style a-text-normal')
        # links = soup2.find_all(attrs={"title" : "product-detail"})
        links = soup2.find_all('a', 'a-link-normal s-no-outline')

        for link in links:

            output += "<br>" + str(link)

            link_href = link['href']

            # Exclude any redirect links
            if not link_href.__contains__("redirect"):
                link_parts = link_href.split("/")

                # Valid URLS have 3 or more parts
                if len(link_parts) > 3:
                    link_url = link_parts[0] + "/" + link_parts[1] + "/" + link_parts[2] + "/" + link_parts[3]

                    output += "BSR: " + self.read_product(amazon_root + link_url) + " URL: " + str(link_url) + "<br>"

        return output






