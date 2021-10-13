import requests
from bs4 import BeautifulSoup
import time
import pandas as pd
import numpy as np

# La cabecera
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}

# Creamos las url con los resultados de la búsqueda de hoteles en Benidorm para 1º quincena de agosto de 2022
# de 1 a 15 de agosto, 2 personas adultas sin niños

# Cada url contiene 25 resultados: 1-25, 26-50, 51-75, 76-100, etc...
url1 = 'https://www.booking.com/searchresults.html?aid=376376&label=bookings-name-x9XjJRNqhtTGZ30YXWfPUQS410902425082%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1005413%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf23yREhrOV9YczHwt1OUN4&sid=b833aa2de6e6c1d9a45bc49e4c7df110&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.html%3Faid%3D376376%3Blabel%3Dbookings-name-x9XjJRNqhtTGZ30YXWfPUQS410902425082%253Apl%253Ata%253Ap1%253Ap22.563.000%253Aac%253Aap%253Aneg%253Afi%253Atikwd-65526620%253Alp1005413%253Ali%253Adec%253Adm%253Appccp%253DUmFuZG9tSVYkc2RlIyh9Yf23yREhrOV9YczHwt1OUN4%3Bsid%3Db833aa2de6e6c1d9a45bc49e4c7df110%3Bsb_price_type%3Dtotal%26%3B&ss=Benidorm%2C+Spain&is_ski_area=&checkin_year=2022&checkin_month=8&checkin_monthday=1&checkout_year=2022&checkout_month=8&checkout_monthday=15&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&dest_id=-373226&dest_type=city&search_pageview_id=15c59652fce6008b&search_selected=true'

url2 = 'https://www.booking.com/searchresults.html?aid=376376&label=bookings-name-x9XjJRNqhtTGZ30YXWfPUQS410902425082%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1005413%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf23yREhrOV9YczHwt1OUN4&sid=c4b3f6f420352b7e6268dbe166abff7d&tmpl=searchresults&checkin_month=8&checkin_monthday=1&checkin_year=2022&checkout_month=8&checkout_monthday=15&checkout_year=2022&class_interval=1&dest_id=-373226&dest_type=city&dtdisc=0&from_sf=1&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms=1&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=index&src_elem=sb&srpvid=8f4d3ed4527c007a&ss=Benidorm%2C%20Spain&ss_all=0&ssb=empty&sshis=0&top_ufis=1&sig=v1uByv_1KT&rows=25&offset=25'

url3 = 'https://www.booking.com/searchresults.html?aid=376376&label=bookings-name-x9XjJRNqhtTGZ30YXWfPUQS410902425082%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1005413%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf23yREhrOV9YczHwt1OUN4&sid=c4b3f6f420352b7e6268dbe166abff7d&tmpl=searchresults&checkin_month=8&checkin_monthday=1&checkin_year=2022&checkout_month=8&checkout_monthday=15&checkout_year=2022&class_interval=1&dest_id=-373226&dest_type=city&from_sf=1&group_adults=2&group_children=0&label_click=undef&no_rooms=1&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=index&src_elem=sb&srpvid=619e684596e20030&ss=Benidorm%2C%20Spain&ssb=empty&top_ufis=1&sig=v1DS1ud_Gq&rows=25&offset=50'

url4 = 'https://www.booking.com/searchresults.html?aid=376376&label=bookings-name-x9XjJRNqhtTGZ30YXWfPUQS410902425082%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1005413%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf23yREhrOV9YczHwt1OUN4&sid=c4b3f6f420352b7e6268dbe166abff7d&tmpl=searchresults&checkin_month=8&checkin_monthday=1&checkin_year=2022&checkout_month=8&checkout_monthday=15&checkout_year=2022&class_interval=1&dest_id=-373226&dest_type=city&dtdisc=0&from_sf=1&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms=1&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=index&src_elem=sb&srpvid=ca0368abc3ba0027&ss=Benidorm%2C%20Spain&ss_all=0&ssb=empty&sshis=0&top_ufis=1&sig=v166odI5h7&rows=25&offset=75'

url5 = 'https://www.booking.com/searchresults.html?aid=376376&label=bookings-name-x9XjJRNqhtTGZ30YXWfPUQS410902425082%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1005413%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf23yREhrOV9YczHwt1OUN4&sid=c4b3f6f420352b7e6268dbe166abff7d&tmpl=searchresults&checkin_month=8&checkin_monthday=1&checkin_year=2022&checkout_month=8&checkout_monthday=15&checkout_year=2022&class_interval=1&dest_id=-373226&dest_type=city&from_sf=1&group_adults=2&group_children=0&label_click=undef&no_rooms=1&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=index&src_elem=sb&srpvid=133768f42fec0015&ss=Benidorm%2C%20Spain&ssb=empty&top_ufis=1&sig=v1AeKlyk2_&rows=25&offset=100'

url6 = 'https://www.booking.com/searchresults.html?aid=376376&label=bookings-name-x9XjJRNqhtTGZ30YXWfPUQS410902425082%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1005413%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf23yREhrOV9YczHwt1OUN4&sid=c4b3f6f420352b7e6268dbe166abff7d&tmpl=searchresults&checkin_month=8&checkin_monthday=1&checkin_year=2022&checkout_month=8&checkout_monthday=15&checkout_year=2022&class_interval=1&dest_id=-373226&dest_type=city&dtdisc=0&from_sf=1&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms=1&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=index&src_elem=sb&srpvid=1e88691ecf3c010b&ss=Benidorm%2C%20Spain&ss_all=0&ssb=empty&sshis=0&top_ufis=1&sig=v1g-gNRe67&rows=25&offset=125'

url7 = 'https://www.booking.com/searchresults.html?aid=376376&label=bookings-name-x9XjJRNqhtTGZ30YXWfPUQS410902425082%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1005413%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf23yREhrOV9YczHwt1OUN4&sid=c4b3f6f420352b7e6268dbe166abff7d&tmpl=searchresults&checkin_month=8&checkin_monthday=1&checkin_year=2022&checkout_month=8&checkout_monthday=15&checkout_year=2022&class_interval=1&dest_id=-373226&dest_type=city&from_sf=1&group_adults=2&group_children=0&label_click=undef&no_rooms=1&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=index&src_elem=sb&srpvid=a7bb69488158007a&ss=Benidorm%2C%20Spain&ssb=empty&top_ufis=1&sig=v1ZT4lt3U0&rows=25&offset=150'

url8 = 'https://www.booking.com/searchresults.html?aid=376376&label=bookings-name-x9XjJRNqhtTGZ30YXWfPUQS410902425082%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1005413%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf23yREhrOV9YczHwt1OUN4&sid=c4b3f6f420352b7e6268dbe166abff7d&tmpl=searchresults&checkin_month=8&checkin_monthday=1&checkin_year=2022&checkout_month=8&checkout_monthday=15&checkout_year=2022&class_interval=1&dest_id=-373226&dest_type=city&dtdisc=0&from_sf=1&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms=1&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=index&src_elem=sb&srpvid=5fe469652be90192&ss=Benidorm%2C%20Spain&ss_all=0&ssb=empty&sshis=0&top_ufis=1&sig=v1ssFvFJ9B&rows=25&offset=175'

url9 = 'https://www.booking.com/searchresults.html?aid=376376&label=bookings-name-x9XjJRNqhtTGZ30YXWfPUQS410902425082%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1005413%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf23yREhrOV9YczHwt1OUN4&sid=c4b3f6f420352b7e6268dbe166abff7d&tmpl=searchresults&checkin_month=8&checkin_monthday=1&checkin_year=2022&checkout_month=8&checkout_monthday=15&checkout_year=2022&class_interval=1&dest_id=-373226&dest_type=city&from_sf=1&group_adults=2&group_children=0&label_click=undef&no_rooms=1&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=index&src_elem=sb&srpvid=0007697c268a012f&ss=Benidorm%2C%20Spain&ssb=empty&top_ufis=1&sig=v1HEgICNQX&rows=25&offset=200'

url10 = 'https://www.booking.com/searchresults.html?aid=376376&label=bookings-name-x9XjJRNqhtTGZ30YXWfPUQS410902425082%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1005413%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf23yREhrOV9YczHwt1OUN4&sid=c4b3f6f420352b7e6268dbe166abff7d&tmpl=searchresults&checkin_month=8&checkin_monthday=1&checkin_year=2022&checkout_month=8&checkout_monthday=15&checkout_year=2022&class_interval=1&dest_id=-373226&dest_type=city&dtdisc=0&from_sf=1&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms=1&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=index&src_elem=sb&srpvid=0b22698b7ac00096&ss=Benidorm%2C%20Spain&ss_all=0&ssb=empty&sshis=0&top_ufis=1&sig=v17Du4-s-g&rows=25&offset=225'

url11 = 'https://www.booking.com/searchresults.html?aid=376376&label=bookings-name-x9XjJRNqhtTGZ30YXWfPUQS410902425082%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1005413%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf23yREhrOV9YczHwt1OUN4&sid=c4b3f6f420352b7e6268dbe166abff7d&tmpl=searchresults&checkin_month=8&checkin_monthday=1&checkin_year=2022&checkout_month=8&checkout_monthday=15&checkout_year=2022&class_interval=1&dest_id=-373226&dest_type=city&from_sf=1&group_adults=2&group_children=0&label_click=undef&no_rooms=1&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=index&src_elem=sb&srpvid=a7bb699d816b00e0&ss=Benidorm%2C%20Spain&ssb=empty&top_ufis=1&sig=v1mxB8EXIK&rows=25&offset=250'

url12 = 'https://www.booking.com/searchresults.html?aid=376376&label=bookings-name-x9XjJRNqhtTGZ30YXWfPUQS410902425082%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1005413%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf23yREhrOV9YczHwt1OUN4&sid=c4b3f6f420352b7e6268dbe166abff7d&tmpl=searchresults&checkin_month=8&checkin_monthday=1&checkin_year=2022&checkout_month=8&checkout_monthday=15&checkout_year=2022&class_interval=1&dest_id=-373226&dest_type=city&dtdisc=0&from_sf=1&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms=1&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=index&src_elem=sb&srpvid=b2d369ae2dee014f&ss=Benidorm%2C%20Spain&ss_all=0&ssb=empty&sshis=0&top_ufis=1&sig=v1au63X3g7&rows=25&offset=275'

url13 = 'https://www.booking.com/searchresults.html?aid=376376&label=bookings-name-x9XjJRNqhtTGZ30YXWfPUQS410902425082%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1005413%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf23yREhrOV9YczHwt1OUN4&sid=c4b3f6f420352b7e6268dbe166abff7d&tmpl=searchresults&checkin_month=8&checkin_monthday=1&checkin_year=2022&checkout_month=8&checkout_monthday=15&checkout_year=2022&class_interval=1&dest_id=-373226&dest_type=city&from_sf=1&group_adults=2&group_children=0&label_click=undef&no_rooms=1&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=index&src_elem=sb&srpvid=fae469bc9a6401c0&ss=Benidorm%2C%20Spain&ssb=empty&top_ufis=1&sig=v1TWCQNJf4&rows=25&offset=300'

url14 = 'https://www.booking.com/searchresults.html?aid=376376&label=bookings-name-x9XjJRNqhtTGZ30YXWfPUQS410902425082%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1005413%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf23yREhrOV9YczHwt1OUN4&sid=c4b3f6f420352b7e6268dbe166abff7d&tmpl=searchresults&checkin_month=8&checkin_monthday=1&checkin_year=2022&checkout_month=8&checkout_monthday=15&checkout_year=2022&class_interval=1&dest_id=-373226&dest_type=city&dtdisc=0&from_sf=1&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms=1&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=index&src_elem=sb&srpvid=d9d269cd793d016d&ss=Benidorm%2C%20Spain&ss_all=0&ssb=empty&sshis=0&top_ufis=1&sig=v1Hgd1h98q&rows=25&offset=325'

url15 = 'https://www.booking.com/searchresults.html?aid=376376&label=bookings-name-x9XjJRNqhtTGZ30YXWfPUQS410902425082%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1005413%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf23yREhrOV9YczHwt1OUN4&sid=c4b3f6f420352b7e6268dbe166abff7d&tmpl=searchresults&checkin_month=8&checkin_monthday=1&checkin_year=2022&checkout_month=8&checkout_monthday=15&checkout_year=2022&class_interval=1&dest_id=-373226&dest_type=city&from_sf=1&group_adults=2&group_children=0&label_click=undef&no_rooms=1&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=index&src_elem=sb&srpvid=761069dcd5fa0070&ss=Benidorm%2C%20Spain&ssb=empty&top_ufis=1&sig=v1urhurX7k&rows=25&offset=350'

url16 = 'https://www.booking.com/searchresults.html?aid=376376&label=bookings-name-x9XjJRNqhtTGZ30YXWfPUQS410902425082%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1005413%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf23yREhrOV9YczHwt1OUN4&sid=c4b3f6f420352b7e6268dbe166abff7d&tmpl=searchresults&checkin_month=8&checkin_monthday=1&checkin_year=2022&checkout_month=8&checkout_monthday=15&checkout_year=2022&class_interval=1&dest_id=-373226&dest_type=city&dtdisc=0&from_sf=1&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms=1&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=index&src_elem=sb&srpvid=af4869eaf3a800f8&ss=Benidorm%2C%20Spain&ss_all=0&ssb=empty&sshis=0&top_ufis=1&sig=v1nlJ7JgLD&rows=25&offset=375'

url17 = 'https://www.booking.com/searchresults.html?aid=376376&label=bookings-name-x9XjJRNqhtTGZ30YXWfPUQS410902425082%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1005413%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf23yREhrOV9YczHwt1OUN4&sid=c4b3f6f420352b7e6268dbe166abff7d&tmpl=searchresults&checkin_month=8&checkin_monthday=1&checkin_year=2022&checkout_month=8&checkout_monthday=15&checkout_year=2022&class_interval=1&dest_id=-373226&dest_type=city&from_sf=1&group_adults=2&group_children=0&label_click=undef&no_rooms=1&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=index&src_elem=sb&srpvid=419669f7e7e900fe&ss=Benidorm%2C%20Spain&ssb=empty&top_ufis=1&sig=v1hqqb6qJH&rows=25&offset=400'

url18 = 'https://www.booking.com/searchresults.html?aid=376376&label=bookings-name-x9XjJRNqhtTGZ30YXWfPUQS410902425082%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1005413%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf23yREhrOV9YczHwt1OUN4&sid=c4b3f6f420352b7e6268dbe166abff7d&tmpl=searchresults&checkin_month=8&checkin_monthday=1&checkin_year=2022&checkout_month=8&checkout_monthday=15&checkout_year=2022&class_interval=1&dest_id=-373226&dest_type=city&dtdisc=0&from_sf=1&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms=1&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=index&src_elem=sb&srpvid=51b36a05dd8e022e&ss=Benidorm%2C%20Spain&ss_all=0&ssb=empty&sshis=0&top_ufis=1&sig=v1Q3QA7_7j&rows=25&offset=425'

url19 = 'https://www.booking.com/searchresults.html?aid=376376&label=bookings-name-x9XjJRNqhtTGZ30YXWfPUQS410902425082%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1005413%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf23yREhrOV9YczHwt1OUN4&sid=c4b3f6f420352b7e6268dbe166abff7d&tmpl=searchresults&checkin_month=8&checkin_monthday=1&checkin_year=2022&checkout_month=8&checkout_monthday=15&checkout_year=2022&class_interval=1&dest_id=-373226&dest_type=city&from_sf=1&group_adults=2&group_children=0&label_click=undef&no_rooms=1&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=index&src_elem=sb&srpvid=a6f16a14186b0056&ss=Benidorm%2C%20Spain&ssb=empty&top_ufis=1&sig=v1ccYFNxps&rows=25&offset=450'

url20 = 'https://www.booking.com/searchresults.html?aid=376376&label=bookings-name-x9XjJRNqhtTGZ30YXWfPUQS410902425082%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1005413%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf23yREhrOV9YczHwt1OUN4&sid=c4b3f6f420352b7e6268dbe166abff7d&tmpl=searchresults&checkin_month=8&checkin_monthday=1&checkin_year=2022&checkout_month=8&checkout_monthday=15&checkout_year=2022&class_interval=1&dest_id=-373226&dest_type=city&dtdisc=0&from_sf=1&group_adults=2&group_children=0&inac=0&index_postcard=0&label_click=undef&no_rooms=1&postcard=0&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=index&src_elem=sb&srpvid=100a6a217ddd014d&ss=Benidorm%2C%20Spain&ss_all=0&ssb=empty&sshis=0&top_ufis=1&sig=v1wBAhUTbD&rows=25&offset=475'

url21 = 'https://www.booking.com/searchresults.html?aid=376376&label=bookings-name-x9XjJRNqhtTGZ30YXWfPUQS410902425082%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp1005413%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Yf23yREhrOV9YczHwt1OUN4&sid=c4b3f6f420352b7e6268dbe166abff7d&tmpl=searchresults&checkin_month=8&checkin_monthday=1&checkin_year=2022&checkout_month=8&checkout_monthday=15&checkout_year=2022&class_interval=1&dest_id=-373226&dest_type=city&from_sf=1&group_adults=2&group_children=0&label_click=undef&no_rooms=1&raw_dest_type=city&room1=A%2CA&sb_price_type=total&search_selected=1&shw_aparth=1&slp_r_match=0&src=index&src_elem=sb&srpvid=60e36a2d8f6d0165&ss=Benidorm%2C%20Spain&ssb=empty&top_ufis=1&sig=v19Nqyg702&rows=25&offset=500'

# Creamos la lista de url
urls = [url1, url2, url3, url4, url5, url6, url7, url8, url9, url10, url11, url12, url13, url14, url15, url16, url17,
        url18, url19, url20, url21]

# Con cada ejecución del script, el nº de resultados defiere.


# Vamos a scrapear los datos: Name(nombre del hotel/apartamento), Stars(nº de estrellas),
# From_Centre(la distancia del centro), From_Beach(la distancia de la playa),
# Reviews(el nº de reviews), Rating, Comfort, Img(link a la imagen) y Price(precio)
# Cada uno de estos valores va a conformar una fila, la cual vamos a guardar en una lista.
# Es decir, cada elemento de la lista será la fila. Después convertiremos esta lista a dataframe,
# utilizando la función pd.DataFrame(list,columns)


# Iniciamos la lista que posteriormente convertiremos en dataframe
res2 = []

# Para cada url de la lista
for u in urls:
    # Creamos bs4
    response = requests.get(u, headers=headers)
    s = BeautifulSoup(response.content, "html.parser")

    # Utilizamos la clase 'sr_property_block' para delimitar los bloques
    for item in s.select(".sr_property_block"):
        # Iniciamos la lista que será la fila
        row = []
        # Vamos rellenando la lista(fila) con los valores
        # Si el nombre del hotel no está vacío, añadimos el nombre a la fila
        if item.select(".sr-hotel__name"):
            for f in item.select(".sr-hotel__name"):
                row.append(f.text.strip())
        # Si está vacío, añadimos 'nan'
        else:
            row.append("nan")
        # Si las Stars(estrellas) no está vacío, añadimos las Stars a la fila
        if item.select(".c-accommodation-classification-rating"):
            for f in item.select(".c-accommodation-classification-rating"):
                row.append(str(f).split('"')[13].strip())
        # De lo contrario, añadimos 'nan'
        else:
            row.append("nan")
        # Si la distancia del centro no está vacío, añadimos la distancia a la fila
        if item.select(".sr_card_address_line__user_destination_address"):
            for f in item.select(".sr_card_address_line__user_destination_address"):
                row.append(f.text.strip())
        # De lo contrario, añadimos 'nan'
        else:
            row.append("nan")
        # Si la distancia de la playa no está vacío, añadimos la distancia a la fila
        if item.select(".beach_team_pilot_distance"):
            for f in item.select(".beach_team_pilot_distance"):
                row.append(f.text.strip())
        # De lo contrario, añadimos 'nan'
        else:
            row.append("nan")
        # Si el número de Reviews no está vacío, añadimos las revistas a la fila
        if item.select(".bui-review-score__text"):
            for f in item.select(".bui-review-score__text"):
                row.append(f.text.strip())
        # De lo contrario, añadimos 'nan'
        else:
            row.append("nan")
        # Si el Ratings no está vacío, añadimos rating a la fila
        if item.select(".bui-review-score__badge"):
            for f in item.select(".bui-review-score__badge"):
                row.append(f.text.strip())
        # De lo contrario, añadimos 'nan'
        else:
            row.append("nan")
        # Si el Comfort no está vacío, añadimos comfort a la fila
        if item.select(".review-score-badge"):
            for f in item.select(".review-score-badge"):
                row.append(f.text.strip())
        # De lo contrario, añadimos 'nan'
        else:
            row.append("nan")
        # Si el link de la imagen no está vacío, añadimos el link a la fila
        if item.select(".hotel_image"):
            for f in item.select(".hotel_image"):
                row.append(str(f).split('"')[7].strip())
        # De lo contrario, añadimos 'nan'
        else:
            row.append("nan")
        # Si el precio no está vacío, añadimos el precio a la fila
        if item.select(".prco-valign-middle-helper"):
            for f in item.select(".prco-valign-middle-helper"):
                row.append(f.text.strip())
        # De lo contrario, añadimos 'nan'
        else:
            row.append("nan")
        # Añadimos la fila a la lista res2
        res2.append(row)
    # Esperamos 2 segundos antes de pasar a la siguiente url
    time.sleep(2)

################# Preprocesamiento del dataframe.##################

# Creamos el dataframe a partir de la lista res2
df = pd.DataFrame(res2, columns=["Name", "Stars", "From_Centre", "From_Beach", "Reviews", "Rating", "Comfort",
                                 "Img", "Price"])

# Stars, sustituimos img por nan
df.loc[df.Stars == 'img', 'Stars'] = 'nan'

# Stars, dejamos sólo valor numérico
df.loc[df.Stars != 'nan', 'Stars'] = df.loc[df.Stars != 'nan', 'Stars'].str.split(" ").str[0]

# Stars np.nan
df.loc[df.Stars == 'nan', 'Stars'] = np.nan

# Stars to_numeric()
df['Stars'] = pd.to_numeric(df['Stars'])

# From_Centre
df.iloc[0:len(df), 2] = df.iloc[0:len(df), 2].str.split(" ").str[0]

# From_Centre to_numeric()
df["From_Centre"] = pd.to_numeric(df["From_Centre"])

# From_Beach asignamos 10 m al valor Beachfront
df.loc[df.From_Beach == "Beachfront", 'From_Beach'] = 10

# From_Beach nos quedamos sólo con el valor numérico
df.loc[df.From_Beach != 'nan', 'From_Beach'] = df.loc[df.From_Beach != 'nan', 'From_Beach'].str.split(" ").str[0]

# From_Beach cambiamos comas por puntos
df['From_Beach'] = [str(x).replace(',', '.') for x in df['From_Beach']]

# From_Beach pasamos 'nan' a np.nan
df.loc[df.From_Beach == 'nan', 'From_Beach'] = np.nan

# From_Beach to numeric
df['From_Beach'] = pd.to_numeric(df['From_Beach'])

# From_Beach pasamos los valores en m a km
df.loc[df.From_Beach > 10, 'From_Beach'] = df.loc[df.From_Beach > 10, 'From_Beach'] / 1000

# Reviews nos quedamos sólo con valores numéricos
df.loc[df.Reviews != 'nan', 'Reviews'] = df.loc[df.Reviews != 'nan', 'Reviews'].str.split(" ").str[0]

# Reviews quitamos los separadores de mil
df['Reviews'] = [x.replace(',', '') for x in df['Reviews']]

# Reviews pasamos 'nan' a np.nan
df.loc[df.Reviews == 'nan', 'Reviews'] = np.nan

# Reviews to_numeric()
df['Reviews'] = pd.to_numeric(df['Reviews'])

# Rating pasamos 'nan' a np.nan
df.loc[df.Rating == 'nan', 'Rating'] = np.nan

# Rating to_numeric()
df['Rating'] = pd.to_numeric(df['Rating'])

# Comfort pasamos 'nan' a np.nan
df.loc[df.Comfort == 'nan', 'Comfort'] = np.nan

# Comfort to_numeric()
df['Comfort'] = pd.to_numeric(df['Comfort'])

# Price nos quedamos sólo con el número
df['Price'] = df.Price.str.split("€").str[1]

# Price sustituimos coma por punto
df['Price'] = [x.replace(',', '.') for x in df['Price']]

# Price podamos los espacios antes y después del valor
df['Price'] = [x.strip() for x in df['Price']]

# Price to_numeric
df['Price'] = pd.to_numeric(df['Price'])

# Price pasamos a miles de eur
df['Price'] = df['Price'] * 1000

# Guardamos el dataframe en formato csv
df.to_csv('booking.csv', sep=';')

print(df.shape)