import streamlit as st

# ---------- Page Config ----------
st.set_page_config(page_title="College Canteen", page_icon="🍴", layout="wide")

# ---------- Custom Background & CSS ----------
page_bg = """
<style>
/* Background Gradient */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #f9f9f9, #e3f2fd);
    background-attachment: fixed;
}

/* Remove header background */
[data-testid="stHeader"] {
    background: rgba(0,0,0,0);
}

/* Headings */
h1 {
    color: #d84315;
    text-align: center;
    font-family: 'Trebuchet MS', sans-serif;
    font-size: 3em;
}
h2, h3 {
    color: #1565c0;
    font-family: 'Segoe UI', sans-serif;
}

/* Food Card Style */
.food-card {
    padding: 20px;
    margin: 10px;
    border-radius: 20px;
    box-shadow: 2px 4px 12px rgba(0,0,0,0.25);
    background-color: white;
    text-align: center;
    transition: transform 0.25s;
}
.food-card:hover {
    transform: scale(1.05);
    box-shadow: 4px 8px 20px rgba(0,0,0,0.3);
}

/* Order Section */
.order-box {
    background: #ffffffcc;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 2px 4px 12px rgba(0,0,0,0.2);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ---------- Title ----------
st.markdown("<h1>🍽 Welcome to Our College Canteen</h1>", unsafe_allow_html=True)
st.write("### 🌟 Good Food = Good Mood! Stay Happy 😋")

# ---------- Weekly Menu (Mon-Sat) ----------
weekly_menu = {
    "Monday": [
        {"name": "Poha", "price": 25, "img": "https://2.bp.blogspot.com/_jg7bOK0iY5E/S-b5FvInviI/AAAAAAAAAGQ/SbVL41SwyTc/s1600/Poha_01.jpg"},
        {"name": "Tea", "price": 10, "img": "https://i.pinimg.com/originals/b4/fd/ea/b4fdea77c96e520dcbec32114fd765fa.jpg"},
        {"name": "Vada Pav", "price": 20, "img": "https://www.indianhealthyrecipes.com/wp-content/uploads/2019/10/vada-pav-recipe-680x510.jpg"}
    ],
    "Tuesday": [
        {"name": "Idli", "price": 30, "img": "https://www.healthifyme.com/blog/wp-content/uploads/2018/03/idly2.jpeg"},
        {"name": "Coffee", "price": 15, "img": "https://images.pexels.com/photos/1170659/pexels-photo-1170659.jpeg?cs=srgb&dl=art-bread-brown-1170659.jpg&fm=jpg"},
        {"name": "Sandwich", "price": 40, "img": "https://tse4.mm.bing.net/th/id/OIP.k6hKBbbjWhRD-jxynvecVQHaFP?rs=1&pid=ImgDetMain&o=7&rm=3"}
    ],
    "Wednesday": [
        {"name": "Pav Bhaji", "price": 50, "img": "https://tse4.mm.bing.net/th/id/OIP.ggkkqdypy7CimfbKdCl9TgHaJQ?rs=1&pid=ImgDetMain&o=7&rm=3"},
        {"name": "Cold Drink", "price": 25, "img": "https://c8.alamy.com/comp/WX0H4X/bottles-of-global-soft-drink-brands-including-products-of-coca-cola-company-and-pepsico-WX0H4X.jpg"},
        {"name": "Samosa", "price": 15, "img": "https://wallpaperaccess.com/full/2069188.jpg"}
    ],
    "Thursday": [
        {"name": "Chole Bhature", "price": 60, "img": "https://wallpaperaccess.com/full/10449454.jpg"},
        {"name": "Lassi", "price": 30, "img": "https://www.indianveggiedelight.com/wp-content/uploads/2023/01/sweet-lassi-recipe-1.jpg"},
        {"name": "Pakora", "price": 20, "img": "https://th.bing.com/th/id/R.5fb78cef3a6b2b1badc917d2798a86f0?rik=pMm%2bIoYNo%2bi7rw&riu=http%3a%2f%2fwww.archanaskitchen.com%2fimages%2farchanaskitchen%2f1-Author%2fShaheen_Ali%2fVeg_Noodle_Pakora.jpg&ehk=wKCzNj%2bMX%2bVUdeQskTZACMTHCIBXEn02zNDiBZGAEjU%3d&risl=&pid=ImgRaw&r=0"}
    ],
    "Friday": [
        {"name": "Masala Dosa", "price": 50, "img": "https://tse4.mm.bing.net/th/id/OIP.AAeMOleCsTZ6bN_MA_cQqQHaEK?rs=1&pid=ImgDetMain&o=7&rm=3"},
        {"name": "maggi ", "price": 20, "img": "https://th.bing.com/th/id/OIP.MRapZiIRkzMJDotroNDHjgHaEK?o=7rm=3&rs=1&pid=ImgDetMain&o=7&rm=3"},
        {"name": "cake", "price": 70, "img": "https://patelbakery.in/wp-content/uploads/2021/06/chocolate-pastry-2-new.jpg"}
    ],
    "Saturday": [
        {"name": "Aloo Paratha", "price": 40, "img": "https://tse4.mm.bing.net/th/id/OIP.Lq0URBXQfvmhpZF0bYbWEAHaFz?rs=1&pid=ImgDetMain&o=7&rm=3"},
        {"name": "Curd", "price": 20, "img": "https://media.istockphoto.com/photos/yogurt-is-good-for-health-with-black-background-picture-id1214850940?b=1&k=20&m=1214850940&s=170667a&w=0&h=TK72cIpgpufxOq8NeL1ZrGs3ZIzc0YlHB3dLdR37-Bo="},
        {"name": "Spring Rolls", "price": 50, "img": "https://wallpaperaccess.com/full/6905828.jpg"}
    ]
}
# ---------- Special Dishes ---------- 
special_dishes = {
    "Monday": "Poha with a twist of peanuts",
    "Tuesday": "Steamy Idli served with spicy chutney",
    "Wednesday": "Chole Bhature – the king of taste",
    "Thursday": "Maggi magic for your hunger",
    "Friday": "Crispy Dosa – south Indian delight",
    "Saturday": "Full Thali – feast like a king"
}


# ---------- Day Selection ----------
day = st.selectbox("📅 Select day of the week", list(weekly_menu.keys()))

# ---------- Show Menu ----------
st.markdown(f"## 🍴 Menu for {day}")
cols = st.columns(len(weekly_menu[day]))
quantities = {}
# ---------- Special Dish ---------- 
st.markdown(
    f"""
    <div class="food-card" style="background:#fff8e1; border-left:6px solid #ff9800; text-align:center;">
        <h3>🌟 Special Dish of the Day</h3>
        <p style="font-size:18px; color:#d84315;">{special_dishes[day]}</p>
    </div>
    """,
    unsafe_allow_html=True
)
for i, item in enumerate(weekly_menu[day]):
    with cols[i]:
        st.markdown(f"<div class='food-card'>", unsafe_allow_html=True)
        st.image(item["img"], use_container_width=True, caption=f"{item['name']} - ₹{item['price']}")
        qty = st.number_input(f"Qty {item['name']}", 0, 10, 0, key=item["name"])
        quantities[item["name"]] = qty
        st.markdown("</div>", unsafe_allow_html=True)



# ---------- Bill Calculation ----------
st.markdown("---")
st.markdown("## 🛒 Place Your Order")

with st.container():
    st.markdown("<div class='order-box'>", unsafe_allow_html=True)
    total = sum(item["price"] * quantities[item["name"]] for item in weekly_menu[day])

    for item in weekly_menu[day]:
        if quantities[item["name"]] > 0:
            st.write(f"➡️ {item['name']} x {quantities[item['name']]} = ₹{item['price']*quantities[item['name']]}")

    st.markdown(f"### 💰 Total Bill: **₹{total}**")

    if st.button("✅ Confirm Order"):
        if total > 0:
            st.success(f"🎉 Order placed successfully! Please pay ₹{total} at the counter.")
        else:
            st.warning("⚠️ Please select at least one item to order.")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("""
<hr>
<div style="text-align:center; font-size:18px; color:#1565c0;">
    ========================================  
    <br>Thank you for visiting our Canteen 🍴  
    <br>Come hungry, leave happy 😋  
    <br>========================================  
</div>
<hr>
""", unsafe_allow_html=True)

