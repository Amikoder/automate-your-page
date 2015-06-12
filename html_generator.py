

def generate_unit_HTML(unit):
    html_text_1 = '''
<div class="unit">
    <h2>
        ''' + unit
    html_text_2 = '''
    </h2>
</div>'''
    
    full_unit_html_text = html_text_1 + html_text_2 
    return full_unit_html_text

def get_unit(text):
    start_location = text.find('UNIT:')
    end_location = text.find('TITLE')
    unit = text[start_location + 6 : end_location - 1]
    return unit

def get_unit_by_number(text, unit_number):
    counter = 0
    while counter < unit_number:
        counter = counter + 1
        next_unit_start = text.find('UNIT:')
        next_unit_end   = text.find('UNIT:', next_unit_start + 1)
        if next_unit_end >= 0:
            unit = text[next_unit_start:next_unit_end]
        else:
            next_unit_end = len(text)
            unit = text[next_unit_start:]
        text = text[next_unit_end:]
    return unit


def generate_unit_html(text):
    current_unit_number = 1
    unit = get_unit_by_number(text, current_unit_number)
    all_unit_html = ''
    while unit != '':
        unit = get_unit(unit)
        unit_html = generate_unit_HTML(unit)
        all_unit_html = all_unit_html + unit_html
        current_unit_number = current_unit_number + 1
        unit = get_unit_by_number(text, current_unit_number)
    return all_unit_html

TEST_TEXT = """UNIT: Two.Five
TITLE: Why Computers are Stupid
NOTES: The phrase "computers are stupid" refers 
to how they interpret instructions literally. This 
means that small typos can cause big problems.
TITLE: Python
NOTES: Python is a "programming language." It 
provides programmers a way to write instructions for a 
computer to execute in a way that the computer can understand.
TITLE: While Loops
NOTES: A while loop repeatedly executes the body of
the loop until the "test condition" is no longer true.
UNIT: Two.Six
TITLE:"""


print get_unit(TEST_TEXT)

print generate_unit_html(TEST_TEXT)










