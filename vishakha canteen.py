# canteen_streamlit.py
import streamlit as st

# Set page config
st.set_page_config(page_title="College Canteen", page_icon="🍴", layout="wide")

# Inject background image with CSS
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://i.ibb.co/zmrK1bq/food-bg.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}
[data-testid="stHeader"] {
    background: rgba(255,255,255,0.4);
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Menu items with image links
weekly_menu = {
    "Monday": {
        1: ("Poha", 20, "image/poha.jpge"),
        2: ("Tea", 10, "https://i.ibb.co/vDXQwMm/tea.jpg"),
        3: ("Samosa", 15, "https://i.ibb.co/NjktzNn/samosa.jpg"),
    },
    "Tuesday": {
        1: ("Idli", 30, "https://i.ibb.co/JB4cNps/idli.jpg"),
        2: ("Coffee", 15, "https://i.ibb.co/6R8S5q3/coffee.jpg"),
        3: ("Sandwich", 40, "https://i.ibb.co/M6gb4zX/sandwich.jpg"),
    },
    "Wednesday": {
        1: ("Paratha", 25, "https://i.ibb.co/BqfmjLr/paratha.jpg"),
        2: ("Lassi", 30, "https://i.ibb.co/TPN4n14/lassi.jpg"),
        3: ("Chole Bhature", 50, "https://i.ibb.co/FWk04tb/chole-bhature.jpg"),
    },
    "Thursday": {
        1: ("Maggi", 25, "https://i.ibb.co/S5fTGn7/maggi.jpg"),
        2: ("Tea", 10, "https://i.ibb.co/vDXQwMm/tea.jpg"),
        3: ("Pakora", 20, "https://i.ibb.co/W61VdFx/pakora.jpg"),
    },
    "Friday": {
        1: ("Dosa", 40, "https://i.ibb.co/RQtx2Dt/dosa.jpg"),
        2: ("Cold Drink", 20, "https://i.ibb.co/M8nxzvH/cold-drink.jpg"),
        3: ("Vada Pav", 15, "https://i.ibb.co/3BC7VrC/vada-pav.jpg"),
    },
    "Saturday": {
        1: ("Thali", 80, "https://i.ibb.co/T0c7ZTY/thali.jpg"),
        2: ("Roti Sabzi", 50, "https://i.ibb.co/YRrx0CJ/roti-sabzi.jpg"),
        3: ("Jalebi", 30, "https://i.ibb.co/sPwsxqJ/jalebi.jpg"),
    },
    "Sunday": {
        1: ("Chole Kulche", 60, "https://i.ibb.co/tM6t2n0/chole-kulche.jpg"),
        2: ("Ice Cream", 40, "https://i.ibb.co/fn9bcn0/icecream.jpg"),
        3: ("Pasta", 50, "https://i.ibb.co/Lgwt7h7/pasta.jpg"),
    },
}

# Special dish
special_dish = {
    "Monday": "Poha with a twist of peanuts",
    "Tuesday": "Steamy Idli served with spicy chutney",
    "Wednesday": "Chole Bhature – the king of taste",
    "Thursday": "Maggi magic for your hunger",
    "Friday": "Crispy Dosa – south Indian delight",
    "Saturday": "Full Thali – feast like a king",
    "Sunday": "Chole Kulche – perfect Sunday vibes",
}

# Title
st.title("🍽 Welcome to the College Canteen")
st.subheader("Good food = Good mood! Stay Happy 😄")
st.markdown("---")

# Day selection
day = st.selectbox("📅 Select day of the week", list(weekly_menu.keys()))

menu = weekly_menu[day]
st.write(f"## Menu for {day}")
st.markdown(f"🌟 *Special Dish:* **{special_dish[day]}**")
st.markdown("---")

# Show menu in columns with images
cols = st.columns(len(menu))
for idx, (key, value) in enumerate(menu.items()):
    item, price, img = value
    with cols[idx]:
        st.image(img, caption=item, use_column_width=True)
        st.markdown(f"💰 Rs.{price}")
        qty = st.number_input(
            f"Qty ({item})",
            min_value=0,
            step=1,
            key=f"qty_{day}_{key}",
        )
        if qty > 0:
            st.session_state.setdefault("order", {})
            st.session_state["order"][item] = (price, qty)

# Generate bill
if st.button("🧾 Generate Bill"):
    order = st.session_state.get("order", {})
    if order:
        st.markdown("## 🧾 Bill Receipt")
        total = 0
        for item, (price, qty) in order.items():
            cost = price * qty
            total += cost
            st.write(f"{item} x {qty} = Rs.{cost}")
        st.markdown(f"### ✅ Total Bill = Rs.{total}")
        st.success("Thank you for visiting our Canteen! Come hungry, leave happy 😋")
        st.session_state["order"] = {}  # reset after bill
    else:
        st.warning("⚠️ No items selected. Visit again when hungry!")
