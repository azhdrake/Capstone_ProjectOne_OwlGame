from owl_traits import owl_dict
from random import randint
from collections import Counter

def make_owl():
    owl = {
        'features' : [],
        'feature_adjs' : [],
        'colors' : [],
        'sounds' : [],
        'sound_adjs' : []
    }
    return owl

mega_owl = make_owl()
nega_owl = make_owl()

def generate_trait(trait_type):
    trait_number = randint(0, len(owl_dict[trait_type])-1)
    return owl_dict[trait_type][trait_number]

def generate_owl():
    owl = {
        'feature' : generate_trait('features'),
        'feature_adj' : generate_trait('adjectives'),
        'color' : generate_trait('colors'),
        'sound' : generate_trait('sounds'),
        'sound_adj' : generate_trait('adjectives')
    }
    return owl

def save_owl(owl, bigger_owl):
    bigger_owl['features'].append(owl['feature'])
    bigger_owl['feature_adjs'].append(owl['feature_adj'])
    bigger_owl['colors'].append(owl['color'])
    bigger_owl['sounds'].append(owl['sound'])
    bigger_owl['sound_adjs'].append(owl['sound_adj'])

def owl_to_string(owl):
    a = 'a '
    if owl['feature'].endswith('s'):
        a = ''

    return 'It has {}{} {} {} and it makes a {} {} sound'.format(a, owl['color'], owl['feature_adj'], owl['feature'], owl['sound_adj'], owl['sound'])

def game_cycle():
    owl = generate_owl()
    user_response = input('\nIs this an owl? \n' + owl_to_string(owl) + '\nRespond \'y\' if I just described an owl, and \'n\' if I described something else. ')
    while user_response != 'y' and user_response != 'Y' and user_response != 'n' and user_response != 'N':
        user_response = input('\nPlease use \'n\' or \'y\' to tell me if I described an owl or not. ')
    if user_response == 'y' or user_response == 'Y':
        save_owl(owl, mega_owl)
        print('Ah... So that\'s what an owl is.\nI will remember this.')
    else:
        save_owl(owl, nega_owl)
        print('Ah... So that\'s what an owl isn\'t\nI will remember this.')

def def_owl(owl):
    an_owl_is = {
        'final_features' : Counter(owl['features']),
        'final_feature_adjs' : Counter(owl['feature_adjs']),
        'final_colors' : Counter(owl['colors']),
        'final_sounds' : Counter(owl['sounds']),
        'final_sound_adjs' : Counter(owl['sound_adjs'])
    }
    return an_owl_is

def compare_owls(final_owl, minor_owl):
    for k, v in final_owl.items():
        v.subtract(minor_owl[k])

def perfect_owl(owl):
    for k, v in owl.items():
        Counter(v).most_common(3)
        owl[k] = dict(v)

def an_owl_is(owl):
    owl_stuff = {}
    for k, v in owl.items():
        owl_stuff[k] = []
        for ke, va in v.items():
            owl_stuff[k].append(ke)
    return 'An owl is {}, {}, and {} and has {}, {}, and {} {}, {}, and {} and it makes {}, {}, and {} sounds that can be described as {}, {}, and {}.'.format(owl_stuff['final_colors'][0], owl_stuff['final_colors'][1], owl_stuff['final_colors'][2], owl_stuff['final_feature_adjs'][0], owl_stuff['final_feature_adjs'][1], owl_stuff['final_feature_adjs'][2], owl_stuff['final_features'][0], owl_stuff['final_features'][1], owl_stuff['final_features'][2], owl_stuff['final_sounds'][0], owl_stuff['final_sounds'][1], owl_stuff['final_sounds'][2], owl_stuff['final_sound_adjs'][0], owl_stuff['final_sound_adjs'][1], owl_stuff['final_sound_adjs'][2])
        
#(*owl_stuff['final_colors'], sep = ', '), (*owl_stuff['final_feature_ads'], sep = ', '), (*owl_stuff['final_features'], sep = ', '), (*owl_stuff['final_sounds'], sep = ', '), (*owl_stuff['final_sound_adjs'], sep = ', ')

cont = ''
while cont != 'n' and cont != 'N' and cont != 'x' and cont != 'X':
    game_cycle()
    cont = input('Press enter to continue or type \'n\' or \'x\' to exit. ')

mega_owl = def_owl(mega_owl)
nega_owl = def_owl(nega_owl)

compare_owls(mega_owl, nega_owl)

perfect_owl(mega_owl)

print(an_owl_is(mega_owl))