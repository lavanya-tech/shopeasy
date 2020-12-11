from flask import Flask,render_template,request,redirect
import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# <-------city1 json ----->

with open('static/json/jiomart.json') as f:
  jiom = json.load(f)

with open('static/json/bigb.json') as f:
  bigbas = json.load(f)

with open('static/json/natureb.json') as f:
  naturebas = json.load(f)

# <-------------cities json-------------->

with open('static/json/visakhapatnam.json') as f:
  visakha = json.load(f)

with open('static/json/madhapur.json') as f:
  madha = json.load(f)

with open('static/json/gachibowli.json') as f:
  gachi = json.load(f)

# <----------city2 json------------>
with open('static/json/tarkariexoticvegetables_madhapur.json') as f:
  tarkari = json.load(f)

with open('static/json/saifruitsandvegetables_madhapur.json') as f:
  sai = json.load(f)

with open('static/json/sirisupermarket_madhapur.json') as f:
  siri = json.load(f)

with open('static/json/halofarm_madhapur.json') as f:
  halo = json.load(f)

with open('static/json/kisanbazaar.json') as f:
  kisan = json.load(f)

# <----------city3 json ------------>

with open('static/json/freshbasket_gachibowli.json') as f:
  fresh = json.load(f)

with open('static/json/akella_gachibowli.json') as f:
  akella = json.load(f)

with open('static/json/polam_gachibowli.json') as f:
  polam = json.load(f)

with open('static/json/ratandeep_gachibowli.json') as f:
  ratan = json.load(f)

with open('static/json/supraja_gachibowli.json') as f:
  raju = json.load(f)

visakha_shops={"Nature Basket":"https://images-eu.ssl-images-amazon.com/images/I/31OWAY09DdL.jpg",
               "Big Basket":"https://paganresearch.io/images/bigbasket.png",
               "Jiomart":"https://images.livemint.com/img/2020/04/25/600x338/Screenshot_2020-04-25-21-46-59-973_com.whatsapp_1587831811236_1587831811708_1587832244925.jpg"}

madhapur_shops={"Sai Fruits and Vegetables": "https://ik.imagekit.io/dunzo/dunzo-catalog-prod/tr:w-300,h-300,cm-pad_resize_store_thumbnail/stores/7ad3cfed-0c57-4103-a5dd-38e43b84f309-1589537711108-store_image.jpg",
                "Siri Supermarket":"https://content3.jdmagicbox.com/comp/hyderabad/x7/040pxx40.xx40.151204210001.y6x7/catalogue/siri-super-market-madhapur-hyderabad-supermarkets-57h68u9p3y-250.jpg",
                "Kisan Bazaar":"https://www.interactive.org/images/games_developers/no_image_available_sm.jpg",
                "Tarkari Exotic Vegetables":"https://www.interactive.org/images/games_developers/no_image_available_sm.jpg",
                "Halo Farm Direct Organic Foods":"https://www.interactive.org/images/games_developers/no_image_available_sm.jpg"
}

gachibowli_shops={"Akella":"https://ik.imagekit.io/dunzo/dunzo-catalog-prod/tr:n-$R$_store_thumbnail/stores/64a06f15-fd7b-4a85-ad46-f1372442c98b-1593089449383-store_image.jpg",
                  "Fresh Basket":"https://ik.imagekit.io/dunzo/dunzo-catalog-prod/tr:n-$R$_store_thumbnail/stores/1202c033-5b6d-41c0-986b-670dbd59afe2-1594119452214-store_image.jpeg",
                  "Pollam":"https://www.interactive.org/images/games_developers/no_image_available_sm.jpg",
                  "Ratandeep":"https://ik.imagekit.io/dunzo/dunzo-catalog-prod/tr:w-300,h-300,cm-pad_resize_store_thumbnail/stores/71b8317b-a314-4cc4-9048-0c62346bc7d0-1574159196904-store_image.jpg",
                  "Supraja Supermarket":"https://www.interactive.org/images/games_developers/no_image_available_sm.jpg"}

grocers={
  "vizaggrocers": [
    {
      "Title": "Tomato",
      "qty": "500g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/23-1395-tamato-tamaatar.html#/34-weight-500gm",
      "Image": "https://vizaggrocers.com/24-home_default/tamato-tamaatar.jpg",
      "Price": "Rs 30.00"
    },
    {
      "Title": "Onion",
      "qty": "500g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/25-1398-onion-ullipaya-pyaaj.html#/34-weight-500gm",
      "Image": "https://vizaggrocers.com/28-home_default/onion-ullipaya-pyaaj.jpg",
      "Price": "Rs 18.00"
    },
    {
      "Title": "Potato",
      "qty": "500g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/28-1399-vg-potato-bangaladumpa-aaloo.html#/34-weight-500gm",
      "Image": "https://vizaggrocers.com/30-home_default/vg-potato-bangaladumpa-aaloo.jpg",
      "Price": "Rs 25.00"
    },
    {
      "Title": "Cauliflower",
      "qty": "1pc",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/29-cauliflower-gobhee.html",
      "Image": "https://vizaggrocers.com/31-home_default/cauliflower-gobhee.jpg",
      "Price": "Rs 70.00"
    },
    {
      "Title": "Beetroot",
      "qty": "500g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/32-1401-beetroot-chukandar.html#/34-weight-500gm",
      "Image": "https://vizaggrocers.com/33-home_default/beetroot-chukandar.jpg",
      "Price": "Rs 30.00"
    },
    {
      "Title": "Ridge Gourd",
      "qty": "500g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/33-1403-ridgeguard-beerakaay-turee.html#/34-weight-500gm",
      "Image": "https://vizaggrocers.com/34-home_default/ridgeguard-beerakaay-turee.jpg",
      "Price": "Rs 30.00"
    },
    {
      "Title": "Cucumber",
      "qty": "500g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/35-1407-cucumber-dosakaya-kheera.html#/34-weight-500gm",
      "Image": "https://vizaggrocers.com/36-home_default/cucumber-dosakaya-kheera.jpg",
      "Price": "Rs 20.00"
    },
    {
      "Title": "Bitter Gourd",
      "qty": "500g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/36-1526-bitter-guard-kakarakaya-karela.html#/34-weight-500gm",
      "Image": "https://vizaggrocers.com/37-home_default/bitter-guard-kakarakaya-karela.jpg",
      "Price": "Rs 25.00"
    },
    {
      "Title": "Radish",
      "qty": "500g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/38-1411-vg-radish-mullangi-1kg.html#/34-weight-500gm",
      "Image": "https://vizaggrocers.com/39-home_default/vg-radish-mullangi-1kg.jpg",
      "Price": "Rs 40.00"
    },
    {
      "Title": "Sweet Corn",
      "qty": "4pc",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/39-vg-sweet-corn-4-pieces.html",
      "Image": "https://vizaggrocers.com/40-home_default/vg-sweet-corn-4-pieces.jpg",
      "Price": "Rs 50.00"
    },
    {
      "Title": "Pumpkin",
      "qty": "250g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/40-vg-pumpkin-250g.html",
      "Image": "https://vizaggrocers.com/41-home_default/vg-pumpkin-250g.jpg",
      "Price": "Rs 50.00"
    },
    {
      "Title": "Drum Sticks",
      "qty": "3pc",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/41-drumsticks-munagakaya.html",
      "Image": "https://vizaggrocers.com/43-home_default/drumsticks-munagakaya.jpg",
      "Price": "Rs 25.00"
    },
    {
      "Title": "Bottle Gourd",
      "qty": "1pc",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/43-bottlegourd-sorakaya-laukee.html",
      "Image": "https://vizaggrocers.com/44-home_default/bottlegourd-sorakaya-laukee.jpg",
      "Price": "Rs 40.00"
    },
    {
      "Title": "Coccinia (dondakaya)",
      "qty": "500g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/44-1413-coccinia-dondakaya-kundru.html#/34-weight-500gm",
      "Image": "https://vizaggrocers.com/45-home_default/coccinia-dondakaya-kundru.jpg",
      "Price": "Rs 30.00"
    },
    {
      "Title": "Beans",
      "qty": "500g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/45-1415-vg-beans-phaliyaan.html#/34-weight-500gm",
      "Image": "https://vizaggrocers.com/46-home_default/vg-beans-phaliyaan.jpg",
      "Price": "Rs 70.00"
    },
    {
      "Title": "Cabbage",
      "qty": "1000g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/46-cabbage-Kyabeji-pattagobhee.html",
      "Image": "https://vizaggrocers.com/47-home_default/cabbage-Kyabeji-pattagobhee.jpg",
      "Price": "Rs 60.00"
    },
    {
      "Title": "Chilli Green","qty": "250g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/47-1419-greenchilli-paccimirci-hareemirch.html#/30-weight-250gm",
      "Image": "https://vizaggrocers.com/2103-home_default/greenchilli-paccimirci-hareemirch.jpg",
      "Price": "Rs 25.00"
    },
    {
      "Title": "Colocasia  (chemadumpa)",
      "qty": "500g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/49-1421-colocasia-cemagadda-aalukee.html#/34-weight-500gm",
      "Image": "https://vizaggrocers.com/50-home_default/colocasia-cemagadda-aalukee.jpg",
      "Price": "Rs 30.00"
    },
    {
      "Title": "Red chillies ( yendu mirapa)",
      "qty": "250g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/50-1557-redchillies-erramirapakayalu-laalmirch.html#/30-weight-250gm",
      "Image": "https://vizaggrocers.com/2102-home_default/redchillies-erramirapakayalu-laalmirch.jpg",
      "Price": "Rs 30.00"
    },
    {
      "Title": "Ladies Finger",
      "qty": "500g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/53-1422-ladiesfinger-bendakaya-bhindee.html#/34-weight-500gm",
      "Image": "https://vizaggrocers.com/53-home_default/ladiesfinger-bendakaya-bhindee.jpg",
      "Price": "Rs 45.00"
    },
    {
      "Title": "Sweet potato",
      "qty": "500g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/54-1425-sweetpotato-cilagadadumpa-shakarakand.html#/34-weight-500gm",
      "Image": "https://vizaggrocers.com/54-home_default/sweetpotato-cilagadadumpa-shakarakand.jpg",
      "Price": "Rs 45.00"
    },
    {
      "Title": "Cluster beans",
      "qty": "500g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/57-1426-clusterbeans-chikkudikaya-ganvaarphalee.html#/34-weight-500gm",
      "Image": "https://vizaggrocers.com/55-home_default/clusterbeans-chikkudikaya-ganvaarphalee.jpg",
      "Price": "Rs 70.00"
    },
    {
      "Title": "Broad beans( Vedalpu chikkudukayalu)",
      "qty": "500g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/58-1475-broadbeans-cikkudukayalu-vyaapaksem.html#/34-weight-500gm",
      "Image": "https://vizaggrocers.com/56-home_default/broadbeans-cikkudukayalu-vyaapaksem.jpg",
      "Price": "Rs 70.00"
    },
    {
      "Title": "Capsicum",
      "qty": "500g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/60-1428-capsicum-shimalamirch.html#/34-weight-500gm",
      "Image": "https://vizaggrocers.com/57-home_default/capsicum-shimalamirch.jpg",
      "Price": "Rs 40.00"
    },
    {
      "Title": "Carrot",
      "qty": "500g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/61-1430-carrot-gaajar.html#/34-weight-500gm",
      "Image": "https://vizaggrocers.com/58-home_default/carrot-gaajar.jpg",
      "Price": "Rs 50.00"
    },
    {
      "Title": "Amaranth leaves (thotakoora)",
      "qty": "3 bunches",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/64-amaranthleaves-thotakura-greenchaulai.html",
      "Image": "https://vizaggrocers.com/60-home_default/amaranthleaves-thotakura-greenchaulai.jpg",
      "Price": "Rs 15.00"
    },
    {
      "Title": "Mint leaves (pudinaakulu)",
      "qty": "1 bunch",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/67-mintleaves-pudinaakulu.html",
      "Image": "https://vizaggrocers.com/63-home_default/mintleaves-pudinaakulu.jpg",
      "Price": "Rs 20.00"
    },
    {
      "Title": "Roselle (Gongura)",
      "qty": "3 bunch",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/68-roselle-gongura.html",
      "Image": "https://vizaggrocers.com/64-home_default/roselle-gongura.jpg",
      "Price": "Rs 15.00"
    },
    {
      "Title": "Greenbanana ( koora aritikayalu )",
      "qty": "3 peices",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/100-greenbanana-aratikaya-kela.html",
      "Image": "https://vizaggrocers.com/93-home_default/greenbanana-aratikaya-kela.jpg",
      "Price": "Rs 30.00"
    },
    {
      "Title": "Spinach (Palakura)",
      "qty": "3 bunches",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/262-vg-spinach-palakura-3bunches.html",
      "Image": "https://vizaggrocers.com/316-home_default/vg-spinach-palakura-3bunches.jpg",
      "Price": "Rs 15.00"
    },
    {
      "Title": "Malabar Spinach (Bachalikura)",
      "qty": "3 bunches",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/263-malabarspinach-baccalikura-malabarpaalak.html",
      "Image": "https://vizaggrocers.com/317-home_default/malabarspinach-baccalikura-malabarpaalak.jpg",
      "Price": "Rs 15.00"
    },
    {
      "Title": "Garlic",
      "qty": "500g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/479-342-garlic-small-velluli-lahasoon.html#/34-weight-500gm",
      "Image": "https://vizaggrocers.com/472-home_default/garlic-small-velluli-lahasoon.jpg",
      "Price": "Rs 90.00"
    },
    {
      "Title": "Garlic Big (Velluli Pedhavi)",
      "qty": "500g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/499-367-Garlic-big-velluli-pedhavi-lahasun.html#/34-weight-500gm",
      "Image": "https://vizaggrocers.com/516-home_default/Garlic-big-velluli-pedhavi-lahasun.jpg",
      "Price": "Rs 90.00"
    },
    {
      "Title": "Lemon",
      "qty": "3pc",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/1667-lemon-nimmakaya-neemboo.html",
      "Image": "https://vizaggrocers.com/1752-home_default/lemon-nimmakaya-neemboo.jpg",
      "Price": "Rs 10.00"
    },
    {
      "Title": "Ginger",
      "qty": "250g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/1668-1432-ginger-allam-adarak.html#/30-weight-250gm",
      "Image": "https://vizaggrocers.com/1753-home_default/ginger-allam-adarak.jpg",
      "Price": "Rs 45.00"
    },
    {
      "Title": "Coconut",
      "qty": "1pc",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/1669-vg-coconut-1piece-.html",
      "Image": "https://vizaggrocers.com/1754-home_default/vg-coconut-1piece-.jpg",
      "Price": "Rs 25.00"
    },
    {
      "Title": "Coriander",
      "qty": "1 bunch",
      "Title_URL": "https://vizaggrocers.com/en/green-leafy-vegetables/63-corianderleaves-Kottimiraakulu-dhaniyekepatte.html",
      "Image": "https://vizaggrocers.com/59-home_default/corianderleaves-Kottimiraakulu-dhaniyekepatte.jpg",
      "Price": "Rs 20.00"
    },
    {
      "Title": "Curry leaves",
      "qty": "1 bunch",
      "Title_URL": "https://vizaggrocers.com/en/green-leafy-vegetables/65-curryleaves-Karivepaku-kareepatte.html",
      "Image": "https://vizaggrocers.com/61-home_default/curryleaves-Karivepaku-kareepatte.jpg",
      "Price": "Rs 5.00"
    },
    {
      "Title": "Yam (kandagadda)",
      "qty": "500g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/1892-1485-vg-yam-kandagadda.html#/34-weight-500gm",
      "Image": "https://vizaggrocers.com/2100-home_default/vg-yam-kandagadda.jpg",
      "Price": "Rs 35.00"
    },
    {
      "Title": "Snake gourd (Potlakaya)",
      "qty": "1 pc",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/1896-vg-snack-guard-potlakaya-1-piece.html",
      "Image": "https://vizaggrocers.com/2119-home_default/vg-snack-guard-potlakaya-1-piece.jpg",
      "Price": "Rs 40.00"
    },
    {
      "Title": " Tapioca Karrapendalam",
      "qty": "500g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/1934-1516-vg-tapioca-karrapendalam.html#/34-weight-500gm",
      "Image": "https://vizaggrocers.com/2191-home_default/vg-tapioca-karrapendalam.jpg",
      "Price": "Rs 45.00"
    },
    {
      "Title": "Brinjal",
      "qty": "500g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/1936-1522-brinjal-vankayalu-baingan.html#/34-weight-500gm",
      "Image": "https://vizaggrocers.com/2206-home_default/brinjal-vankayalu-baingan.jpg",
      "Price": "Rs 30.00"
    },
    {
      "Title": "Raw Groundnuts",
      "qty": "500g",
      "Title_URL": "https://vizaggrocers.com/en/seeds-beans-nuts/1709-raw-groundnuts-.html",
      "Image": "https://vizaggrocers.com/1796-home_default/raw-groundnuts-.jpg",
      "Price": "Rs 70.00"
    },
    {
      "Title": "Green peas (Pachi Batani)",
      "qty": "500g",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/257-269-green-peas-pacci-bathani-haree-matar.html#/34-weight-500gm",
      "Image": "https://vizaggrocers.com/547-home_default/green-peas-pacci-bathani-haree-matar.jpg",
      "Price": "Rs 70.00"
    },
    {
      "Title": "Fenugreek leaves (మెంతి ఆకులు)",
      "qty": "3pc",
      "Title_URL": "https://vizaggrocers.com/en/vegetables/66-fenugreekleaves-mentiakulu-kasooreemethee.html",
      "Image": "https://vizaggrocers.com/62-home_default/fenugreekleaves-mentiakulu-kasooreemethee.jpg",
      "Price": "Rs 15.00"
    }
  ]
}
@app.route('/')
def hello_world():
  return render_template('index.html')

@app.route('/visakhapatnam cart',methods=["GET","POST"])
def cartv():
  if request.method == "POST":
    onionqty = request.form.get("onionquantity")
    tomatoqty = request.form.get("tomatoquantity")
    potatoqty = request.form.get("potatoquantity")
    beetrootqty = request.form.get("beetrootquantity")
    cucumberqty=request.form.get("cucumberquantity")
    bittergourdqty = request.form.get("bittergourdquantity")
    bottlegourdqty = request.form.get("bottlegourdquantity")
    dic={}
    for k, i in visakha.items():
      dic[k] = 0
    for k, i in visakha.items():
      for j in i:
        if j["Title"] == "Onion":
          if j["qty"] == "250g":
            dic[k] += float(onionqty) * float(j["Price"][3:]) * 4
          elif j["qty"] == "500g":
            dic[k] += float(onionqty) * float(j["Price"][3:]) * 2
          else:
            dic[k] += float(onionqty) * float(j["Price"][3:])

    for k, i in visakha.items():
      for j in i:
        if j["Title"] == "Tomato":
          if j["qty"] == "250g":
            dic[k] += float(tomatoqty) * float(j["Price"][3:]) * 4
          elif j["qty"] == "500g":
            dic[k] += float(tomatoqty) * float(j["Price"][3:]) * 2
          else:
            dic[k] += float(tomatoqty) * float(j["Price"][3:])

    for k, i in visakha.items():
      for j in i:
        if j["qty"] == "250g":
          dic[k] += float(potatoqty) * float(j["Price"][3:]) * 4
        elif j["qty"] == "500g":
          dic[k] += float(potatoqty) * float(j["Price"][3:]) * 2
        else:
          dic[k] += float(potatoqty) * float(j["Price"][3:])

    for k, i in visakha.items():
      for j in i:
        if j["qty"] == "250g":
          dic[k] += float(beetrootqty) * float(j["Price"][3:]) * 4
        elif j["qty"] == "500g":
          dic[k] += float(beetrootqty) * float(j["Price"][3:]) * 2
        else:
          dic[k] += float(beetrootqty) * float(j["Price"][3:])

    for k, i in visakha.items():
      for j in i:
        if j["qty"] == "250g":
          dic[k] += float(cucumberqty) * float(j["Price"][3:]) * 4
        elif j["qty"] == "500g":
          dic[k] += float(cucumberqty) * float(j["Price"][3:]) * 2
        else:
          dic[k] += float(cucumberqty) * float(j["Price"][3:])

    for k, i in visakha.items():
      for j in i:
        if j["qty"] == "250g":
          dic[k] += float(bittergourdqty) * float(j["Price"][3:]) * 4
        elif j["qty"] == "500g":
          dic[k] += float(bittergourdqty) * float(j["Price"][3:]) * 2
        else:
          dic[k] += float(bittergourdqty) * float(j["Price"][3:])

    for k, i in visakha.items():
      for j in i:
        if j["qty"] == "250g":
          dic[k] += float(bottlegourdqty) * float(j["Price"][3:]) * 4
        elif j["qty"] == "500g":
          dic[k] += float(bottlegourdqty) * float(j["Price"][3:]) * 2
        else:
          dic[k] += float(bottlegourdqty) * float(j["Price"][3:])

    key_value = dic
    k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
    res=dict(k)
    return render_template("visakha_cartresult.html",visakha=visakha,res=res,visakha_shops=visakha_shops,vegetables=vegetables)
  return render_template('visakha_cart.html',visakha=visakha,vegetables=vegetables)

@app.route('/madhapur cart',methods=["GET","POST"])
def cartm():
  flag=0
  if request.method == "POST":
    flag=1
    onionqty = request.form.get("onionquantity")
    tomatoqty = request.form.get("tomatoquantity")
    potatoqty = request.form.get("potatoquantity")
    beetrootqty = request.form.get("beetrootquantity")
    cucumberqty=request.form.get("cucumberquantity")
    bittergourdqty = request.form.get("bittergourdquantity")
    bottlegourdqty = request.form.get("bottlegourdquantity")
    dic={}
    for k, i in madha.items():
      dic[k] = 0
    for k, i in madha.items():
      for j in i:
        if j["Title"] == "Onion":
          if j["qty"] == "250g":
            dic[k] += float(onionqty) * float(j["Price"][3:]) * 4
          elif j["qty"] == "500g":
            dic[k] += float(onionqty) * float(j["Price"][3:]) * 2
          else:
            dic[k] += float(onionqty) * float(j["Price"][3:])


    for k, i in madha.items():
      for j in i:
        if j["Title"] == "Tomato":
          if j["qty"] == "250g":
            dic[k] += float(tomatoqty) * float(j["Price"][3:]) * 4
          elif j["qty"] == "500g":
            dic[k] += float(tomatoqty) * float(j["Price"][3:]) * 2
          else:
            dic[k] += float(tomatoqty) * float(j["Price"][3:])

    for k, i in madha.items():
      for j in i:
        if j["Title"] == "Potato":
          if j["qty"] == "250g":
            dic[k] += float(potatoqty) * float(j["Price"][3:]) * 4
          elif j["qty"] == "500g":
            dic[k] += float(potatoqty) * float(j["Price"][3:]) * 2
          else:
            dic[k] += float(potatoqty) * float(j["Price"][3:])

    for k, i in madha.items():
      for j in i:
        if j["Title"] == "Beetroot":
          if j["qty"] == "250g":
            dic[k] += float(beetrootqty) * float(j["Price"][3:]) * 4
          elif j["qty"] == "500g":
            dic[k] += float(beetrootqty) * float(j["Price"][3:]) * 2
          else:
            dic[k] += float(beetrootqty) * float(j["Price"][3:])

    for k, i in madha.items():
      for j in i:
        if j["Title"] == "Cucumber":
          if j["qty"] == "250g":
            dic[k] += float(cucumberqty) * float(j["Price"][3:]) * 4
          elif j["qty"] == "500g":
            dic[k] += float(cucumberqty) * float(j["Price"][3:]) * 2
          else:
            dic[k] += float(cucumberqty) * float(j["Price"][3:])

    for k, i in madha.items():
      for j in i:
        if j["Title"] == "Bitter Gourd":
          if j["qty"] == "250g":
            dic[k] += float(bittergourdqty) * float(j["Price"][3:]) * 4
          elif j["qty"] == "500g":
            dic[k] += float(bittergourdqty) * float(j["Price"][3:]) * 2
          else:
            dic[k] += float(bittergourdqty) * float(j["Price"][3:])

    for k, i in madha.items():
      for j in i:
        if j["Title"] == "Bottle Gourd":
          if j["qty"] == "250g":
            dic[k] += float(bottlegourdqty) * float(j["Price"][3:]) * 4
          elif j["qty"] == "500g":
            dic[k] += float(bottlegourdqty) * float(j["Price"][3:]) * 2
          else:
            dic[k] += float(bottlegourdqty) * float(j["Price"][3:])

    key_value = dic
    k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
    res=dict(k)
    return render_template("madhapur_cartresult.html",madha=madha,res=res,madhapur_shops=madhapur_shops,vegetables=vegetables)
  return render_template('madhapur_cart.html',madha=madha,vegetables=vegetables)

@app.route('/gachibowli cart',methods=["GET","POST"])
def cartg():
  flag=0
  if request.method == "POST":
    flag=1
    onionqty = request.form.get("onionquantity")
    tomatoqty = request.form.get("tomatoquantity")
    potatoqty = request.form.get("potatoquantity")
    beetrootqty = request.form.get("beetrootquantity")
    cucumberqty=request.form.get("cucumberquantity")
    bottlegourdqty = request.form.get("bottlegourdquantity")
    dic={}
    for k, i in gachi.items():
      dic[k] = 0
    for k, i in gachi.items():
      for j in i:
        if j["Title"] == "Onion":
          if j["qty"] == "250g":
            dic[k] += float(onionqty) * float(j["Price"][3:]) * 4
          elif j["qty"] == "500g":
            dic[k] += float(onionqty) * float(j["Price"][3:]) * 2
          else:
            dic[k] += float(onionqty) * float(j["Price"][3:])

    for k, i in gachi.items():
      for j in i:
        if j["Title"] == "Tomato":
          if j["qty"] == "250g":
            dic[k] += float(tomatoqty) * float(j["Price"][3:]) * 4
          elif j["qty"] == "500g":
            dic[k] += float(tomatoqty) * float(j["Price"][3:]) * 2
          else:
            dic[k] += float(tomatoqty) * float(j["Price"][3:])

    for k, i in gachi.items():
      for j in i:
        if j["Title"] == "Potato":
          if j["qty"] == "250g":
            dic[k] += float(potatoqty) * float(j["Price"][3:]) * 4
          elif j["qty"] == "500g":
            dic[k] += float(potatoqty) * float(j["Price"][3:]) * 2
          else:
            dic[k] += float(potatoqty)* float(j["Price"][3:])

    for k, i in gachi.items():
      for j in i:
        if j["Title"] == "Beetroot":
          if j["qty"] == "250g":
            dic[k] += float(beetrootqty) * float(j["Price"][3:]) * 4
          elif j["qty"] == "500g":
            dic[k] += float(beetrootqty) * float(j["Price"][3:]) * 2
          else:
            dic[k] += float(beetrootqty) * float(j["Price"][3:])

    for k, i in gachi.items():
      for j in i:
        if j["Title"] == "Cucumber":
          if j["qty"] == "250g":
            dic[k] += float(cucumberqty) * float(j["Price"][3:]) * 4
          elif j["qty"] == "500g":
            dic[k] += float(cucumberqty) * float(j["Price"][3:]) * 2
          else:
            dic[k] += float(cucumberqty) * float(j["Price"][3:])

    for k, i in gachi.items():
      for j in i:
        if j["Title"] == "Bottle Gourd":
          if j["qty"] == "250g":
            dic[k] += float(bottlegourdqty) * float(j["Price"][3:]) * 4
          elif j["qty"] == "500g":
            dic[k] += float(bottlegourdqty) * float(j["Price"][3:]) * 2
          else:
            dic[k] += float(bottlegourdqty) * float(j["Price"][3:])

    key_value = dic
    k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
    res=dict(k)
    return render_template("gachibowli_cartresult.html",gachi=gachi,res=res,gachibowli_shops=gachibowli_shops,vegetables=vegetables)
  return render_template('gachibowli_cart.html',gachi=gachi,vegetables=vegetables)

# <-----------city1 websites------------------>

@app.route('/jiomart')
def jio():
    return render_template('city1/jiomart.html',jiom=jiom,vegetables=vegetables)

@app.route('/vizaggrocers')
def vizaggro():
    return render_template('city1/vizaggrocers.html',grocers=grocers,vegetables=vegetables)

@app.route('/bigbasket')
def bigb():
    return render_template('city1/bigbasket.html',bigbas=bigbas,vegetables=vegetables)

@app.route('/naturebasket')
def natureb():
    return render_template('city1/naturebasket.html',naturebas=naturebas,vegetables=vegetables)

# <----------city2 websites--------------->

@app.route('/saifruitsandvegetables')
def saiveg():
    return render_template('city2/saifruitsandvegetables.html',sai=sai,vegetables=vegetables)

@app.route('/sirisupermarket')
def sirism():
    return render_template('city2/sirisupermarket.html',siri=siri,vegetables=vegetables)

@app.route('/kisanbazaar')
def kisanb():
    return render_template('city2/kisanbazaar.html',kisan=kisan,vegetables=vegetables)

@app.route('/tarkariexoticvegetables')
def tarkar():
    return render_template('city2/tarkariexoticvegetables.html',tarkari=tarkari,vegetables=vegetables)

@app.route('/halofarm')
def halog():
    return render_template('city2/halofarm.html',halo=halo,vegetables=vegetables)

# <------------city3 websites-------------->

@app.route('/akella')
def akellag():
    return render_template('city3/akellaagro.html',akella=akella,vegetables=vegetables)

@app.route('/polam')
def polamg():
    return render_template('city3/polam.html',polam=polam,vegetables=vegetables)

@app.route('/ratandeep')
def ratandeepg():
    return render_template('city3/ratandeep.html',ratan=ratan,vegetables=vegetables)

@app.route('/supraja')
def rajugarig():
    return render_template('city3/supraja.html',raju=raju,vegetables=vegetables)

@app.route('/freshbasket')
def freshg():
    return render_template('city3/freshbasket.html',fresh=fresh,vegetables=vegetables)


vegetables=["Onion","Beetroot","Bitter Gourd","Potato","Cucumber","Bottle Gourd","Ladies Finger","Tomato"]

# <----------cities--------------->
@app.route('/visakhapatnam')
def visakhap():
    return render_template('visakhapatnam.html',visakha=visakha,vegetables=vegetables)

@app.route('/madhapur')
def madhapurr():
    return render_template('madhapur.html',vegetables=vegetables,madha=madha)

@app.route('/gachibowli')
def gachib():
    return render_template('gachibowli.html',vegetables=vegetables,gachi=gachi)

dic={}
# <---------------------city1 veggies ------------>
@app.route('/Onion visakha')
def onionv():
  dic = {}
  for j, i in visakha.items():
    for k in i:
      if k["Title"] == "Onion":
        dic[j] = k["Price"]
  key_value=dic
  k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
  return render_template('city1/onion.html',visakha=visakha,vegetables=vegetables,k=k)

@app.route('/Bottle Gourd visakha')
def bottlegourdv():
  dic = {}
  for j, i in visakha.items():
    for k in i:
      if k["Title"] == "Bottle Gourd":
        dic[j] = k["Price"]
  key_value = dic
  k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
  return render_template('city1/Bottle Gourd.html',visakha=visakha,vegetables=vegetables,k=k)

@app.route('/Cucumber visakha')
def cucumberv():
  dic = {}
  for j, i in visakha.items():
    for k in i:
      if k["Title"] == "Cucumber":
        dic[j] = k["Price"]
  key_value = dic
  k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
  return render_template('city1/Cucumber.html',visakha=visakha,vegetables=vegetables,k=k)

@app.route('/Tomato visakha')
def tomatov():
  dic = {}
  for j, i in visakha.items():
    for k in i:
      if k["Title"] == "Tomato":
        dic[j] = k["Price"]
  key_value = dic
  k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
  return render_template('city1/Tomato.html',visakha=visakha,vegetables=vegetables,k=k)

@app.route('/Beetroot visakha')
def beetrootv():
  dic = {}
  for j, i in visakha.items():
    for k in i:
      if k["Title"] == "Beetroot":
        dic[j] = k["Price"]
  key_value = dic
  k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
  return render_template('city1/Beetroot.html',visakha=visakha,vegetables=vegetables,k=k)

@app.route('/Potato visakha')
def potatov():
  dic = {}
  for j, i in visakha.items():
    for k in i:
      if k["Title"] == "Potato":
        dic[j] = k["Price"]
  key_value = dic
  k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
  return render_template('city1/Potato.html',visakha=visakha,vegetables=vegetables,k=k)

@app.route('/Bitter Gourd visakha')
def bittergourdv():
  dic = {}
  for j, i in visakha.items():
    for k in i:
      if k["Title"] == "Bitter Gourd":
        dic[j] = k["Price"]
  key_value = dic
  k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
  return render_template('city1/Bitter Gourd.html',visakha=visakha,vegetables=vegetables,k=k)

@app.route('/Ladies Finger visakha')
def ladiesfingerv():
  dic = {}
  for j, i in visakha.items():
    for k in i:
      if k["Title"] == "Ladies Finger":
        dic[j] = k["Price"]
  key_value = dic
  k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
  return render_template('city1/Ladies Finger.html',visakha=visakha,vegetables=vegetables,k=k)

# <---------------city2 veggies ---------------->

@app.route('/Onion madhapu')
def onionm():
  dic = {}
  for j, i in madha.items():
    for k in i:
      if k["Title"] == "Onion":
        dic[j] = k["Price"]
  key_value = dic
  k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
  return render_template('city2/onion.html',madha=madha,vegetables=vegetables,k=k)

@app.route('/Bottle Gourd madhapu')
def bottlegourdm():
  dic = {}
  for j, i in madha.items():
    for k in i:
      if k["Title"] == "Bottle Gourd":
        dic[j] = k["Price"]
  key_value = dic
  k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
  return render_template('city2/bottlegourd.html',madha=madha,vegetables=vegetables,k=k)

@app.route('/Cucumber madhapu')
def cucumberm():
  dic = {}
  for j, i in madha.items():
    for k in i:
      if k["Title"] == "Cucumber":
        dic[j] = k["Price"]
  key_value = dic
  k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
  return render_template('city2/cucumber.html',madha=madha,vegetables=vegetables,k=k)

@app.route('/Tomato madhapu')
def tomatom():
  dic = {}
  for j, i in madha.items():
    for k in i:
      if k["Title"] == "Tomato":
        dic[j] = k["Price"]
  key_value = dic
  k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
  return render_template('city2/tomato.html',madha=madha,vegetables=vegetables,k=k)

@app.route('/Beetroot madhapu')
def beetrootm():
  dic = {}
  for j, i in madha.items():
    for k in i:
      if k["Title"] == "Beetroot":
        dic[j] = k["Price"]
  key_value = dic
  k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
  return render_template('city2/beetroot.html',madha=madha,vegetables=vegetables,k=k)

@app.route('/Potato madhapu')
def potatom():
  dic = {}
  for j, i in madha.items():
    for k in i:
      if k["Title"] == "Potato":
        dic[j] = k["Price"]
  key_value = dic
  k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
  return render_template('city2/potato.html',madha=madha,vegetables=vegetables,k=k)

@app.route('/Bitter Gourd madhapu')
def bittergourdm():
  dic = {}
  for j, i in madha.items():
    for k in i:
      if k["Title"] == "Bitter Gourd":
        dic[j] = k["Price"]
  key_value = dic
  k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
  return render_template('city2/bittergourd.html',madha=madha,vegetables=vegetables,k=k)

@app.route('/Ladies Finger madhapu')
def ladiesfingerm():
  dic = {}
  for j, i in madha.items():
    for k in i:
      if k["Title"] == "Ladies Finger":
        dic[j] = k["Price"]
  key_value = dic
  k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
  return render_template('city2/ladiesfinger.html',madha=madha,vegetables=vegetables,k=k)

# <--------------city3 veggies ----------->

@app.route('/Onion gachibow')
def oniong():
  dic = {}
  for j, i in gachi.items():
    for k in i:
      if k["Title"] == "Onion":
        dic[j] = k["Price"]
  key_value = dic
  k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
  return render_template('city3/onion.html',gachi=gachi,vegetables=vegetables,k=k)

@app.route('/Bottle Gourd gachibow')
def bottlegourdg():
  dic = {}
  for j, i in gachi.items():
    for k in i:
      if k["Title"] == "Bottle Gourd":
        dic[j] = k["Price"]
  key_value = dic
  k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
  return render_template('city3/bottlegourd.html',gachi=gachi,vegetables=vegetables,k=k)

@app.route('/Cucumber gachibow')
def cucumberg():
  dic = {}
  for j, i in gachi.items():
    for k in i:
      if k["Title"] == "Cucumber":
        dic[j] = k["Price"]
  key_value = dic
  k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
  return render_template('city3/cucumber.html',gachi=gachi,vegetables=vegetables,k=k)

@app.route('/Tomato gachibow')
def tomatog():
  dic = {}
  for j, i in gachi.items():
    for k in i:
      if k["Title"] == "Tomato":
        dic[j] = k["Price"]
  key_value = dic
  k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
  return render_template('city3/tomato.html',gachi=gachi,vegetables=vegetables,k=k)

@app.route('/Beetroot gachibow')
def beetrootg():
  dic = {}
  for j, i in gachi.items():
    for k in i:
      if k["Title"] == "Beetroot":
        dic[j] = k["Price"]
  key_value = dic
  k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
  return render_template('city3/beetroot.html',gachi=gachi,vegetables=vegetables,k=k)

@app.route('/Potato gachibow')
def potatog():
  dic = {}
  for j, i in gachi.items():
    for k in i:
      if k["Title"] == "Potato":
        dic[j] = k["Price"]
  key_value = dic
  k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
  return render_template('city3/potato.html',gachi=gachi,vegetables=vegetables,k=k)

@app.route('/Bitter Gourd gachibow')
def bittergourdg():
  dic = {}
  for j, i in gachi.items():
    for k in i:
      if k["Title"] == "Bitter Gourd":
        dic[j] = k["Price"]
  key_value = dic
  k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
  return render_template('city3/bittergourd.html',gachi=gachi,vegetables=vegetables,k=k)

@app.route('/Ladies Finger gachibow')
def ladiesfingerg():
  dic = {}
  for j, i in gachi.items():
    for k in i:
      if k["Title"] == "Ladies Finger":
        dic[j] = k["Price"]
  key_value = dic
  k = sorted(key_value.items(), key=lambda kv: (kv[1], kv[0]))
  return render_template('city3/ladiesfinger.html',gachi=gachi,vegetables=vegetables,k=k)


