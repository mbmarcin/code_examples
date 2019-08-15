def add_prop(group):
	group['prop'] = group.births / group.births.sum()
	return group
names = names.groupby(['year', 'sex']).apply(add_prop)

sprawdzenie
names.groupby(['year', 'sex']).prop.sum()

Wybór tych danych to kolejna operacja przeprowadzana na grupach:

def get_top1000(group):
	return group.sort_values(by='births', ascending=False)[:1000]
grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)

# Odrzuć indeks grupy, nie jest on potrzebny.
top1000.reset_index(inplace=True, drop=True)
Jeżeli wolisz wykonać tę operację ręcznie, to możesz skorzystać z następującego kodu:

pieces = []
for year, group in names.groupby(['year', 'sex']):
pieces.append(group.sort_values(by='births', ascending=False)[:1000])
top1000 = pd.concat(pieces, ignore_index=True)



Po posortowaniu danych w kolejności malejącej chcemy dowiedzieć się, ile z najpopularniejszych
imion wystarczy, aby objąć 50% liczby obserwacji. Można to zrobić za pomocą pętli for , ale lepiej bę-
dzie wykonać to w sposób wektorowy za pomocą pakietu NumPy. Biorąc sumę kumulacyjną
( cumsum ) obiektu prop i wywołując metodę searchsorted , zwrócimy sumę kumulacyjną, przy której
należałoby umieścić wartość 0,5 w celu utrzymania kolejności sortowania:

In [120]: prop_cumsum = df.sort_values(by='prop', ascending=False).prop.cumsum()
In [121]: prop_cumsum[:10]
Out[121]:
260877 0.011523
260878 0.020934
260879 0.029959
260880 0.038930
260881 0.047817
260882 0.056579
260883 0.065155
260884 0.073414
260885 0.081528
260886 0.089621
Name: prop, dtype: float64
In [122]: prop_cumsum.values.searchsorted(0.5)
Out[122]: 116
Tablice są indeksowane od zera, a więc dodanie 1 do tej wartości da wynik 117. Dla porównania
w roku 1900 wartość ta była o wiele niższa:
In [123]: df = boys[boys.year == 1900]
In [124]: in1900 = df.sort_values(by='prop', ascending=False).prop.cumsum()
In [125]: in1900.values.searchsorted(0.5) + 1
Out[125]: 25
396 
Rozdział 14. Przykłady analizy danych
d34875cd169d1518165720875104aac3Operację tę możemy wykonać dla każdej kombinacji roku i płci, pogrupować te pola za pomocą
metody groupby i przetworzyć przy użyciu funkcji apply w celu zwrócenia sumy dla każdej grupy:
def get_quantile_count(group, q=0.5):
group = group.sort_values(by='prop', ascending=False)
return group.prop.cumsum().values.searchsorted(q) + 1
diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')
