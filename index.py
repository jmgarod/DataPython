# Importamos los paquetes necesarios
import matplotlib.pyplot as plt
import numpy as np, locale, calendar
import seaborn as sns
import matplotlib.ticker as ticker

# Configuramos el LOCALE para que la numeración y las fechas estén en español
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')

sns.set(style='whitegrid', font="Calibri")
fig, ax = plt.subplots()

# Generamos la DATA que mostraremos en el gráfico
meses = (s:=np.char.replace(list(calendar.month_abbr),'.',''))[s!=''].tolist() # Meses de ene...dic
ventas_2022 = np.random.uniform(1000,5000,12).round(2)  # Nºs aleatorios para 2022
ventas_2023 = np.random.uniform(5000,10000,12).round(2) # Nºs aleatorios para 2023

# Calculamos los valores máximos de ambos años
max_valor_2022=max(ventas_2022)
max_valor_2023=max(ventas_2023)
mes_2022=list(ventas_2022).index(max_valor_2022)
mes_2023=list(ventas_2023).index(max_valor_2023)

# Eje Y en formato moneda
formatter = ticker.FuncFormatter(lambda x, pos: f'{locale.format_string("%d", x, grouping=True)} €')
plt.gca().yaxis.set_major_formatter(formatter)

# Generamos ambas gráficas
plt.plot(meses, ventas_2022, marker='o', label='Ventas 2022', color='purple', markersize=8, markeredgecolor='white', markerfacecolor='purple', linewidth=3)
plt.plot(meses, ventas_2023, marker='o', label='Ventas 2023', color='green', markersize=8, markeredgecolor='white', markerfacecolor='green',linewidth=3)

# Valores en formato moneda sobre cada marcador
for i in range(len(meses)):
    plt.text(meses[i], ventas_2022[i]+500, str(locale.currency(ventas_2022[i], grouping=True)), ha='center', va='top', fontsize=7)
    plt.text(meses[i], ventas_2023[i]+500, str(locale.currency(ventas_2023[i],grouping=True)), ha='center', va='top', fontsize=7)

# El límite del eje Y siempre será el valor máximo de la DATA de ambos años + 500
plt.ylim(0,max(np.concatenate((ventas_2022,ventas_2023),axis=0))+500)

# Círculos rojos de valores máximos
plt.scatter(mes_2022, max_valor_2022, s=150, c='red', marker='o')
plt.scatter(mes_2023, max_valor_2023, s=150, c='red', marker='o')

# Líneas verticales a trazos de valores máximos
plt.vlines(mes_2023, ymin=0, ymax=max_valor_2023, color='red', linestyles='dashed', linewidth=0.5)
plt.vlines(mes_2022, ymin=0, ymax=max_valor_2022, color='red', linestyles='dashed', linewidth=0.5)

# Damos formato a la gráfica
ax.xaxis.label.set_color('black')
ax.yaxis.label.set_color('black')
plt.grid(True, linestyle='dashed', alpha=0.3)
plt.xlabel('Meses', weight='bold')
plt.ylabel('Ventas',weight='bold')
plt.xticks(fontweight='bold')
plt.yticks(fontweight='bold')
plt.title('Ventas Mensuales 2022 vs. 2023', weight='bold')
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.3), ncol=2,frameon=False)

# Visualizamos los ejes X e Y inferior e izquierdo. Ocultamos el resto.
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_edgecolor('black')
plt.gca().spines['left'].set_edgecolor('black')

# Finalmente mostramos el gráfico por pantalla
plt.xticks(rotation=0)
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
plt.tight_layout()
plt.show()