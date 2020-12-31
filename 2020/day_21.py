from collections import defaultdict
import copy


def load_input(filename):
    z = defaultdict(list)
    i, a = [], []
    for line in open(filename).readlines():
        ingredients, allergies = line.strip().split(' (contains ')
        allergies = allergies[:-1]
        ingredients = ingredients.split()
        allergies = allergies.split(', ')
        i.append(ingredients)
        a.append(allergies)
    return i, a


def get_allergy_set(allergies):
    all_allergies = set()
    for i in allergies:
        for j in i:
            all_allergies.add(j)
    return all_allergies


def get_ingredients_list(ingredients):
    all_individual_ingredients = []
    for i in ingredients:
        for j in i:
            all_individual_ingredients.append(j)
    all_ingredients = set(all_individual_ingredients)
    return all_individual_ingredients, all_ingredients


def get_allergy_intersections(ingredients, allergies, all_allergies):
    intersections = {}
    for a_all in all_allergies:
        temp = []
        for i, a in zip(ingredients, allergies):
            if a_all in a:
                temp.append(set(i))
        # get intersection of lists in temp
        intersections[a_all] = temp[0].intersection(*temp)
    return intersections


def get_intersections_by_ingredient(intersections, all_ingredients):
    intersections_by_ingredient = defaultdict(list)
    for ingredient in all_ingredients:
        for a, i in intersections.items():
            if ingredient in i:
                intersections_by_ingredient[ingredient].append(a)
    return intersections_by_ingredient


def get_no_allergen_ingredients(all_ingredients, intersections_by_ingredient):
    return set(all_ingredients).difference(set(intersections_by_ingredient.keys()))


def get_allergens(intersections_by_ingredient):
    allergens = {}
    while len(intersections_by_ingredient.keys()) > 0:
        intersections_by_ingredient_temp = copy.deepcopy(intersections_by_ingredient)
        for i, a in intersections_by_ingredient_temp.items():
            if len(a) == 1:
                allergens[i] = a[0]
                del intersections_by_ingredient[i]
                for i1, a1 in intersections_by_ingredient.items():
                    if a[0] in a1:
                        intersections_by_ingredient[i1].remove(a[0])
                break
    return allergens

if __name__ == '__main__':
    filename = 'day_21.txt'
    ingredients, allergies = load_input(filename)
    all_allergies = get_allergy_set(allergies)
    all_individual_ingredients, all_ingredients = get_ingredients_list(ingredients)
    intersections = get_allergy_intersections(ingredients, allergies, all_allergies)
    intersections_by_ingredient = get_intersections_by_ingredient(intersections, all_ingredients)
    no_allergen_ingredients = get_no_allergen_ingredients(all_ingredients, intersections_by_ingredient)

    answer = 0
    for i in no_allergen_ingredients:
        answer += all_individual_ingredients.count(i)

    print('\nAnswer part 1:', answer)

    # part 2
    allergens = get_allergens(intersections_by_ingredient)

    # List alphabetically by allergen
    allergens_by_allergy = {}
    for i, a in allergens.items():
        allergens_by_allergy[a] = i

    answer_part2 = []
    for entry in sorted(allergens_by_allergy.items(), key = lambda x: x[0], reverse=False):
        answer_part2.append(entry[1])

    print('\nAnswer part 2:')
    print(','.join(answer_part2))