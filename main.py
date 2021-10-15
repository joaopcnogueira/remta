from remta import DataImport
from remta import SpectraTreatment

# Load Data
df = DataImport.read_tsv(path='./datasets/example.txt')

# Spectra Plotting
SpectraTreatment.plot_spectra(df)

# PCA Calculation
SpectraTreatment.plot_spectra(df, pca=True)

