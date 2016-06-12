import os
import json
import sys

if len(sys.argv) != 3:
    filename_1 = 'Lesson_5402929278 en.json'
    filename_2 = 'Lesson_5402929278 zh.json'
else:
    filename_1 = sys.argv[1]
    filename_2 = sys.argv[2]

if not os.path.exists(filename_1):
    print 'Error: File %s does not exist.' % filename_1
    sys.exit(1)
if not os.path.exists(filename_2):
    print 'Error: File %s does not exist.' % filename_2
    sys.exit(1)

sequence = []

with open(filename_1, 'r') as f1:
    dict_1 = json.loads(f1.read())

with open(filename_2, 'r') as f2:
    dict_2 = json.loads(f2.read())

base_url = 'https://classroom.udacity.com/nanodegrees/nd009/parts/0091345400/modules/009134540075460/lessons/'
key = dict_1['key']

for i in range(len(dict_1['concepts'])):

    sequence.append('===============')

    concept_1 = dict_1['concepts'][i]
    concept_2 = dict_2['concepts'][i]

    url = base_url + key + '/concepts/' + concept_1['key']

    sequence.append(url)

    sequence.append(concept_1['title'])
    sequence.append(concept_2['title'])

    for j in range(len(concept_1['atoms'])):
        atom_1 = concept_1['atoms'][j]
        atom_2 = concept_2['atoms'][j]

        if atom_1['semantic_type'] == 'VideoAtom':
            if 'instructor_notes' in atom_1 and atom_1['instructor_notes']:
                sequence.append(atom_1['instructor_notes'])
                sequence.append(atom_2['instructor_notes'])
        elif atom_1['semantic_type'] == 'QuizAtom':
            if 'instruction' in atom_1 and atom_1['instruction'] and \
                'text' in atom_1['instruction'] and \
                    atom_1['instruction']['text']:
                sequence.append(atom_1['instruction']['text'])
                sequence.append(atom_2['instruction']['text'])

            if 'instructor_notes' in atom_1 and atom_1['instructor_notes']:
                sequence.append(atom_1['instructor_notes'])
                sequence.append(atom_2['instructor_notes'])

            if 'answer' in atom_1 and atom_1['answer'] and \
                'text' in atom_1['answer'] and \
                    atom_1['answer']['text']:
                sequence.append(atom_1['answer']['text'])
                sequence.append(atom_2['answer']['text'])

        elif atom_1['semantic_type'] == 'TextAtom':
            if 'text' in atom_1 and atom_1['text']:
                sequence.append(atom_1['text'])
                sequence.append(atom_2['text'])

        elif atom_1['semantic_type'] == 'ReflectAtom':
            if 'question' in atom_1 and atom_1['question']:
                sequence.append(atom_1['question']['text'])
                sequence.append(atom_2['question']['text'])
            if 'answer' in atom_1 and atom_1['answer']:
                sequence.append(atom_1['answer']['text'])
                sequence.append(atom_2['answer']['text'])
        else:
            pass

output_sequence = []

for s in sequence:
    if isinstance(s, unicode):
        s = s.encode('utf-8')
    output_sequence.append(s + '\n\n')

output_filename = os.path.splitext(filename_1)[0] + '_output.md'
with open(output_filename, 'w') as of:
    of.writelines(output_sequence)

print 'completed!'
