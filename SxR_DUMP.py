# Important note : Among all my projects, this one has taken the most time and effort to complete. I can confidently say that very few — if any — would invest this much dedication into creating a project. It has been crafted with precision, so if you choose to use it in your own way, please make sure to give proper credit.
# Important note2 : This project was created on February 23, 2024. While everything still works properly, the method may need to be updated to match Facebook’s current algorithm and security standards. Apart from the method, all other parts function correctly. The existing method can still work, but it requires a strong access token for effective use.
"""
Project: Facebook Ida Bumper
Author: Masudur Rahman Sifat (Mr.SxR)
Date Published: 20 May 2025 | Last Modified: 23 Feb 2024
"""
#▬▭▬▭▬▭▬▭[ IMPORT MODULE ]▬▭▬▭▬▭▬▭#
import os,re,random,uuid,time,json,sys
try:import requests
except:os.system("pip install requests")
try:from bs4 import BeautifulSoup as bs
except:os.system("pip install bs4")
from concurrent.futures import ThreadPoolExecutor as threadpol
#▬▭▬▭▬▭▬▭[ COLLOR VARIABLES ]▬▭▬▭▬▭▬▭#
a = "\033[1;97m";b = "\033[1;92m";c = "\033[1;91m";d = "\033[1;32m";e = "\033[1;37m";f = "\033[1;96m";g = "\033[1;93m";h = "\033[1;94m";i = "\033[1;95m";j = "\x1b[38;5;208m"
#▬▭▬▭▬▭▬▭[ OPTION VARIABLES ]▬▭▬▭▬▭▬▭#
l1 = f"{b}[{c}1{b}]";l2 = f"{b}[{c}2{b}]";l3 = f"{b}[{c}3{b}]";l4 = f"{b}[{c}4{b}]";l5 = f"{b}[{c}5{b}]";l6 = f"{b}[{c}6{b}]";l7 = f"{b}[{c}7{b}]";l8 = f"{b}[{c}8{b}]";l0 = f"{b}[{c}0{b}]";ekl = f"{f}:{a}"
colors = ["\033[0;31m", "\033[1;31m", "\033[0;32m", "\033[1;32m","\033[0;92m","\033[1;92m","\033[1;93m","\033[1;94m","\033[1;95m","\033[1;96m","\033[0;33m", "\033[1;33m", "\033[0;34m", "\033[1;34m", "\033[0;35m", "\033[1;35m", "\033[0;36m", "\033[1;36m", "\033[0;37m", "\033[1;37m", "\033[1;90m", "\033[0;91m","\033[1;91m", "\033[0;92m", "\033[1;93m", "\033[0;94m", "\033[1;94m", "\033[0;95m","\033[1;95m", "\033[0;96m", "\033[1;96m", "\033[0;97m"]
#▬▭▬▭▬▭▬▭[ LINE ]▬▭▬▭▬▭▬▭#
sxrline = f"{f}•━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━•"
#▬▭▬▭▬▭▬▭[ WP GROUP ]▬▭▬▭▬▭▬▭#
os.system("xdg-open https://chat.whatsapp.com/F2RbcimhWQF1v5nnPZHHr2")
#▬▭▬▭▬▭▬▭[ CHECK SDCARD ]▬▭▬▭▬▭▬▭#
try:open("/sdcard/.txt","a").write("")
except PermissionError:os.system("clear");print(f"{b}Please give sdcard permission to save Accounts{a}");os.system("termux-setup-storage")
#▬▭▬▭▬▭▬▭[ APPEND ]▬▭▬▭▬▭▬▭#
id_alx,sprt,extrt = [],[],[]
#▬▭▬▭▬▭▬▭[ UA+INFO ]▬▭▬▭▬▭▬▭#
sm_hni = str(random.randint(20000, 40000))
bnd_wh = str(random.randint(20000000, 30000000))
trc_id = str(uuid.uuid4())
def uaua():
    fbop = random.choice(("1","19","20"))
    archite = random.choice(("arm64-v8a:null","arm64-v8a:","armeabi-v7a:armeabi","arm64-v8a:armeabi-v7a:armeabi","x86:armeabi-v7a","x86_64:armeabi-v7a","x86:arm64-v8a:armeabi-v7a","x86_64:arm64-v8a:armeabi-v7a","x86_64:x86:armeabi-v7a","x86_64:x86:arm64-v8a"))
    build = random.choice(("SP1A.", "TP2A.", "TP1A.", "RKQ1.", "RP1A.", "TQ3A.", "TD2A.", "TD4A.", "SP2A.", "SD2A.", "SQ3A.", "RD2A.", "RQ3A.", "QD4A.", "QQ3A.", "QP1A.", "PQ3B.", "PD2A.", "PPR2.", "PPR1.", "OPM8.", "OPR6."))
    numberr = str(random.randint(7, 24)).zfill(2)+str(random.randint(1, 12)).zfill(2)+str(random.randint(1, 28)).zfill(2)+"."+str(random.randint(1, 70)).zfill(3)
    density = random.choice(("1.0", "1.25",  "1.2506", "1.278", "1.5", "1.625", "1.75", "1.8", "1.875", "2.0", "2.125", "2.2", "2.25", "2.375", "2.5", "2.75", "2.8", "2.9", "2.29375", "3.0", "3.25", "3.5", "3.75", "3.8", "4.0"));width = random.randint(420,1440);height = random.randint(720,2560)
    fbdm = f"{{density={density},width={width},height={height}}}"
    #https://androidapksfree.com/facebook/com-facebook-katana/old/ #4 otc 2024 to 2004
    fbsv = str(random.randint(8,15))+"."+str(random.randint(5,9))+"."+str(random.randint(0,5))
    if 12 <= int(fbsv.split(".")[0]) <= 15:fbav_bv = [("485.0.0.0.51", "456005032"),("484.0.0.0.50", "455803383"),("482.0.0.51.80", "455415830"),("482.0.0.0.81", "455409026"),("480.0.0.55.88", "455016452"),("480.0.0.0.67", "455007274"),("480.0.0.0.51", "455005459"),("478.0.0.41.86", "454614319"),("477.0.0.56.80", "454415688"),("476.0.0.49.74", "454214857"),("475.0.0.40.82", "454014379"),("474.0.0.52.74", "453811755"),("474.0.0.44.74", "453810718"),("474.0.0.0.48", "453802389"),("472.0.0.45.79", "453410037"),("472.0.0.0.49", "453403994"),("471.0.0.0.2", "453200356"),("467.1.0.52.83", "452416153"),("467.0.0.46.83", "452415324"),("466.0.0.55.85", "452214655"),("465.0.0.60.83", "452016700"),("465.0.0.0.6", "452000754"),("464.0.0.0.55", "451805674"),("463.0.0.0.50", "451606073"),("461.0.0.0.73", "451208771"),("460.0.0.0.52", "451006355"),("458.0.0.38.86", "450614458"),("455.0.0.0.35", "450004028"),("454.0.0.0.77", "449808468"),("450.0.0.42.110", "449017334"),("445.0.0.34.118", "448014984"),("443.0.0.23.229", "447626277"),("427.0.0.31.63", "444411021"),("426.0.0.26.50", "444209262"),("420.0.0.32.61", "443010639"),("419.0.0.37.71", "442812559"),("419.0.0.29.71", "442811621"),("418.0.0.33.69", "442611883"),("417.0.0.33.65", "442410873"),("416.0.0.35.85", "442213661"),("415.0.0.34.107", "442016421"),("414.0.0.30.113", "441815108"),("413.0.0.30.104", "441615153"),("412.0.0.22.115", "441416105"),("411.1.0.29.112", "441216522"),("410.0.0.26.115", "441017073"),("409.0.0.27.106", "440813707"),("408.1.0.36.103", "440614097"),("407.0.0.30.97", "440412261"),("406.0.0.26.90", "440212037"),("405.1.0.28.72", "440003403"),("405.0.0.23.72", "440002512"),("404.0.0.35.70", "421812321"),("403.0.0.27.81", "421611052"),("402.0.0.21.84", "421409151"),("401.0.0.24.77", "421209723"),("400.0.0.37.76", "421011115"),("399.0.0.24.93", "420811604"),("398.0.0.21.105", "420612354"),("397.0.0.23.404", "420441389"),("396.1.0.28.104", "319214969"),("396.0.0.21.104", "319214045"),("395.0.0.27.214", "319025405"),("394.1.0.51.107", "318819992"),("394.0.0.50.107", "318819784"),("392.2.0.33.108", "318413506"),("392.0.0.32.108", "318413147"),("391.1.0.37.104", "318217130"),("391.0.0.33.104", "318216484"),("390.0.0.27.105", "318014885"),("389.0.0.42.111", "317817218"),("388.0.0.32.105", "317616396"),("387.0.0.24.102", "317416518"),("386.0.0.35.108", "317217654"),("385.0.0.32.114", "317016274"),("384.1.0.29.111", "316818200"),("383.0.0.23.106", "316614371"),("382.0.0.33.111", "316416485"),("381.0.0.29.105", "316215288"),("380.0.0.29.109", "316015926"),("379.0.0.24.109", "315814638"),("378.0.0.18.112", "315613980"),("377.0.0.22.107", "315414711"),("376.0.0.12.108", "315213325"),("375.1.0.28.111", "315015375"),("375.0.0.26.111", "315015017"),("374.0.0.20.109", "314813437"),("373.0.0.31.112", "314614855"),("372.1.0.23.107", "314414840"),("371.0.0.24.109", "314214459"),("370.0.0.23.112", "314014367"),("369.0.0.18.103", "313811870"),("368.0.0.24.108", "313613498"),("367.2.0.26.107", "313413508")]
    else:fbav_bv = [("305.1.0.40.120", "272401224"),("305.0.0.40.120", "272369098"),("304.0.0.39.118", "271126404"),("303.0.0.30.122", "269803905"),("302.0.0.45.119", "268946212"),("300.2.0.58.129", "265245015"),("300.1.0.57.129", "263723580"),("300.0.0.51.129", "262618495"),("299.0.0.51.236", "261476335"),("298.0.0.46.116", "259886945"),("297.0.0.36.116", "257460566"),("296.0.0.44.119", "255824605"),("295.0.0.34.119", "254426061"),("294.0.0.39.118", "253340452"),("222.0.0.10.118", "253197554"),("293.0.0.43.120", "251953126"),("292.0.0.61.123", "251145638"),("292.0.0.60.123", "250937654"),("291.0.0.44.120", "249604761"),("290.0.0.44.121", "248231979"),("289.0.0.40.121", "246888155"),("288.0.0.46.123", "245199169"),("286.0.0.48.112", "242171807"),("285.0.0.43.120", "240747247"),("284.0.0.50.107", "239634218"),("283.0.0.31.121", "237966513"),("282.0.0.40.117", "236468560"),("281.0.0.36.124", "234741944"),("280.0.0.44.122", "233235235"),("279.0.0.43.120", "231020918"),("278.0.0.51.119", "229281747"),("277.0.0.41.126", "227128646"),("276.0.0.44.127", "225129281"),("275.0.0.49.127", "221372446"),("274.0.0.46.119", "219237426"),("273.0.0.39.123", "218047935"),("272.0.0.50.125", "216845461"),("271.0.0.55.109", "215365644"),("270.1.0.66.127", "214895118"),("270.0.0.57.127", "214125758"),("269.0.0.50.127", "212782999"),("268.1.0.54.121", "211681886"),("267.1.0.46.120", "210653367"),("266.0.0.64.124", "209629347"),("266.0.0.56.124", "209027740"),("265.0.0.61.103", "208173431"),("264.0.0.44.111", "206636693"),("263.0.0.46.121", "205281664"),("262.0.0.34.117", "203997157"),("261.0.0.52.126", "202681551"),("260.0.0.42.118", "201518779"),("259.0.0.36.115", "200359502"),("258.0.0.34.119", "199294483"),("257.0.0.44.118", "197851391"),("256.0.0.39.117", "196542471"),("255.0.0.33.121", "195354805"),("254.0.0.37.125", "194387467"),("253.0.0.28.116", "193013915"),("252.0.0.22.355", "191850036"),("251.0.0.31.111", "188827985"),("250.0.0.26.241", "187584912"),("249.0.0.47.118", "186228239"),("248.1.0.44.116", "184540721"),("247.0.0.42.116", "182642037"),("246.0.0.49.121", "181448462"),("245.0.0.39.118", "180475969"),("244.0.0.43.118", "179053252"),("243.0.0.49.108", "178248449"),("243.0.0.47.108", "178056619"),("242.0.0.43.119", "176515204"),("241.0.0.39.120", "175428060"),("240.0.0.38.121", "174075057"),("239.0.0.41.152", "172860670"),("238.0.0.41.116", "171725783"),("237.0.0.44.120", "170693384"),("236.0.0.40.117", "169421929"),("235.0.0.38.118", "168314968"),("234.0.0.30.115", "167211814"),("233.0.0.36.117", "166104927"),("232.0.0.35.115", "165032968"),("231.0.0.39.113", "163964762"),("230.0.0.36.117", "162942669"),("229.0.0.35.117", "162302402"),("228.0.0.41.124", "161383643"),("227.0.0.43.158", "160467766"),("226.0.0.49.120", "159526651"),("225.0.0.47.118", "158425850"),("224.0.0.33.114", "157411927"),("223.0.0.47.120", "156649449"),("222.0.0.48.113", "155323327"),("221.0.0.48.102", "154683417"),("220.0.0.46.112", "153408057"),("219.0.0.46.114", "152515137"),("219.0.0.42.114", "152362346"),("218.0.0.46.109", "151380998"),("217.0.0.45.98", "150298377"),("216.0.0.38.104", "149356190"),("215.0.0.45.98", "148268798"),("214.0.0.43.83", "147376170"),("212.0.0.28.110", "145459230"),("211.0.0.43.112", "144693239"),("210.0.0.43.119", "143667885"),("209.0.0.39.91", "142863906"),("208.0.0.38.104", "141745697"),("207.0.0.33.100", "140791845"),("206.0.0.36.105", "139932195"),("205.0.0.27.113", "139196834")]
    av_bv = random.choice(fbav_bv);fbav = av_bv[0];fbbv = av_bv[1]
    rvplus = int(random.randint(1,99));fbrv = (int(fbav.split(".")[0]) * 1000) + int(fbbv) + rvplus
    fbcr = random.choice(("U.S. Cellular", "Verizon", "Verizon Wireless", "Cricket", "Google Fi", "T-Mobile", "AT&T", "Sprint","Metro by T-Mobile","Boost Mobile","TracFone Wireless","Xfinity Mobile","Mint Mobile","Visible","Republic Wireless","Consumer Cellular","Straight Talk","Spectrum Mobile","Ting","H2O Wireless","FreedomPop","Boost Infinite","Simple Mobile","Pure Talk","C-Spire Wireless","SouthernLINC Wireless","GCI Wireless","Bluegrass Cellular","Nex-Tech Wireless","T-Mobile Prepaid","Ultra Mobile","TracFone","Freedom Wireless","MetroPCS","Cellcom","Nextel","Cricket Wireless"))
    phone = random.choice(("Samsung","OnePlus","OPPO","Infinix"))
    if phone == "Samsung":modle = random.choice(("SM-S918B", "SM-S916B", "SM-S911B", "SM-F936B", "SM-F721B", "SM-S908B", "SM-S906B", "SM-S901B", "SM-A546B", "SM-A346B", "SM-A146B", "SM-A736B", "SM-A536B", "SM-A336B", "SM-A236B", "SM-A135F", "SM-A047F", "SM-M546B", "SM-M536B", "SM-M336B", "SM-M236B", "SM-E236B", "SM-E135F", "SM-A725F", "SM-A528B", "SM-A525F", "SM-A326B", "SM-A226B", "SM-M426B", "SM-M326B", "SM-M127F", "SM-F415F", "SM-A022F", "SM-A025F", "SM-A013F", "SM-E025F", "SM-A105F", "SM-A107F", "SM-A205F", "SM-A207F", "SM-A305F", "SM-A307F", "SM-A505F", "SM-A515F", "SM-A705F", "SM-A715F", "SM-M215F", "SM-M315F", "SM-M515F", "SM-M405F", "SM-M307F", "SM-A600F", "SM-A605F", "SM-J600F", "SM-J810F", "SM-J415F", "SM-J530F", "SM-G611F", "SM-J720F", "SM-G885F", "SM-A920F", "SM-G965F", "SM-G960F", "SM-G955F", "SM-G950F", "SM-G935F", "SM-G930F", "SM-N960F", "SM-N950F", "SM-A530F", "SM-A730F", "SM-J260F", "SM-J701F", "SM-J500F", "SM-A500F", "SM-A300F", "SM-A700F", "SM-G887F", "SM-A507F", "SM-A707F", "SM-C900F", "SM-C701F", "SM-C501F", "SM-J200F", "SM-J210F", "SM-G532F", "SM-J3119", "SM-J400F", "SM-G570F", "SM-J610F", "SM-G615F", "SM-J701F", "SM-J730F", "SM-J700F", "SM-G610F", "SM-J727P", "SM-J320F", "SM-J330F", "SM-J337P", "SM-J327P", "SM-J110F", "SM-J105F", "SM-J106B", "SM-G360F", "SM-G355H", "GT-I8260", "SM-G530F", "SM-J250F", "SM-G710F", "SM-A202F", "SM-A405F", "SM-A908B", "SM-M015G", "SM-M017F", "SM-M115F", "SM-M217F", "SM-M315F", "SM-M013F", "SM-F900F", "SM-F700F", "SM-F707B", "SM-N920F", "SM-N930F", "SM-N935F", "SM-N910F", "SM-N9005", "GT-I9200", "SM-G750F", "GT-I9152", "SM-G900F", "SM-G800F", "SM-G903F", "SM-G920F", "SM-G925F", "SM-G928F", "SM-G850F", "SM-E700F", "SM-E500F", "SM-J500F", "SM-J100F", "SM-A217F", "SM-A207F", "SM-A315F", "SM-A415F", "SM-A115F", "SM-A215F", "SM-A615F", "SM-A815F", "SM-M115F", "SM-A015F"))
    elif phone == "OnePlus":modle = random.choice(("A0001", "A2001", "E1001", "A3000", "A3010", "A5000", "A5010", "A6000", "A6010", "GM1901", "GM1911", "HD1901", "IN2013", "IN2023", "KB2001", "AC2001", "BE2013", "LE2113", "LE2123", "LE2101", "CPH2401", "CPH2411", "CPH2413", "CPH2447", "CPH2487", "PGKM10", "DN2101", "DN2103", "DN2109", "MT2110", "A2003", "A3003", "A6001", "GM1903", "GM1913", "HD1903", "IN2020", "KB2002", "AC2002", "BE2020", "LE2110", "LE2120", "CPH2402", "CPH2412", "CPH2414", "CPH2448", "CPH2488", "PGKM11", "DN2102", "DN2104", "DN2110", "MT2111", "A5001", "A5002", "A6002", "A6003", "GM1904", "GM1914", "HD1904", "IN2021", "KB2003", "AC2003", "BE2021", "LE2111", "LE2121", "CPH2403", "CPH2413", "CPH2415", "CPH2449", "CPH2489", "PGKM12", "DN2105", "DN2106", "DN2111", "MT2112", "A5003", "A5004", "A6004", "GM1905", "GM1915", "HD1905", "IN2022", "KB2004", "AC2004", "BE2022", "LE2112", "LE2122", "CPH2404", "CPH2414", "CPH2416", "CPH2450", "CPH2490", "PGKM13", "DN2107", "DN2108", "DN2112", "MT2113", "A5005", "A5006", "A6005", "GM1906", "GM1916", "HD1906", "IN2023", "KB2005", "AC2005", "BE2023", "LE2113", "LE2123", "CPH2405", "CPH2415", "CPH2417", "CPH2451", "CPH2491", "PGKM14", "DN2109", "DN2110", "DN2113", "MT2114", "A5007", "A5008", "A6006", "GM1907", "GM1917", "HD1907", "IN2024", "KB2006", "AC2006", "BE2024", "LE2114", "LE2124", "CPH2406", "CPH2416", "CPH2418", "CPH2452", "CPH2492", "PGKM15", "DN2111", "DN2112", "DN2114", "MT2115", "A5009", "A5010", "A6007", "GM1908", "GM1918", "HD1908", "IN2025", "KB2007", "AC2007", "BE2025", "LE2115", "LE2125", "CPH2407", "CPH2417", "CPH2419", "CPH2453", "CPH2493", "PGKM16", "DN2113", "DN2114", "DN2115", "MT2116"))
    elif phone == "OPPO":modle = random.choice(("CPH2371", "CPH2511", "CPH2499", "CPH1831", "CPH1853", "CPH1925", "CPH1901", "CPH1893", "CPH1933", "CPH1935", "CPH2015", "CPH2127", "CPH2235", "CPH2301", "CPH2197", "CPH2207", "CPH1609", "CPH1607", "CPH1711", "CPH1723", "CPH1819", "CPH1823", "CPH1969", "CPH1965", "CPH2015", "CPH2111", "CPH2219", "CPH2201", "CPH2205", "CPH2209", "CPH7001", "CPH7002", "CPH7003", "CPH1851", "CPH1951", "CPH1933", "CPH2105", "CPH1917", "CPH1941", "CPH1989", "CPH1987", "CPH2030", "CPH2035", "CPH2105", "CPH2107", "CPH2159", "CPH2158", "CPH2389", "CPH2388", "CPH2469", "CPH2489", "CPH2539", "CPH2559", "CPH2609", "CPH2619", "CPH1819", "CPH1809", "CPH1821", "CPH1835", "CPH1925", "CPH1945", "CPH2045", "CPH2043", "CPH2155", "CPH2159", "CPH2193", "CPH2191", "CPH2201", "CPH2205", "CPH2249", "CPH2248", "CPH2461", "CPH2449", "CPH2281", "CPH1971", "CPH1997", "CPH2173", "CPH2175", "CPH2171", "CPH1711", "CPH1901", "CPH1819", "CPH2075", "CPH1725", "CPH1601", "CPH1602", "CPH1701", "CPH1702", "CPH2219", "CPH1909", "CPH1973", "CPH2050", "CPH2073", "CPH2071", "CPH1919", "CPH2101", "CPH1847", "CPH2255", "CPH2363", "CPH2443", "CPH2211", "CPH2055", "CPH2175", "CPH2161", "CPH1931", "CPH1987", "CPH2021", "CPH1831", "CPH1853", "CPH1893", "CPH1897", "CPH1845", "CPH2239", "CPH2158", "CPH2485", "CPH2523", "CPH2241", "CPH2545", "CPH2151", "CPH2153", "CPH2157", "CPH2150", "CPH2154", "CPH2156", "CPH2152", "CPH2555", "CPH2551", "CPH2553", "CPH2552", "CPH2550", "CPH2554", "CPH2556", "CPH2557", "CPH2558", "CPH2559", "CPH2600", "CPH2601", "CPH2602", "CPH2603", "CPH2604", "CPH2605", "CPH2606", "CPH2607"))
    elif phone == "Infinix":modle = random.choice(("X5010", "X5515", "X267", "X653", "X657", "X6511B", "X6515", "X6525", "X655C", "X682B", "X663", "X6817", "X6817", "X573", "X626", "X682C", "X6818", "X6512", "X6513", "X6521", "X6523", "X659", "X673", "X665", "X6810", "X6811", "X610", "X620", "X640", "X650", "X620C", "X640C", "X641", "X642", "X640S", "X660", "X6817F", "X6811F", "X6817G", "X6817H", "X673S", "X6515S", "X653B", "X657D", "X660S", "X661", "X662", "X664", "X670", "X671", "X672", "X675", "X676", "X678", "X679", "X6812", "X682", "X683", "X684", "X685", "X686", "X687", "X688", "X689", "X690", "X691", "X692", "X693", "X694", "X695", "X696", "X697", "X698", "X699", "X700", "X701", "X702", "X703", "X704", "X705", "X706", "X707", "X708", "X709", "X710", "X711", "X712", "X713", "X714", "X715", "X716", "X717", "X718", "X719", "X720", "X721", "X722", "X723", "X724", "X725", "X726", "X727", "X728", "X729", "X730", "X731", "X732", "X733", "X734", "X735", "X736", "X737", "X738", "X739", "X740", "X741", "X742", "X743", "X744", "X745", "X746", "X747", "X748", "X749", "X750"))
    #dalvik = f"Dalvik/2.1.0 (Linux; U; Android {fbsv}; {modle} Build/{build}{numberr})"
    dblifb = f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};"
    uaD1 = f"[FBAN/FB4A;FBAV/{fbav};FBPN/com.facebook.katana;FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/{phone};FBBD/{phone.lower()};FBDV/{modle};FBSV/{fbsv};FBCA/{archite};FBDM/{fbdm};]"
    uaD2 = f"[FBAN/FB4A;FBAV/{fbav};FBPN/com.facebook.katana;FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/{phone};FBBD/{phone.lower()};FBDV/{modle};FBSV/{fbsv};FBCA/{archite};FBDM/{fbdm};FB_FW/1;]"
    uaD3 = f"[FBAN/FB4A;FBAV/{fbav};FBPN/com.facebook.katana;FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/{phone};FBBD/{phone.lower()};FBDV/{modle};FBSV/{fbsv};FBCA/{archite};FBDM/{fbdm};FB_FW/1;] FBBK/1"
    uaD4 = f"[FBAN/FB4A;FBAV/{fbav};FBPN/com.facebook.katana;FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/{phone};FBBD/{phone.lower()};FBDV/{modle};FBSV/{fbsv};FBCA/{archite};FBDM/{fbdm};FB_FW/1;FBRV/{fbrv};]"
    uaD5 = f"[FBAN/FB4A;FBAV/{fbav};FBPN/com.facebook.katana;FBLC/en_US;FBBV/{fbbv};FBCR/{fbcr};FBMF/{phone};FBBD/{phone.lower()};FBDV/{modle};FBSV/{fbsv};FBCA/{archite};FBDM/{fbdm};FB_FW/1;FBRV/{fbrv};] FBBK/1"
    uaD6 = f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{fbdm};FBLC/en_US;FBRV/{fbrv};FB_FW/2;FBCR/{fbcr};FBMF/{phone};FBBD/{phone.lower()};FBPN/com.facebook.katana;FBDV/{modle};FBSV/{fbsv};FBOP/{fbop};FBCA/{archite};]"
    uaD7 = f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{fbdm};FBLC/en_US;FBCR/{fbcr};FBMF/{phone};FBBD/{phone.lower()};FBPN/com.facebook.katana;FBDV/{modle};FBSV/{fbsv};FBCA/{archite};]"   
    ua = random.choice((uaD1,uaD2,uaD3,uaD4,uaD5,uaD6,uaD7))
    return f"{dblifb}{ua}"
ua = uaua()
#▬▭▬▭▬▭▬▭[ STATUS CHECKER ]▬▭▬▭▬▭▬▭#
def ck_sttus():
    try:
        token = open(".MrSxR_TkN.txt", "r").read()
        uid = "61565919664817"
        _data = {"User-Agent": ua,"client_doc_id": "42003896889828048564952729208","method": "post","locale": "en_US","pretty": "false","format": "json","variables": "{\"profile_id\":"+ uid +",\"suggestion_friends_paginating_first\":2500}","fb_api_req_friendly_name": "SuggestionsFriendListContentQuery","fb_api_caller_class": "graphservice","fb_api_analytics_tags": "[\"At_Connection\",\"GraphServices\"]","client_trace_id": f"{trc_id}","server_timestamps": "true","purpose": "fetch"}
        _header = {"X-Graphql-Client-Library": "graphservice","X-Graphql-Request-Purpose": "fetch","X-Fb-Privacy-Context": "2368177546817046","X-Fb-Background-State": "1","X-Fb-Net-Hni": sm_hni,"X-Fb-Sim-Hni": sm_hni,"Authorization": f"OAuth {token}","X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9","X-Fb-Connection-Type": "MOBILE.LTE","X-Fb-Device-Group": "3941","X-Tigon-Is-Retry": "False","X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE","X-Fb-Ta-Logging-Ids": f"graphql:{trc_id}","X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery","X-Fb-Request-Analytics-Tags": "graphservice","Priority": "u=0","Accept-Encoding": "gzip, deflate","X-Fb-Http-Engine": "Liger","X-Fb-Client-Ip": "True","X-Fb-Server-Cluster": "True","X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9","Content-Type": "application/x-www-form-urlencoded","Content-Length": "567"}
        url = "https://graph.facebook.com/graphql"
        sxrresps = requests.post(url, headers=_header, data=_data).json()
        try:
            respx = sxrresps["data"]["user"]["friends"]["edges"]
            if len(respx) < 10:return f"{c}Expire"
            else:return f"{b}Active"
        except:return f"{c}Expire"
    except:return f"{a}None"
#▬▭▬▭▬▭▬▭[ LOGO ]▬▭▬▭▬▭▬▭#
def clr_logo(stts=True):
    global status
    if stts:status = ck_sttus()
    os.system("clear")
    print(f"""{b}
      .d8888.  db    db  d8888b. 
      88'  YP  `8b  d8'  88  `8D 
      `8bo.     `8bd8'   88oobY' 
        `Y8b.   .dPYb.   88`8b   
      db   8D  .8P  Y8.  88 `88. 
      `8888Y'  YP    YP  88   YD   {j}FILE
{sxrline}
 {b}[{c}●{b}] DEVELOPER    {f}:{b} Mr.SxR
 {b}[{c}●{b}] FACEBOOK     {f}:{b} Masudur Rahman Sifat
 {b}[{c}●{b}] GITHUB       {f}:{b} github.com/Mr-SxR
 {b}[{c}●{b}] TOOL         {f}:{b} FILE MAKE
{sxrline}
           {b}--●([{status}{b})]●--
{sxrline}""")
#▬▭▬▭▬▭▬▭[ MAIN MENU DEF ]▬▭▬▭▬▭▬▭#
def sxr_main():
    clr_logo(stts=True)
    if "Active" in status:
        print(f" {l1} MAKE DUMP FILE\n {l2} DUPLICATE REMOVE\n {l3} REMOVE STYLIST NAME IDS\n {l4} REMOVE ID IN USE\n {l5} SEPARATE IDS\n {l6} SEPARATE SPECIFIC NAMES\n {l7} DIVIDE LARGE FILE\n {l8} REMOVE TOKEN\n {l0} EXIT\n{sxrline}")
        choice1 = input(f"{b} [{c}●{b}] CHOOSE OPTION {ekl} ")
        if choice1 in ["1","01","A","a"]:creat_mnu()
        elif choice1 in ["2","02","B","b"]:duplicte_rmv()
        elif choice1 in ["3","03","C","c"]:stylist_rmv()
        elif choice1 in ["4","04","D","d"]:line_rmv()
        elif choice1 in ["5","05","E","e"]:saprt_ids()
        elif choice1 in ["6","06","F","f"]:saprt_nam()
        elif choice1 in ["7","07","G","g"]:divider()
        elif choice1 in ["8","08","H","h"]:ckki_rmv()
        elif choice1 in ["0","00","O","o"]:exit()
        else:print(f"\n{c} You have selected the wrong option..");time.sleep(2);sxr_main()
    else:
        print(f" {l1} LOGIN\n {l2} DUPLICATE REMOVE\n {l3} REMOVE STYLIST NAME IDS\n {l4} REMOVE ID IN USE\n {l5} SEPARATE IDS\n {l6} SEPARATE SPECIFIC NAMES\n {l7} DIVIDE LARGE FILE\n {l8} REMOVE TOKEN\n {l0} EXIT\n{sxrline}")
        choice2 = input(f"{b} [{c}●{b}] CHOOSE OPTION {ekl} ")
        if choice2 in ["1","01","A","a"]:login_menu()
        elif choice2 in ["2","02","B","b"]:duplicte_rmv()
        elif choice2 in ["3","03","C","c"]:stylist_rmv()
        elif choice2 in ["4","04","D","d"]:line_rmv()
        elif choice2 in ["5","05","E","e"]:saprt_ids()
        elif choice2 in ["6","06","F","f"]:saprt_nam()
        elif choice2 in ["7","07","G","g"]:divider()
        elif choice2 in ["8","08","H","h"]:ckki_rmv()
        elif choice2 in ["0","00","O","o"]:exit()
        else:print(f"\n{c} You have selected the wrong option..");time.sleep(2);sxr_main()
#▬▭▬▭▬▭▬▭[ CREATE MENU DEF ]▬▭▬▭▬▭▬▭#
def creat_mnu():
    clr_logo(stts=False)
    print(f" {l1} CREATE SIMPLE FILE\n {l2} MAKE UNLIMITED IDS FILE\n {l3} DUMP FOLLOWER (COMING)\n {l0} BACK MENU\n{sxrline}")
    choicex = input(f"{b} [{c}●{b}] CHOOSE OPTION {ekl} ")
    if choicex in ["1","01","A","a"]:smpl_fbmkr()
    elif choicex in ["2","02","B","b"]:unlimd_flmkr()
    elif choicex in ["3","03","C","c"]:exit("\n This feature is coming soon")
    elif choicex in ["0","00","O","o"]:sxr_main()
    else:print(f"\n{c} You have selected the wrong option..");time.sleep(2);creat_mnu()
#▬▭▬▭▬▭▬▭[ LOGIN MENU DEF ]▬▭▬▭▬▭▬▭#
def login_menu():
    try:os.remove(".MrSxR_TkN.txt")
    except:pass
    clr_logo(stts=True)
    print(f" {l1} LOGIN WITH EMAIL/UID - PASSWORD\n {l2} LOGIN WITH COOKIE\n {l3} LOGIN WITH TOKEN\n {l0} BACK MENU\n{sxrline}")
    choice3 = input(f"{b} [{c}●{b}] CHOOSE OPTION {ekl} ")
    if choice3 in ["1","01","A","a"]:login_id_ps()
    elif choice3 in ["2","02","B","b"]:login_coki()
    elif choice3 in ["3","03","C","c"]:login_tkkn()
    elif choice3 in ["0","00","O","o"]:sxr_main()
    else:print(f"\n{c} You have selected the wrong option..");time.sleep(2);login_menu()
#▬▭▬▭▬▭▬▭[ LOGIN UID/PASS ]▬▭▬▭▬▭▬▭#
def login_id_ps():
    try:
        ids = input(f"{b} [{c}●{b}] UID/EMAIL {ekl} ")
        pww = input(f"{b} [{c}●{b}] PASSWORD {ekl} ")
        _data = {"access_token": "256002347743983|374e60f8b9bb6b8cbb30f78030438895","sdk_version": str(random.randint(1,26)),"email": ids,"password": pww,"sdk": "android","locale": "en_US","generate_session_cookies": "1","sig": "c1e620fa708a1d5696fb991c1bde5662"}
        _header = {"Host": "graph.facebook.com","x-fb-connection-bandwidth": bnd_wh,"x-fb-sim-hni": sm_hni,"x-fb-net-hni": sm_hni,"x-fb-connection-quality": "EXCELLENT","user-agent": ua,"content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
        url = "https:/"+"/gr"+"a"+"p"+"h.facebook.com/auth/login"
        sxr_respns = requests.post(url,data=_data,headers=_header,allow_redirects=False).json()
        if "access_token" in sxr_respns:
            token = sxr_respns["access_token"]
            print(f"\n{b} [{c}●{b}] TOKEN {ekl} " + token)
            open(".MrSxR_TkN.txt","w").write(token)
            input("\n LOGIN DONE PRESS ENTER");sxr_main()
        elif "www.facebook.com" in sxr_respns["error"]["message"]:exit(f"\n {c}ACCOUNT IS IN CHECKPOINT");time.sleep(3);login_menu()
        else:
            _data = {"email":ids, "password":pww, "adid":str(uuid.uuid4()), "device_id":str(uuid.uuid4()), "family_device_id":str(uuid.uuid4()), "session_id":str(uuid.uuid4()), "advertiser_id":str(uuid.uuid4()), "reg_instance":str(uuid.uuid4()), "logged_out_id":str(uuid.uuid4()), "locale":"en_US", "client_country_code":"US", "cpl":"true", "source":"login", "format":"json", "omit_response_on_success":"false", "credentials_type":"password", "error_detail_type":"button_with_disabled", "generate_session_cookies":"1", "generate_analytics_claim":"1", "generate_machine_id":"1", "tier":"regular", "currently_logged_in_userid":"0", "fb_api_req_friendly_name":"authenticate", "fb_api_caller_class":"com.facebook.account.login.protocol.Fb4aAuthHandler", "fb4a_shared_phone_cpl_experiment":"fb4a_shared_phone_nonce_cpl_at_risk_v3", "fb4a_shared_phone_cpl_group":"enable_v3_at_risk", "access_token":"350685531728%7C62f8ce9f74b12f84c123cc23437a4a32", "api_key":"882a8490361da98702bf97a021ddc14d", "sig":"62f8ce9f74b12f84c123cc23437a4a32"}
            _header = {"Host":"graph.facebook.com", "User-Agent":ua, "Accept-Encoding":"gzip, deflate", "Accept":"*/*", "Connection":"keep-alive", "Authorization":"OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32", "X-FB-SIM-HNI":sm_hni, "X-FB-Net-HNI":sm_hni, "X-FB-Connection-Bandwidth":bnd_wh, "X-FB-Connection-Quality":"EXCELLENT", "X-FB-Connection-Type":"MOBILE.LTE", "X-FB-HTTP-Engine":"Liger", "X-FB-Client-IP":"True", "X-FB-Friendly-Name":"authenticate", "Content-Type":"application/x-www-form-urlencoded", "Content-Length":"1026"}
            url = "https:/"+"/b-"+"g"+"ra"+"ph.facebook.com/auth/login"
            sxr_respns = requests.post(url,data=_data,headers=_header,allow_redirects=False).json()
            if "access_token" in sxr_respns:
                token = sxr_respns["access_token"]
                print(f"\n{b} [{c}●{b}] TOKEN {ekl} " + token)
                open(".MrSxR_TkN.txt","w").write(token)
                input("\n LOGIN DONE PRESS ENTER");sxr_main()
            else:print(f"\n {c}WORNG ID PASSWORD...");time.sleep(3);login_menu()
    except Exception as e:print(f"Error : {e}");time.sleep(3);login_menu()
#▬▭▬▭▬▭▬▭[ LOGIN COOKIE ]▬▭▬▭▬▭▬▭#
def login_coki():
    try:
        cokki = input(f"{b} [{c}●{b}] COOKIE {ekl} ")
        session = requests.session()
        _data = {"access_token": "1348564698517390|007c0a9101b9e1c8ffab727666805038", "scope": ""}
        reqstx1 = session.post("https://graph.facebook.com/v16.0/device/login/", data=_data).json()
        code = reqstx1["code"];user_code = reqstx1["user_code"]
        cookie = {"Cookie": cokki}
        reqstx2 = bs(session.get("https://m.facebook.com/device", cookies=cookie).content, "html.parser")
        jazo_ = reqstx2.find("form", {"method": "post"})
        _data2 = {"jazoest": re.search('name="jazoest" type="hidden" value="(.*?)"', str(jazo_)).group(1), "fb_dtsg": re.search(r'name="fb_dtsg" type="hidden" value="([^"]+)"', str(reqstx2)).group(1), "qr": "0", "user_code": user_code}
        url1 = "https://m.facebook.com" + jazo_["action"]
        postx = bs(session.post(url1, data=_data2, cookies=cookie).content, "html.parser")
        _dataf = {}
        reqjazo_ = postx.find("form", {"method": "post"})
        for x in reqjazo_("input", {"value": True}):
            try:
                if x["name"] == "__CANCEL__":pass
                else:_dataf.update({x["name"]: x["value"]})
            except Exception as e:pass
        url2 = "https://m.facebook.com" + reqjazo_["action"]
        url = f"https://graph.facebook.com/v16.0/device/login_status?method=post&code={code}&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038"
        postx2 = bs(session.post(url2, data=_dataf, cookies=cookie).content, 'html.parser')
        sxrresp = session.get(url, cookies=cookie).json()
        if "access_token" in sxrresp:
            token = sxrresp["access_token"]
            print(f"\n{b} [{c}●{b}] TOKEN {ekl} "+token)
            open(".MrSxR_TkN.txt", "w").write(token)
            input("\n LOGIN DONE PLEASE ENTER");sxr_main()
        else:print(f"\n {c}INVALID COOKIE FORMAT...");time.sleep(3);login_menu()
    except Exception as e:print(f"Error : {e}");time.sleep(3);login_menu()
#▬▭▬▭▬▭▬▭[ LOGIN INSTA ADDED COOKIE ]▬▭▬▭▬▭▬▭#
def fuxk():
    try:
        cokki = input(f"{b} [{c}●{b}] COOKIE {ekl} ")
        session = requests.session()
        session.headers.update({'Accept-Language': 'id,en;q=0.9','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36','Referer': 'https://www.instagram.com/','Host': 'www.facebook.com','Sec-Fetch-Mode': 'cors','Accept': '*/*','Connection': 'keep-alive','Sec-Fetch-Site': 'cross-site','Sec-Fetch-Dest': 'empty','Origin': 'https://www.instagram.com','Accept-Encoding': 'gzip, deflate',})
        response = session.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cokki})
        if '"access_token":' in str(response.headers):
            token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
            print(f"\n{b} [{c}●{b}] TOKEN {ekl} "+token)
            open(".MrSxR_TkN.txt", "w").write(token)
            input("\n LOGIN DONE PLEASE ENTER");sxr_main()
        else:print(f"\n {c}INVALID COOKIE FORMAT...");time.sleep(3);login_menu()
    except Exception as e:print(f"Error : {e}");time.sleep(3);login_menu()
#▬▭▬▭▬▭▬▭[ LOGIN TOKEN ]▬▭▬▭▬▭▬▭#
def login_tkkn():
    try:
        token = input(f"{b} [{c}●{b}] TOKEN {ekl} ")
        if token.startswith("EAAG") and token.startswith("EAAB"):print(f"\n {c}INVALID TOKEN FORMAT...");time.sleep(3);login_menu()
        else:open(".MrSxR_TkN.txt", "w").write(token);sxr_main()
    except Exception as e:print(f"Error : {e}...");time.sleep(3);login_menu()
#▬▭▬▭▬▭▬▭[ SIMPLE FILE MAKER ]▬▭▬▭▬▭▬▭#
def smpl_fbmkr():
    clr_logo(stts=False)
    token = open(".MrSxR_TkN.txt", "r").read()
    sv_dpfl = input(f"{b} [{c}●{b}] ENTER FILE NAME {ekl} ")
    if not (sv_dpfl == "/sdcard/" or sv_dpfl == "/sdcard" or sv_dpfl == "/storage/emulated/0/" or sv_dpfl == "/storage/emulated/0"):
        os.system(f"rm -rf {sv_dpfl}")
    print(f"{b} [{c}●{b}] PAST ALL UID⬎\n{sxrline}{a}")
    while True:
        ids_all = input()
        if ids_all == "":
            if id_alx:break
            else:continue
        try:id_alx.append(ids_all.split("|")[0])
        except:id_alx.append(ids_all)
    with threadpol(max_workers=30) as sifatx:
        clr_logo(stts=True)
        total = len(id_alx)
        for uid in id_alx:
            sifatx.submit(simpl_lop,uid,token,sv_dpfl,total)
    time.sleep(2);exit(f"\r\n{sxrline}\n {f}•{a}SUCESSFULLY DONE ALL IDS, FILE SAVE AS {ekl} {b}{sv_dpfl}")
def simpl_lop(uid,token,sv_dpfl,total):
    try:
        _data = {"User-Agent": ua,"client_doc_id": "42003896889828048564952729208","method": "post","locale": "en_US","pretty": "false","format": "json","variables": "{\"profile_id\":"+ uid +",\"suggestion_friends_paginating_first\":2500}","fb_api_req_friendly_name": "SuggestionsFriendListContentQuery","fb_api_caller_class": "graphservice","fb_api_analytics_tags": "[\"At_Connection\",\"GraphServices\"]","client_trace_id": f"{trc_id}","server_timestamps": "true","purpose": "fetch"}
        _header = {"X-Graphql-Client-Library": "graphservice","X-Graphql-Request-Purpose": "fetch","X-Fb-Privacy-Context": "2368177546817046","X-Fb-Background-State": "1","X-Fb-Net-Hni": sm_hni,"X-Fb-Sim-Hni": sm_hni,"Authorization": f"OAuth {token}","X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9","X-Fb-Connection-Type": "MOBILE.LTE","X-Fb-Device-Group": "3941","X-Tigon-Is-Retry": "False","X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE","X-Fb-Ta-Logging-Ids": f"graphql:{trc_id}","X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery","X-Fb-Request-Analytics-Tags": "graphservice","Priority": "u=0","Accept-Encoding": "gzip, deflate","X-Fb-Http-Engine": "Liger","X-Fb-Client-Ip": "True","X-Fb-Server-Cluster": "True","X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9","Content-Type": "application/x-www-form-urlencoded","Content-Length": "567"}
        url = "https://graph.facebook.com/graphql"
        sxrresps = requests.post(url, headers=_header, data=_data).json()
        try:respx = sxrresps["data"]["user"]["friends"]["edges"]
        except:pass
        for xdge in respx:
            try:ndex = xdge["node"]
            except:pass
            open(sv_dpfl, "a", encoding="utf-8").write(ndex["id"] + "|" + ndex["name"] + "\n")
        try:totl_act=len(open(sv_dpfl,"r").readlines())
        except:totl_act="?"
        clor = random.choice(colors)
        print(f"\r {clor}SUCESSFULLY EXTRACTED {uid}")
        extrt.append(uid)
        sys.stdout.write(f"\r {a}[{b}Mr.SxR{a}] ~ [{f}{total} {b}●{a} {str(len(extrt))}{a}] ~ [{f}{totl_act}{a}]");sys.stdout.flush()
    except KeyError:pass
    except requests.exceptions.ConnectionError:time.sleep(6)
#▬▭▬▭▬▭▬▭[ UNLIMITED FILE MAKER ]▬▭▬▭▬▭▬▭#
def unlimd_flmkr():
    clr_logo(stts=False)
    try:os.remove(".MrSxR_UNLiMTD.txt")
    except:pass
    token = open(".MrSxR_TkN.txt", "r").read()
    sv_dpfl = input(f"{b} [{c}●{b}] ENTER FILE NAME {ekl} ")
    if not (sv_dpfl == "/sdcard/" or sv_dpfl == "/sdcard" or sv_dpfl == "/storage/emulated/0/" or sv_dpfl == "/storage/emulated/0"):
        os.system(f"rm -rf {sv_dpfl}")
    clr_logo(stts=True)
    try:
        uid_lmit = int(input(f"{b} [{c}●{b}] HOW MANY IDS YOU WANT TO ADD {ekl} "))
        if uid_lmit < 1 or uid_lmit > 20:print(f"\n {c}IDS MUST BE BETWEEN 1 - 20...");time.sleep(3);unlimd_flmkr()
    except Exception as e:print(f"Error : {e}...");time.sleep(3);unlimd_flmkr()
    for i in range(uid_lmit):
        while True:
            uid = input(f"{b} [{c}●{b}]{a} PUT ID {i+1} {ekl}{b} ")
            try:
                _data = {"User-Agent": ua,"client_doc_id": "42003896889828048564952729208","method": "post","locale": "en_US","pretty": "false","format": "json","variables": "{\"profile_id\":"+ uid +",\"suggestion_friends_paginating_first\":2500}","fb_api_req_friendly_name": "SuggestionsFriendListContentQuery","fb_api_caller_class": "graphservice","fb_api_analytics_tags": "[\"At_Connection\",\"GraphServices\"]","client_trace_id": f"{trc_id}","server_timestamps": "true","purpose": "fetch"}
                _header = {"X-Graphql-Client-Library": "graphservice","X-Graphql-Request-Purpose": "fetch","X-Fb-Privacy-Context": "2368177546817046","X-Fb-Background-State": "1","X-Fb-Net-Hni": sm_hni,"X-Fb-Sim-Hni": sm_hni,"Authorization": f"OAuth {token}","X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9","X-Fb-Connection-Type": "MOBILE.LTE","X-Fb-Device-Group": "3941","X-Tigon-Is-Retry": "False","X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE","X-Fb-Ta-Logging-Ids": f"graphql:{trc_id}","X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery","X-Fb-Request-Analytics-Tags": "graphservice","Priority": "u=0","Accept-Encoding": "gzip, deflate","X-Fb-Http-Engine": "Liger","X-Fb-Client-Ip": "True","X-Fb-Server-Cluster": "True","X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9","Content-Type": "application/x-www-form-urlencoded","Content-Length": "567"}
                url = "https://graph.facebook.com/graphql"
                sxrresps = requests.post(url, headers=_header, data=_data).json()
                try:respx = sxrresps["data"]["user"]["friends"]["edges"]
                except:print(f"{f}• {a}FRIEND LIST PRIVATE");continue
                if len(respx) < 10:print(f"{f}• {a}FRIEND LIST PRIVATE");continue
                else:
                    for xdge in respx:
                        try:ndex = xdge["node"]
                        except:pass
                        open(".MrSxR_UNLiMTD.txt", "a", encoding="utf-8").write(ndex["id"] + "\n")
                    print(f"{f}• {a}DONE {i+1}");break
            except KeyError:print(f"{f}• {a}FRIEND LIST PRIVATE");continue
            except requests.exceptions.ConnectionError:time.sleep(6)
    try:total = open(".MrSxR_UNLiMTD.txt", "r").read().splitlines()
    except:total = []
    with threadpol(max_workers=30) as sifatx:
        clr_logo(stts=True)
        for uid in total:
            sifatx.submit(unlkmedfl_lop,uid,token,sv_dpfl,total)
    time.sleep(2);exit(f"\r\n{sxrline}\n {f}•{a}SUCESSFULLY DONE ALL IDS, FILE SAVE AS {ekl} {b}{sv_dpfl}")
def unlkmedfl_lop(uid,token,sv_dpfl,total):
    try:
        _data = {"User-Agent": ua,"client_doc_id": "42003896889828048564952729208","method": "post","locale": "en_US","pretty": "false","format": "json","variables": "{\"profile_id\":"+ uid +",\"suggestion_friends_paginating_first\":2500}","fb_api_req_friendly_name": "SuggestionsFriendListContentQuery","fb_api_caller_class": "graphservice","fb_api_analytics_tags": "[\"At_Connection\",\"GraphServices\"]","client_trace_id": f"{trc_id}","server_timestamps": "true","purpose": "fetch"}
        _header = {"X-Graphql-Client-Library": "graphservice","X-Graphql-Request-Purpose": "fetch","X-Fb-Privacy-Context": "2368177546817046","X-Fb-Background-State": "1","X-Fb-Net-Hni": sm_hni,"X-Fb-Sim-Hni": sm_hni,"Authorization": f"OAuth {token}","X-Fb-Session-Id": "nid=DQGq3fmNKvVh;tid=135;nc=1;fc=1;bc=0;cid=ef0e330bff1cd312f36aa5f2c69c59a9","X-Fb-Connection-Type": "MOBILE.LTE","X-Fb-Device-Group": "3941","X-Tigon-Is-Retry": "False","X-Fb-Rmd": "cached=0;state=URL_ELIGIBLE","X-Fb-Ta-Logging-Ids": f"graphql:{trc_id}","X-Fb-Friendly-Name": "SuggestionsFriendListContentQuery","X-Fb-Request-Analytics-Tags": "graphservice","Priority": "u=0","Accept-Encoding": "gzip, deflate","X-Fb-Http-Engine": "Liger","X-Fb-Client-Ip": "True","X-Fb-Server-Cluster": "True","X-Fb-Connection-Token": "ef0e330bff1cd312f36aa5f2c69c59a9","Content-Type": "application/x-www-form-urlencoded","Content-Length": "567"}
        url = "https://graph.facebook.com/graphql"
        sxrresps = requests.post(url, headers=_header, data=_data).json()
        try:respx = sxrresps["data"]["user"]["friends"]["edges"]
        except:pass
        if len(respx) < 10:pass
        else:
            for xdge in respx:
                try:ndex = xdge["node"]
                except:pass
                open(sv_dpfl, "a", encoding="utf-8").write(ndex["id"] + "|" + ndex["name"] + "\n")
            try:totl_act=len(open(sv_dpfl,"r").readlines())
            except:totl_act="?"
            clor = random.choice(colors)
            print(f"\r {clor}SUCESSFULLY EXTRACTED {uid}")
            extrt.append(uid)
            sys.stdout.write(f"\r {a}[{b}Mr.SxR{a}] ~ [{f}{len(total)} {b}●{a} {str(len(extrt))}{a}] ~ [{f}{totl_act}{a}]");sys.stdout.flush()
    except KeyError:pass
    except requests.exceptions.ConnectionError:time.sleep(6)
#▬▭▬▭▬▭▬▭[ BINARY CLEANER ]▬▭▬▭▬▭▬▭#
def clean_file(file_path):
    try:
        fresh_lines = []
        with open(file_path, "rb") as file:lines = file.readlines()       
        for line in lines:
            try:
                line.decode("utf-8")
                fresh_lines.append(line.decode("utf-8"))
            except UnicodeDecodeError:continue
        with open(file_path, "w", encoding="utf-8") as file:file.writelines(fresh_lines)
    except Exception as e:exit(f"\n {c}Error {ekl} {e}")
#▬▭▬▭▬▭▬▭[ DUPLICATE REMOVE ]▬▭▬▭▬▭▬▭#
def duplicte_rmv():
    try:
        clr_logo(stts=False)
        file_path = input(f"{b} [{c}●{b}] INPUT YOUR PATH {ekl} ")
        clean_file(file_path)
        with open(file_path, "r", encoding="utf8") as file:
            lines = file.readlines()
        unq_lns = list(set(line.strip() for line in lines))
        srt_lns = sorted(unq_lns, reverse=True)
        with open(file_path, "w", encoding="utf8") as file:
            for line in srt_lns:
                file.write(line+"\n")
        input(f"\n{b} [{c}●{b}] DUPLICATE REMOVE DONE");sxr_main()
    except FileNotFoundError:exit(f"\n {c}THE FILE '{file_path}' WAS NOT FOUND.")
    except Exception as e:exit(f"\n {c}Error {ekl} {e}")
#▬▭▬▭▬▭▬▭[ STYLIST REMOVE ]▬▭▬▭▬▭▬▭#
def stylist_rmv():
    try:
        clr_logo(stts=False)
        file_path = input(f"{b} [{c}●{b}] INPUT YOUR PATH {ekl} ")
        clean_file(file_path)
        #spcl_regex = re.compile(r'[#@#%&*\-+()!"\':;/\\?.,<>{}_~`$^\[\]=]')@#%&*-+()!"':;/\?.,<>{}_~`$^=[]
        spcl_regex = re.compile(r'[#@#%&*+()!":;/\\?,<>{}_~`$^\[\]=]')
        eng_regex = re.compile(r'^[\x00-\x7F]+$')
        tmp_pth = file_path+".tmp"
        with open(file_path, "r", encoding="utf-8") as infile, open(tmp_pth, "w", encoding="utf-8") as outfile:
            vld_lns = []
            for line in infile:
                if not spcl_regex.search(line) and eng_regex.match(line.strip()):
                    vld_lns.append(line.strip())
            srt_lns = sorted(vld_lns, reverse=True)
            for line in srt_lns:
                outfile.write(line+"\n")
        os.replace(tmp_pth, file_path)
        input(f"\n{b} [{c}●{b}] STYLIST NAMES ACCOUNT REMOVE DONE");sxr_main()
    except FileNotFoundError:exit(f"\n {c}THE FILE '{file_path}' WAS NOT FOUND.")
    except Exception as e:exit(f"\n {c}Error {ekl} {e}")
#▬▭▬▭▬▭▬▭[ USE ID REMOVE ]▬▭▬▭▬▭▬▭#
def line_rmv():
    try:
        clr_logo(stts=False)
        file_path = input(f"{b} [{c}●{b}] INPUT YOUR PATH {ekl} ")
        clean_file(file_path)
        lns_numbr = int(input(f"{b} [{c}●{b}] YOU WANT TO REMOVE THE FIRST FEW IDS {ekl} "))
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
        rmning_lns = lines[lns_numbr:]
        with open(file_path, "w", encoding="utf-8") as file:
            file.writelines(rmning_lns)
        input(f"\n{b} [{c}●{b}] SICCESSFULLY REMOVE FIRST {lns_numbr} IDS");sxr_main()
    except FileNotFoundError:exit(f"\n {c}THE FILE '{file_path}' WAS NOT FOUND.")
    except Exception as e:exit(f"\n {c}Error {ekl} {e}")
#▬▭▬▭▬▭▬▭[ SEPARATE IDS ]▬▭▬▭▬▭▬▭#
def saprt_ids():
    try:
        open(".MrSxR_SPrT.txt", "w").close()
        clr_logo(stts=False)
        file_path = input(f"{b} [{c}●{b}] INPUT YOUR PATH {ekl} ")  # Input main file path
        clean_file(file_path)
        output_file = input(f"{b} [{c}●{b}] ENTER THE NAME OF THE OUTPUT FILE {ekl} ")  # Input output file name
        try:lnks = int(input(f"{b} [{c}●{b}] HOW MANY LINKS SHOULD BE KEPT {ekl} "))
        except:lnks = 1
        lnksx_lmt = []
        print(f"\n{b} [{c}●{b}] EXAMPLE {ekl} 6155, 6156, 100092 EtC..")
        for lnksx in range(lnks):
            lnksx_lmt.append(input(f"{b} [{c}●{b}] {a}PUT LINK {lnksx + 1} {ekl}{b} "))
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
        with open(".MrSxR_SPrT.txt", "a", encoding="utf-8") as out_file:
            mxmng_lins = []
            for line in lines:
                if any(uid_lnks in line for uid_lnks in lnksx_lmt):
                    out_file.write(line)
                else:
                    mxmng_lins.append(line)
        with open(file_path, "w", encoding="utf-8") as main_file:
            main_file.writelines(mxmng_lins)
        with open(".MrSxR_SPrT.txt", "r", encoding="utf-8") as sorted_file:
            unique_lines = sorted(set(sorted_file.readlines()), reverse=True)
        with open(output_file, "w", encoding="utf-8") as final_file:
            final_file.writelines(unique_lines)
        input(f"\n{b} [{c}●{b}] YOUR SELECTED IDS ARE SAVED IN THE '{output_file}' FILE AND REMOVED FROM THE MAIN FILE.");sxr_main()
    except FileNotFoundError:exit(f"\n {c}THE FILE '{file_path}' WAS NOT FOUND.")
    except Exception as e:exit(f"\n {c}Error {ekl} {e}")
#▬▭▬▭▬▭▬▭[ SEPARATE NAME ]▬▭▬▭▬▭▬▭#
def saprt_nam():
    try:
        clr_logo(stts=False)
        file_path = input(f"{b} [{c}●{b}] INPUT YOUR PATH {ekl} ")
        clean_file(file_path)
        output_file = input(f"{b} [{c}●{b}] ENTER THE NAME OF THE OUTPUT FILE {ekl} ")
        try:kyds_nm = int(input(f"\n{b} [{c}●{b}] ENTER NUMBER OF NAMES {ekl} "))
        except:kyds_nm = 1
        keywords = []
        for i in range(kyds_nm):
            keyword = input(f"{b} [{c}●{b}] {a}ENTER NAME {i+1} {ekl}{b} ").strip().lower()
            keywords.append(keyword)
        with open(file_path, "r", encoding="utf-8") as f:lines = f.readlines()
        flter_nms = []
        rmnig_lns = []
        for line in lines:
            if any(keyword in line.lower() for keyword in keywords):
                flter_nms.append(line.strip())
            else:rmnig_lns.append(line.strip())
        with open(output_file, "w", encoding="utf-8") as f:f.write("\n".join(flter_nms))
        with open(file_path, "w", encoding="utf-8") as f:f.write("\n".join(rmnig_lns))
        input(f"\n{b} [{c}●{b}] YOUR SELECTED NAME IDS ARE SAVED IN THE '{output_file}' FILE AND REMOVED FROM THE MAIN FILE.");sxr_main()
    except FileNotFoundError:exit(f"\n {c}THE FILE '{file_path}' WAS NOT FOUND.")
    except Exception as e:exit(f"\n {c}Error {ekl} {e}")
#▬▭▬▭▬▭▬▭[ FILE DIVIDER ]▬▭▬▭▬▭▬▭#
def divider():
    try:
        clr_logo(stts=False)
        file_path = input(f"{b} [{c}●{b}] INPUT YOUR PATH {ekl} ")
        clean_file(file_path)
        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()
        prtsx = int(input(f"\n{b} [{c}●{b}] HOW MANY PARTS TO DIVIDE THE FILE {ekl} "))
        if prtsx <= 1:
            exit(f"\n {c}PARTS MUST BE MORE THAN 1.")
        ttal_lns = len(lines)
        lns_prpts = ttal_lns // prtsx
        for i in range(prtsx):
            fst = i * lns_prpts
            xnd = fst + lns_prpts if i < prtsx - 1 else ttal_lns
            output_file = input(f"{b} [{c}●{b}] OUTPUT FILE NAME {i+1} {ekl} ")
            if os.path.exists(output_file):
                print(f"{b} [{c}●{b}] '{output_file}' EXISTS. CHOOSE ANOTHER NAME.")
                continue
            with open(output_file, "w", encoding="utf-8") as file:
                file.writelines(lines[fst:xnd])
        input(f"\n{b} [{c}●{b}] FILE DIVIDED SUCCESSFULLY");sxr_main()
    except FileNotFoundError:exit(f"\n {c}THE FILE '{file_path}' WAS NOT FOUND.")
    except Exception as e:exit(f"\n {c}Error {ekl} {e}")
#▬▭▬▭▬▭▬▭[ REMOVE TOKEN ]▬▭▬▭▬▭▬▭#
def ckki_rmv():
    try:os.remove(".MrSxR_TkN.txt")
    except:pass
    sxr_main()
#▬▭▬▭▬▭▬▭[ THE END ]▬▭▬▭▬▭▬▭#
sxr_main()
