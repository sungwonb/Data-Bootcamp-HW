
# Heroes of Pymoli Data Analysis

### Observed Trends
1. 64.71% of all players are between the ages of 15 and 24 (63.17% of all purchases came from this age group)
1. Thus, the majority of active buyers are in their late teens to mid twenties. 
2. Popular games are not necessarily the most profitable.
3. Arcane Gem, however, is both profitable and popular (ranking 1st in popular and 5th in profitable).
4. A significant majority of players are males (88.8%). 


```python
#Dependencies
import pandas as pd
```


```python
#Import json files
jsonpath = '../USCLOS201710DATA5-Class-Repository-DATA-master-29e7262cebcc6bf323c4d2103b21632da16f324c/Pandas/Homework Instructions/Instructions/HeroesOfPymoli/purchase_data.json'
jsonpath2 = '../USCLOS201710DATA5-Class-Repository-DATA-master-29e7262cebcc6bf323c4d2103b21632da16f324c/Pandas/Homework Instructions/Instructions/HeroesOfPymoli/purchase_data2.json'

pd_df = pd.read_json(jsonpath)
pd_df2 = pd.read_json(jsonpath2)

pd_df = pd_df.append(pd_df2)
pd_df = pd_df.reset_index().drop("index",1)
pd_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Aela59</td>
    </tr>
    <tr>
      <th>5</th>
      <td>20</td>
      <td>Male</td>
      <td>10</td>
      <td>Sleepwalker</td>
      <td>1.73</td>
      <td>Tanimnya91</td>
    </tr>
    <tr>
      <th>6</th>
      <td>20</td>
      <td>Male</td>
      <td>153</td>
      <td>Mercenary Sabre</td>
      <td>4.57</td>
      <td>Undjaskla97</td>
    </tr>
    <tr>
      <th>7</th>
      <td>29</td>
      <td>Female</td>
      <td>169</td>
      <td>Interrogator, Blood Blade of the Queen</td>
      <td>3.32</td>
      <td>Iathenudil29</td>
    </tr>
    <tr>
      <th>8</th>
      <td>25</td>
      <td>Male</td>
      <td>118</td>
      <td>Ghost Reaver, Longsword of Magic</td>
      <td>2.77</td>
      <td>Sondenasta63</td>
    </tr>
    <tr>
      <th>9</th>
      <td>31</td>
      <td>Male</td>
      <td>99</td>
      <td>Expiration, Warscythe Of Lost Worlds</td>
      <td>4.53</td>
      <td>Hilaerin92</td>
    </tr>
    <tr>
      <th>10</th>
      <td>24</td>
      <td>Male</td>
      <td>57</td>
      <td>Despair, Favor of Due Diligence</td>
      <td>3.81</td>
      <td>Chamosia29</td>
    </tr>
    <tr>
      <th>11</th>
      <td>20</td>
      <td>Male</td>
      <td>47</td>
      <td>Alpha, Reach of Ending Hope</td>
      <td>1.55</td>
      <td>Sally64</td>
    </tr>
    <tr>
      <th>12</th>
      <td>30</td>
      <td>Male</td>
      <td>81</td>
      <td>Dreamkiss</td>
      <td>4.06</td>
      <td>Iskossa88</td>
    </tr>
    <tr>
      <th>13</th>
      <td>23</td>
      <td>Male</td>
      <td>77</td>
      <td>Piety, Guardian of Riddles</td>
      <td>3.68</td>
      <td>Seorithstilis90</td>
    </tr>
    <tr>
      <th>14</th>
      <td>40</td>
      <td>Male</td>
      <td>44</td>
      <td>Bonecarvin Battle Axe</td>
      <td>2.46</td>
      <td>Sundast29</td>
    </tr>
    <tr>
      <th>15</th>
      <td>21</td>
      <td>Male</td>
      <td>96</td>
      <td>Blood-Forged Skeletal Spine</td>
      <td>4.77</td>
      <td>Haellysu29</td>
    </tr>
    <tr>
      <th>16</th>
      <td>22</td>
      <td>Female</td>
      <td>123</td>
      <td>Twilight's Carver</td>
      <td>1.14</td>
      <td>Sundista85</td>
    </tr>
    <tr>
      <th>17</th>
      <td>22</td>
      <td>Female</td>
      <td>59</td>
      <td>Lightning, Etcher of the King</td>
      <td>1.65</td>
      <td>Aenarap34</td>
    </tr>
    <tr>
      <th>18</th>
      <td>28</td>
      <td>Male</td>
      <td>91</td>
      <td>Celeste</td>
      <td>3.71</td>
      <td>Iskista88</td>
    </tr>
    <tr>
      <th>19</th>
      <td>31</td>
      <td>Male</td>
      <td>177</td>
      <td>Winterthorn, Defender of Shifting Worlds</td>
      <td>4.89</td>
      <td>Assossa43</td>
    </tr>
    <tr>
      <th>20</th>
      <td>24</td>
      <td>Male</td>
      <td>78</td>
      <td>Glimmer, Ender of the Moon</td>
      <td>2.33</td>
      <td>Irith83</td>
    </tr>
    <tr>
      <th>21</th>
      <td>15</td>
      <td>Male</td>
      <td>3</td>
      <td>Phantomlight</td>
      <td>1.79</td>
      <td>Iaralrgue74</td>
    </tr>
    <tr>
      <th>22</th>
      <td>11</td>
      <td>Female</td>
      <td>11</td>
      <td>Brimstone</td>
      <td>2.52</td>
      <td>Deural48</td>
    </tr>
    <tr>
      <th>23</th>
      <td>19</td>
      <td>Male</td>
      <td>183</td>
      <td>Dragon's Greatsword</td>
      <td>2.36</td>
      <td>Chanosia65</td>
    </tr>
    <tr>
      <th>24</th>
      <td>11</td>
      <td>Male</td>
      <td>65</td>
      <td>Conqueror Adamantite Mace</td>
      <td>1.96</td>
      <td>Qarwen67</td>
    </tr>
    <tr>
      <th>25</th>
      <td>21</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>1.27</td>
      <td>Idai61</td>
    </tr>
    <tr>
      <th>26</th>
      <td>29</td>
      <td>Male</td>
      <td>132</td>
      <td>Persuasion</td>
      <td>3.90</td>
      <td>Aerithllora36</td>
    </tr>
    <tr>
      <th>27</th>
      <td>34</td>
      <td>Male</td>
      <td>106</td>
      <td>Crying Steel Sickle</td>
      <td>2.29</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>28</th>
      <td>15</td>
      <td>Male</td>
      <td>49</td>
      <td>The Oculus, Token of Lost Worlds</td>
      <td>4.23</td>
      <td>Ilariarin45</td>
    </tr>
    <tr>
      <th>29</th>
      <td>16</td>
      <td>Female</td>
      <td>45</td>
      <td>Glinting Glass Edge</td>
      <td>2.46</td>
      <td>Phaedai25</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>828</th>
      <td>25</td>
      <td>Male</td>
      <td>84</td>
      <td>Arcane Gem</td>
      <td>4.81</td>
      <td>Eusty71</td>
    </tr>
    <tr>
      <th>829</th>
      <td>20</td>
      <td>Male</td>
      <td>14</td>
      <td>Possessed Core</td>
      <td>2.82</td>
      <td>Frichilsa31</td>
    </tr>
    <tr>
      <th>830</th>
      <td>23</td>
      <td>Male</td>
      <td>176</td>
      <td>Relentless Iron Skewer</td>
      <td>2.12</td>
      <td>Filon68</td>
    </tr>
    <tr>
      <th>831</th>
      <td>28</td>
      <td>Male</td>
      <td>1</td>
      <td>Crucifer</td>
      <td>3.67</td>
      <td>Palyon91</td>
    </tr>
    <tr>
      <th>832</th>
      <td>23</td>
      <td>Female</td>
      <td>118</td>
      <td>Ghost Reaver, Longsword of Magic</td>
      <td>2.95</td>
      <td>Assistast50</td>
    </tr>
    <tr>
      <th>833</th>
      <td>16</td>
      <td>Female</td>
      <td>94</td>
      <td>Mourning Blade</td>
      <td>3.64</td>
      <td>Seostylis96</td>
    </tr>
    <tr>
      <th>834</th>
      <td>25</td>
      <td>Male</td>
      <td>111</td>
      <td>Misery's End</td>
      <td>1.79</td>
      <td>Iskadar31</td>
    </tr>
    <tr>
      <th>835</th>
      <td>20</td>
      <td>Male</td>
      <td>108</td>
      <td>Extraction, Quickblade Of Trembling Hands</td>
      <td>2.26</td>
      <td>Pheodaisun84</td>
    </tr>
    <tr>
      <th>836</th>
      <td>17</td>
      <td>Male</td>
      <td>79</td>
      <td>Alpha, Oath of Zeal</td>
      <td>1.31</td>
      <td>Yarmol79</td>
    </tr>
    <tr>
      <th>837</th>
      <td>23</td>
      <td>Female</td>
      <td>107</td>
      <td>Splitter, Foe Of Subtlety</td>
      <td>4.15</td>
      <td>Aeri79</td>
    </tr>
    <tr>
      <th>838</th>
      <td>30</td>
      <td>Female</td>
      <td>105</td>
      <td>Hailstorm Shadowsteel Scythe</td>
      <td>1.02</td>
      <td>Undosian34</td>
    </tr>
    <tr>
      <th>839</th>
      <td>39</td>
      <td>Female</td>
      <td>2</td>
      <td>Verdict</td>
      <td>2.65</td>
      <td>Aesririam61</td>
    </tr>
    <tr>
      <th>840</th>
      <td>23</td>
      <td>Female</td>
      <td>68</td>
      <td>Storm-Weaver, Slayer of Inception</td>
      <td>4.39</td>
      <td>Firon67</td>
    </tr>
    <tr>
      <th>841</th>
      <td>21</td>
      <td>Male</td>
      <td>31</td>
      <td>Trickster</td>
      <td>4.59</td>
      <td>Jiskjask76</td>
    </tr>
    <tr>
      <th>842</th>
      <td>18</td>
      <td>Male</td>
      <td>25</td>
      <td>Hero Cane</td>
      <td>4.78</td>
      <td>Chanirra64</td>
    </tr>
    <tr>
      <th>843</th>
      <td>11</td>
      <td>Female</td>
      <td>41</td>
      <td>Orbit</td>
      <td>3.85</td>
      <td>Isristira52</td>
    </tr>
    <tr>
      <th>844</th>
      <td>24</td>
      <td>Male</td>
      <td>164</td>
      <td>Exiled Doomblade</td>
      <td>1.31</td>
      <td>Chaniman66</td>
    </tr>
    <tr>
      <th>845</th>
      <td>23</td>
      <td>Male</td>
      <td>181</td>
      <td>Reaper's Toll</td>
      <td>4.12</td>
      <td>Yarithrgue83</td>
    </tr>
    <tr>
      <th>846</th>
      <td>24</td>
      <td>Male</td>
      <td>4</td>
      <td>Bloodlord's Fetish</td>
      <td>1.91</td>
      <td>Airi27</td>
    </tr>
    <tr>
      <th>847</th>
      <td>22</td>
      <td>Male</td>
      <td>94</td>
      <td>Mourning Blade</td>
      <td>3.64</td>
      <td>Undilsan50</td>
    </tr>
    <tr>
      <th>848</th>
      <td>21</td>
      <td>Male</td>
      <td>82</td>
      <td>Nirvana</td>
      <td>1.77</td>
      <td>Aidaira26</td>
    </tr>
    <tr>
      <th>849</th>
      <td>34</td>
      <td>Male</td>
      <td>126</td>
      <td>Exiled Mithril Longsword</td>
      <td>1.08</td>
      <td>Chamalo71</td>
    </tr>
    <tr>
      <th>850</th>
      <td>25</td>
      <td>Male</td>
      <td>98</td>
      <td>Deadline, Voice Of Subtlety</td>
      <td>1.29</td>
      <td>Undadar97</td>
    </tr>
    <tr>
      <th>851</th>
      <td>25</td>
      <td>Male</td>
      <td>60</td>
      <td>Wolf</td>
      <td>2.70</td>
      <td>Sundaky74</td>
    </tr>
    <tr>
      <th>852</th>
      <td>21</td>
      <td>Male</td>
      <td>180</td>
      <td>Stormcaller</td>
      <td>2.77</td>
      <td>Lisirra44</td>
    </tr>
    <tr>
      <th>853</th>
      <td>35</td>
      <td>Male</td>
      <td>93</td>
      <td>Apocalyptic Battlescythe</td>
      <td>4.49</td>
      <td>Chamast86</td>
    </tr>
    <tr>
      <th>854</th>
      <td>38</td>
      <td>Male</td>
      <td>163</td>
      <td>Thunderfury Scimitar</td>
      <td>4.16</td>
      <td>Ardcil81</td>
    </tr>
    <tr>
      <th>855</th>
      <td>15</td>
      <td>Male</td>
      <td>167</td>
      <td>Malice, Legacy of the Queen</td>
      <td>3.25</td>
      <td>Heudai45</td>
    </tr>
    <tr>
      <th>856</th>
      <td>24</td>
      <td>Male</td>
      <td>97</td>
      <td>Swan Song, Gouger Of Terror</td>
      <td>1.92</td>
      <td>Chaniman66</td>
    </tr>
    <tr>
      <th>857</th>
      <td>20</td>
      <td>Male</td>
      <td>134</td>
      <td>Undead Crusader</td>
      <td>2.15</td>
      <td>Syalallodil59</td>
    </tr>
  </tbody>
</table>
<p>858 rows × 6 columns</p>
</div>




```python
#Check for empty values
pd_df.isnull().any()
```




    Age          False
    Gender       False
    Item ID      False
    Item Name    False
    Price        False
    SN           False
    dtype: bool




```python
## Player Count

tot_players = [len(pd_df["SN"].unique())]
total_players = pd.DataFrame(tot_players,columns={"Total Players"})
total_players
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>612</td>
    </tr>
  </tbody>
</table>
</div>




```python
## Purchasing Analysis (Total)

tot_items = [len(pd_df["Item Name"].unique())]
avg_price = '${:,.2f}'.format(pd_df["Price"].mean())
tot_purchases = [len(pd_df)]
tot_rev = '${:,.2f}'.format(pd_df["Price"].sum())

total_dic = {"Number of Unique Items":tot_items,
       "Average Price":avg_price,
       "Number of Purchases":tot_purchases,
       "Total Revenue":tot_rev}

#part1 = pd.DataFrame(list(dic.items()))
purchasing_analysis = pd.DataFrame(total_dic, columns=total_dic.keys())
purchasing_analysis.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Number of Unique Items</th>
      <th>Average Price</th>
      <th>Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>180</td>
      <td>$2.93</td>
      <td>858</td>
      <td>$2,514.43</td>
    </tr>
  </tbody>
</table>
</div>




```python
## Gender Demographics

unique_df = pd_df.drop_duplicates(subset=['SN'])
gender_dem = unique_df["Gender"].value_counts()  

total = gender_dem.sum()
gender_percent = gender_dem/total*100

gender = pd.DataFrame(gender_dem)
gender.columns =['Total Count']
gender.insert(0,'Percentage of Players',gender_percent)
gender['Percentage of Players'] = gender['Percentage of Players'].map('{:,.2f}%'.format)
gender
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>80.88%</td>
      <td>495</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>17.65%</td>
      <td>108</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.47%</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
## Purchasing Analysis (Gender)

#group by gender, then create the 'purchase count' column
purchasing_gender = pd_df.groupby("Gender")
purchasing_gender_df = pd.DataFrame(purchasing_gender["SN"].count()).rename(columns={"SN":"Purchase Count"})

#calculate avg and total purchase
avg_purchase = ["${:.2f}".format(x) for x in purchasing_gender["Price"].mean()]
total_purchase = ["${:.2f}".format(y) for y in purchasing_gender["Price"].sum()]

#insert avg and total purchase columns into dataframe
purchasing_gender_df.insert(1,'Average Purchase Price',avg_purchase)
purchasing_gender_df.insert(2,'Total Purchase Value',total_purchase)


#Bring in total count to match index, then use for-loop to calculate normalized totals 
#Use temporary dataframe to retain 'Gender'index header in working dataframe
temporary_df = purchasing_gender_df.join(gender["Total Count"],how='outer')

normalized_totals=[]
for row in range(0,len(purchasing_gender_df)):
    normalized_totals.append(purchasing_gender["Price"].sum()[row]/temporary_df["Total Count"][row])
normalized_totals = ["${:.2f}".format(z) for z in normalized_totals]

#insert normalized totals
purchasing_gender_df.insert(3,'Normalized Totals',normalized_totals)

purchasing_gender_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Gender</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>149</td>
      <td>$2.85</td>
      <td>$424.29</td>
      <td>$3.93</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>697</td>
      <td>$2.94</td>
      <td>$2052.28</td>
      <td>$4.15</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>12</td>
      <td>$3.15</td>
      <td>$37.86</td>
      <td>$4.21</td>
    </tr>
  </tbody>
</table>
</div>




```python
## Age Demographics

#add appropriate age group to each purchase
labels = ['<10','10-14','15-19','20-24','25-29','30-34','35-39','40+']
bins = [0,10,15,20,25,30,35,40,100]
pd_df["Age Group"] = pd.cut(pd_df["Age"],bins,labels=labels)

#drop duplicate users
unique_df = pd_df.drop_duplicates(subset=['SN'])

#groupby age group
age_group = unique_df.groupby("Age Group")["Age"].count().to_frame()
del age_group.index.name
age_group = age_group.rename(columns={"Age":"Total Count"})

#calculate percentages
age_percent = age_group["Total Count"]/tot_players*100
age_percent = ["{:.2f}%".format(z) for z in age_percent]

age_group.insert(0,"Percentage of Players",age_percent)
age_group
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>3.92%</td>
      <td>24</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>9.31%</td>
      <td>57</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>24.51%</td>
      <td>150</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>40.20%</td>
      <td>246</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>8.99%</td>
      <td>55</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>7.84%</td>
      <td>48</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>4.74%</td>
      <td>29</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>0.49%</td>
      <td>3</td>
    </tr>
  </tbody>
</table>
</div>




```python
## Purchasing Analysis (Age)
purchase_age = pd_df.groupby("Age Group")
purchase_age_df = pd.DataFrame(purchase_age["SN"].count()).rename(columns={"SN":"Purchase Count"})

avg_purchase_age = ["${:.2f}".format(x) for x in purchase_age["Price"].mean()]
total_purchase_age = ["${:.2f}".format(y) for y in purchase_age["Price"].sum()]

purchase_age_df.insert(1,'Average Purchase Price',avg_purchase_age)
purchase_age_df.insert(2,'Total Purchase Value',total_purchase_age)

temporary_df_age = purchase_age_df.join(age_group["Total Count"],how='outer')

normalized_totals_age = []
for row in range(0,len(purchase_age_df)):
    normalized_totals_age.append(purchase_age["Price"].sum()[row]/temporary_df_age["Total Count"][row])
normalized_totals_age = ["${:.2f}".format(z) for z in normalized_totals_age]

#insert normalized totals
purchase_age_df.insert(3,'Normalized Totals',normalized_totals_age)

purchase_age_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
      <th>Normalized Totals</th>
    </tr>
    <tr>
      <th>Age Group</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>37</td>
      <td>$2.98</td>
      <td>$110.44</td>
      <td>$4.60</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>82</td>
      <td>$2.88</td>
      <td>$236.36</td>
      <td>$4.15</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>204</td>
      <td>$2.86</td>
      <td>$583.43</td>
      <td>$3.89</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>338</td>
      <td>$2.97</td>
      <td>$1003.03</td>
      <td>$4.08</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>80</td>
      <td>$2.88</td>
      <td>$230.59</td>
      <td>$4.19</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>65</td>
      <td>$3.00</td>
      <td>$194.73</td>
      <td>$4.06</td>
    </tr>
    <tr>
      <th>35-39</th>
      <td>49</td>
      <td>$3.00</td>
      <td>$147.21</td>
      <td>$5.08</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>3</td>
      <td>$2.88</td>
      <td>$8.64</td>
      <td>$2.88</td>
    </tr>
  </tbody>
</table>
</div>




```python
## Top Spenders

user_total_purchase = pd_df.groupby("SN")["Price"].sum()
user_purchase_count = pd_df.groupby("SN")["Age"].count()

user_avg_price = []

for a in range(0,len(user_total_purchase)):
    user_avg_price.append("${:.2f}".format(user_total_purchase[a]/user_purchase_count[a]))

#user_total_purchase = "${:.2f}".format(user_total_purchase)
user_group = pd.concat([user_purchase_count,user_total_purchase],axis=1,join='outer')
user_group = user_group.rename(columns={"Age":"Purchase Count","Price":"Total Purchase Value"}).sort_values("Total Purchase Value",ascending=False)
user_group.insert(1,"Average Purchase Price",user_avg_price)
user_group = user_group[:5]
user_group["Total Purchase Value"] = user_group["Total Purchase Value"].map('${:,.2f}'.format)
user_group
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>5</td>
      <td>$2.46</td>
      <td>$17.06</td>
    </tr>
    <tr>
      <th>Aerithllora36</th>
      <td>4</td>
      <td>$2.23</td>
      <td>$15.10</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>4</td>
      <td>$1.93</td>
      <td>$13.56</td>
    </tr>
    <tr>
      <th>Sondim43</th>
      <td>4</td>
      <td>$2.46</td>
      <td>$13.02</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>4</td>
      <td>$1.27</td>
      <td>$12.74</td>
    </tr>
  </tbody>
</table>
</div>




```python
## Most Popular Items

grouped_items = pd_df.groupby(["Item ID","Item Name"])
count_items = grouped_items.count().sort_values("Age",ascending=False)
count_items = count_items['Age']

total_purchase_items = grouped_items['Price'].sum()
#total_purchase_items

item_groups = pd.concat([count_items,total_purchase_items],axis=1,join='outer')
item_groups = item_groups.rename(columns={'Price':'Total Purchase Value','Age':'Purchase Count'})

temporary_df = pd_df.drop_duplicates(subset=['Item ID'])
temporary_df = temporary_df.groupby(['Item ID','Item Name']).sum()
temporary_df = temporary_df['Price']

item_groups.insert(1,"Item Price",temporary_df)
item_groups['Item Price'] = item_groups['Item Price'].map('${:.2f}'.format)

popular_items = item_groups.sort_values('Purchase Count',ascending=False)
popular_items['Total Purchase Value'] = popular_items['Total Purchase Value'].map('${:.2f}'.format)
popular_items = popular_items[:5]
popular_items

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>12</td>
      <td>$2.23</td>
      <td>$29.34</td>
    </tr>
    <tr>
      <th>39</th>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>11</td>
      <td>$2.35</td>
      <td>$25.85</td>
    </tr>
    <tr>
      <th>31</th>
      <th>Trickster</th>
      <td>10</td>
      <td>$2.07</td>
      <td>$23.22</td>
    </tr>
    <tr>
      <th>44</th>
      <th>Bonecarvin Battle Axe</th>
      <td>9</td>
      <td>$2.46</td>
      <td>$24.04</td>
    </tr>
    <tr>
      <th>154</th>
      <th>Feral Katana</th>
      <td>9</td>
      <td>$2.19</td>
      <td>$23.55</td>
    </tr>
  </tbody>
</table>
</div>




```python
## Most Profitable Items

profitable_items = item_groups.sort_values('Total Purchase Value',ascending=False)
profitable_items['Total Purchase Value'] = profitable_items['Total Purchase Value'].map('${:.2f}'.format)
profitable_items = profitable_items[:5]
profitable_items
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Purchase Count</th>
      <th>Item Price</th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item ID</th>
      <th>Item Name</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>34</th>
      <th>Retribution Axe</th>
      <td>9</td>
      <td>$4.14</td>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>107</th>
      <th>Splitter, Foe Of Subtlety</th>
      <td>9</td>
      <td>$3.61</td>
      <td>$33.03</td>
    </tr>
    <tr>
      <th>115</th>
      <th>Spectral Diamond Doomblade</th>
      <td>7</td>
      <td>$4.25</td>
      <td>$29.75</td>
    </tr>
    <tr>
      <th>32</th>
      <th>Orenmir</th>
      <td>6</td>
      <td>$4.95</td>
      <td>$29.70</td>
    </tr>
    <tr>
      <th>84</th>
      <th>Arcane Gem</th>
      <td>12</td>
      <td>$2.23</td>
      <td>$29.34</td>
    </tr>
  </tbody>
</table>
</div>


