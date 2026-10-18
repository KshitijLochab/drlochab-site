"""Diet charts and food diary: language-independent rules (19 Oct 2026). Texts are in diet_text_en.py and diet_text_hi.py.

Foods come from thali_foods.F (the Thali meter list). Each food is tagged here by its English name:
  group  G whole grain or millet · R refined grain or white rice · T potato or sweet potato · P dal, beans, besan · D milk and curd foods
         E egg · M chicken, fish or meat · V vegetable · F fruit · N nuts and seeds · O added fat · S fried or fast food · W sweet · K drink · X mixed dish · Y fibre supplement
  flags  f fried or very oily · s salty · u sugary · g gluten · q oats (gluten-free only if certified) · l milk sugar (lactose) · o high-FODMAP
         r common reflux trigger · x skins, seeds or raw (high residue) · k high potassium · c caffeine · p red meat
  fit    meal slots the food suits: e early morning · b breakfast · m lunch or dinner · s snack · n bedtime

Plans set daily targets (protein per kg, fibre, fat limit, vegetable and fruit servings, water glasses, limits on fried, sugary and salty items)
and food rules (good, limit, avoid). A rule entry is a food name, a flag ('@f') or a group ('#R'). Comorbidity rules work the same way.
All numbers are general guidance for adults; the pages say so and send people to their doctor for individual advice."""

TAGS = {
 # roti, rice and breakfast
 "Atta roti": "G|g|m", "Bajra or jowar roti": "G||m", "Plain paratha, with ghee or oil": "G|g|b", "Oats, made with water": "G|q|b",
 "Brown rice": "G||m", "White rice": "R||m", "Idli": "R||b", "Plain dosa": "R||b", "White bread": "R|g|b",
 "Brown or whole wheat bread": "G|g|b", "Puri": "R|fg|b", "Bhatura": "R|fg|m", "Aloo paratha": "G|g|b", "Poha": "R||bsn",
 "Upma": "R|g|b", "Besan chilla": "P||bs", "Veg pulao or jeera rice": "R||m", "Masala dosa": "R||b", "Khichdi": "X||mn",
 "Muesli or cornflakes, with milk": "R|lu|b", "Dalia (broken wheat), with vegetables": "G|g|bm", "Ragi (nachni) roti or porridge": "G||bm",
 "Quinoa, cooked": "G||m", "Pasta in red (tomato) sauce": "R|gr|m", "Pasta in white (cheese) sauce": "R|gl|m", "Veg sandwich, whole wheat bread": "G|g|bs",
 "Curd rice": "X||mn",
 # dal and beans
 "Dal, with tadka": "P||m", "Rajma or chole": "P|ox|m", "Roasted chana, with skin": "P|x|s", "Soya chunks curry": "P|o|m",
 "Sambar": "P||bm", "Kadhi": "X||m", "Sprouts (moong), as chaat or salad": "P|x|bs", "Moong dal chilla": "P||bs",
 # milk, curd and paneer
 "Milk (toned)": "D|lo|en", "Curd (dahi)": "D||m", "Chaas": "D||ms", "Paneer": "D||m", "Paneer sabzi (bhurji or matar paneer)": "D||m",
 "Raita": "D||m", "Hung curd or Greek yoghurt": "D||bs",
 # eggs, chicken, fish and meat
 "Egg, boiled": "E||bs", "Chicken curry": "M||m", "Fish curry": "M||m", "Omelette or egg bhurji": "E||b", "Egg curry": "E||m",
 "Tandoori or grilled chicken": "M||m", "Butter chicken": "M|sr|m", "Chicken biryani": "M||m", "Fish fry": "M|f|m", "Mutton curry": "M|p|m",
 "Chicken momos, steamed": "M|g|s", "Grilled or steamed fish": "M||m", "Grilled chicken or fish salad": "M|x|m", "Chicken soup, clear": "M||sn",
 # vegetables
 "Mixed sabzi": "V||m", "Aloo sabzi": "T|k|m", "Matar (green peas)": "V|o|m", "Bhindi": "V||m", "Palak or saag": "V|k|m", "Gobhi": "V|o|m",
 "Beans": "V||m", "Baingan": "V||m", "Patta gobhi (cabbage)": "V||m", "Lauki or tori": "V||m", "Gajar (carrot), raw": "V|x|s",
 "Shakarkandi (sweet potato), roasted": "T|k|s", "Bhutta (corn), roasted": "G|x|s", "Salad": "V|x|m", "Clear vegetable soup": "V||sn",
 # fruits, nuts and seeds
 "Guava": "F|x|s", "Pear": "F|o|s", "Apple, with peel": "F|o|s", "Anaar (pomegranate)": "F|x|s", "Banana": "F|k|sn", "Orange": "F|kr|s",
 "Papaya": "F||bs", "Almonds": "N|x|es", "Peanuts, roasted": "N|x|s", "Mango": "F|o|s", "Watermelon or melon": "F|o|s", "Grapes": "F||s",
 "Dates (khajoor)": "F|uko|s", "Kiwi": "F||s", "Prunes (dried plums)": "F|o|sn", "Walnuts": "N|x|es", "Makhana, roasted": "N||sn",
 "Isabgol (psyllium husk) in water": "Y||n",
 # drinks
 "Chai, with milk": "K|c|es", "Coffee with milk": "K|c|es", "Black tea, green tea or black coffee": "K|c|es", "Lassi, sweet or salted": "D||ms",
 "Milkshake (banana or mango)": "D|luo|s", "Nimbu paani or shikanji": "K|ur|s", "Coconut water": "K|k|s", "Fruit juice": "K|u|s",
 "Cold drink": "K|urc|s", "ORS": "K||s",
 # oil, snacks, fast food
 "Extra ghee, butter or oil": "O||", "Samosa": "S|fg|s", "Pakora": "S|f|s", "Namkeen or bhujia": "S|fs|s", "Chips": "S|fs|s",
 "Cream biscuits": "S|ug|s", "Kachori": "S|fg|s", "Medu vada": "S|f|bs", "Veg momos, steamed": "S|g|s", "Pav bhaji": "S|sgr|m",
 "Pizza": "S|sgr|m", "Instant noodles": "S|sg|m", "Rusk or plain biscuits": "R|g|es", "Burger (aloo tikki or chicken)": "S|fsg|m",
 "Pickle (achaar)": "O|s|m", "Papad": "S|s|m",
 # sweets
 "Jalebi": "W|ufg|s", "Gulab jamun": "W|uf|s", "Ladoo or barfi": "W|u|s", "Kheer or sevaiyan": "W|ul|s", "Ice cream": "W|ul|s", "Chocolate": "W|urc|s",
}

SLOTS = ["early", "bf", "mid", "lunch", "eve", "dinner", "bed"]
# hour each slot starts (device clock); used to pick the default slot and the rest of the day
SLOT_START = {"early": 4, "bf": 7.5, "mid": 10.5, "lunch": 12.5, "eve": 16, "dinner": 19, "bed": 21.5}
SLOT_FIT = {"early": "e", "bf": "b", "mid": "s", "lunch": "m", "eve": "s", "dinner": "m", "bed": "n"}

GOOD_BASE = ["Atta roti", "Bajra or jowar roti", "Ragi (nachni) roti or porridge", "Oats, made with water", "Dalia (broken wheat), with vegetables", "Brown rice",
             "Idli", "Dal, with tadka", "Sambar", "Moong dal chilla", "Besan chilla", "Sprouts (moong), as chaat or salad", "Rajma or chole", "Curd (dahi)", "Chaas",
             "Hung curd or Greek yoghurt", "Egg, boiled", "Grilled or steamed fish", "Tandoori or grilled chicken", "Mixed sabzi", "Palak or saag", "Beans", "Bhindi",
             "Salad", "Guava", "Papaya", "Orange", "Pear", "Apple, with peel", "Kiwi", "Almonds", "Walnuts", "Makhana, roasted", "Roasted chana, with skin", "Khichdi"]

# t: fib = fibre minimum (None = not a goal), prot = g per kg (low, high), fat = upper limit (g), veg = katoris (min), fruit = servings (min, max),
#    water = glasses (min, max) or None (as advised), fried / sugary / salty = most items a day, meals = slots to fill (small frequent meals), bed = bedtime snack advised
# extra = more counters shown for this plan: {flag: limit}
PLANS = [
 dict(key="gut", t=dict(fib=25, prot=(0.8, 1.0), fat=60, veg=3, fruit=(2, 4), water=(8, 10), fried=1, sugary=1, salty=1),
      good=GOOD_BASE, limit=["@f", "@u", "@s", "#S"], avoid=[]),
 dict(key="fatty-liver", t=dict(fib=30, prot=(1.0, 1.2), fat=50, veg=4, fruit=(2, 3), water=(8, 10), fried=1, sugary=0, salty=1),
      good=GOOD_BASE + ["Black tea, green tea or black coffee", "Coffee with milk", "Quinoa, cooked", "Grilled chicken or fish salad", "Clear vegetable soup"],
      limit=["#R", "@f", "@s", "@p", "#S", "#W", "Extra ghee, butter or oil", "Dates (khajoor)", "Plain paratha, with ghee or oil", "Aloo paratha"],
      avoid=["Cold drink", "Fruit juice", "Milkshake (banana or mango)", "Nimbu paani or shikanji", "@u"]),
 dict(key="acidity", t=dict(fib=25, prot=(0.8, 1.0), fat=50, veg=3, fruit=(1, 3), water=(8, 10), fried=1, sugary=1, salty=1), extra={"r": 1, "c": 2},
      good=["Oats, made with water", "Idli", "Dalia (broken wheat), with vegetables", "Brown rice", "Khichdi", "Curd rice", "Dal, with tadka", "Moong dal chilla",
            "Curd (dahi)", "Hung curd or Greek yoghurt", "Paneer", "Egg, boiled", "Grilled or steamed fish", "Tandoori or grilled chicken", "Lauki or tori", "Beans",
            "Mixed sabzi", "Banana", "Papaya", "Apple, with peel", "Pear", "Watermelon or melon", "Makhana, roasted", "Coconut water", "Atta roti", "Ragi (nachni) roti or porridge"],
      limit=["@f", "@r", "@c", "@u", "#S", "Extra ghee, butter or oil", "Mutton curry", "Paneer sabzi (bhurji or matar paneer)", "Plain paratha, with ghee or oil", "Aloo paratha"],
      avoid=[]),
 dict(key="ibs", t=dict(fib=25, prot=(0.8, 1.0), fat=60, veg=3, fruit=(1, 2), water=(8, 10), fried=1, sugary=1, salty=1), extra={"o": 1},
      good=["Oats, made with water", "White rice", "Brown rice", "Idli", "Plain dosa", "Ragi (nachni) roti or porridge", "Quinoa, cooked", "Poha", "Curd (dahi)",
            "Chaas", "Hung curd or Greek yoghurt", "Paneer", "Egg, boiled", "Grilled or steamed fish", "Tandoori or grilled chicken", "Moong dal chilla", "Lauki or tori",
            "Bhindi", "Beans", "Gajar (carrot), raw", "Palak or saag", "Papaya", "Kiwi", "Banana", "Orange", "Grapes", "Isabgol (psyllium husk) in water", "Walnuts",
            "Makhana, roasted", "Peanuts, roasted", "Baingan"],
      limit=["@o", "@f", "@c", "#S", "Cold drink", "Chocolate", "Rajma or chole", "Sprouts (moong), as chaat or salad"], avoid=[]),
 dict(key="constipation", t=dict(fib=30, prot=(0.8, 1.0), fat=60, veg=4, fruit=(2, 4), water=(10, 12), fried=1, sugary=1, salty=1),
      good=["Kiwi", "Prunes (dried plums)", "Guava", "Pear", "Papaya", "Isabgol (psyllium husk) in water", "Oats, made with water", "Dalia (broken wheat), with vegetables",
            "Bajra or jowar roti", "Ragi (nachni) roti or porridge", "Atta roti", "Brown rice", "Dal, with tadka", "Rajma or chole", "Sprouts (moong), as chaat or salad",
            "Palak or saag", "Mixed sabzi", "Salad", "Beans", "Bhindi", "Matar (green peas)", "Roasted chana, with skin", "Walnuts", "Almonds", "Curd (dahi)", "Chaas",
            "Apple, with peel", "Orange", "Moong dal chilla", "Besan chilla"],
      limit=["#R", "@f", "@u", "#S", "Cream biscuits", "Rusk or plain biscuits"], avoid=[]),
 dict(key="gallstones", t=dict(fib=25, prot=(0.8, 1.0), fat=50, veg=4, fruit=(2, 3), water=(8, 10), fried=0, sugary=1, salty=1, meals=4),
      good=["Oats, made with water", "Dalia (broken wheat), with vegetables", "Atta roti", "Bajra or jowar roti", "Brown rice", "Idli", "Dal, with tadka", "Sambar",
            "Sprouts (moong), as chaat or salad", "Moong dal chilla", "Curd (dahi)", "Chaas", "Hung curd or Greek yoghurt", "Grilled or steamed fish", "Tandoori or grilled chicken",
            "Chicken soup, clear", "Mixed sabzi", "Palak or saag", "Beans", "Lauki or tori", "Salad", "Clear vegetable soup", "Guava", "Papaya", "Apple, with peel", "Orange",
            "Pear", "Kiwi", "Khichdi", "Coffee with milk"],
      limit=["@f", "#O", "#S", "#W", "Paneer sabzi (bhurji or matar paneer)", "Butter chicken", "Mutton curry", "Pasta in white (cheese) sauce", "Plain paratha, with ghee or oil",
             "Aloo paratha", "Omelette or egg bhurji", "Egg curry", "Peanuts, roasted"], avoid=[]),
 dict(key="cirrhosis", t=dict(fib=25, prot=(1.2, 1.5), fat=60, veg=3, fruit=(2, 3), water=None, fried=1, sugary=1, salty=0, meals=5, bed=True),
      good=["Dal, with tadka", "Moong dal chilla", "Besan chilla", "Paneer", "Curd (dahi)", "Hung curd or Greek yoghurt", "Milk (toned)", "Egg, boiled", "Omelette or egg bhurji",
            "Grilled or steamed fish", "Fish curry", "Chicken curry", "Tandoori or grilled chicken", "Soya chunks curry", "Khichdi", "Poha", "Idli", "Atta roti", "Oats, made with water",
            "Dalia (broken wheat), with vegetables", "Curd rice", "Mixed sabzi", "Lauki or tori", "Beans", "Papaya", "Apple, with peel", "Guava", "Banana", "Pear", "Makhana, roasted"],
      limit=["@f", "@u", "@p", "#S"],
      avoid=["@s", "Pickle (achaar)", "Papad", "Namkeen or bhujia", "Chips", "Instant noodles"]),
 dict(key="jaundice", t=dict(fib=20, prot=(0.8, 1.0), fat=60, veg=3, fruit=(2, 3), water=(8, 12), fried=0, sugary=1, salty=1, meals=5),
      good=["Khichdi", "Curd rice", "Idli", "Poha", "Upma", "Dalia (broken wheat), with vegetables", "Atta roti", "White rice", "Dal, with tadka", "Moong dal chilla", "Curd (dahi)",
            "Chaas", "Paneer", "Egg, boiled", "Fish curry", "Chicken soup, clear", "Clear vegetable soup", "Lauki or tori", "Mixed sabzi", "Papaya", "Banana", "Orange",
            "Apple, with peel", "Coconut water", "Sambar", "Oats, made with water"],
      limit=["@f", "@s", "#S", "Mutton curry", "Butter chicken", "Extra ghee, butter or oil"], avoid=[]),
 dict(key="panc-acute", t=dict(fib=20, prot=(1.0, 1.2), fat=40, veg=3, fruit=(2, 3), water=(8, 10), fried=0, sugary=1, salty=1, meals=5),
      good=["Khichdi", "Idli", "Poha", "Oats, made with water", "Dalia (broken wheat), with vegetables", "White rice", "Curd rice", "Atta roti", "Dal, with tadka",
            "Moong dal chilla", "Curd (dahi)", "Chaas", "Hung curd or Greek yoghurt", "Egg, boiled", "Grilled or steamed fish", "Chicken soup, clear", "Tandoori or grilled chicken",
            "Clear vegetable soup", "Lauki or tori", "Mixed sabzi", "Beans", "Papaya", "Banana", "Apple, with peel", "Guava", "Coconut water", "Sambar"],
      limit=["#O", "#N", "#W", "Paneer", "Paneer sabzi (bhurji or matar paneer)", "Omelette or egg bhurji", "Egg curry", "Plain paratha, with ghee or oil", "Aloo paratha",
             "Milkshake (banana or mango)", "Mutton curry", "Chicken curry", "Chicken biryani", "Pasta in white (cheese) sauce", "@u", "Milk (toned)"],
      avoid=["@f", "#S", "Butter chicken"]),
 dict(key="panc-chronic", t=dict(fib=25, prot=(1.0, 1.2), fat=60, veg=3, fruit=(2, 3), water=(8, 10), fried=1, sugary=0, salty=1, meals=5),
      good=GOOD_BASE + ["Fish curry", "Chicken curry", "Paneer", "Omelette or egg bhurji", "Milk (toned)", "Curd rice", "Poha"],
      limit=["@f", "#S", "Extra ghee, butter or oil", "Isabgol (psyllium husk) in water"], avoid=["@u"]),
 dict(key="ibd-flare", t=dict(fib=None, prot=(1.2, 1.5), fat=60, veg=2, fruit=(1, 2), water=(8, 12), fried=0, sugary=1, salty=1, meals=5), extra={"x": 0},
      good=["Khichdi", "Curd rice", "Idli", "Plain dosa", "Poha", "Upma", "White rice", "Oats, made with water", "Dal, with tadka", "Moong dal chilla", "Curd (dahi)",
            "Hung curd or Greek yoghurt", "Chaas", "Paneer", "Egg, boiled", "Omelette or egg bhurji", "Grilled or steamed fish", "Fish curry", "Chicken soup, clear",
            "Tandoori or grilled chicken", "Lauki or tori", "Clear vegetable soup", "Papaya", "Banana", "Coconut water", "ORS", "Atta roti"],
      limit=["@f", "@c", "@r", "@l", "#S", "@o"],
      avoid=["@x", "Rajma or chole", "Roasted chana, with skin", "Sprouts (moong), as chaat or salad", "Salad", "Gajar (carrot), raw", "Bhutta (corn), roasted"]),
 dict(key="ibd-remission", t=dict(fib=25, prot=(1.0, 1.2), fat=60, veg=4, fruit=(2, 3), water=(8, 10), fried=1, sugary=1, salty=1),
      good=GOOD_BASE + ["Fish curry", "Grilled chicken or fish salad", "Quinoa, cooked"],
      limit=["@p", "@f", "@u", "#S", "#W"], avoid=[]),
 # Crohn's disease with a narrowing: low residue for as long as the stricture is present, even when the disease is quiet
 dict(key="ibd-stricture", why="stuck", t=dict(fib=None, prot=(1.0, 1.2), fat=60, veg=2, fruit=(1, 2), water=(8, 10), fried=1, sugary=1, salty=1, meals=5), extra={"x": 0},
      good=["Khichdi", "Curd rice", "Idli", "Plain dosa", "Poha", "Upma", "White rice", "Atta roti", "Oats, made with water", "Dal, with tadka", "Moong dal chilla",
            "Besan chilla", "Curd (dahi)", "Hung curd or Greek yoghurt", "Chaas", "Paneer", "Milk (toned)", "Egg, boiled", "Omelette or egg bhurji", "Grilled or steamed fish",
            "Fish curry", "Chicken soup, clear", "Chicken curry", "Lauki or tori", "Clear vegetable soup", "Papaya", "Banana", "Coconut water"],
      limit=["@f", "@r", "#S", "Matar (green peas)", "Beans", "Patta gobhi (cabbage)", "Palak or saag", "Bhindi", "Gobhi", "Mutton curry", "Brown rice",
             "Tandoori or grilled chicken", "Mixed sabzi", "Grapes", "Mango"],
      avoid=["@x", "Rajma or chole", "Roasted chana, with skin", "Sprouts (moong), as chaat or salad", "Salad", "Gajar (carrot), raw", "Bhutta (corn), roasted",
             "Isabgol (psyllium husk) in water", "Orange", "Apple, with peel", "Pear", "Dates (khajoor)", "Prunes (dried plums)", "Grilled chicken or fish salad"]),
 dict(key="celiac", t=dict(fib=25, prot=(0.8, 1.0), fat=60, veg=3, fruit=(2, 3), water=(8, 10), fried=1, sugary=1, salty=1), extra={"g": 0},
      good=["White rice", "Brown rice", "Bajra or jowar roti", "Ragi (nachni) roti or porridge", "Quinoa, cooked", "Idli", "Plain dosa", "Poha", "Khichdi", "Curd rice",
            "Besan chilla", "Moong dal chilla", "Dal, with tadka", "Rajma or chole", "Sambar", "Sprouts (moong), as chaat or salad", "Curd (dahi)", "Paneer", "Egg, boiled",
            "Grilled or steamed fish", "Tandoori or grilled chicken", "Mixed sabzi", "Palak or saag", "Salad", "Guava", "Papaya", "Banana", "Orange", "Almonds",
            "Makhana, roasted", "Roasted chana, with skin", "Shakarkandi (sweet potato), roasted"],
      limit=["@q", "@f", "@u", "Namkeen or bhujia", "Papad", "Kadhi", "Sambar"], avoid=["@g"]),
 dict(key="diarrhoea", t=dict(fib=None, prot=(0.8, 1.0), fat=40, veg=1, fruit=(1, 2), water=(10, 14), fried=0, sugary=0, salty=1),
      good=["ORS", "Coconut water", "Khichdi", "Curd rice", "Idli", "Banana", "Curd (dahi)", "Chaas", "Poha", "Clear vegetable soup", "Chicken soup, clear", "White rice",
            "Dal, with tadka", "White bread", "Rusk or plain biscuits", "Papaya", "Aloo sabzi"],
      limit=["Milk (toned)", "Milkshake (banana or mango)", "@c", "@x", "@o", "@r", "Extra ghee, butter or oil", "#N", "Isabgol (psyllium husk) in water"],
      avoid=["@f", "@u", "#S", "#W"]),
]

# conditions people often have alongside; same rule format, plus how they change the targets
CO = {
 "diabetes": dict(avoid=["@u"], limit=["#R", "#T", "Mango", "Grapes", "Banana", "Coconut water"], fruit_max=3),
 "bp": dict(avoid=["@s"], limit=["@f", "@p", "#O", "Pickle (achaar)"]),
 "kidney": dict(avoid=["@s"], limit=["@k", "Soya chunks curry"], prot_doc=True),
 "preg": dict(limit=["@c"], prot_add=10),
 "lactose": dict(limit=["@l"]),
 "old": dict(prot=(1.0, 1.2)),
}

# one or more diary plans per chart page
PAGES = [
 ("gut-healthy-diet", ["gut"], None),
 ("fatty-liver", ["fatty-liver"], "fatty-liver"),
 ("acidity-gastritis", ["acidity"], "acidity-reflux-gerd"),
 ("ibs-bloating", ["ibs"], "ibs-irritable-bowel-syndrome"),
 ("constipation", ["constipation"], "constipation"),
 ("gallstones", ["gallstones"], "gallstones"),
 ("cirrhosis", ["cirrhosis"], "cirrhosis"),
 ("jaundice-hepatitis", ["jaundice"], "jaundice"),
 ("pancreatitis", ["panc-acute", "panc-chronic"], "pancreatitis"),
 ("ulcerative-colitis-crohns", ["ibd-flare", "ibd-remission", "ibd-stricture"], "ulcerative-colitis-crohns-disease"),
 ("celiac-gluten-free", ["celiac"], None),
 ("loose-motions", ["diarrhoea"], None),
]

def check(food_names):
    """Every food has tags, and every rule names a real food or a known flag or group."""
    missing = [n for n in food_names if n not in TAGS]
    extra = [n for n in TAGS if n not in food_names]
    assert not missing and not extra, (missing, extra)
    flags, groups = set("fsugqlorxkcp"), set("GRTPDEMVFNOSWKXY")
    def ok(r):
        return (r[0] == "@" and r[1] in flags) or (r[0] == "#" and r[1] in groups) or r in TAGS
    for p in PLANS:
        for k in ("good", "limit", "avoid"):
            bad = [r for r in p[k] if not ok(r)]
            assert not bad, (p["key"], k, bad)
    for k, c in CO.items():
        for kk in ("limit", "avoid"):
            assert all(ok(r) for r in c.get(kk, [])), (k, kk)
    keys = [p["key"] for p in PLANS]
    assert sorted(sum((pp for _, pp, _ in PAGES), [])) == sorted(keys)
