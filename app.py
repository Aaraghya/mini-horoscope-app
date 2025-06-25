import streamlit as st
import random

st.set_page_config(page_title="✨Horoscope App", page_icon="🔮")

if "show_result" not in st.session_state:
    st.session_state.show_result = False

def go_to_result():
    st.session_state.show_result = True
def get_zodiac(month, day):
    signs = [
        ("Capricorn", (1, 19)), ("Aquarius", (2, 18)), ("Pisces", (3, 20)),
        ("Aries", (4, 19)), ("Taurus", (5, 20)), ("Gemini", (6, 20)),
        ("Cancer", (7, 22)), ("Leo", (8, 22)), ("Virgo", (9, 22)),
        ("Libra", (10, 22)), ("Scorpio", (11, 21)), ("Sagittarius", (12, 21)),
        ("Capricorn", (12, 31))
    ]
    for sign, (m, d) in signs:
        if (month < m) or (month == m and day <= d):
            return sign
    return "Capricorn"


horoscope_db = {
    "Aries": ["You're bold and unstoppable today!💌", 
              "Chase your dreams like a rocket!🚀", 
              "Be the spark in someone's day!🌟",
              "You were born to lead, not follow. Blaze your own trail, Aries.🧚🏻‍♀️",
              "Your fire isnt meant to be tamed, is meant to light up the world!🌍"],
    "Taurus": ["You're calm, strong, and powerful.💪🏻", 
               "Patience is your secret superpower.🧘🏻‍♀️",
                 "Luxury is your love language ✨", 
                 "🍓 You're a soft soul with a tough shell 🍓"],
    "Gemini": ["Change is your superpower. Keep dancing with the wind! 💃",
               "Talk your dreams into reality, Gemini. Your words are magic! 🗣️",
               "You're not two-faced — you're multi-talented! 🎭",
               "Stay curious, stay wild, the world is your playground! 🌍🧸",
               "Your mind is a galaxy of ideas — let them sparkle! ✨"
               ],
    "Cancer": ["Your heart is your greatest strength 💖🌙 trust it always",
               "You're soft like the moonlight but strong like the tide 🌊",
               "You protect others so well — don't forget to protect yourself too 🛡️",
               "You bring comfort just by being you 🏡✨",
               "Your emotions are not a weakness, they're your magic 💫💞"],
    "Leo": ["You were born to shine, don't hold back your sparkle 🌟🦁",
        "Your confidence is contagious — keep spreading it 🔥💛",
        "Lead with your heart, and the world will follow 💖👑",
        "You light up every room you walk into ☀️🚪",
        "Roar louder, dream bigger, love brighter 🦁💫🌈"],
    "Virgo":  ["Your kindness is in the details — and that's your power 🧹🌿✨",
          "You bring calm to chaos like magic 🧘‍♀️🌾💫",
          "You're not overthinking — you're just deeply caring 💭💖",
          "Little by little, you build greatness 🧱🌟",
          "Your quiet strength moves mountains 🏔️🍃"],
    "Libra":  ["Your sense of harmony brings peace to the world ⚖️🌸",
          "Balance is beautiful — and so are you 💗🕊️",
          "You make life feel like poetry 📖🌷",
          "Kindness is your aesthetic 💞✨",
          "Your love for fairness makes everything brighter 💫🌈"],
    "Scorpio": ["You're powerful even in silence 🦂🌑✨",
            "Your depth is your magic — don't hide it 🌊💜",
            "Feel it all, then rise stronger 🔥🌹",
            "Mysterious, loyal, and fierce — that's your vibe 🖤🌌",
            "Your emotions are deep oceans, and you're the captain 🚢💧"],
    "Sagittarius": ["Your spirit was made to wander and wonder 🌍🏹",
                "Adventure is your middle name 🏞️🔥",
                "Keep chasing the sun — your soul needs the sky ☀️🕊️",
                "You spread joy like confetti 🎉💛",
                "You're a free soul with wild dreams 🌟🌻"],

    "Capricorn": ["You climb steady and shine quietly 🏔️✨",
              "Discipline is your magic power 🧠💼",
              "You turn dreams into goals and goals into wins 🏆📈",
              "You're the calm in the storm and the rock in the rush 🪨🌪️",
              "Slow and steady doesn't mean boring — it means unstoppable 🐢💪"],

    "Aquarius": ["You think differently — and that's your genius 💡🌌",
             "Your weird is your wonderful 🛸💙",
             "You bring fresh air to stale places 💨✨",
             "Change flows through you like electricity ⚡🔮",
             "Dream big, rebel louder, love smarter 🧠💫"],

    "Pisces": ["You dream in colors others can't even imagine 🎨🐠",
           "Your heart is an ocean of empathy 💖🌊",
           "You feel deeply — and that's your superpower 🦋💞",
           "You see the world with a soft soul and starry eyes ✨👁️",
           "Magic follows you wherever you go 🌈🐚"]
}


st.markdown("""
    <style>
    body, [data-testid="stAppViewContainer"] {
        background-color: var(--background-color);
        color: var(--text-color);
    }

    .big-font {
        font-size:30px !important;
        color: var(--text-color);
    }

    .cute-box {
        background-color: var(--box-bg);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px var(--box-shadow);
        margin-top: 20px;
        color: var(--box-text);
    }

    /* Light mode variables */
    @media (prefers-color-scheme: light) {
        :root {
            --background-color: #e6e6fa;
            --text-color: #ff66cc;
            --box-bg: #fff0f5;
            --box-shadow: #ffcce6;
            --box-text: #000000;
        }
    }

    /* Dark mode variables */
    @media (prefers-color-scheme: dark) {
        :root {
            --background-color: #121212;
            --text-color: #ff99cc;
            --box-bg: #1e1e1e;
            --box-shadow: #ff99cc;
            --box-text: #ffffff;
        }
    }
    </style>
""", unsafe_allow_html=True)


if not st.session_state.show_result:
    st.markdown('<p class="big-font">🌸 Welcome to Your Everyday Horoscope 🌸</p>', unsafe_allow_html=True)
    st.write("Enter your birthday to get your sign and a cute message! 💖")

    # Use only month and day
    month = st.selectbox("🌙 Select Month", [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ])
    day = st.number_input("🌼 Enter Day", min_value=1, max_value=31)

    if st.button("Show Horoscope 💌"):
        month_number = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ].index(month) + 1
        st.session_state.zodiac = get_zodiac(month_number, day)
        st.session_state.show_result = True
        st.rerun()


else:
    st.markdown('<p class="big-font">🔮 Your Horoscope: </p>', unsafe_allow_html=True)
    zodiac = st.session_state.zodiac
    st.subheader(f"Your Sign: **{zodiac}**")

    message = random.choice(horoscope_db.get(zodiac, ["You're magical just as you are! 🌈"]))
    st.markdown(f'<div class="cute-box">💌 {message}</div>', unsafe_allow_html=True)

    if st.button("🔁 Start Over"):
        st.session_state.show_result = False
        st.rerun()
