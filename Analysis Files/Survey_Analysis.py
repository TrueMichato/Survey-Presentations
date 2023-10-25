import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio


IDEAS = ['Prestige Classes', 'Effect of Aging', 'Weapons Reworked',
       'Skill Based Bonus Actions', 'Multiclassing Overhaul',
       'Cross Breeding ( aka \'Half Races\')', 'Warlock - Dragon Patron',
       'Paladin - Oath of Inquisition', 'Sorcerer - Devil',
       'Warlock - Beholder Patron', 'Paladin - Oath of Corrosion',
       'Monk - Way of Five Animals', 'Paladin - Oath of Bastion',
       'Wizard - School of Smoke', 'Sorcerer - Fey',
       'Barbarian - Path of the Spellshield', 'Rogue - Trickster',
       'Sorcerer - Heroic Soul', 'Rogue - Acrobat']
FEATURES = ['Intresting', 'Special / Original', 'Fun', 'Include in our Game', 'Depth', 'Background Image']

df = pd.read_csv('Data Files/Homebrew Survey #1/Homebrew Ideas Survey (Responses).csv')
# prediction_df = pd.DataFrame()
# for idea in IDEAS:
#     temp_df = df[[col for col in df.columns if idea in col]]
#     temp_df.columns = [col.replace(f'{idea} - ', '') for col in temp_df.columns]
#     temp_df.insert(0, 'Idea', idea)
#     prediction_df = pd.concat([prediction_df, temp_df])
# print(prediction_df.corr())
# prediction_df.to_csv('Data Files/Homebrew Survey #1/clear_ideas_data.csv')


score_df = pd.DataFrame()
for title in FEATURES:
    temp_df = df[[col for col in df.columns if title in col]]
    temp_df.columns = [col.replace(f' - {title}', '') for col in temp_df.columns]
    if title in ['Fun', 'Include in our Game']:
        for col in temp_df.columns:
            if any(val in temp_df[f'{col}'].values for val in [1 ,2]):
                num = sum([val in temp_df[f'{col}'].values for val in [1 ,2]])
                print(f"Got {num} case{'s' if num > 1 else ''} of "
                      f"really low '{title}' score in {col}")
    data_df = temp_df.mean().sort_values().to_frame("means")
    data_df['stdv'] = temp_df.std()
    data_df['score'] = data_df.means - data_df.stdv
    data_df['score'] = data_df.score / data_df.score.sum() * 100
    fig1 = px.bar(data_df, x=data_df.index.to_numpy(), y="means", color="means", error_y="stdv", text_auto='.3s',
           labels=data_df.index.to_numpy(),
           title=f"{title} - Average Rating with error bars")
    fig1.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    # fig1.show()
    fig1.write_image(f"Presentation Files/Hombrew Presentation 1/Plots/{title if '/' not in title else title.replace('/', 'or')} Average Rating with error bars.webp")
    data_df.sort_values(by='score', inplace=True)
    fig2 = px.bar(data_df, x=data_df.index.to_numpy(),  y="score", color="score", text_auto='.3s',
           labels=data_df.index.to_numpy(),
           title=f"{title} - Normalized Score")
    fig2.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    # fig2.show()
    fig2.write_image(f"Presentation Files/Hombrew Presentation 1/Plots/{title if '/' not in title else title.replace('/', 'or')} Normalized Score.webp")
    if score_df.index.empty:
        score_df.index = data_df.index
    score_df[title] = data_df.score

formula_A = {"Include": 1, "Fun": 0.9, "Depth": 0.7, "Intresting": 0.5, "Special": 0.3}
formula_B = {"Include": 1, "Fun": 0.9, "Depth": 0.7, "Intresting": 0.5, "Special": 0.2}
formula_C = {"Include": 1, "Fun": 0.9, "Depth": 0.7, "Intresting": 0.5, "Special": 0.1}
formula_D = {"Include": 1, "Fun": 0.9, "Depth": 0.7, "Intresting": 0.5, "Special": 0}



formula_list = [formula_A, formula_B, formula_C, formula_D]

for i, formula in enumerate(formula_list):
    title = f"{formula['Include']} * 'Include in our Game' + {formula['Fun']} * Fun + {formula['Depth']} * Depth <br> + {formula['Intresting']} * Intresting + {formula['Special']} * 'Special / Original'"
    score_df['final_score'] = score_df.apply(lambda r: formula['Include'] * r['Include in our Game'] +
                                                       formula['Fun'] * r.Fun + formula['Depth'] * r.Depth +
                                                       formula['Intresting'] * r.Intresting +
                                                       formula['Special'] * r['Special / Original'], axis=1)
    score_df['final_score'] = score_df.final_score / score_df.final_score.sum() * 100
    score_df.sort_values(by='final_score', inplace=True)
    fig = px.bar(score_df, x=score_df.index.to_numpy(), y="final_score", color="final_score", text_auto='.3s',
               labels=score_df.index.to_numpy(),
               title=f"Final Scores, formula is '{title}'")
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False)
    # fig.show()
    fig.write_image(f"Presentation Files/Hombrew Presentation 1/Plots/Final_Formula_{i}.webp")




# df_interest = df[[col for col in df.columns if 'Intresting' in col]]
# df_special = df[[col for col in df.columns if 'Special' in col]]
# df_fun = df[[col for col in df.columns if 'Fun' in col]]
# df_game_includement = df[[col for col in df.columns if 'Game' in col]]
# df_depth = df[[col for col in df.columns if 'Depth' in col]]
# df_image = df[[col for col in df.columns if 'Image' in col]]




