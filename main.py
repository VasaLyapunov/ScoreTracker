import re


def main(current_scores, html_data):
    _, _, names, scores = html_data.split('<tr')
    print(1, names)
    print(2, scores)

    names = get_html_contents(names)
    scores = get_html_contents(scores, op=lambda x: int(x))
    print(2, scores)
    print(3, names)

    new_scores = dict(zip(names, scores))
    for name in names:
        if name in current_scores:
            current_scores[name] = current_scores[name] + new_scores[name]
        else:
            current_scores[name] = new_scores[name]

    print(current_scores)
    current_scores = sorted(current_scores.items(), key=lambda x: x[1], reverse=True)
    print(current_scores)
    place = 1
    for score in current_scores:
        print('{}. {}: \t{}'.format(place, score[0], score[1]))
        place = place + 1


def get_html_contents(str, op=lambda x: x):
    items = re.findall('(?<=>).*(?=<)', str)
    output_list = [op(x) for x in items]
    return output_list


html_data = '''
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
                        <td id="bottom-inline-score">1</td>
                        <td id="left-inline-score">0</td>
                        <td id="top-inline-score">0</td>
                        <td id="right-inline-score">0</td>
                    </tr>
                </tbody>
'''
current_scores = {
    'Vasa': 117,
    'Sam': 143,
    'Jon': 194,
    'Mike': 170
}
protected_names = ['Vasa', 'Sam', 'Jon']
main(current_scores, html_data)
