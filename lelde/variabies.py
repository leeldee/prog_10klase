teksts= 'python'
skaitlis= 5
man_ir_dators= True

saraksts= ['python', 'java', 'c#']
saraksts_ar_skaitliem= [1,2,3,4]

vardnica={
    'vards': 'anna',
    'uzvards':'berzina',
    'vecums': 16

     }





saraksts_ar_vardnicam = [
    {
        'vārds': 'Anna', 
        'uzvārds': 'Bērziņa',
        'vecums': 18
    },
    {
        'vārds': 'Oskars', 
        'uzvārds': 'Bērziņa',
        'vecums': 18
    },
    {
        'vārds': 'Anna', 
        'uzvārds': 'Bērziņa',
        'vecums': 18
    }
]




valoda = 'PHP'

if valoda == 'Python':
    print('Es mācos Python.')
elif valoda == 'Java':
    print('Es mācos Java')
else:
    print('False')



    has_TV = True
has_laptop = False
has_console = False

if has_console and has_TV:
    print('You can play! Good luck!')
elif has_console and not has_TV:
  print('You need a TV')
elif has_TV and not has_console:
  print('You need a console')
elif not has_TV and not has_console:
  print('You need a console and a TV')
else:
  print('Something')

  


has_TV = False
has_laptop = False
has_console = False

if has_console and has_TV:
    print('You can play!')
else:
  print('You can not play')