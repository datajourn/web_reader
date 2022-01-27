import os
from flask import Flask, request, render_template, Response, redirect, session
from web_reader import Web_Reader

app = Flask(__name__)


# ------------------------------------------------------------------------------------------

###############################
# Routes - Index

@app.route('/')
def index():
    output = index_nav("Index:")
    return render_template('index.html', display =  output)

###############################
# Back to Index nav

def to_index_nav(header):
    output = '<h2>' + header + '</h2>'
    output +=  "<a href='/'>Index</a><br/>"    

    return output

###############################
# Index

def index_nav(header):
    output = '<h1>' + header + '</h1>'

    output += "<br/><br/><a href='/'>Index</a>"

    output += "<br/><br/><a href='/read_product'>Read Product Page</a>"
    output += "<br/><br/><a href='/read_keywords'>Read Search Keywords</a>"
    output += "<br/><br/><a href='/read_category'>Read Category</a>"
    output += "<hr><br>"

    return output


# ------------------------------------------------------------------------------------------


@app.route('/read_product')
def read_product():

    render_url = 'index.html'

    output = index_nav('Reading URL')

    url = "https://www.amazon.com/Storytelling-Data-Visualization-Business-Professionals/dp/1119002257/"
    # url1 = "https://www.amazon.com/Big-Book-Dashboards-Visualizing-Real-World/dp/1119282713/ref=pd_sim_2/140-0116433-6058319?pd_rd_w=b0hOg&pf_rd_p=dee70060-7c6d-4721-a321-50a27281cd22&pf_rd_r=WKBKFQGSJFY3HFDKJZ12&pd_rd_r=5f47bf39-5249-42a3-92d5-99dc8cd4bc22&pd_rd_wg=a6qxi&pd_rd_i=1119282713&psc=1"
    # url2 = "https://www.amazon.com/Press-Reset-Recovery-Video-Industry-ebook/dp/B08HLR61MG"

    output += Web_Reader().read_product(url)

    return render_template(render_url, display = output)



@app.route('/read_keywords')
def read_keywords():

    render_url = 'index.html'

    output = index_nav('Reading Keywords')
    keywords = "Solana+Crypto"

    output += Web_Reader().read_category("s?k=" + keywords + "&i=digital-text")
    
    return render_template(render_url, display = output)



@app.route('/read_category')
def read_category():

    render_url = 'index.html'

    output = index_nav('Reading Category')

    # Category
    cat = "s?rh=n%3A6361571011&fs=true"
    # cat2 = "s?i=digital-text&bbn=156116011&rh=n%3A133140011%2Cn%3A154606011%2Cn%3A156116011%2Cn%3A156117011&dc&fs=true&qid=1643023059&rnid=156116011"
    # cat_page2 = "s?i=digital-text&bbn=156117011&rh=n%3A133140011%2Cn%3A154606011%2Cn%3A156116011%2Cn%3A156117011%2Cn%3A16977191011&dc&fs=true&page=2&qid=1643024183&rnid=156117011&ref=sr_pg_2"

    output += Web_Reader().read_category(cat)
    
    return render_template(render_url, display = output)



