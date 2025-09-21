import streamlit as st
from PIL import Image, ImageOps
import requests
from io import BytesIO

# ---- PAGE CONFIG ----
st.set_page_config(page_title="College Canteen", page_icon="🍽", layout="wide")

# ---- CUSTOM BACKGROUND WITH SOFT DARK OVERLAY ----
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.4)), 
                      url("https://images.unsplash.com/photo-1600891964599-f61ba0e24092?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwxfDB8MXxyYW5kb218MHx8Y2FudGVlbnwxfHx8fHww&ixlib=rb-4.0.3&q=80&w=1080");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}
.block-container {
    background: rgba(255,255,255,0);  /* fully transparent */
    padding: 1rem;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ---- MENU DATA WITH IMAGE URLS ----
weekly_menu = {
    "Monday": {1: ("Poha", 20, "https://blog.eatfit.in/wp-content/uploads/2022/12/image-31-1024x1024.png"),
               2: ("Tea", 10, "https://masalaandchai.com/wp-content/uploads/2021/07/Masala-Chai.jpg"),
               3: ("Samosa", 15, "https://im.whatshot.in/img/2019/Aug/shutterstock-1381163087-cropped-1565077618.jpg")},
    "Tuesday": {1: ("Idli", 30, "https://www.healthifyme.com/blog/wp-content/uploads/2018/03/idly2.jpeg"),
                2: ("Coffee", 15, "https://images.pexels.com/photos/414720/pexels-photo-414720.jpeg"),
                3: ("Sandwich", 40, "https://www.baltana.com/files/wallpapers-1/Sandwich-01186.jpg")},
    "Wednesday": {1: ("Paratha", 25, "https://i.ytimg.com/vi/3rkXplTcAOA/maxresdefault.jpg"),
                  2: ("Lassi", 30, "https://www.yourhungerstop.com/wp-content/uploads/2015/04/SweetLassi.jpg"),
                  3: ("Chole Bhature", 50, "https://tse3.mm.bing.net/th/id/OIP.ymwwbTsC9la3suJmIJ-3eQHaE_?rs=1&pid=ImgDetMain")},
    "Thursday": {1: ("Maggi", 25, "https://i.pinimg.com/originals/fd/f6/ab/fdf6ab5a30b921bc4b8b68ccf5db040e.png"),
                 2: ("Tea", 10, "https://masalaandchai.com/wp-content/uploads/2021/07/Masala-Chai.jpg"),
                 3: ("Pakora", 20, "https://tse4.mm.bing.net/th/id/OIP.apZBEEyC3P6-NDhQ9BgHYQHaE7?rs=1&pid=ImgDetMain")},
    "Friday": {1: ("Dosa", 40, "https://png.pngtree.com/background/20230613/original/pngtree-plate-of-dosa-with-sauce-on-top-picture-image_3422751.jpg"),
               2: ("Cold Drink", 20, "https://www.shutterstock.com/shutterstock/photos/2075670211/display_1500/stock-photo-poznan-poland-oct-bottles-of-global-soft-drink-brands-including-products-of-coca-cola-2075670211.jpg"),
               3: ("Vada Pav", 15, "https://i.pinimg.com/736x/c4/f2/df/c4f2df229b163a961afbf8001c69d8fd.jpg")},
    "Saturday": {1: ("Thali", 80, "https://img.freepik.com/premium-photo/indian-hindu-veg-thali-also-known-as-food-platter-is-complete-lunch-dinner-meal-closeup-selective-focus_466689-9137.jpg"),
                 2: ("Roti Sabzi", 50, "https://st2.depositphotos.com/19320080/46492/i/950/depositphotos_464927076-stock-photo-puri-sabji-poori-sabzi-indian.jpg"),
                 3: ("Jalebi", 30, "https://as1.ftcdn.net/v2/jpg/04/39/55/84/1000_F_439558401_z4va4arE91OhmGE8XkEhZCRQiYEMlarb.jpg")}
}

special_dish = {
    "Monday": "Poha with a twist of peanuts",
    "Tuesday": "Steamy Idli served with spicy chutney",
    "Wednesday": "Chole Bhature – the king of taste",
    "Thursday": "Maggi magic for your hunger",
    "Friday": "Crispy Dosa – south Indian delight",
    "Saturday": "Full Thali – feast like a king"
}

# ---- APP TITLE ----
st.title("🍽 Welcome to Our College Canteen")
st.subheader("Good Food = Good Mood! Stay Happy 😄")

# ---- DAY SELECTION ----
day = st.selectbox("Select day of the week", list(weekly_menu.keys()))
menu = weekly_menu[day]

# ---- FUNCTION TO LOAD AND PAD IMAGES ----
def load_and_pad_image(url, size=(150,150)):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = ImageOps.fit(img, size, Image.ANTIALIAS)
    return img

# ---- DISPLAY MENU ----
st.write(f"### Menu for {day}")
cols = st.columns(len(menu))
for idx, (key, value) in enumerate(menu.items()):
    item, price, img_url = value
    with cols[idx]:
        img = load_and_pad_image(img_url)
        st.image(img, caption=f"{item}\nRs.{price}")

st.write(f"**Special Dish:** {special_dish[day]}")

# ---- ORDER SECTION ----
st.write("---")
st.write("### Place your order")
order = {}
for key, value in menu.items():
    item, price, img_url = value
    qty = st.number_input(f"{item} (Rs.{price})", min_value=0, step=1, key=key)
    if qty > 0:
        order[key] = qty

# ---- BILL ----
if st.button("Generate Bill"):
    if order:
        st.write("### 🧾 Bill Receipt")
        total = 0
        for item_no, qty in order.items():
            item, price, img_url = menu[item_no]
            cost = price * qty
            total += cost
            st.write(f"{item} x {qty} = Rs.{cost}")
        st.write(f"**Total Bill = Rs.{total}**")
        st.success("Thank you for visiting our Canteen! Come hungry, leave happy 😋")
    else:
        st.warning("No items selected. Visit again when hungry!")
