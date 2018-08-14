from textwrap import dedent
import sys

done_ordering = False
ORDER = dict()
WIDTH = 72
BANK = [
    {
        'category': 'Appetizers',
        'foods': ['Wings','Bees','Spring Rolls'],
    },
    {
        'category': 'Entrees',
        'foods': ['Fish','Chicken','Sawdust'],
    },
    {
        'category': 'Desserts',
        'foods': ['Ice Cream','Cookies','Cake'],
    },
    {
        'category': 'Drinks',
        'foods': ['Water','Milk','Apple Juice'],
    },
]
FOODS = [
  'Wings','Cookies','Spring Rolls',
  'Fish','Chicken','Sawdust',
  'Ice Cream','Cookies','Cake',
  'Water','Milk','Apple Juice'
]

def greeting():
    """Function which will greet the user when the application executes for
    the first time.
    """
    ln_one = 'Welcome to Snakes Cafe!'
    ln_two = 'Order from our menu options below'
    ln_three = 'To quit at any time, type "quit"'

    print(dedent(f'''
        {'*' * WIDTH}
        {(' ' * ((WIDTH - len(ln_one)) // 2)) + ln_one + (' ' * ((WIDTH - len(ln_one)) // 2))}
        {(' ' * ((WIDTH - len(ln_two)) // 2)) + ln_two + (' ' * ((WIDTH - len(ln_two)) // 2))}
        {(' ' * ((WIDTH - len(ln_three)) // 2)) + ln_three + (' ' * ((WIDTH - len(ln_three)) // 2))}
        {'*' * WIDTH}
    '''))

    for items in BANK:
      print('\n')
      print(items['category'])
      print('-' * len(items['category']))
      for foods in items['foods']:
        print(foods)

def take_order():
    prompting = 'What would you like to order?'
    decor = len(prompting)
    print(dedent(f'''
        {'_' * decor}
        {prompting}
        {'Enter DONE to stop'}
        {'_' * decor}
    '''))  
    user_input = str(input())
    check_input(user_input)

def check_input(order):
  for foods in FOODS:
    if (order == foods):
      if (order in ORDER):
        ORDER[order] += 1
        print(f'{ORDER[order]} orders of {order} added to your meal')
      else:
        ORDER[order] = 1 
        print(f'{ORDER[order]} order of {order} added to your meal')
    elif(order == 'DONE'):
      done_ordering = True
      return done_ordering
      
def run():
    greeting()
    while done_ordering == False:
            take_order()

if __name__ == '__main__':
    run()