data = [
    ['0001' , 'Male' , 'Yamada' , 'Tarou' , '25' , 'Tokyo'],
    ['0002' , 'Male' , 'Satou' , 'Takeshi' , '27' , 'Kanagawa'],
    ['0003' , 'Female' , 'Tanaka' , 'Yuko' , '25' , 'Saitama'],
    ['0004' , 'Male' , 'Suzuki' , 'Ichirou' , '35' , 'Hokkaido']
]
data

member_infomation = {}

for record in data:
    key = record[0]
    info = record[1:]
    member_infomation[key] = info

print('number', 'infomation', sep='\t')
for key, info in member_infomation.items():
    print(key, info)
