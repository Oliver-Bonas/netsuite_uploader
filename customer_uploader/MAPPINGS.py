"""
### There are two types of mappings in this file:
1. Value mappings
2. Column mappings

### Value mappings

* status is mapped to an internal id
* subsidiary is mapped to an internal id
* currency is mapped to an internal id
* country is mapped to a value like _unitedStates, which is required by the api


### Column mappings

The column mappings are simpler, they are just mapped to the correct column name required by netsuite
"""
from pprint import pprint

#netsuite = ['_afghanistan', '_alandIslands', '_albania', '_algeria', '_americanSamoa', '_andorra', '_angola', '_anguilla', '_antarctica', '_antiguaAndBarbuda', '_argentina', '_armenia', '_aruba', '_australia', '_austria', '_azerbaijan', '_bahamas', '_bahrain', '_bangladesh', '_barbados', '_belarus', '_belgium', '_belize', '_benin', '_bermuda', '_bhutan', '_bolivia', '_bonaireSaintEustatiusAndSaba', '_bosniaAndHerzegovina', '_botswana', '_bouvetIsland', '_brazil', '_britishIndianOceanTerritory', '_bruneiDarussalam', '_bulgaria', '_burkinaFaso', '_burundi', '_cambodia', '_cameroon', '_canada', '_canaryIslands', '_capeVerde', '_caymanIslands', '_centralAfricanRepublic', '_ceutaAndMelilla', '_chad', '_chile', '_china', '_christmasIsland', '_cocosKeelingIslands', '_colombia', '_comoros', '_congoDemocraticPeoplesRepublic', '_congoRepublicOf', '_cookIslands', '_costaRica', '_coteDIvoire', '_croatiaHrvatska', '_cuba', '_curacao', '_cyprus', '_czechRepublic', '_denmark', '_djibouti', '_dominica', '_dominicanRepublic', '_eastTimor', '_ecuador', '_egypt', '_elSalvador', '_equatorialGuinea', '_eritrea', '_estonia', '_ethiopia', '_falklandIslands', '_faroeIslands', '_fiji', '_finland', '_france', '_frenchGuiana', '_frenchPolynesia', '_frenchSouthernTerritories', '_gabon', '_gambia', '_georgia', '_germany', '_ghana', '_gibraltar', '_greece', '_greenland', '_grenada', '_guadeloupe', '_guam', '_guatemala', '_guernsey', '_guinea', '_guineaBissau', '_guyana', '_haiti', '_heardAndMcDonaldIslands', '_holySeeCityVaticanState', '_honduras', '_hongKong', '_hungary', '_iceland', '_india', '_indonesia', '_iranIslamicRepublicOf', '_iraq', '_ireland', '_isleOfMan', '_israel', '_italy', '_jamaica', '_japan', '_jersey', '_jordan', '_kazakhstan', '_kenya', '_kiribati', '_koreaDemocraticPeoplesRepublic', '_koreaRepublicOf', '_kosovo', '_kuwait', '_kyrgyzstan', '_laoPeoplesDemocraticRepublic', '_latvia', '_lebanon', '_lesotho', '_liberia', '_libya', '_liechtenstein', '_lithuania', '_luxembourg', '_macau', '_macedonia', '_madagascar', '_malawi', '_malaysia', '_maldives', '_mali', '_malta', '_marshallIslands', '_martinique', '_mauritania', '_mauritius', '_mayotte', '_mexico', '_micronesiaFederalStateOf', '_moldovaRepublicOf', '_monaco', '_mongolia', '_montenegro', '_montserrat', '_morocco', '_mozambique', '_myanmar', '_namibia', '_nauru', '_nepal', '_netherlands', '_newCaledonia', '_newZealand', '_nicaragua', '_niger', '_nigeria', '_niue', '_norfolkIsland', '_northernMarianaIslands', '_norway', '_oman', '_pakistan', '_palau', '_panama', '_papuaNewGuinea', '_paraguay', '_peru', '_philippines', '_pitcairnIsland', '_poland', '_portugal', '_puertoRico', '_qatar', '_reunionIsland', '_romania', '_russianFederation', '_rwanda', '_saintBarthelemy', '_saintHelena', '_saintKittsAndNevis', '_saintLucia', '_saintMartin', '_saintVincentAndTheGrenadines', '_samoa', '_sanMarino', '_saoTomeAndPrincipe', '_saudiArabia', '_senegal', '_serbia', '_seychelles', '_sierraLeone', '_singapore', '_sintMaarten', '_slovakRepublic', '_slovenia', '_solomonIslands', '_somalia', '_southAfrica', '_southGeorgia', '_southSudan', '_spain', '_sriLanka', '_stPierreAndMiquelon', '_stateOfPalestine', '_sudan', '_suriname', '_svalbardAndJanMayenIslands', '_swaziland', '_sweden', '_switzerland', '_syrianArabRepublic', '_taiwan', '_tajikistan', '_tanzania', '_thailand', '_togo', '_tokelau', '_tonga', '_trinidadAndTobago', '_tunisia', '_turkey', '_turkmenistan', '_turksAndCaicosIslands', '_tuvalu', '_uSMinorOutlyingIslands', '_uganda', '_ukraine', '_unitedArabEmirates', '_unitedKingdom', '_unitedStates', '_uruguay', '_uzbekistan', '_vanuatu', '_venezuela', '_vietnam', '_virginIslandsBritish', '_virginIslandsUSA', '_wallisAndFutunaIslands', '_westernSahara', '_yemen', '_zambia', '_zimbabwe']
oliverbonas = ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Virgin Islands', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Hong Kong, SAR China', 'Macao, SAR China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo\xa0(Brazzaville)', 'Congo, (Kinshasa)', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard and Mcdonald Islands', 'Holy See\xa0(Vatican City State)', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea\xa0(North)', 'Korea\xa0(South)', 'Kuwait', 'Kyrgyzstan', 'Lao PDR', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'Netherlands Antilles', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint-Barthélemy', 'Saint Helena', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint-Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Svalbard and Jan Mayen Islands', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic\xa0(Syria)', 'Taiwan, Republic of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States of America', 'US Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela\xa0(Bolivarian Republic)', 'Viet Nam', 'Virgin Islands, US', 'Wallis and Futuna Islands', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']

# todo: netherlands antillies is not a recognised country in netsuite

COUNTRY_VALUE_MAP = {
 'Afghanistan': '_afghanistan',
 'Aland Islands': '_alandIslands',
 'Albania': '_albania',
 'Algeria': '_algeria',
 'American Samoa': '_americanSamoa',
 'Andorra': '_andorra',
 'Angola': '_angola',
 'Anguilla': '_anguilla',
 'Antarctica': '_antarctica',
 'Antigua and Barbuda': '_antiguaAndBarbuda',
 'Argentina': '_argentina',
 'Armenia': '_armenia',
 'Aruba': '_aruba',
 'Australia': '_australia',
 'Austria': '_austria',
 'Azerbaijan': '_azerbaijan',
 'Bahamas': '_bahamas',
 'Bahrain': '_bahrain',
 'Bangladesh': '_bangladesh',
 'Barbados': '_barbados',
 'Belarus': '_belarus',
 'Belgium': '_belgium',
 'Belize': '_belize',
 'Benin': '_benin',
 'Bermuda': '_bermuda',
 'Bhutan': '_bhutan',
 'Bolivia': '_bolivia',
 'Bosnia and Herzegovina': '_bosniaAndHerzegovina',
 'Botswana': '_botswana',
 'Bouvet Island': '_bouvetIsland',
 'Brazil': '_brazil',
 'British Indian Ocean Territory': '_britishIndianOceanTerritory',
 'British Virgin Islands': '_virginIslandsBritish',
 'Brunei Darussalam': '_bruneiDarussalam',
 'Bulgaria': '_bulgaria',
 'Burkina Faso': '_burkinaFaso',
 'Burundi': '_burundi',
 'Cambodia': '_cambodia',
 'Cameroon': '_cameroon',
 'Canada': '_canada',
 'Cape Verde': '_capeVerde',
 'Cayman Islands': '_caymanIslands',
 'Central African Republic': '_centralAfricanRepublic',
 'Chad': '_chad',
 'Chile': '_chile',
 'China': '_china',
 'Christmas Island': '_christmasIsland',
 'Cocos (Keeling) Islands': '_cocosKeelingIslands',
 'Colombia': '_colombia',
 'Comoros': '_comoros',
 'Congo (Brazzaville)': '_congoRepublicOf',
 'Congo, (Kinshasa)': '_congoDemocraticPeoplesRepublic',
 'Cook Islands': '_cookIslands',
 'Costa Rica': '_costaRica',
 'Croatia': '_croatiaHrvatska',
 'Cuba': '_cuba',
 'Cyprus': '_cyprus',
 'Czech Republic': '_czechRepublic',
 "Côte d'Ivoire": '_coteDIvoire',
 'Denmark': '_denmark',
 'Djibouti': '_djibouti',
 'Dominica': '_dominica',
 'Dominican Republic': '_dominicanRepublic',
 'Ecuador': '_ecuador',
 'Egypt': '_egypt',
 'El Salvador': '_elSalvador',
 'Equatorial Guinea': '_equatorialGuinea',
 'Eritrea': '_eritrea',
 'Estonia': '_estonia',
 'Ethiopia': '_ethiopia',
 'Falkland Islands (Malvinas)': '_falklandIslands',
 'Faroe Islands': '_faroeIslands',
 'Fiji': '_fiji',
 'Finland': '_finland',
 'France': '_france',
 'French Guiana': '_frenchGuiana',
 'French Polynesia': '_frenchPolynesia',
 'French Southern Territories': '_frenchSouthernTerritories',
 'Gabon': '_gabon',
 'Gambia': '_gambia',
 'Georgia': '_georgia',
 'Germany': '_germany',
 'Ghana': '_ghana',
 'Gibraltar': '_gibraltar',
 'Greece': '_greece',
 'Greenland': '_greenland',
 'Grenada': '_grenada',
 'Guadeloupe': '_guadeloupe',
 'Guam': '_guam',
 'Guatemala': '_guatemala',
 'Guernsey': '_guernsey',
 'Guinea': '_guinea',
 'Guinea-Bissau': '_guineaBissau',
 'Guyana': '_guyana',
 'Haiti': '_haiti',
 'Heard and Mcdonald Islands': '_heardAndMcDonaldIslands',
 'Holy See (Vatican City State)': '_holySeeCityVaticanState',
 'Honduras': '_honduras',
 'Hong Kong, SAR China': '_hongKong',
 'Hungary': '_hungary',
 'Iceland': '_iceland',
 'India': '_india',
 'Indonesia': '_indonesia',
 'Iran, Islamic Republic of': '_iranIslamicRepublicOf',
 'Iraq': '_iraq',
 'Ireland': '_ireland',
 'Isle of Man': '_isleOfMan',
 'Israel': '_israel',
 'Italy': '_italy',
 'Jamaica': '_jamaica',
 'Japan': '_japan',
 'Jersey': '_jersey',
 'Jordan': '_jordan',
 'Kazakhstan': '_kazakhstan',
 'Kenya': '_kenya',
 'Kiribati': '_kiribati',
 'Korea (North)': '_koreaDemocraticPeoplesRepublic',
 'Korea (South)': '_koreaRepublicOf',
 'Kuwait': '_kuwait',
 'Kyrgyzstan': '_kyrgyzstan',
 'Lao PDR': '_laoPeoplesDemocraticRepublic',
 'Latvia': '_latvia',
 'Lebanon': '_lebanon',
 'Lesotho': '_lesotho',
 'Liberia': '_liberia',
 'Libya': '_libya',
 'Liechtenstein': '_liechtenstein',
 'Lithuania': '_lithuania',
 'Luxembourg': '_luxembourg',
 'Macao, SAR China': '_macau',
 'Macedonia, Republic of': '_macedonia',
 'Madagascar': '_madagascar',
 'Malawi': '_malawi',
 'Malaysia': '_malaysia',
 'Maldives': '_maldives',
 'Mali': '_mali',
 'Malta': '_malta',
 'Marshall Islands': '_marshallIslands',
 'Martinique': '_martinique',
 'Mauritania': '_mauritania',
 'Mauritius': '_mauritius',
 'Mayotte': '_mayotte',
 'Mexico': '_mexico',
 'Micronesia, Federated States of': '_micronesiaFederalStateOf',
 'Moldova': '_moldovaRepublicOf',
 'Monaco': '_monaco',
 'Mongolia': '_mongolia',
 'Montenegro': '_montenegro',
 'Montserrat': '_montserrat',
 'Morocco': '_morocco',
 'Mozambique': '_mozambique',
 'Myanmar': '_myanmar',
 'Namibia': '_namibia',
 'Nauru': '_nauru',
 'Nepal': '_nepal',
 'Netherlands': '_netherlands',
 'New Caledonia': '_newCaledonia',
 'New Zealand': '_newZealand',
 'Nicaragua': '_nicaragua',
 'Niger': '_niger',
 'Nigeria': '_nigeria',
 'Niue': '_niue',
 'Norfolk Island': '_norfolkIsland',
 'Northern Mariana Islands': '_northernMarianaIslands',
 'Norway': '_norway',
 'Oman': '_oman',
 'Pakistan': '_pakistan',
 'Palau': '_palau',
 'Palestinian Territory': '_stateOfPalestine',
 'Panama': '_panama',
 'Papua New Guinea': '_papuaNewGuinea',
 'Paraguay': '_paraguay',
 'Peru': '_peru',
 'Philippines': '_philippines',
 'Pitcairn': '_pitcairnIsland',
 'Poland': '_poland',
 'Portugal': '_portugal',
 'Puerto Rico': '_puertoRico',
 'Qatar': '_qatar',
 'Romania': '_romania',
 'Russian Federation': '_russianFederation',
 'Rwanda': '_rwanda',
 'Réunion': '_reunionIsland',
 'Saint Helena': '_saintHelena',
 'Saint Kitts and Nevis': '_saintKittsAndNevis',
 'Saint Lucia': '_saintLucia',
 'Saint Pierre and Miquelon': '_stPierreAndMiquelon',
 'Saint Vincent and Grenadines': '_saintVincentAndTheGrenadines',
 'Saint-Barthélemy': '_saintBarthelemy',
 'Saint-Martin (French part)': '_saintMartin',
 'Samoa': '_samoa',
 'San Marino': '_sanMarino',
 'Sao Tome and Principe': '_saoTomeAndPrincipe',
 'Saudi Arabia': '_saudiArabia',
 'Senegal': '_senegal',
 'Serbia': '_serbia',
 'Seychelles': '_seychelles',
 'Sierra Leone': '_sierraLeone',
 'Singapore': '_singapore',
 'Slovakia': '_slovakRepublic',
 'Slovenia': '_slovenia',
 'Solomon Islands': '_solomonIslands',
 'Somalia': '_somalia',
 'South Africa': '_southAfrica',
 'South Georgia and the South Sandwich Islands': '_southGeorgia',
 'South Sudan': '_southSudan',
 'Spain': '_spain',
 'Sri Lanka': '_sriLanka',
 'Sudan': '_sudan',
 'Suriname': '_suriname',
 'Svalbard and Jan Mayen Islands': '_svalbardAndJanMayenIslands',
 'Swaziland': '_swaziland',
 'Sweden': '_sweden',
 'Switzerland': '_switzerland',
 'Syrian Arab Republic (Syria)': '_syrianArabRepublic',
 'Taiwan, Republic of China': '_taiwan',
 'Tajikistan': '_tajikistan',
 'Tanzania, United Republic of': '_tanzania',
 'Thailand': '_thailand',
 'Timor-Leste': '_eastTimor',
 'Togo': '_togo',
 'Tokelau': '_tokelau',
 'Tonga': '_tonga',
 'Trinidad and Tobago': '_trinidadAndTobago',
 'Tunisia': '_tunisia',
 'Turkey': '_turkey',
 'Turkmenistan': '_turkmenistan',
 'Turks and Caicos Islands': '_turksAndCaicosIslands',
 'Tuvalu': '_tuvalu',
 'US Minor Outlying Islands': '_uSMinorOutlyingIslands',
 'Uganda': '_uganda',
 'Ukraine': '_ukraine',
 'United Arab Emirates': '_unitedArabEmirates',
 'United Kingdom': '_unitedKingdom',
 'United States of America': '_unitedStates',
 'Uruguay': '_uruguay',
 'Uzbekistan': '_uzbekistan',
 'Vanuatu': '_vanuatu',
 'Venezuela (Bolivarian Republic)': '_venezuela',
 'Viet Nam': '_vietnam',
 'Virgin Islands, US': '_virginIslandsUSA',
 'Wallis and Futuna Islands': '_wallisAndFutunaIslands',
 'Western Sahara': '_westernSahara',
 'Yemen': '_yemen',
 'Zambia': '_zambia',
 'Zimbabwe': '_zimbabwe'
}

STATUS_VALUE_MAP_CSV = {
    "CustomER-Closed Won": "Closed Won",
}

STATUS_VALUE_MAP = {
    'Closed Lost': {'internalId': 14},
    'Closed Won': {'internalId': 13},
    'Identified Decision Makers': {'internalId': 9},
    'In Discussion': {'internalId': 8},
    'In Negotiation': {'internalId': 11},
    'Lost Customer': {'internalId': 16},
    'Proposal': {'internalId': 10},
    'Purchasing': {'internalId': 12},
    'Qualified': {'internalId': 7},
    'Renewal': {'internalId': 15},
    'Unqualified': {'internalId': 6}
}

CURRENCY_VALUE_MAP = {
    'AUD': {'internalId': 14},
    'CAD': {'internalId': 3},
    'Chinese RMB': {'internalId': 5},
    'DKK': {'internalId': 6},
    'EUR': {'internalId': 4},
    'GBP': {'internalId': 1},
    'Hong Kong Dollar': {'internalId': 7},
    'Indian Rupees': {'internalId': 8},
    'Japanese Yen': {'internalId': 9},
    'Korean Wong': {'internalId': 10},
    'Philippine Pesos': {'internalId': 11},
    'Thai Bhat': {'internalId': 12},
    'Turkish Lira': {'internalId': 13},
    'USD': {'internalId': 2}
}

SUBSIDIARY_VALUE_MAP_CSV = {
    "Parent Company": "Oliver Bonas Limited",
}

SUBSIDIARY_VALUE_MAP = {
    'Elimination Subsidiary': {'internalId': 5},
    'Oliver Bonas (Holding)': {'internalId': 1},
    'Oliver Bonas (Ireland) Limited': {'internalId': 4},
    'Oliver Bonas Limited': {'internalId': 2}
}

COLUMN_MAPPING = {
    "status": "entityStatus",
}

COLUMN_MAPPING_ADDRESS_BOOK = {
    "Address1_AddressName": "label",
    'Address1_defaultBillTo': "defaultBilling",
    'Address1_defaultShipTo': "defaultShipping",
    ################################# same for address2
    "Address2_AddressName": "label",
    'Address2_defaultBillTo':"defaultBilling",
    'Address2_defaultShipTo':"defaultShipping",
}

COLUMN_MAPPING_ADDRESS = {
    'Address1_attention':"attention",
    'Address1_phone':"addrPhone",
    'Address1_line1':"addr1",
    'Address1_city':"city",
    'Address1_state':"state",
    'Address1_zipCode':"zip",
    'Address1_country':"country",
    ################################# same for address2
    'Address2_attention':"attention",
    'Address2_phone':"addrPhone",
    'Address2_line1':"addr1",
    'Address2_city':"city",
    'Address2_state':"state",
    'Address2_zipCode':"zip",
    'Address2_country':"country",
}