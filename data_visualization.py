import pandas as pd
import matplotlib.pyplot as plt

# 1. Dataset
data = {
    'Sample': ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8'],
    'Score': [95, 85, 40, 92, 35, 88, 75, 42]
}
df = pd.DataFrame(data)

# 2. Criando o Gráfico
plt.figure(figsize=(10, 6))
colors = ['#2ecc71' if x > 50 else '#e74c3c' for x in df['Score']] # Cores profissionais
plt.bar(df['Sample'], df['Score'], color=colors)

# 3. Customização (Estilo Accenture/Consultoria)
plt.title('Genomic Sequencing Quality Control Report', fontsize=14, fontweight='bold')
plt.xlabel('Patient Samples', fontsize=12)
plt.ylabel('Phred Quality Score', fontsize=12)
plt.axhline(y=50, color='#3498db', linestyle='--', label='Quality Threshold (50)')
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 4. SALVANDO A IMAGEM
# Isso cria o arquivo que você vai postar no GitHub
plt.savefig('quality_report.png')
print("--- Success! ---")
print("File 'quality_report.png' has been created in your folder.")
