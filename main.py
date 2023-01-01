import wcag_contrast_ratio as contrast
from colour import Color

def get_colour_rgb(input_prompt):
    while True:
        col = input(input_prompt)
        try:
            col = Color(col)
            return col
        except:
            print('Invalid colour. Try again.')
            pass 

first_colour = get_colour_rgb('Enter first colour hex: ')
second_colour = get_colour_rgb('Enter second colour hex: ')

print('First colour:', first_colour.hex)
print('Second colour:', second_colour.hex)
con = contrast.rgb(first_colour.rgb, second_colour.rgb)
print(f'Contrast ratio: {con:.2f}')
print('AA = minimum recommended compliance, AAA = gold standard')
print('Passes AA (smol text):', contrast.passes_AA(con))
print('Passes AA (lorg text):', contrast.passes_AA(con, large=True))
print('Passes AAA (smol text):', contrast.passes_AAA(con))
print('Passes AAA (lorg text):', contrast.passes_AAA(con, large=True))
