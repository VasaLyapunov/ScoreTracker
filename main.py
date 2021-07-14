import re
input = '''
<tr>
                        <td id="bottom-inline-score">4</td>
                        <td id="left-inline-score">24</td>
                        <td id="top-inline-score">23</td>
                        <td id="right-inline-score">27</td>
                    </tr>
'''
input = input.split('/')
l = []
j = 0
for i in input:
    a = 'lkdfhisoe78347834 (())&/&745  '
    result = re.sub('[^0-9]','', i)
    numb = int(result)
    if j==0:
        numb = numb + 113
    if j==1:
        numb = numb + 119
    if j==2:
        numb = numb + 147
    if j==3:
        numb = numb + 167
    l.append(numb)
    j = j+1
    if j==4:
        break

people = ['vasa','sam','mike','jon']

for i in range(4):
    print(people[i], l[i])