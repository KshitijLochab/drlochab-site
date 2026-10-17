"""Reference record for the Thali meter (reviewed 17 Oct 2026): every food with its serving, grams of fibre, protein and fat, and how each was worked out. js("en") or js("hi") prints the FOODS array for the page; keep lochab-gastro.html and hindi.py in step with this file."""
# Reviewed thali meter data. Each row: cat, EN name, EN serving, HI name, HI serving, fibre, protein, fat (g per serving), basis
F=[
("g","Atta roti","1 medium roti","आटे की रोटी","1 मीडियम रोटी",3,3,0.5,"~30 g whole-wheat atta: IFCT TDF 11.4, protein 10.6, fat 1.5 /100 g; no ghee"),
("g","Bajra or jowar roti","1 roti","बाजरा या ज्वार की रोटी","1 रोटी",3.5,3.5,1.5,"~35 g flour: IFCT bajra TDF 11.5 P 11 F 5.4; jowar TDF 10.2 P 10 F 1.7"),
("g","Plain paratha, with ghee or oil","1 paratha","सादा पराठा, घी या तेल वाला","1 पराठा",3.5,4,8,"~35 g atta + ~1.5 tsp fat"),
("g","Oats, made with water","1 bowl","ओट्स, पानी में बने","1 बाउल",4,5,2.5,"40 g dry oats: USDA fibre 10.1 P 13.2 F 6.5 /100 g"),
("g","Brown rice","1 katori","ब्राउन राइस","1 कटोरी",2.5,4,1.5,"150 g cooked: USDA fibre 1.8 P 2.6 F 0.9"),
("g","White rice","1 katori","सफ़ेद चावल","1 कटोरी",0.5,4,0.5,"150 g cooked: USDA fibre 0.4 P 2.7 F 0.3"),
("g","Idli","2 idlis","इडली","2 इडली",1.5,4,0.5,"2 x ~40 g"),
("g","Plain dosa","1 dosa","सादा डोसा","1 डोसा",1,3,4,"~80 g batter + ~1 tsp oil"),
("g","White bread","2 slices","सफ़ेद ब्रेड","2 स्लाइस",1.5,4.5,1.5,"50 g: USDA fibre 2.7 P 9 F 3.3"),
("g","Brown or whole wheat bread","2 slices","ब्राउन या होल व्हीट ब्रेड","2 स्लाइस",3,6,2,"50 g; Indian brown breads vary, many 4-6 g fibre/100 g"),
("d","Dal, with tadka","1 katori","दाल, तड़के वाली","1 कटोरी",3,7,3,"~30 g raw dal: IFCT P 21-24 TDF 9-11 /100 g + ~1/2 tsp oil"),
("d","Rajma or chole","1 katori","राजमा या छोले","1 कटोरी",7,9,6,"~100 g cooked beans: USDA chickpeas fibre 7.6 P 8.9 F 2.6; rajma fibre 6.4 P 8.7 F 0.5 + ~1 tsp oil"),
("d","Roasted chana, with skin","1 handful","भुने चने, छिलके वाले","1 मुट्ठी",4,6,1.5,"30 g"),
("d","Soya chunks curry","1 katori","सोया चंक्स की सब्ज़ी","1 कटोरी",3,13,5,"25 g dry chunks: P 52 fibre ~13 F 0.5 /100 g + ~1 tsp oil"),
("m","Milk (toned)","1 glass","दूध (टोंड)","1 गिलास",0,6.5,6,"200 ml, 3% fat, 3.2 g protein /100 ml"),
("m","Curd (dahi)","1 katori","दही","1 कटोरी",0,4.5,4.5,"150 g, toned milk curd"),
("m","Chaas","1 glass","छाछ","1 गिलास",0,2,1,"200 ml, diluted"),
("m","Paneer","50 g, about 5 cubes","पनीर","50 ग्राम, लगभग 5 टुकड़े",0,9,10,"IFCT paneer P 18.3 F 20.8 /100 g"),
("m","Egg, boiled","1 egg","अंडा, उबला","1 अंडा",0,6,5,"50 g edible"),
("m","Chicken curry","1 katori, about 100 g meat","चिकन करी","1 कटोरी, लगभग 100 ग्राम मीट",0,25,12,"cooked skinless mixed meat P ~27 F ~7 /100 g + ~1 tsp oil"),
("m","Fish curry","1 katori, about 100 g fish","मछली करी","1 कटोरी, लगभग 100 ग्राम मछली",0,20,7,"rohu-type fish cooked P ~20 F ~2 + ~1 tsp oil"),
("v","Mixed sabzi","1 katori","मिक्स सब्ज़ी","1 कटोरी",3,2,5,"~120 g + ~1 tsp oil"),
("v","Aloo sabzi","1 katori","आलू की सब्ज़ी","1 कटोरी",2.5,2.5,5,"150 g potato: USDA fibre 1.8 P 1.7 + ~1 tsp oil"),
("v","Matar (green peas)","1 katori","मटर","1 कटोरी",5,5,5,"100 g: USDA fibre 5.5 P 5.4 + ~1 tsp oil"),
("v","Bhindi","1 katori","भिंडी","1 कटोरी",2.5,2,6,"100 g: USDA fibre 2.5 P 1.9 + ~1 1/4 tsp oil"),
("v","Palak or saag","1 katori","पालक या साग","1 कटोरी",3.5,4,5,"150 g: USDA spinach cooked fibre 2.4 P 3.0 + ~1 tsp oil"),
("v","Gobhi","1 katori","गोभी","1 कटोरी",2.5,2,5,"120 g: USDA fibre 2.3 P 1.8 + ~1 tsp oil"),
("v","Beans","1 katori","बीन्स","1 कटोरी",3,2,5,"100 g: USDA fibre 3.2 P 1.9 + ~1 tsp oil"),
("v","Baingan","1 katori","बैंगन","1 कटोरी",2.5,1,6,"100 g: USDA fibre 2.5 P 0.8 + oil"),
("v","Patta gobhi (cabbage)","1 katori","पत्ता गोभी","1 कटोरी",2,1.5,5,"100 g: USDA fibre 1.9 P 1.3 + ~1 tsp oil"),
("v","Lauki or tori","1 katori","लौकी या तोरी","1 कटोरी",1,1,4,"150 g: fibre 0.5-1.1 P 0.6 + oil"),
("v","Gajar (carrot), raw","1 medium","गाजर, कच्ची","1 मीडियम",2,0.5,0,"60 g: USDA fibre 2.8 P 0.9 /100 g"),
("v","Shakarkandi (sweet potato), roasted","1 medium","शकरकंदी, भुनी","1 मीडियम",4,2.5,0,"130 g: USDA baked fibre 3.3 P 2.0"),
("v","Bhutta (corn), roasted","1 cob","भुट्टा, भुना","1 भुट्टा",2.5,3,1.5,"~90 g kernels: USDA fibre 2.4 P 3.4 F 1.5"),
("v","Salad","1 plate","सलाद","1 प्लेट",2,1,0,"~150 g cucumber, tomato, onion, carrot"),
("f","Guava","1 fruit","अमरूद","1 फल",5,2.5,1,"100 g: USDA fibre 5.4 P 2.6 F 1.0"),
("f","Pear","1 fruit","नाशपाती","1 फल",5.5,0.5,0,"178 g: USDA fibre 3.1/100 g"),
("f","Apple, with peel","1 fruit","सेब, छिलके समेत","1 फल",4,0.5,0,"~170 g: USDA fibre 2.4"),
("f","Anaar (pomegranate)","1 katori seeds","अनार","1 कटोरी दाने",3.5,1.5,1,"~90 g arils: USDA fibre 4.0 P 1.7 F 1.2"),
("f","Banana","1 fruit","केला","1 फल",3,1.5,0.5,"~115 g: USDA fibre 2.6 P 1.1"),
("f","Orange","1 fruit","संतरा","1 फल",3,1,0,"~130 g: USDA fibre 2.4 P 0.9"),
("f","Papaya","1 bowl","पपीता","1 बाउल",2.5,0.5,0.5,"145 g: USDA fibre 1.7 P 0.5"),
("f","Almonds","1 handful, about 20","बादाम","1 मुट्ठी, लगभग 20",3,5,12,"24 g: USDA fibre 12.5 P 21 F 50"),
("f","Peanuts, roasted","1 handful","मूँगफली, भुनी","1 मुट्ठी",2.5,7,15,"30 g: USDA fibre 8.4 P 24 F 50"),
("o","Extra ghee, butter or oil","1 teaspoon","ऊपर से घी, मक्खन या तेल","1 छोटा चम्मच",0,0,5,"5 g"),
("o","Samosa","1 samosa","समोसा","1 समोसा",2,4,15,"~70 g deep fried"),
("o","Pakora","1 plate, about 6","पकौड़े","1 प्लेट, लगभग 6",3,5,15,"~100 g besan fritters, deep fried"),
("o","Namkeen or bhujia","1 small bowl","नमकीन या भुजिया","1 छोटी कटोरी",1.5,4,10,"30 g: fat ~33%"),
("o","Chips","1 small packet","चिप्स","1 छोटा पैकेट",1,1.5,9,"~26 g: USDA fat 34 P 6.6 fibre 3.1 /100 g"),
("o","Cream biscuits","4 biscuits","क्रीम बिस्कुट","4 बिस्कुट",0.5,2,8,"~40 g: fat ~20%"),
]
def js(lang):
    out=[]
    for c,en,es,hi,hs,f,p,t,_ in F:
        n,s=(en,es) if lang=="en" else (hi,hs)
        out.append(f'{{c:"{c}",n:"{n}",s:"{s}",f:{f:g},p:{p:g},t:{t:g}}}')
    rows=[]; line=[]
    for o in out:
        line.append(o)
        if len(line)==3: rows.append(",".join(line)); line=[]
    if line: rows.append(",".join(line))
    return "const FOODS=[\n "+",\n ".join(rows)+"\n];"
