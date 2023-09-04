#5.1
empty_lst=list()
print(type(empty_lst))

#5.2
empty_lst=[1,2,3,4,5]

#5.3
print(len(empty_lst))

#5.4
first_item=empty_lst[0]
last_item=empty_lst[-1]
mid_item=empty_lst[2]
print( first_item,'\t',last_item,'\t',mid_item)

#5.5
mixed_data_types=['Lokesh',29,5.9,'Single','Bangalore']

#5.6
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

#5.7
print(it_companies)

#5.8
print(len(it_companies))

#5.9
first_comp=it_companies[0]
mid_comp=it_companies[3]
last_comp=it_companies[-1]
print(first_comp,mid_comp,last_comp)

#5.10
it_companies.append('BOSCH')
print(it_companies)

#5.11
it_companies.append('Intel')
print(it_companies)

#5.12
it_companies.insert(4,'Meta')
print(it_companies)

#5.13***
it_companies[0].upper()
print(it_companies)

#5.14
new_list=['TI','ADI']
it_companies.extend(new_list)
print(it_companies)

#5.15
print('ADI' in it_companies)

#5.16
it_companies.sort()
print(it_companies)

#5.17
it_companies.sort(reverse=True)
print(it_companies)

#5.18
print(it_companies[0:3])

#5.19
print(it_companies[-3:])

#5.20
print(it_companies[6])

#5.21
del it_companies[0]
print(it_companies)

#5.22
del it_companies[6]
print(it_companies)

#5.23
it_companies.pop()
print(it_companies)

#5.24
it_companies.clear()
print(it_companies)

#5.25
del it_companies

#5.26
fron_end=['HTML','CSS','JS','React','Redux']
back_end=['Node','Express','MongoDB']

fron_end.extend(back_end)
print(fron_end)

#5.27
full_stack=fron_end
print(full_stack)

#Exercise:Level 2
ages=[19,22,19,24,20,25,26,24,25,24]
print(min(ages))
print(max(ages))
ages.sort()
print(ages)
print(len(ages))
print(sum(ages))
print(sum(ages)/len(ages))
print(max(ages)-6)

#2.1.1
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

print(abs(len(countries)/2))
print(countries[96])
new_Clist=countries[:96]
new_Clist2=countries[97:]
print(len(new_Clist))
print(len(new_Clist2))

cl=['China','Russia','USA','Finland','Sweden','Norway','Denmark']
first,second,third,*rest=cl
