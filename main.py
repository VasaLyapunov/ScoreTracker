import re

input = '''
<tbody>
                    <tr>
                        <th colspan="4">Total game score</th>
                    </tr>
                    <tr class="names-row">
                        <th class="bottom-player-name">Vasa</th>
                        <th class="left-player-name">Mike</th>
                        <th class="top-player-name">Bill</th>
                        <th class="right-player-name">Lisa</th>
                    </tr>
                    <tr>
                        <td id="bottom-inline-score">0</td>
                        <td id="left-inline-score">0</td>
                        <td id="top-inline-score">0</td>
                        <td id="right-inline-score">0</td>
                    </tr>
                </tbody>
'''
def main():
    _, _, names, scores = input.split('<tr')
    print(1,names)
    print(2,scores)

    names = getHTMLContents(names)
    scores = getHTMLContents(scores, op=lambda x: int(x))
    print(2,scores)
    print(3,names)

def getHTMLContents(str, op=lambda x: x):
    items = re.findall('(?<=>).*(?=<)', str)
    output_list = [op(x) for x in items]
    return output_list

main()
'''
input = input.split('/')
l = []
j = 0
for i in input:
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
'''