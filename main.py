import re


def main(current_scores, html_data, protected_names, merge_ai=True):
    _, _, names, scores = html_data.split('<tr')
    names = get_html_contents(names)
    scores = get_html_contents(scores, op=lambda x: int(x))

    new_scores = dict(zip(names, scores))
    for name in names:
        if name in current_scores:
            current_scores[name] = current_scores[name] + new_scores[name]
        else:
            current_scores[name] = new_scores[name]

    # Combine all non-protected names into one overall AI score
    if merge_ai:
        current_scores = merge_ai_scores(current_scores, protected_names)

    current_scores = sorted(current_scores.items(), key=lambda x: x[1])
    print_scores(current_scores)


# Given HTML data grabbed off of a table of scores, extract data into a list
def get_html_contents(str, op=lambda x: x):
    items = re.findall('(?<=>).*(?=<)', str)
    output_list = [op(x) for x in items]
    return output_list


def merge_ai_scores(scores, protected_names):
    protected_names.append('AI')
    new_scores = {'AI': 0}
    for k, v in scores.items():
        if k not in protected_names:
            new_scores['AI'] = new_scores['AI'] + scores[k]
        else:
            new_scores[k] = scores[k]
    return new_scores


# Print formatted scores, given a list of tuples
def print_scores(scores):

    max_len = 0
    for data in scores:
        max_len = max(max_len, len(data[0]))

    place = 1
    for data in scores:
        name = data[0]
        score = data[1]
        print('{}. {}: {}{}'.format(place, name, ' '*(max_len - len(name)), score))
        place = place + 1


_html_data = '''
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
_current_scores = {
    'Vasa': 117,
    'Sam': 143,
    'Jon': 194,
    'Mike': 170
}
_protected_names = ['Vasa', 'Sam', 'Jon']
main(_current_scores, _html_data, _protected_names)
